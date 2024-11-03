import requests
import http.server
import threading
import RPi.GPIO as GPIO
import time
import os

# Setup LED
LED_PIN = 18  # Change to the correct GPIO pin number
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# PID file
PID_FILE_PATH = "/tmp/blink-led.pid"

def create_pid_file():
    with open(PID_FILE_PATH, 'w') as pid_file:
        pid_file.write(str(os.getpid()))

def remove_pid_file():
    if os.path.exists(PID_FILE_PATH):
        os.remove(PID_FILE_PATH)

# HTTP server for health check
class HealthCheckHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.end_headers()

def start_http_server():
    server_address = ('', 5005)
    httpd = http.server.HTTPServer(server_address, HealthCheckHandler)
    httpd.serve_forever()

# Start HTTP server in a separate thread
http_thread = threading.Thread(target=start_http_server)
http_thread.daemon = True
http_thread.start()

# Create PID file
create_pid_file()

# Blink the LED
try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    # Cleanup
    GPIO.cleanup()
    remove_pid_file()
