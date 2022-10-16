import pynput.keyboard as kb
import random
import time
import threading
from tkinter import *
from tkinter import messagebox

keyboard = kb.Controller()
running = False

event = time.time()
def start():
    global running
    running = True


def stop():
    global running
    running = False


def random_press(y):  # Fonction qui permet de rester appuyer sur une touche pendant 0.5sec
    timer = 0
    while timer < random.uniform(0.5, 0.8):
        time.sleep(0.1)
        timer += 0.1
        keyboard.press(y)
    keyboard.release(y)


y = 0


def truc():
    global event
    event = time.time()
    x = random.randint(1, 4)  # Et attends de 2 min a 3 min pour le refaire
    if x == 1:
        random_press('z')
    elif x == 2:
        random_press('q')
    elif x == 3:
        random_press('s')
    elif x == 4:
        random_press('d')
    test()


def event_minute_later(event, a):
    return event + a < time.time()

def test():
    global y
    y = random.randint(200, 300)

def showMsg():
    global y
    if running:
        if event_minute_later(event, y):
            truc()
    root.after(10, showMsg)


def start():
    global running
    global w2
    w2.destroy()
    w2 = Label(root, text="En pleine session AFK la , sale tricheur")
    w2.grid()
    running = True
    test()


def stop():
    global running
    global w2
    running = False
    w2.destroy()
    w2 = Label(root, text="L'AFK est pas lancé fdp")
    w2.grid()


root = Tk()
root.title("BOT FF ANTI AFK UWU HIHIIH VIVE BUS <3")
root.geometry("400x100")
w = Label(root, text="SALUT ALORS CLIQUUE QUAND TU ES SOLO ET QUE TU VEUX AFK <3")
app = Frame(root)
app.grid()

w2 = Label(root, text="L'AFK est pas lancé fdp")
w2.grid()

start = Button(app, text="Début de l'AFK", command=start)
stop = Button(app, text="Fin de l'AFK", command=stop)

start.grid()
stop.grid()

root.after(1000, showMsg)  # After 1 second, call scanning
root.mainloop()
