from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

# กำหนดขา GPIO สำหรับ LED 1 และ LED 2
led1_pin = 26
led2_pin = 16

# กำหนดโหมดของขา GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(led1_pin, GPIO.OUT)
GPIO.setup(led2_pin, GPIO.OUT)

# สถานะเริ่มต้นของ LED
led1_status = False
led2_status = False

# หน้าแสดงสถานะ LED
@app.route('/')
def index():
    return f"LED 1 - {'ON' if led1_status else 'OFF'}<br>LED 2 - {'ON' if led2_status else 'OFF'}"

# เปิด-ปิด LED ผ่าน URL
@app.route('/led1/<action>')
def control_led1(action):
    global led1_status
    if action == 'on':
        GPIO.output(led1_pin, GPIO.HIGH)
        led1_status = True
    elif action == 'off':
        GPIO.output(led1_pin, GPIO.LOW)
        led1_status = False
    return f"LED 1 - {'ON' if led1_status else 'OFF'}"

@app.route('/led2/<action>')
def control_led2(action):
    global led2_status
    if action == 'on':
        GPIO.output(led2_pin, GPIO.HIGH)
        led2_status = True
    elif action == 'off':
        GPIO.output(led2_pin, GPIO.LOW)
        led2_status = False
    return f"LED 2 - {'ON' if led2_status else 'OFF'}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
