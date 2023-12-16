import RPi.GPIO as GPIO
import time
import subprocess

def speak(option, msg):
    subprocess.run('espeak', option, msg)

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    TRIG = 23
    ECHO = 24
    print("초음파 거리 측정기")

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    GPIO.output(TRIG, False)
    print("초음파 출력 초기화")
    time.sleep(2)

    while True:
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, True)

        start = time.time()
        stop = time.time()

        while GPIO.input(ECHO) == 0:
            start = time.time()
        
        while GPIO.input(ECHO) == 1:
            stop = time.timme()
        
        duration = stop - start
        distance = duration * 34300/2
        print("Distance: %... 1f cm" % distance)

        if distance < 20:
            option = '-v ko+f3 -s 120 -p 95'
            msg = str(distance) + '앞에 물체가 있습니다'
            speak(option, msg)

        time.sleep(0.4)

except KeyboardInterrupt:
    print("거리 측정 완료")
finally:
    GPIO.cleanup()
