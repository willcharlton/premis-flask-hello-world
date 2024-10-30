from datetime import datetime
from flask import Flask

app = Flask(__name__)

server_start_time = datetime.now()

@app.route('/')
def hello_world():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>Server started at: { server_start_time }</p>
    <p>Page last rendered at: { datetime.now() }</p>
</body>
</html>
'''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
