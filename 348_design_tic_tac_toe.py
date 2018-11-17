# Leetcode: 348. Design Tic-Tac-Toe
# Design a Tic-tac-toe game that is played between two players on a n x n grid.
# You may assume the following rules:
#
#     A move is guaranteed to be valid and is placed on an empty block.
#     Once a winning condition is reached, no more moves is allowed.
#     A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
#
# Example:
#
# Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.
#
# TicTacToe toe = new TicTacToe(3);
#
# toe.move(0, 0, 1); -> Returns 0 (no one wins)
# |X| | |
# | | | |    // Player 1 makes a move at (0, 0).
# | | | |
#
# toe.move(0, 2, 2); -> Returns 0 (no one wins)
# |X| |O|
# | | | |    // Player 2 makes a move at (0, 2).
# | | | |
#
# toe.move(2, 2, 1); -> Returns 0 (no one wins)
# |X| |O|
# | | | |    // Player 1 makes a move at (2, 2).
# | | |X|
#
# toe.move(1, 1, 2); -> Returns 0 (no one wins)
# |X| |O|
# | |O| |    // Player 2 makes a move at (1, 1).
# | | |X|
#
# toe.move(2, 0, 1); -> Returns 0 (no one wins)
# |X| |O|
# | |O| |    // Player 1 makes a move at (2, 0).
# |X| |X|
#
# toe.move(1, 0, 2); -> Returns 0 (no one wins)
# |X| |O|
# |O|O| |    // Player 2 makes a move at (1, 0).
# |X| |X|
#
# toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
# |X| |O|
# |O|O| |    // Player 1 makes a move at (2, 1).
# |X|X|X|
#
# Follow up:
# Could you do better than O(n2) per move() operation?
# Hint:
#
#     Could you trade extra space such that move() operation can be done in O(1)?
#     You need two arrays: int rows[n], int cols[n], plus two variables: diagonal, anti_diagonal.
#
# Solution:
# Use additional arrays rows[n], cols[n] and two variables diagonal, anti_diagonal to mark the number of Xs and Os.


class TicTacToe:
    # https://www.jianshu.com/p/1c921c15ead2
    def __init__(self, n):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.xdiag = 0

    # we use only one array for both of the players.
    # Say, if it is player 1 put one chess, add that location by 1. If it is player 2, deduce it by one.
    # Finally, if either player 1 or player 2 win, that location must be equal to n or -n.
    def move(self, row, col, player):
        val = 1 if player == 1 else -1
        self.rows[row] += val
        self.cols[col] += val
        if row == col:
            self.diag += val
        if row + col == self.n - 1:  # x-diagonal
            self.xdiag += val

        # if any of the equals to n, return player
        if abs(self.rows[row]) == self.n \
                or abs(self.cols[col]) == self.n \
                or abs(self.diag) == self.n \
                or abs(self.xdiag) == self.n:
            return player

        return 0


# /**
#  * Your TicTacToe object will be instantiated and called as such:
#  * TicTacToe obj = new TicTacToe(n);
#  * int param_1 = obj.move(row,col,player);
#  */


toe = TicTacToe(3)

print(toe.move(0, 0, 1))  # Returns 0 (no one wins)
print(toe.move(0, 2, 2))  # Returns 0 (no one wins)
print(toe.move(2, 2, 1))  # Returns 0 (no one wins)
print(toe.move(1, 1, 2))  # Returns 0 (no one wins)
print(toe.move(2, 0, 1))  # Returns 0 (no one wins)
print(toe.move(1, 0, 2))  # Returns 0 (no one wins)
print(toe.move(2, 1, 1))  # Returns 1 (player 1 wins)
