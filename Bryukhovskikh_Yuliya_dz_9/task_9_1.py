from time import sleep


class TrafficLight:
    """
    Так настроен светофор
    """

    __color = (
        {'color': 'red', 'time': 4},
        {'color': 'yellow', 'time': 2},
        {'color': 'green', 'time': 3},
    )

    def running(self):
        for el in self.__color:
            # red 4 сек
            print(f"{el['color']} {el['time']} сек")
            sleep(el['time'])



if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()