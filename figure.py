import random

import config

class Figure:
    def __init__(self, grid):
        # Выбираем рандомно фигуру и вытаскиваем её положения
        self.figurePositions = config.FIGURES[random.randint(1, len(config.FIGURES))]
        # Положение по умолчанию стоит 0
        self.figurePosition = 0
        # Выбираем данную позицию
        self.figure = self.figurePositions[self.figurePosition]
        # Устанавливаем начальные координаты фигуры
        self.figureXY = {
            'x1': 4,
            'y1': 0,
            'x2': len(self.figure[0])+4,
            'y2': len(self.figure),
        }

        self.grid = grid
        self.statusDecline = True


    def declineMethod(self):
        ''' Опускает фигуру, увеличивая её координаты проекции на сетку '''
        self.figureXY['y1']  += 1
        self.figureXY['y2']  += 1

        self.grid.print_grid(self)

    def insertFigureInGrid(self):
        ''' Вставляем фигуру в сетку игры '''

        # Создаём диапазоны значений координат сетки, в которые нужно будет
        # произвести вставку фигуры.
        figureRangeY = range(self.figureXY['y1'], self.figureXY['y2'])
        figureRangeX = range(self.figureXY['x1'], self.figureXY['x2'])

        # FigureLineY&FigureLineX - для вставляемых значений фигуры и сетки.
        figureLineY  = 0
        for y in figureRangeY:
            figureLineX = 0
            for x in figureRangeX:
                if self.figure[figureLineY][figureLineX]:
                    # Если значение координаты фигуры - не равно 0, то
                    # вставляем его в сетку.
                    self.grid.matrix[y][x] = 1
                figureLineX += 1
            self.grid.cleanCollectedLine(y)
            figureLineY += 1

    def declineCheckConditions(self):
        '''
        Проверяет нижнюю линию на присутствие блоков, если они стоят - опускаем
        фигуру вниз, ставим её, и выходим из главного цикла работы с фигурой,
        если нету - меняем координаты её видимости (y1, y2).
        '''
        try:
            # Беру линию находящуюся под фигурой
            mainline = self.grid.matrix[self.figureXY['y2']+1]

            # Инкрементация, дальше будет цикл for, который начнёт перебирать
            # значения нижней линии сетки и сравнивать со значением нижней
            # линии фигуры, если каждый из них будет равен 1 - обрывает
            # выполнение функции, и устанавливает статус опускания фигуры
            # в False.
            figureLineX = 0

            for mlKey in range(self.figureXY['x1'],self.figureXY['x2']):
                ml = mainline[mlKey]
                if ml and self.figure[-1][figureLineX] == 1:
                    self.statusDecline = False
                    return
                figureLineX += 1

            # Опускаем фигуру
            self.declineMethod()
        except IndexError:
            # Реагирует на начало стакана, обрывает выполнение и меняет статус
            # падения фигуры
            self.statusDecline = False
            return


    def moving(self, side):
        ''' Перемещает фигуру вправо или влево, если в той стороне нет помех '''

        # FigureLineY, для цикла for, который начнёт перебирать
        # значения всех линий сетки по Yn, в пределах которогых находится
        # фигура (определены в mainlines, работа через yline).

        mainlines = [self.grid.matrix[y] for y in range(self.figureXY['y1'], self.figureXY['y2'])]

        figureLineY = 0

        if side == 'left':
            # Индекс блока, находящегося слева от блока фигуры и его проверка
            # на случай попытки выходка за границы сетки
            xIndexChar = self.figureXY['x1']-1
            if xIndexChar < 0:
                return False

            for yline in mainlines:
                xchar = yline[xIndexChar]

                # Проверяем, нет ли слева блока, который может помешать.
                if xchar == 1 and self.figure[figureLineY][0] == 1:
                    return False
                figureLineY += 1

            # Перемещение влево
            self.figureXY['x1'] -= 1
            self.figureXY['x2'] -= 1

        elif side == 'right':
            # Индекс блока, находящегося справа от блока фигуры и его проверка
            # на случай попытки выхода за границы сетки
            xIndexChar = self.figureXY['x2']
            if xIndexChar > config.WEIGHT_GRID-1:
                return False

            for yline in mainlines:
                xchar = yline[xIndexChar]

                # Проверяем, нет ли спрва блока, который может помешать.
                if xchar == 1 and self.figure[figureLineY][-1] == 1:
                    return False
                figureLineY += 1

            # Перемещение вправо
            self.figureXY['x1'] += 1
            self.figureXY['x2'] += 1

        self.grid.print_grid(self)

    def coup(self):
        ''' Меняем положение фигуры '''

        # Инкрементируем идекс позиции
        self.figurePosition += 1

        # Вытаскиваем значение и устанавливаем его фигуре, если его нет, то
        # возвращаемся в позицию по умолчанию
        try:
            self.figure = self.figurePositions[self.figurePosition]
        except IndexError:
            self.figurePosition = 0
            self.figure = self.figurePositions[self.figurePosition]

        # Устанавливаем новые координты фигуры, т.к при изменении её размер
        # может меняться.
        self.figureXY['x2'] = len(self.figure[-1]) + self.figureXY['x1']
        self.figureXY['y2'] = len(self.figure) + self.figureXY['y1']

        # Сразу выводим, что бы не заставлять ждать пользователя появления
        # позиции.
        self.grid.print_grid(self)

    def checkLose(self):
        figureRangeY = range(self.figureXY['y1'], self.figureXY['y2'])
        figureRangeX = range(self.figureXY['x1'], self.figureXY['x2'])

        for yCoord in figureRangeY:
            for xCoord in figureRangeX:
                if self.grid.matrix[yCoord][xCoord] == 1:
                    print('\nLosing!')
                    exit()
