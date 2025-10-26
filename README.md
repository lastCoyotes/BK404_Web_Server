# Orei BK-404 Web Terminal

A simple flask web server that allows running serial commands on the BK-404 using GET requests.

## Background

While the Orei BK-404 has a fully functional web interface, its API is poorly documented. While it is
possible to use the existing web API on the BK-404, it requires completing a network capture to determine
the specific commands being passed to the Video Matrix. This web application allows use of the
serial terminal commands through a web API.

## WARNINGs and Caveats

This application has not been developed with security in mind as this is for my own airgapped A/V network.
If intending to use this application in a public facing environment, I highly encourage developing
additional security controls to ensure that reverse shells aren't possible.

Additionally, this application was developed quickly for my local environment and may need modification
to work on other systems. Some basic information about the environment I am running this on:

- Raspberry Pi 4B running CompanionPi image
- This web server is being autostarted on boot by systemd (I recommended setting this up. More details below)

## Installation

1. Clone this Repo
2. Install python requirements (typically in a virtual environment)
   `python -m venv venv`
   `source venv/bin/active`
   `pip install -r requirements.txt`
3. Update the `WorkingDirectory` property in the `.service` file to point to the root of this repo
4. Copy the `.service` file to the service directory directory
   `sudo cp bk404-serial.service /etc/systemd/system/`
5. Enable the `bk404-serial service`
   `sudo systemctl enable bk404-serial`
6. Reboot
   `reboot now`

## Running the Software Manually.

If you've installed the service file as described above, you should not need to run the server, but
if you are working on developing this tool and need to run manually, you have some options:

- Run on localhost: `flask --app app run`
- Run open to network `flask --app app run --host 0.0.0.0`

## Available API Endpoints

- `/hello`: A basic "Hello World Endpoint
- `/command/<command_str>`: The primary endpoint for running commands on the BK-404.
  The command string should be any serial command that can run on the BK-404 video matrix. Generally,
  these should be URL encoded. Do not include the `!` or a new line that is generally included in the
  actual terminal commands. These are automatically appended by the application.
  Examples:
  - `http://127.0.0.1/command/status`: Returns the status. Equivalent to status!
  - `http://127.0.0.1/command/s%20output%201%20in%20source%203`: Updates output 1 to display video from source 3.
