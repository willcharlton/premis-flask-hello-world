import RPi.GPIO as GPIO
import time
import os
import signal

# Constants
LED_PIN = 18  # Change to the correct GPIO pin number
PID_FILE = "/tmp/blink_led.pid"

# Write the PID file
def write_pid_file():
    with open(PID_FILE, 'w') as f:
        f.write(str(os.getpid()))

# Remove the PID file
def remove_pid_file():
    if os.path.exists(PID_FILE):
        os.remove(PID_FILE)

# Handle script exit
def cleanup(signum, frame):
    GPIO.cleanup()
    remove_pid_file()
    exit(0)

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Write PID to file
write_pid_file()

# Set signal handlers for cleanup
signal.signal(signal.SIGTERM, cleanup)
signal.signal(signal.SIGINT, cleanup)

# Blink the LED
try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt:
    cleanup(None, None)
