import tkinter as tk
from model.Settings import*

from model.Controller import Controller
from views.RoomView import RoomView


class HotelView():
    root = tk.Tk()

    def __init__(self, hotel):
        self.count = 0
        self.hotel = hotel

        self.currentRequest = None

        self.controller = Controller()
        self.controller.hotel = self.hotel

        self.roomFrame = tk.LabelFrame(self.root, text = "Номера")
        self.roomsViews = []

        # self.requestFrame = tk.LabelFrame(self.root, text = "Заявки")

        self.update()
        self.root.mainloop()


    def update(self):
        self.count += 1
        self.room_pack()
        self.controller.update()
        self.updateCurrentRequest()

        if (self.count < LONG_MODELING):
            self.root.after(DELTA_TIME, self.update)
        else:
            self.controller.report()
            self.root.destroy()

    def updateCurrentRequest(self):
        if self.currentRequest is not None:
            self.currentRequest.destroy()
        self.currentRequest = RoomView(self.root, self.controller.currentRequest.room)

        # Упаковка комнат
    def room_pack(self):
        for room in self.roomFrame.winfo_children():
            room.destroy()


        for room in self.hotel.rooms:
            self.roomsViews.append(RoomView(self.roomFrame, room))
        self.roomFrame.pack()

