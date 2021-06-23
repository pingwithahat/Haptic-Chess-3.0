# 2021/06/23
# This code tests: specifically defining 'the process' as a function that you can call in an if statement.

from stockfish import Stockfish


class Position(Stockfish):
    number_of_positions = 0

    quit = 1

    tactics_list_in_Position = [
        "4r1k1/p4p2/1r4pp/2pQ2q1/1P4n1/2P3P1/P1B2PP1/1R1R2K1 b - - 0 0",
        # The best move for this FEN is e8e1.
        "2r2rk1/pp3ppp/3p4/5Q2/2BP4/1N2q3/PP4PP/2R4K w - - 0 0",
        # The best move for this FEN is c4f7.
        "r3nrk1/p1pq1pbp/3p4/2p1P1N1/5Pb1/1P6/PBP1Q1N1/4RRK1 w - - 0 0",  # Qe4Bf5
        "r3kb1r/1pqb1ppp/p1p1p3/2PpP3/N3Pn2/2QB1N2/PP3PPP/R4RK1 b - - 0 0",  # dxc4 Bc4
        "6k1/4p1b1/5p2/2q1pP1Q/8/7R/6PP/2r2R1K w - - 0 0"  # h5e8
    ]

    def __init__(self, name: str = "", index: int = 0, path: str = 'stockfish_13_win_x64_bmi2.exe', depth: int = 26,
                 parameters: dict = None):
        super().__init__(path, depth, parameters)
        self.name = name
        self.is_SF = True  # will show best move by default if just '.bm' is called
        Position.add_to_number_of_positions()

    @classmethod
    def add_to_number_of_positions(cls):
        cls.number_of_positions += 1

    def SF(self):
        while Position.quit:
            user_input = input("What position type? Single-position analysis [S] or Multi-position analysis [M]?")
            # if user_input == 'Quit' or 'quit' or 'Q' or 'q':
            #     Position.quit = 0
            # elif user_input == 'S' or 's':
            if user_input == 'S' or 's':
                user_input = input("Please enter position number you would like:    ['M' for Multi-position analysis]")
                if user_input == 'M' or 'm' or 'cancel' or 'Cancel':
                    self.SF()  # will this make the code loop successfully when a user tries to change from S to M
                    pass

                elif user_input == 'Quit' or 'quit' or 'Q' or 'q':
                    Position.quit = 0

                elif int(float(user_input)) >= 0 & int(
                        float(user_input)) <= Position.number_of_positions:  # so the input
                    # needs to be first passed through the float conversion, before the int conversion, or it will throw
                    # up an error: "ValueError: invalid literal for int() with base 10: 'M'"
                    self.set_fen_position(Position.tactics_list_in_Position[int(float(user_input))])
                    self.bm()
                    print(self.get_board_visual())
                    # code will go here to prepare for move to be transmitted over BLE to Buzz
                    # how to check if user input is a valid move?
                    # input("Please enter your move:")
                elif int(user_input) < 0 | int(user_input) > Position.number_of_positions:
                    # have code here that loops back to asking what position number you would like and a prompt to choose a
                    # higher number or a lower number, respectfully
                    pass

            elif user_input == 'M' or 'm':
                user_input = input(
                    "Please enter the first position to cycle through: [insert range option 0-??]  ['S' for"
                    "Single-position analysis]")
                if user_input == 'S' or 's':
                    self.SF()
                elif int(float(user_input)) >= 0 & int(
                        float(user_input)) <= Position.number_of_positions:  # so the input
                    # needs to be first passed through the float conversion, before the int conversion, or it will throw
                    # up an error: "ValueError: invalid literal for int() with base 10: 'M'"
                    self.set_fen_position(Position.tactics_list_in_Position[int(float(user_input))])
                    self.bm()
                    print(self.get_board_visual())
                    # code will go here to prepare for move to be transmitted over BLE to Buzz
                    # how to check if user input is a valid move?
                    # input("Please enter your move:")














    def bm(self):
        if self.is_SF:  # if it is true then it check ' == True' anyway, same with False
            print(self.get_best_move())
        else:
            return


iop = Position()
print(iop.SF())
# iop.bm()

