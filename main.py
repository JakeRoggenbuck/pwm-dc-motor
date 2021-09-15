import RPi.GPIO as GPIO
from time import sleep


class Motor:
    def __init__(self, in1: int, in2: int, en: int):
        self.input_one_pin = in1
        self.input_two_pin = in2


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
    IN1 = 23
    IN2 = 24

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(EN, GPIO.OUT)

    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)

    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)

    motor = Motor(IN1, IN2, en=EN)
    motor.start(25)

    motor.forward()

    speed = 0
    while speed < 100:
        motor.set_speed(speed)

        speed += 1
        sleep(0.2)

    motor.end()


