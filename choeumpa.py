import RPi.GPIO as GPIO
import time
import os

def speak(option, msg) :
    os.system("espeak {} '{}'".format(option, msg))
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

try:
    while True:
        GPIO.output(TRIG,True)
        time.sleep(0.00001)        # 10uS의 펄스 발생을 위한 딜레이
        GPIO.output(TRIG, False)
        
        while GPIO.input(ECHO)==0:
            start = time.time()     # Echo핀 상승 시간값 저장
            
        while GPIO.input(ECHO)==1:
            stop = time.time()      # Echo핀 하강 시간값 저장
            
        check_time = stop - start
        distance = check_time * 34300 / 2
        print("Distance : %.1f cm" % distance)
        time.sleep(0.4)

        option = '-v ko+f3 -s 120 -p 95'
        msg = str(distance) + '앞에 물체가 있습니다'
        
        if distance < 20:
            print('espeak', option, msg)
            speak(option, str(distance) + '앞에 물체가 있습니다')

except KeyboardInterrupt:
    print("거리 측정 완료 ")
    GPIO.cleanup()
