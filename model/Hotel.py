from model.Room import Room
from model.Settings import ROOM_QUNTITY

class Hotel:

    # хранение накопленного капитала, упущенной прибыли
    money = 0
    loss = 0
    # комнаты на сдачу
    rooms = [Room.instance() for x in range(ROOM_QUNTITY)]

    # проверка есть ли свободные комнаты для заявки, если есть - заселение
    def isCanApply(self, request):
        for r in self.rooms:
            if (not r.isBusy) and (type(request.room) == type(r)):
                self.reserverved(r, request)
                return True
        self.loss += request.cost * request.time
        return False

    def update(self):
        for r in self.rooms:
            r.update()

    def reserverved(self, room, request):
        room.reservation(request.time)
        self.money += request.time * room.cost
