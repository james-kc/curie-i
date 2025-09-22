# This code is untested, it was generated using a single ChatGPT prompt. Raspberry Pi Zero 2 W was
# destroyed in car on the way to BALLS33 before code completion.

import csv
from datetime import datetime

import RPi.GPIO as GPIO

GEIGER_PIN = 17
CSV_FILE = 'geiger_pulses.csv'

def log_pulse(channel):
    now = datetime.now().isoformat()
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([now])

def setup_geiger_logging():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GEIGER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    # Write CSV header if file is empty
    try:
        with open(CSV_FILE, 'x', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['datetime'])
    except FileExistsError:
        pass
    GPIO.add_event_detect(GEIGER_PIN, GPIO.RISING, callback=log_pulse, bouncetime=1)

if __name__ == '__main__':
    setup_geiger_logging()
    try:
        while True:
            pass  # Keep the script running
    except KeyboardInterrupt:
        GPIO.cleanup()