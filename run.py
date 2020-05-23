import time

import config
import controls

from grid import Grid
from figure import Figure

# Создаём саму сетку игры (Стакан)
grid = Grid()

while True:
    figure = Figure(grid)
    figure.checkLose()

    # Горячие клавиши управления фигурой
    controls.update(figure)

    # Цикл падения фигуры
    while figure.statusDecline:
        figure.declineCheckConditions()
        time.sleep(grid.level()["time_sleep"])

    # Последний раз вызываем, для того что бы встало на место
    figure.declineMethod()
    figure.insertFigureInGrid()
