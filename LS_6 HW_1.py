import time
class TrafficLight:
    lightcolor = 'Светофор'
    def running(self):
        while True:
            print('Красный')
            time.sleep(2)
            print('Желтый')
            time.sleep(2)
            print('Зеленый')
            time.sleep(2)
            break
a = TrafficLight()
a.running()