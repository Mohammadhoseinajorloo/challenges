import random 

class LenException(BaseException):
    pass

class Color:
    CRED    = '\33[31m'
    CYELLOW = '\33[33m'
    CEND    = '\33[0m'

class Board:

    COLUMN = "abcdefglm" 
    ROW = "123456789"

    def __init__(self):
       self.__board = {row:{col:'.' for col in Board.COLUMN} for row in Board.ROW}
       self.__board = self._fill_board_by_multipl_symbol(Board.COLUMN, Board.ROW)


    def _fill_board_by_multipl_symbol(self, columns, rows):
        loc_list = []
        for i in range(10):
            c = str(random.sample(columns, 1)[0])
            r = str(random.sample(rows, 1)[0])
            self.__board[c][r] = "x"
      

    def __repr__(self):
        text = ""
        for row in self.__board:
            line = " ".join(self.__board[row].values())
            text = f' {Color.CRED}{row:<2}{Color.CEND}{line}\n{text}'
        text += f'   {Color.CYELLOW}{" ".join([x for x in COLUMN])}{Color.CEND}'
        return text

    def __getitem__(self, loc:str):
        if len(loc) != 2:
            raise LenException(f'lenght of loc string is not valid.your len loc:{len(loc)}')
        row, col = loc
        return self.__board[col][row]

    def __setitem__(self, loc:str, value):
        if len(loc) != 2:
            raise LenException(f'lenght of loc string is not valid.your len loc:{len(loc)}')
        row, col = loc
        self.__board[col][row] = value


def main():
    board = Board()
    print(board)

if __name__ == "__main__":
    main()
