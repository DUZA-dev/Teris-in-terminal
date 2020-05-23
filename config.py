from colorama import Back, Style

FIGURES = {
    1: [
        [[1,1], [1,1]],
    ], # o
    2: [
        [[1], [1], [1], [1]],
        [[1,1,1,1]],
    ], # l
    3: [
        [[1,1,0], [0,1,1]],
        [[0,1], [1,1], [1,0]],
    ], # z
    4: [
        [[0,1,1], [1,1,0]],
        [[1,0], [1,1], [0,1]],
    ], # s
    5: [
        [[1,1,1], [0,1,0]],
        [[0,1], [1,1], [0, 1]],
        [[0,1,0], [1,1,1]],
        [[1,0], [1,1], [1,0]],
    ], # T
    6: [
        [[1,0], [1,0], [1,1]],
        [[1,1,1], [1,0,0]],
        [[1,1],[0,1],[0,1]],
        [[0,0,1], [1,1,1]],
    ], # L
    7: [
        [[0,1], [0,1], [1,1]],
        [[1,0,0], [1,1,1]],
        [[1,1], [1,0], [1,0]],
        [[1,1,1], [0,0,1]],
    ], # J
}

KEYS = {
    'DOWN': "down",
    'LEFT': "left",
    'RIGHT': "right",
    'UP': "up",
}

START_TIME_DECLINE_FIGURE = 1 # В секундах / In seconds

COUNT_LEVELS  = 10
WEIGHT_LEVELS = 5 # Для определения кол-ва очков для перехода на уровень

START_SCORE_VALUE = 0
SCORE_INCREMENT   = 100

WEIGHT_GRID = 10
HEIGHT_GRID = 20

COUNT_HIDDEN_LINES = 2 # Спрятанные линии сверху, от куда будет падать фигура

ACTIVE_FIGURE     = "".join([Back.BLUE,  '  ', Style.RESET_ALL])
FIGURE_ON_MATRIX  = "".join([Back.GREEN, '  ', Style.RESET_ALL])
BACKGROUND_MATRIX = "".join([Back.RED,   '  ', Style.RESET_ALL])
