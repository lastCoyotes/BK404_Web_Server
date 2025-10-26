from flask import Flask, render_template
import serial

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "Hello, World!"

@app.route('/command/<command_str>')
def run_command(command_str):
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
    full_command = command_str.encode("utf-8") + b'!\n'
    ser.write(full_command)
    output = ""
    while True:
        data = ser.readline().decode('utf-8').strip()
        if not data:
            break
        output += data + "\n"
    ser.close()
    text_array = output.split("\n")
    return render_template('command.html', command=full_command.decode(), data=text_array)

if __name__ == "__main__":
    app.run(debug=False)

