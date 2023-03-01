class Square:

    def __init__(self, x, y, value=None) -> None:
        self.x = x
        self.y = y
        self.value = value

    def __str__(self) -> str:
        return f"({self.x}, {self.y} = {self.value})"


class Matrix:  # This is a MaTriX XD

    @staticmethod
    def fromMatrix(matrix: list[list[Square]]) -> Matrix:
        m = Matrix(len(matrix), len(matrix[0]), False)
        m.__matrix = matrix
        return m

    def __init__(self, rows: int = 0, columns: int = -1, generate: bool = True) -> None:
        self.__rows = rows
        self.__columns = columns if columns != -1 else rows
        self.__matrix = []
        if generate:
            self.__generate()

    def __generate(self) -> None:
        for y in range(self.__rows):
            self.__matrix.append([Square(x, y) for x in range(self.__columns)])

    def __str__(self) -> str:
        return "\n".join([" ".join([str(square.value) for square in row]) for row in self.__matrix])

    @property
    def rows(self) -> int:
        return self.__rows

    @property
    def columns(self) -> int:
        return self.__columns

    def setRows(self, rows: int) -> None:
        self.__updateMatrix(rows, self.__columns)

    def setColumns(self, columns: int) -> None:
        self.__updateMatrix(self.__rows, columns)

    def setSquare(self, x: int, y: int, value) -> None:
        self.__updateMatrix(max(y+1, self.__rows), max(x+1, self.__columns))
        try:
            self.__matrix[y][x].value = value
        except:
            self.__matrix[y][x] = Square(x, y, value)

    def setSquareRaw(self, square: Square) -> None:
        x = square.x
        y = square.y

        self.__updateMatrix(max(y+1, self.__rows), max(x+1, self.__columns))
        self.__matrix[y][x] = square

    def __updateMatrix(self, rows: int, columns: int) -> None:
        if self.__rows != rows:
            if rows > self.__rows:
                for y in range(self.__rows, rows):
                    self.__matrix.append([Square(x, y)
                                         for x in range(self.__columns)])
            else:
                for y in range(rows, self.__rows):
                    del self.__matrix[y]
            self.__rows = rows

        if self.__columns != columns:
            if columns > self.__columns:
                for y, row in enumerate(self.__matrix):
                    row.extend([Square(x, y)
                               for x in range(self.__columns, columns)])
            else:
                for row in self.__matrix:
                    for x in range(columns, self.__columns):
                        del row[x]
            self.__columns = columns

    def isSquare(self, x: int, y: int, realResult: bool = False):
        if not realResult:
            return (x > 0 and x < self.__columns and y > 0 and y < self.__rows)

        try:
            a = self.__matrix[y][x]
            return not a is None
        except:
            return False

    def getSquare(self, x: int, y: int, newSquareIfOutside: bool = False) -> Square or None:
        if self.isSquare(x, y, True):
            return self.__matrix[y][x]
        if newSquareIfOutside and not self.isSquare(x, y):
            return Square(x, y)
        s = Square(x, y)
        self.setSquareRaw(s)

    def getWindow(self, m_x: int, m_y: int, size: int, onlyHorizontalAndVertical: bool = False) -> list[Square]:
        ws = size//2
        possible_x = list(range(m_x - ws, m_x + ws + 1))
        possible_y = list(range(m_y - ws, m_y + ws + 1))

        for y in possible_y:
            for x in possible_x:
                if onlyHorizontalAndVertical and (y != m_y and x != m_x):
                    continue
                s = self.getSquare(x, y)
                if s is not None:
                    yield s

    @property
    def squares(self) -> list[Square]:
        for row in self.__matrix:
            for c in row:
                yield c

    def getSquaresInZone(self, x1: int, y1: int, x2: int, y2: int) -> list[Square]:
        return self.getMatrixOfZone(x1, y1, x2, y2).squares

    def getMatrixOfZone(self, x1: int, y1: int, x2: int, y2: int) -> Matrix:
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1

        cm = [row.copy() for row in self.__matrix]
        for _ in range(y2 + 1, self.__rows):
            del cm[y2+1]
        for _ in range(0, y1):
            del cm[0]
        for _ in range(x2 + 1, self.__columns):
            for row in cm:
                del row[x2+1]
        for _ in range(0, x1):
            for row in cm:
                del row[0]

        return Matrix.fromMatrix(cm)
