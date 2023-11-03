from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS
from unfucker.unfucker import Unfucker
import logging
import tempfile
import re

app = Flask(__name__)
CORS(app)
limiter = Limiter(key_func=get_remote_address, app=app, default_limits=["20 per minute"])
logging.basicConfig(filename='api.log', level=logging.INFO)
ALLOWED_FILE_TYPES = {"txt", "json", "xml"}

@app.route("/unfuck", methods=["POST"])
@limiter.limit("20 per minute")
def unfuck_file():
    file_content = request.form.get("file_content")
    if file_content is None:
        return bad_request("Missing required field: file_content")

    max_iterations = request.form.get("max_iterations", 10, type=int)
    file_type = request.form.get("file_type", "txt").lower()
    if file_type not in ALLOWED_FILE_TYPES:
        return bad_request("Invalid file type. Allowed types are: txt, json, xml")

    file_extension = re.sub(r'[^a-zA-Z]', '', file_type)
    try:
        with tempfile.NamedTemporaryFile(suffix=f"_unfuck_temp.{file_extension}", delete=True) as temp:
            temp.write(file_content.encode())
            temp.flush()
            unfucker = Unfucker(temp.name, file_extension, max_iterations)
            fixed_content, error = unfucker.unfuck()

        if fixed_content:
            logging.info(f"Successfully unfucked {temp.name}")
            return jsonify({"success": True, "unfucked_content": fixed_content, "file_type": file_extension}), 200
        return bad_request(f"Failed to unfuck. Maybe it's you, not the file. Reason: {error}")
    except Exception as e:
        logging.exception("Error during unfuck operation")
        return internal_error(e)

@app.errorhandler(400)
def bad_request(error):
    logging.warning(f"Bad request: {error}")
    return jsonify({"success": False, "error": f"Your request is fucked: {error}"}), 400

@app.errorhandler(429)
def rate_limit_exceeded(e):
    logging.warning("Rate limit exceeded")
    return jsonify({"success": False, "error": "Too fast, cowboy. Try again in a minute"}), 429

@app.errorhandler(500)
def internal_error(e):
    logging.exception("Internal error")
    return jsonify({"success": False, "error": "The server is pretty fucked"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3825)
