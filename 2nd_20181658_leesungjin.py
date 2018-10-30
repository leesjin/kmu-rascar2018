#########################################################################
# Date: 2018/10/02
# file name: 2nd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import time


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        
        self.car.drive_parking()

    # =======================================================================
    # 2ND_ASSIGNMENT_CODE
    # Complete the code to perform Second Assignment
    # =======================================================================
    def car_startup(self):
        # implement the assignment code here
        self.car.accelerator.go_forward(60)
        
        while(True):
            print(self.car.line_detector.read_digital())
            if(self.car.line_detector.read_digital() == [0,0,1,0,0]):
                self.car.accelerator.go_forward(60)
            elif(self.car.line_detector.read_digital() == [1,0,0,0,0]):
                self.car.steering.turn_left(60)
                self.car.accelerator.go_forward(60)
            elif(self.car.line_detector.read_digital() == [1,1,0,0,0]):
                self.car.steering.turn_left(65)
                self.car.accelerator.go_forward(60)
            elif(self.car.line_detector.read_digital() == [0,1,0,0,0]):
                self.car.steering.turn_left(80)
                self.car.accelerator.go_forward(60)
            elif(self.car.line_detector.read_digital() == [0,1,1,0,0]):
                self.car.steering.turn_left(85)
                self.car.accelerator.go_forward(60)
            elif(self.car.line_detector.read_digital() == [0,0,1,1,0]):
                self.car.steering.turn_right(95)
                self.car.accelerator.go_forward(60)
            elif(self.car.line_detector.read_digital() == [0,0,0,1,0]):
                self.car.steering.turn_right(110)
                self.car.accelerator.go_forward(60)
            elif(self.car.line_detector.read_digital() == [0,0,0,1,1]):
                self.car.steering.turn_right(115)
                self.car.accelerator.go_forward(60)
            elif(self.car.line_detector.read_digital() == [0,0,0,0,1]):
                self.car.steering.turn_right(120)
                self.car.accelerator.go_forward(60)
            elif(self.car.line_detector.read_digital() == [0,0,0,0,0]):
                self.car.accelerator.stop()
                break
           


if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             