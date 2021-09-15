import RPi.GPIO as GPIO
from time import sleep


class Motor:
    def __init__(self, in1: int, in2: int, en: int):
        self.input_one_pin = in1
        self.input_two_pin = in2

        GPIO.setup(in1, GPIO.OUT)
        GPIO.setup(in2, GPIO.OUT)

        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)

        self.pwm = GPIO.PWM(en, 1000)

    def command(self, one_state: GPIO, two_state: GPIO):
        GPIO.output(self.input_one_pin, one_state)
        GPIO.output(self.input_two_pin, two_state)

    def forward(self):
        self.command(GPIO.HIGH, GPIO.LOW)

    def backward(self):
        self.command(GPIO.LOW, GPIO.HIGH)

    def set_speed(self, x):
        self.pwm.ChangeDutyCycle(x)

    def start(self, x):
        self.pwm.start(x)

    @staticmethod
    def end():
        GPIO.cleanup()


if __name__ == "__main__":
    EN = 25

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(EN, GPIO.OUT)

    motor = Motor(in1=24, in2=23, en=EN)
    motor.start(25)

    try:
        while 1:
            sleep(4)
            print("low")
            motor.set_speed(25)

            sleep(4)
            print("med")
            motor.set_speed(50)

            sleep(4)
            print("high")
            motor.set_speed(75)

    except KeyboardInterrupt:
        motor.end()


