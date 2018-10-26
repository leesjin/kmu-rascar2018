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
        
        if(self.line_detector.is_equal_status([0,0,1,0,0])):
            go.forward_with_speed(50)
        elif(self.line_detector.is_equal_status([1,0,0,0,0])):
            self.front_wheel_drive.turn_left(35)
        elif(self.line_detector.is_equal_status([1,1,0,0,0])):
            self.front_wheel_drive.turn_left(30)
        elif(self.line_detector.is_equal_status([0,1,0,0,0])):
            self.front_wheel_drive.turn_left(10)
        elif(self.line_detector.is_equal_status([0,1,1,0,0])):
            self.front_wheel_drive.turn_left(5)
        elif(self.line_detector.is_equal_status([0,0,1,1,0])):
            self.front_wheel_drive.turn_right(5)
        elif(self.line_detextor.is_equal_status([0,0,0,1,0])):
            self.front_wheel_drive.turn_right(10)
        elif(self.line_detector.is_equal_status([0,0,0,1,1])):
            self.front_wheel_drive.turn_right(30)
        elif(self.line_detector.is_equal_status([0,0,0,0,1])):
            self.front_wheel_drive.turn_right(35)

if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()