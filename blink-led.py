import requests
import http.server
import threading
import time
import os

# LED path
LED_BRIGHTNESS_PATH = "/sys/class/leds/ACT/brightness"

# PID file
PID_FILE_PATH = "/tmp/blink-led.pid"

def create_pid_file():
    with open(PID_FILE_PATH, 'w') as pid_file:
        pid_file.write(str(os.getpid()))

def remove_pid_file():
    if os.path.exists(PID_FILE_PATH):
        os.remove(PID_FILE_PATH)

def set_led_brightness(value):
    """Set the brightness of the ACT LED by writing to the sysfs file."""
    try:
        with open(LED_BRIGHTNESS_PATH, 'w') as led_file:
            led_file.write(str(value))
    except PermissionError:
        print(f"Permission denied when trying to write to {LED_BRIGHTNESS_PATH}. Try running with elevated permissions.")

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
        set_led_brightness(1)  # Turn LED on
        time.sleep(2)
        set_led_brightness(0)  # Turn LED off
        time.sleep(2)
except KeyboardInterrupt:
    pass
finally:
    # Cleanup
    remove_pid_file()
