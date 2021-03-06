from time import sleep


class TrafficLight:
    __color_1 = "red"
    __color_2 = "yellow"
    __color_3 = "green"
    def running(self, time):
        day = 0
        while day < 24:
            print(TrafficLight.__color_1)
            sleep(7)
            print(TrafficLight.__color_2)
            sleep(3)
            print(TrafficLight.__color_3)
            sleep(time)
            day += 1


traffic_light = TrafficLight()
print(f"Traffic light can work only one day.\nPlease choose time for green light of traffic light.")
time = input("Time for green light: ")
traffic_light.running(int(time))
