from PIL import Image, ImageDraw
from Other.constants import Constants


class Board:
    """
    represents the word hunt board
    """

    def __init__(self, chars: str, rows: int, cols: int):
        self.board = [[""] * cols] * rows
        if cols * rows != len(chars):
            raise Exception(f"len of chars:{chars} does not equal rows: {cols} * cols: {cols} ")

        self.make_board(rows, cols, chars)

    def make_board(self, rows, cols, chars):
        """
        Places the given chars in a row-col traversal
        :param rows: the number of rows in the board
        :param cols:  the number of columns in the board
        :param chars:  the chars to be placed in the positions.
        EFFECT: edits the rows field
        """
        counter = 0
        for r in rows:
            for c in cols:
                self.rows[r][c] = chars[counter]
                counter += 1

    def __draw_board(self) -> Image:
        """
        draws this board
        :return: this board
        """
        for r in range(len(self.board)):
            for c in range(len(r)):
                image = Image.new("RGB", (r * Constants.SCALE_FACTOR, c * Constants.SCALE_FACTOR))
                draw = ImageDraw.Draw(image)
                offset_y = r * Constants.SCALE_FACTOR
                offset_x = c * Constants.SCALE_FACTOR
                draw.rectangle((offset_x, offset_y, offset_x + Constants.SCALE_FACTOR,
                                offset_y + Constants.SCALE_FACTOR), fill="red")
                text = self.board[r][c]
                return draw.text((offset_x + 0.5 * Constants.SCALE_FACTOR,
                                  offset_y + 0.5 * Constants.SCALE_FACTOR, text))

    def show_board(self):
        """
        shows this board outputting a window
        """
        self.__draw_board().show()

