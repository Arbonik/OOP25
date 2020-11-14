import tkinter as tk


class RoomView:
    def __init__(self, root, room):
        self.root = root
        self.room = room
        self.view = tk.Button(self.root, width = 10, height = self.room.cost)
        self.update()

    def update(self):
        self.view.destroy()
        self.view = tk.Button(self.root, width = 10, height = self.room.cost)

        if self.room.isBusy:
            self.view.config(bg = 'red')
        else:
            self.view.config(bg = 'green')

        self.view.pack(side = tk.RIGHT)

    def destroy(self):
        self.view.destroy()