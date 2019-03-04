class TicTacToe:
    def __init__(self, turn=-1):
        self.board = [[0,0,0],
                      [0,0,0],
                      [0,0,0]]
        self.turn = turn
        self.state = 'ongoing'

    def display(self):
        for i in range(3):
            row_res = ''
            for j in range(3):
                if self.board[i][j] == 0:
                    row_res += ' - '
                elif self.board[i][j] == -1:
                    row_res += ' X '
                elif self.board[i][j] == 1:
                    row_res += ' O '
            print(row_res)
        print('________')

    def check_victory(self):
        for row in self.board:
            rs = sum(row)
            if rs == 3:
                self.state = 'over'
                return (True, 'O', 1)
            elif rs == -3:
                self.state = 'over'
                return (True, 'X', -1)

        for i in range(3):
            cs = self.board[0][i] + self.board[1][i] + self.board[2][i]
            if cs == 3:
                self.state = 'over'
                return (True, 'O', 1)
            elif cs == -3:
                self.state = 'over'
                return (True, 'X', -1)

        diag1 = sum([self.board[x][x] for x in range(3)])
        diag2 = sum([self.board[2-x][x] for x in range(3)])

        if diag1 == 3:
            self.state = 'over'
            return (True, 'O', 1)
        elif diag1 == -3:
            self.state = 'over'
            return (True, 'X', -1)

        if diag2 == 3:
            self.state = 'over'
            return (True, 'O', 1)
        elif diag2 == -3:
            self.state = 'over'
            return (True, 'X', -1)

        return (False, '', 0)

    def make_move(self, x, y):
        if self.board[x][y] == 0:
            self.board[x][y] = self.turn
        else:
            print("Invalid move at x:",x,"y:",y)
            return
        res = self.check_victory()
        if res[0]:
            print("Game Over",res[1],"won")
        else:
            self.turn = -self.turn


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def find_moves(self, board):
        moves = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    moves.append((i,j))
        return moves

    def find_best_move(self,board):
        best_move = None
        highest_value = -10000

        for move in self.find_moves(board):
            board[move[0]][move[1]] = self.symbol
            value = self.minimax(board)
            if value >= highest_value:
                highest_value = value
                best_move = move
            board[move[0]][move[1]] = 0


        return best_move

    def minimax(self, board, depth=0, is_max_player=False):
        status = self.check_victory(board)
        if status[0]:
            if self.symbol == status[2]:
                return 10 - depth
            else:
                return -10 + depth

        if not self.moves_left(board):
            return 0

        if is_max_player:
            best_val = -1000
            for move in self.find_moves(board):
                board[move[0]][move[1]] = self.symbol
                value = self.minimax(board,depth+1,False)
                best_val = max(value,best_val)
                board[move[0]][move[1]] = 0
            return best_val
        else:
            best_val = 1000
            for move in self.find_moves(board):
                board[move[0]][move[1]] = -1*self.symbol
                value = self.minimax(board,depth+1,True)
                best_val = min(value,best_val)
                board[move[0]][move[1]] = 0
            return best_val


    def check_victory(self, board):
        for row in board:
            rs = sum(row)
            if rs == 3:
                return (True, 'O', 1)
            elif rs == -3:
                return (True, 'X', -1)

        for i in range(3):
            cs = board[0][i] + board[1][i] + board[2][i]
            if cs == 3:
                return (True, 'O', 1)
            elif cs == -3:
                return (True, 'X', -1)

        diag1 = sum([board[x][x] for x in range(3)])
        diag2 = sum([board[2-x][x] for x in range(3)])

        if diag1 == 3:
            return (True, 'O', 1)
        elif diag1 == -3:
            return (True, 'X', -1)

        if diag2 == 3:
            return (True, 'O', 1)
        elif diag2 == -3:
            return (True, 'X', -1)

        return (False, '', 0)

    def moves_left(self,board):
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    return True
        return False


    def display(self,board):
        for i in range(3):
            row_res = ''
            for j in range(3):
                if board[i][j] == 0:
                    row_res += ' - '
                elif board[i][j] == -1:
                    row_res += ' X '
                elif board[i][j] == 1:
                    row_res += ' O '
            print(row_res)
        print('_________')

t = TicTacToe()
t.display()
p = Player(-1)
while t.state == 'ongoing':
    move = p.find_best_move(t.board)
    t.make_move(move[0],move[1])
    t.display()
    if t.state != 'ongoing':
        break
    x = int(input('Row : '))
    y = int(input('Col : '))
    t.make_move(x,y)
    t.display()
