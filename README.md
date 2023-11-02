# Unfucker API

```
88        88                 ad88                           88
88        88                d8"                             88
88        88                88                              88
88        88  8b,dPPYba,  MM88MMM  88       88   ,adPPYba,  88   ,d8   ,adPPYba,  8b,dPPYba,
88        88  88P'   `"8a   88     88       88  a8"     ""  88 ,a8"   a8P_____88  88P'   "Y8
88        88  88       88   88     88       88  8b          8888[     8PP"""""""  88
Y8a.    .a8P  88       88   88     "8a,   ,a88  "8a,   ,aa  88`"Yba,  "8b,   ,aa  88
 `"Y8888Y"'   88       88   88      `"YbbdP'Y8   `"Ybbd8"'  88   `Y8a  `"Ybbd8"'  88


                                          @@@@@@
                                        .@. ..#*@
                                        @&  ...*@
                                        @. ....*@
                                       @& .*,.**@
                                       @. ....*/@
                                @@@@@@#@. ....*&@@**/@@@@@@@
                          .@@@@@@@@***@@......*#..,***/*****@,
                       .@#**(@@@#****&@@,#&@(.*&@  .......**@@
                       @,. ..,*%  ...*@.  ,,.,*@@****%@@.,**@%
                      @@  ...*@. ....*@. ....**@. ....**@*(@
                     @@. ...**/ .....*@. ....,*@. ....,*@/@
                    @#@.....*@.......*& ......*@. ....,*@*@,
                    @&,....,*/......*/(.......*@*.....*#**@
                    *@..............*,@......**..*....*%/@.
                     ,@. ............................,*(@
                       @@@@@@. .,.**................**@@
                            .@@/(@@@,. ..**&*. ...*@@,
                                    @@@@@@@@&@@@@@%
 _     _        ___             _                                    ___ _ _
| |   | |      / __)           | |                                  / __|_) |
| |   | |____ | |__ _   _  ____| |  _    _   _  ___  _   _  ____   | |__ _| | ____  ___
| |   | |  _ \|  __) | | |/ ___) | / )  | | | |/ _ \| | | |/ ___)  |  __) | |/ _  )/___)
| |___| | | | | |  | |_| ( (___| |< (   | |_| | |_| | |_| | |      | |  | | ( (/ /|___ |
 \______|_| |_|_|   \____|\____)_| \_)   \__  |\___/ \____|_|      |_|  |_|_|\____|___/
                                        (____/

```

Welcome to the Unfucker API, a seamless extension of [Unfucker](https://github.com/skullzarmy/unfucker), a Python utility designed for repairing corrupted or malformed text files. With support for JSON, XML, and TXT formats, Unfucker API inherits the capability to automatically fix syntax errors, missing attributes, or encoding issues in these files. Crafted with Flask and optimized for Docker, this API transforms your text content into a more legible and structured format swiftly and efficiently. 🚀

[![SoCalTechLab.com logo - click to visit](./sctl_xs_rounded_white_text.webp)](https://socaltechlab.com/?rel=unfuckerApiGitHubRepo)

[a SoCalTechLab.com project](https://socaltechlab.com/?rel=unfuckerApiGitHubRepo)

## 📜 License

This project is open-source and available under the MIT License. Check out the [LICENSE](./LICENSE) file for more details.

## 🚀 Getting Started

Ready to unfuck some text files? Here’s how you can get the Unfucker API up and running on your local machine using Docker.

**NOTE:** This API project is meant for slightly more advanced use-cases. If you are just looking to unfuck a few files, you should probably start with the [Unfucker](https://github.com/skullzarmy/unfucker) utility. That should cover most single-use needs. If you are looking to add some automated unfucking to your tech stack, read on.

### Prerequisites

Make sure you have the following installed:

-   Docker
-   Docker Compose (optional)

### 🛠 Installation and Running with Docker

1. Clone this repository:

    ```bash
    git clone https://github.com/skullzarmy/unfucker-api.git
    cd unfucker-api
    ```

2. Build the Docker image:

    ```bash
    docker build -t unfucker-api .
    ```

3. Run the Docker container, mapping the internal port 3825 to your desired external port (here we use 3825 as an example):
    ```bash
    docker run -p 3825:3825 -d unfucker-api
    ```

🎉 The API is now running at `http://localhost:3825/`.

## 🎈 Usage

To interact with the Unfucker API, make a POST request to `http://localhost:3825/unfuck` with a JSON payload including:

-   `file_content` (required): A string of the file's content that you want to process.
-   `max_iterations` (optional): An integer defining the maximum number of processing iterations. Defaults to 10.

Example using `curl`:

```bash
curl -X POST http://localhost:3825/unfuck \
-H "Content-Type: application/json" \
-d '{"file_content": "your file content here", "max_iterations": 10}'
```

### Responses

-   **200 OK**: The file was successfully processed! 🎉 The response includes `success: true` and `unfucked_content`.
-   **400 Bad Request**: Something was off with your request. Check and try again! Response includes `success: false` and an `error` message.
-   **429 Too Many Requests**: You've hit the rate limit. Take a breather and try again later! Response includes `success: false` and an `error` message.
-   **500 Internal Server Error**: Oops, something went wrong on our end. Response includes `success: false` and an `error` message.

## 🛡 Rate Limiting

Fair usage by default. The API allows up to 20 requests per minute from a single IP address. If you are using locally you may wish to remove or change this limit. This can be done with `@limiter.limit()` using natural language such as `@limiter.limit("20 per minute")`.

## 📝 Logging

All API requests and errors are logged to `api.log` in the project's root directory. Keep an eye out!

## 🤝 Contributing to Unfucker API

Hey there, awesome human! Interested in contributing to Unfucker? That's fuckin' great! 🎉 Before you dive into the code, make sure to read our [Contributing Guidelines](./CONTRIBUTING.md) and our rather entertaining [Code of Conduct](./CODE_OF_CONDUCT.md).

Whether it's submitting a bug report, proposing a new feature, or creating a pull request, every contribution is valuable and appreciated. 🙏

Let's build something badass together! 👩‍💻👨‍💻

## Why port 3825??

If you ever owned a Nokia 33xx you know, if you didn't you don't care...
