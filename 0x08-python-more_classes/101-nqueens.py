#!/usr/bin/python3
"""a module where the queen class is defined"""

import sys


class Nqueen:
    """the class that defines a N x N chessboard that returns
        the configuration of a solved N-queen problem"""
    board = [[]]
    res = []
    cols = set()
    p_diags = set()
    n_diags = set()

    def __init__(self, num):
        """the constructor"""
        self.__num = num
        Nqueen.board = [["_"] * self.num for _ in range(self.num)]
        Nqueen.res = []

    @property
    def num(self):
        """public instance method that returns the size of the chessboard"""
        return self.__num

    @num.setter
    def num(self, val):
        """public instance method that sets the size of the chessboard"""
        self.__num = val

    def compute_n_pos(self):
        """a public instance method that returns a solved configuration\
            of a chessboard that has an N-queen problem"""
        def solve_n_queens(r):
            """a function that holds the core algorithm to solve the\
                    N-queen problem"""
            if (r == self.num):
                tmp = ["".join(row) for row in Nqueen.board]
                n_arr = []
                for count, i in enumerate(tmp):
                    n_tmp = []
                    for i_count, j in enumerate(i):
                        if (j == "Q"):
                            n_tmp.append(count)
                            n_tmp.append(i_count)
                    n_arr.append(n_tmp)
                Nqueen.res.append(n_arr)
                return

            for col in range(self.num):
                if col in Nqueen.cols or (col - r)\
                        in Nqueen.n_diags or (col + r) in Nqueen.p_diags:
                    continue

                Nqueen.cols.add(col)
                Nqueen.p_diags.add(col + r)
                Nqueen.n_diags.add(col - r)
                Nqueen.board[r][col] = "Q"

                solve_n_queens(r + 1)
                Nqueen.cols.remove(col)
                Nqueen.p_diags.remove(col + r)
                Nqueen.n_diags.remove(col - r)
                Nqueen.board[r][col] = "_"

        solve_n_queens(0)
        return Nqueen.res


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    new_queen = Nqueen(int(sys.argv[1]))
    queen_board = new_queen.compute_n_pos()
    for pos in queen_board:
        print(pos)
