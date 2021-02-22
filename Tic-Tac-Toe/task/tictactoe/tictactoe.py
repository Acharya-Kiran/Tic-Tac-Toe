
class TicTacToe:

    def __init__(self):
        self.game_state = " " * 9
        self.player = "X"
        self.xo_rows = [[0, 0] for _ in range(3)]
        self.xo_cols = [[0, 0] for _ in range(3)]
        self.max_xrow, self.max_orow = 0, 0
        self.max_xcol, self.max_ocol = 0, 0
        self.empty_cells = 9
        self.cx, self.cy = None, None
        self.end_game = False

    def get_input(self):
        inp_list = input("Enter the coordinates: ").strip().split()
        if len(inp_list) != 2:
            print("Enter appropriate input")
            return False
        else:
            self.cx, self.cy = inp_list
            return True

    def display_game(self):
        dashes = "---------"
        pipe = "|"
        print(dashes)
        for i in range(0, 9, 3):
            print(pipe + " " + " ".join(self.game_state[i:i + 3]) + " " + pipe)
        print(dashes)

    def process_input(self):
        if self.player == 'X':
            self.xo_rows[int(self.cx) - 1][0] += 1
            self.max_xrow = max(self.max_xrow, self.xo_rows[int(self.cx) - 1][0])
            self.xo_cols[int(self.cy) - 1][0] += 1
            self.max_xcol = max(self.max_xcol, self.xo_cols[int(self.cy) - 1][0])
            if self.max_xcol == 3 or self.max_xrow == 3 or self.check_diagonal():
                print("X wins")
                self.end_game = True
            self.player = 'O'
            self.empty_cells -= 1
        else:
            self.xo_rows[int(self.cx) - 1][1] += 1
            self.max_orow = max(self.max_orow, self.xo_rows[int(self.cx) - 1][1])
            self.xo_cols[int(self.cy) - 1][1] += 1
            self.max_ocol = max(self.max_ocol, self.xo_cols[int(self.cy) - 1][1])
            if self.max_ocol == 3 or self.max_orow == 3 or self.check_diagonal():
                print("O wins")
                self.end_game = True
            self.player = 'X'
            self.empty_cells -= 1
        if self.empty_cells == 0:
            print("Draw")
            self.end_game = True

    def check_diagonal(self):
        if self.game_state[0] == self.player and self.game_state[4] == self.player and self.game_state[8] == self.player:
            return True
        elif self.game_state[2] == self.player and self.game_state[4] == self.player and self.game_state[6] == self.player:
            return True
        return False

    def check_coordinates(self):
        flag = False
        if not self.get_input():
            return flag
        if self.cx == None and self.cy == None:
            return flag
        elif not self.cx.isdigit() or not self.cy.isdigit():
            print("You should enter numbers!")
        elif int(self.cx) < 1 or int(self.cx) > 3 or int(self.cy) < 1 or int(self.cy) > 3:
            print("Coordinates should be from 1 to 3!")
        else:
            idx = (int(self.cx) - 1) * 3 + int(self.cy) - 1
            game_list = list(self.game_state)
            if game_list[idx] == " " or game_list[idx] == "_":
                game_list[idx] = self.player
                flag = True
            else:
                print("This cell is occupied! Choose another one!")
            self.game_state = "".join(game_list)
        return flag

if __name__ == "__main__":
    tictactoe = TicTacToe()
    tictactoe.display_game()
    while not tictactoe.end_game:
        flag = False
        while not flag:
            # tictactoe.get_input()
            flag = tictactoe.check_coordinates()
        tictactoe.display_game()
        tictactoe.process_input()

    del tictactoe

    # game_state = " " * 9
    # player = 'X'
    # display_grid(game_state)
    # cx, cy = input("Enter the coordinates: ").split()
    #
    # while not process(game_state):
    #     check_flag, check_res = check_coordinates(cx, cy, player)
    #     while check_flag:
    #         print(check_res)
    #         cx, cy = input("Enter the coordinates: ").split()
    #         check_flag, check_res = check_coordinates(cx, cy, player)
    #     display_grid(game_state)
    #     if player == 'X':
    #         player = 'O'
    #     else:
    #         player = 'X'