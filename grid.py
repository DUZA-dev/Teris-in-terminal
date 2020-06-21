import os

import config

# For calculations range score
SI_WL = lambda nLevel: config.SCORE_INCREMENT * config.WEIGHT_LEVELS * nLevel
levels = [
    {
        'level': nLevel,
        'range_score': range(SI_WL(nLevel), SI_WL(nLevel+1)),
        'time_sleep': 1 / config.COUNT_LEVELS * (config.COUNT_LEVELS - nLevel)
    } for nLevel in range(config.COUNT_LEVELS)
]

class Grid:
    def __init__(self):
        self.score = config.START_SCORE_VALUE

        self.matrix = [[0 for x in range(config.WEIGHT_GRID)] for y in range(config.HEIGHT_GRID)]

        # Текущий уровень
        self.level = lambda: next((level for level in levels
                                   if self.score in level["range_score"]))

    def print_grid(self, figure):
        gameStr = ""

        countHiddenLines = config.COUNT_HIDDEN_LINES

        figureRangeY = range(figure.figureXY['y1'], figure.figureXY['y2'])
        figureRangeX = range(figure.figureXY['x1'], figure.figureXY['x2'])

        yIndexFigure = 0
        for yIndexMatrix, yMatrix in enumerate(self.matrix):
            if yIndexMatrix < config.COUNT_HIDDEN_LINES:
                continue

            xIndexFigure = 0
            for xIndexMatrix, xMatrix in enumerate(yMatrix):

                # Если координата матрицы - является координатой фигуры
                if (yIndexMatrix in figureRangeY) and (xIndexMatrix in figureRangeX):
                    figureBlock = figure.figure[yIndexFigure][xIndexFigure]

                    # Если блок является частью фигуры
                    if figureBlock:
                        gameStr += config.ACTIVE_FIGURE
                    elif not xMatrix:
                        gameStr += config.BACKGROUND_MATRIX
                    else:
                        gameStr += config.FIGURE_ON_MATRIX

                    xIndexFigure += 1
                elif xMatrix:
                    # Если в этой координате лежит часть уже упавшей фигуры
                    gameStr += config.FIGURE_ON_MATRIX
                else:
                    gameStr += config.BACKGROUND_MATRIX

            if xIndexFigure != 0:
                xIndexFigure = 0
                yIndexFigure += 1

            gameStr += "\n"

        # Очищаем консоль от старых данных
        os.system('clear')

        print(
            gameStr,
            'Score: %i' % self.score,
            'Level: %i' %  self.level()["level"],
            sep="\n"
        )

    def cleanCollectedLine(self, indexLineY):
        ''' Удаляет собранную линию и добавляет очки '''

        countBlocks = self.matrix[indexLineY].count(1)
        if countBlocks == config.WEIGHT_GRID:
            del self.matrix[indexLineY]
            self.matrix.insert(0, [0 for i in range(config.WEIGHT_GRID)])

            self.score += config.SCORE_INCREMENT

    def checkLose(self):
        figureRangeY = range(self.figureXY['y1'], self.figureXY['y2'])
        figureRangeX = range(self.figureXY['x1'], self.figureXY['x2'])

        for yCoord in figureRangeY:
            for xCoord in figureRangeX:
                if grid.matrix[yCoord][xCoord] == 1:
                    exit('\nLosing!')
