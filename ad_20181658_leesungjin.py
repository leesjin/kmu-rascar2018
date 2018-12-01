#########################################################################
# Date: 2018/10/02
# file name: 3rd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import RPi.GPIO as GPIO
import time

buzzer_pin = 8

GPIO.setmode(GPIO.BOARD)

scale = [200, 0.1, 200]
GPIO.setup(buzzer_pin, GPIO.OUT)

class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        
        self.car.drive_parking()

    # =======================================================================
    # 3RD_ASSIGNMENT_CODE
    # Complete the code to perform Second Assignment
    # =======================================================================
    def car_startup(self):
        # implement the assignment code here
        distance = self.car.distance_detector.get_distance()
        self.car.accelerator.go_forward(40)
        count = 0
        GPIO.setmode(GPIO.BOARD)
        print("start")
        countstop = 0
        while(True):
            rawData = self.car.color_getter.get_raw_data()
            
            print("R: ", rawData[0])
            print("G: ", rawData[1])
            print("B: ", rawData[2])
            print("Clear: ", rawData[3])
            print(type(rawData[1]))
            
        
            if 400< rawData[0] < 800 and 300 > rawData[2]:
                print("Red light")
                self.car.accelerator.stop()
                time.sleep(3)
                self.car.accelerator.go_forward(40)
                time.sleep(0.5)
            #print(self.car.line_detector.read_digital())
            distance = self.car.distance_detector.get_distance()
            #print(distance)
            if distance == -1:
                continue
            if distance <= 30:
                count += 1
            if count >= 10:
                countstop += 1
                p = GPIO.PWM(buzzer_pin, 100)
                p.start(5)     # start the PWM on 5% duty cycle
                self.car.accelerator.stop()
                self.car.steering.turn_left(60)
                self.car.accelerator.go_forward(45)
                p.ChangeFrequency(scale[0])
                time.sleep(0.35)
                p.ChangeFrequency(scale[1])
                time.sleep(0.25)
                p.ChangeFrequency(scale[2])
                time.sleep(0.25)
                self.car.accelerator.stop()
                self.car.steering.turn_right(155)
                self.car.accelerator.go_forward(70)
                p.ChangeFrequency(scale[0])
                time.sleep(0.5)
                p.ChangeFrequency(scale[1])
                time.sleep(1.0)
                count = 0
                while(True):
                    if(self.car.line_detector.read_digital() != [0,0,0,0,0]):
                        break
                
            if(self.car.line_detector.read_digital() == [0,0,1,0,0]):
                self.car.accelerator.go_forward(40)
            elif(self.car.line_detector.read_digital() == [1,1,1,1,1]):
                print("all")
                if countstop == 1:
                    self.car.accelerator.stop()
                    break
            elif(self.car.line_detector.read_digital() == [1,1,1,0,0]):
                print("1101111011011")
            elif(self.car.line_detector.read_digital()[0] == 1):
                self.car.steering.turn_left(60)
                self.car.accelerator.go_forward(40)
            elif(self.car.line_detector.read_digital()[1] == 1):
                self.car.steering.turn_left(80)
                self.car.accelerator.go_forward(40)
            elif(self.car.line_detector.read_digital()[3] == 1):
                self.car.steering.turn_right(110)
                self.car.accelerator.go_forward(40)
            elif(self.car.line_detector.read_digital()[4] == 1):
                self.car.steering.turn_right(120)
                self.car.accelerator.go_forward(40)
            elif(self.car.line_detector.read_digital() == [0,0,0,0,0]):
                self.car.steering.turn(100)
                self.car.accelerator.go_backward(40)
                time.sleep(0.33)
                self.car.accelerator.stop()
            else: 
                continue
        #self.car.accelerator.stop()
                
if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   