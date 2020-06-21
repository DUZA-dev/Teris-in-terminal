import time
import threading

from grid import Grid
from figure import Figure
from controls import update as cupd

def soundplay():
    try:
        import playsound
        while True:
            playsound.playsound('./bgmusic.mp3')
    except:
        pass

threading.Thread(target=soundplay).start()


# Создаём саму сетку игры (Стакан)
grid = Grid()

while True:
    figure = Figure(grid)
    figure.checkLose()

    # Горячие клавиши управления фигурой
    cupd(figure)

    # Цикл падения фигуры
    while figure.statusDecline:
        figure.declineCheckConditions()
        time.sleep(grid.level()["time_sleep"])

    # Последний раз вызываем, для того что бы встало на место
    figure.declineMethod()
    figure.insertFigureInGrid()
