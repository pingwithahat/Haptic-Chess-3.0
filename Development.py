# 2021/06/23
# This code tests: specifically defining 'the process' as a function that you can call in a while or an if statement.

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

    # number_of_potential_positions = len(tactics_list_in_Position)

    def __init__(self, name: str = "", index: int = 0, path: str = 'stockfish_13_win_x64_bmi2.exe', depth: int = 26,
                 parameters: dict = None):
        super().__init__(path, depth, parameters)
        self.name = name
        self.is_SF = True  # will show best move by default if just '.bm' is called
        self.current_mode = "S"
        Position.add_to_number_of_positions()  # is this needed?
        self.load_position()

    @classmethod
    def add_to_number_of_positions(cls):
        cls.number_of_positions += 1

    def bm(self):
        if self.is_SF:  # if it is true then it check ' == True' anyway, same with False
            print(self.get_best_move())
        else:
            return

    def display_score(self):
        score_location = self.info.index("score")  # This will find the assigned
        score_end = self.info.index("nodes")
        score = self.info[score_location:score_end]
        print(score)

    def display_pv(self):
        # i need to find a way to isolate the 'pv' information

        pv_string_location = self.info.index(" pv ")
        pure_pv = self.info[pv_string_location:]
        pure_pv = pure_pv.replace(" pv ", "")
        print('PV: ' + pure_pv)


    # def load_position(self):  # might be more correct to use 'try except' as I am expecting the user to be correct most
    #     # of the time
    #     user_input = input('Position to load:    ')
    #     if 0 <= int(float(user_input)) < len(Position.tactics_list_in_Position):
    #         self.name = Position.tactics_list_in_Position[int(float(user_input))]
    #         self.set_fen_position(self.name)
    #         print(self.get_board_visual())
    #     elif int(float(user_input)) < 0 or int(float(user_input)) >= len(Position.tactics_list_in_Position):
    #         print('Invalid user input')
    #         self.load_position()
    #     elif ValueError:  # this doesn't work at catching the ValueError: could not convert string to float
    #         print('Invalid user input')


    def load_position(self):
        try:
            if self.current_mode == 'S':
                user_input = input('Position to load:    ')
                if 0 <= int(float(user_input)) < len(Position.tactics_list_in_Position):
                    self.name = Position.tactics_list_in_Position[int(float(user_input))]
                    self.set_fen_position(self.name)
                    print(self.name)
                    print(self.get_board_visual())
                    # code to send signal to buzz



                    self.request_user_move()
                elif int(float(user_input)) < 0 or int(float(user_input)) >= len(Position.tactics_list_in_Position):
                    print('Invalid user input')
                    self.load_position()
            elif self.current_mode == 'M':
                print('multi-position learning not available at this time (i.e. not needed for Stage I)')
                # code will go here for selecting a start and end position, making sure that no invalid input is given
                pass
        except ValueError:
            print('Invalid user input')
            self.load_position()


    def request_user_move(self):
        try:
            user_best_move = input('Best move:     ')
            if self.is_move_correct(user_best_move):
                print('Correct move!')
                self.make_moves_from_current_position([user_best_move])
                self.load_position()
            else:
                print('Wrong move')
                # code to send best move to buzz
                self.request_user_move()
        except:
            pass


    def set_mode_to_S(self, name: str = "S"):
        self.current_mode = name
        user_input = input('Mode set to [S]')
        if user_input == "M":
            self.set_mode_to_M()
        else:
            pass

    def set_mode_to_M(self, name: str = "M"):
        self.current_mode = name
        user_input = input('Mode set to [M]')
        if user_input == "S":
            self.set_mode_to_S()
        else:
            pass


    # def SF(self):
    #     try:
    #         while Position.quit:  # just removing the while loop didn't solve the 'cycling problem' (2021-06-23)
    #             user_input = input("What position type? Single-position analysis [S] or Multi-position analysis [M]?")
    #             # if user_input == 'Quit' or 'quit' or 'Q' or 'q':
    #             #     Position.quit = 0
    #     # break
    #             # elif user_input == 'S' or 's':
    #             # print(type(user_input))  # used to show that user_input is type <class 'str'>
    #             if user_input == 'S' or 's':
    #                 user_input = input(
    #                     "Please enter position number you would like:    ['M' for Multi-position analysis]")
    #                 if user_input == 'M' or 'm' or 'cancel' or 'Cancel':
    #                     self.SF()  # will this make the code loop successfully when a user tries to change from S to M
    #                     pass
    #
    #                 elif user_input == 'Quit' or 'quit' or 'Q' or 'q':
    #                     Position.quit = 0
    #                     break
    #
    #
    #                 elif int(float(user_input)) >= 0 & int(
    #                         float(user_input)) <= Position.number_of_positions:  # so the input
    #                     # needs to be first passed through the float conversion, before the int conversion, or it will throw
    #                     # up an error: "ValueError: invalid literal for int() with base 10: 'M'"
    #                     self.set_fen_position(Position.tactics_list_in_Position[int(float(user_input))])
    #                     self.bm()
    #                     print(self.get_board_visual())
    #                     # code will go here to prepare for move to be transmitted over BLE to Buzz
    #                     # how to check if user input is a valid move?
    #                     # input("Please enter your move:")
    #                 elif int(user_input) < 0 | int(user_input) > Position.number_of_positions:
    #                     # have code here that loops back to asking what position number you would like and a prompt to choose a
    #                     # higher number or a lower number, respectfully
    #                     pass
    #
    #             elif user_input == 'M' or 'm':
    #                 user_input = input(
    #                     "Please enter the first position to cycle through: [insert range option 0-??]  ['S' for"
    #                     "Single-position analysis]")
    #                 if user_input == 'S' or 's':
    #                     self.SF()
    #                 elif int(float(user_input)) >= 0 & int(
    #                         float(user_input)) <= Position.number_of_positions:  # so the input
    #                     # needs to be first passed through the float conversion, before the int conversion, or it will throw
    #                     # up an error: "ValueError: invalid literal for int() with base 10: 'M'"
    #                     self.set_fen_position(Position.tactics_list_in_Position[int(float(user_input))])
    #                     self.bm()
    #                     print(self.get_board_visual())
    #                     # code will go here to prepare for move to be transmitted over BLE to Buzz
    #                     # how to check if user input is a valid move?
    #                     # input("Please enter your move:")
    #
    #             else:
    #                 print('Unclear input; please start again. Thank you')
    #                 self.SF()  # catch to send back to beginning
    #
    #     except:
    #         print('Something went wrong.')


#######################################################################################################################

# [2021/06/25]

iop = Position()
iop.load_position()
# print(len(Position.tactics_list_in_Position))
# print(iop.name)
# iop.display_score()
# iop.display_pv()

# [2021/07/01]

# if I say 'user_input = input('test')' and then say 'if user_input >= 0: pass' will it re-prompt the user for input?
# Yes. Running the code below, the input 'test' is only printed once.

# user_input = input('test')
# if int(float(user_input)) > 10:
#     print("it's bigger than 10")
# elif user_input == "fuck":
#     pass
# elif int(float(user_input)) > 20:
#     print("it's bigger than 20")


