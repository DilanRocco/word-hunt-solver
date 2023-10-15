from PIL import Image, ImageDraw, ImageFont
from Other.constants import Constants


class Board:
    """
    represents the word hunt board
    """

    def __init__(self, chars: str, rows: int, cols: int):
        if cols * rows != len(chars):
            raise Exception(f"len of chars:{len(chars)} does not equal rows: {cols} * cols: {cols} ")

        self.board = []
        self.make_board(rows, cols, chars)
        self.num_of_rows = rows
        self.num_of_cols = cols

    def make_board(self, rows, cols, chars):
        """
        Places the given chars in a row-col traversal
        :param rows: the number of rows in the board
        :param cols:  the number of columns in the board
        :param chars:  the chars to be placed in the positions.
        EFFECT: edits the rows field
        """
        counter = 0
        for _ in range(rows):
            row = []
            self.board.append(row)
            for _ in range(cols):
                row.append(chars[counter].upper())
                counter += 1

    def __draw_board(self) -> Image:
        """
        draws this board
        :return: this board
        """
        image = Image.new("RGB", (self.num_of_cols * Constants.SCALE_FACTOR, self.num_of_rows * Constants.SCALE_FACTOR))

        draw = ImageDraw.Draw(image)
        for r in range(self.num_of_rows):
            for c in range(self.num_of_cols):
                offset_y = r * Constants.SCALE_FACTOR
                offset_x = c * Constants.SCALE_FACTOR
                draw.rectangle((offset_x, offset_y, offset_x + Constants.SCALE_FACTOR,
                                offset_y + Constants.SCALE_FACTOR), fill="yellow", outline="black")
                text = self.board[r][c]
                font = ImageFont.truetype("Other/KommonGrotesk-UltraBold.ttf", 45)
                draw.text((offset_x + 0.4 * Constants.SCALE_FACTOR,
                           offset_y + 0.4 * Constants.SCALE_FACTOR), font=font, text=text, fill="black")
        return image

    def show_board(self):
        """
        shows this board outputting a window
        """
        self.__draw_board().show()
