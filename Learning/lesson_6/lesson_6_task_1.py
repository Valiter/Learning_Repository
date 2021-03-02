from time import time

class TrafficLight(time):
    __color = "red"
    time_for_green = time

    def running(self):
        print(TrafficLight.__color)

obj = TrafficLight()
