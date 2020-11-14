from model.Hotel import Hotel
from model.Request import Request


def countRequst(requests):
    sum = 0
    for req in requests:
        sum += req.cost

    return len(requests), sum


class Controller:
    hotel = Hotel()
    # Отклоненные заявки
    rejectedRequest = []

    # Принятые заявки
    applyRequest = []

    def update(self):
        # генерация заявок
        self.currentRequest = Request.instance()
        if self.hotel.isCanApply(self.currentRequest):
            self.applyRequest.append(self.currentRequest)
        else:
            self.rejectedRequest.append(self.currentRequest)

        #     обновление состояния отеля
        self.hotel.update()

    def report(self):
        positive = countRequst(self.applyRequest)
        print("Обработано заявок : ",positive[0]," Прибыль составила: ", self.hotel.money)

        negative = countRequst(self.rejectedRequest)
        print("Не обработано заявок : ",negative[0]," Потери составили: ", self.hotel.loss)

