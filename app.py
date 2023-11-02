from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from unfucker.unfucker import Unfucker
import logging
import tempfile
import os

app = Flask(__name__)

# Initialize Limiter
limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["20 per minute"],
)

# Configure logging
logging.basicConfig(filename='api.log', level=logging.INFO)

@app.route("/unfuck", methods=["POST"])
@limiter.limit("20 per minute")
def unfuck_file():
    """
    Endpoint to unfuck a file's content. It expects a POST request with JSON payload.

    The JSON should contain:
    - file_content (str): The content of the file to be unfucked.
    - max_iterations (int, optional): Maximum iterations to attempt unfucking. Defaults to 10.

    Returns:
    - On success: JSON object containing 'success': True and 'unfucked_content': <content>
    - On failure: JSON object containing 'success': False and 'error': <error message>

    Raises HTTP 400 for bad requests and HTTP 429 for rate limit exceeded.
    """
    try:
        data = request.get_json()
    except:
        return bad_request("Your request is empty, like your soul")

    file_content = data.get("file_content")
    max_iterations = data.get("max_iterations", 10)

    if not all([file_content]):
        return bad_request("Missing required field: file_content")

    with tempfile.NamedTemporaryFile(suffix=f"_unfuck_temp", delete=False) as temp:
        temp_file_path = temp.name
        temp.write(file_content.encode())

    unfucker = Unfucker(temp_file_path, max_iterations)
    fixed_content, error = unfucker.unfuck()

    os.remove(temp_file_path)  # Deleting the tempfile

    if fixed_content:
        logging.info("Successfully unfucked a file")
        return jsonify({"success": True, "unfucked_content": fixed_content}), 200

    return bad_request(f"Failed to unfuck. Maybe it's you, not the file. Reason: {error}")

@app.errorhandler(400)
def bad_request(e):
    """
    Error handler for HTTP 400 Bad Request.

    Args:
    e (str): Error message to be included in the response.

    Returns:
    JSON object containing 'success': False and 'error': <error message>, HTTP status 400
    """
    logging.warning(f"Bad request: {e}")
    return jsonify({"success": False, "error": f"Your request is fucked: {e}"}), 400

@app.errorhandler(429)
def rate_limit_exceeded(e):
    """
    Error handler for HTTP 429 Too Many Requests (rate limit exceeded).

    Returns:
    JSON object containing 'success': False and 'error': 'Too fast, cowboy. Try again in a minute', HTTP status 429
    """
    logging.warning("Rate limit exceeded")
    return jsonify({"success": False, "error": "Too fast, cowboy. Try again in a minute"}), 429

@app.errorhandler(500)
def internal_error(e):
    """
    Error handler for HTTP 500 Internal Server Error.

    Returns:
    JSON object containing 'success': False and 'error': 'The server is pretty fucked', HTTP status 500
    """
    logging.exception("Internal error")
    return jsonify({"success": False, "error": "The server is pretty fucked"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3825)
