from random import Random


class Room:
    # цена номера
    cost = 10
    # Занятость номера в данный момент
    isBusy = False
    time = 0

    def reservation(self, time: int):
        if not self.isBusy:
            self.isBusy = True
            self.time = time

    #     отслеживает занятость комнаты во времени
    def update(self):
        if self.isBusy:
            self.time = self.time - 1
            if self.time <= 0:
                self.isBusy = False

    @staticmethod
    def instance():
        r = Random().randint(0, 2)
        if r == 0:
            return SingleRoom()
        elif r == 1:
            return DoubleRoom()
        elif r == 2:
            return LuxuryRoom()

class SingleRoom(Room):
    cost = 10


class DoubleRoom(Room):
    cost = 20


class LuxuryRoom(Room):
    cost = 30

