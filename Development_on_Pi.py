import asyncio, io, base64, time, board, requests
import numpy as np

import matplotlib.pyplot as plt
from PIL import Image
from bleak import BleakClient
from bleak import discover
from neosensory_python import NeoDevice

from stockfish import Stockfish


def notification_handler(sender, data):
    print("{0}: {1}".format(sender, data))


async def run(loop):
    # "X" will  get overwritten if a Buzz is found
    buzz_addr = "X"  # e.g. "EB:CA:85:38:19:1D"
    devices = await discover()
    for d in devices:
        if str(d).find("Buzz") > 0:
            print("Found a Buzz! " + str(d) +
                  "\r\nAddress substring: " + str(d)[:17])
            # set the address to a found Buzz
            buzz_addr = str(d)[:17]

    async with BleakClient(buzz_addr, loop=loop) as client:

        my_buzz = NeoDevice(client)

        await asyncio.sleep(1)

        x = await client.is_connected()
        print("Connection State: {0}\r\n".format(x))

        await my_buzz.enable_notifications(notification_handler)

        await asyncio.sleep(1)

        await my_buzz.request_developer_authorization()

        await my_buzz.accept_developer_api_terms()

        await my_buzz.pause_device_algorithm()

        sweep_left = [255, 0, 0, 0, 0, 255, 0, 0, 0, 0, 255, 0, 0, 0, 0, 255, 0, 0, 0, 0]
        sweep_right = [0, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0]
        sweep_centre = [255, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 255, 0, 0, 255, 0, 0, 0, 0, 0]

        try:
            while True:
                try:

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
                                elif int(float(user_input)) < 0 or int(float(user_input)) >= len(
                                        Position.tactics_list_in_Position):
                                    print('Invalid user input')
                                    self.load_position()
                            elif self.current_mode == 'M':
                                print(
                                    'multi-position learning not available at this time (i.e. not needed for Stage I)')
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





                    iop = Position()
                    iop.load_position


                except:
                    pass






                    # end_request=time.time()
                    # print("total request time: " + str(end_request - start_request))

            print("still buzzing")

        # except KeyboardInterrupt:
        #     await my_buzz.resume_device_algorithm()
        #     pass
        except:
            pass


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))

#####

# This section of code is taken from Development on 2021/07/02

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
        # self.load_position()

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


    # def load_position(self):
    #     try:
    #         if self.current_mode == 'S':
    #             user_input = input('Position to load:    ')
    #             if 0 <= int(float(user_input)) < len(Position.tactics_list_in_Position):
    #                 self.name = Position.tactics_list_in_Position[int(float(user_input))]
    #                 self.set_fen_position(self.name)
    #                 print(self.name)
    #                 print(self.get_board_visual())
    #                 # code to send signal to buzz
    #
    #                 self.request_user_move()
    #             elif int(float(user_input)) < 0 or int(float(user_input)) >= len(Position.tactics_list_in_Position):
    #                 print('Invalid user input')
    #                 self.load_position()
    #         elif self.current_mode == 'M':
    #             print('multi-position learning not available at this time (i.e. not needed for Stage I)')
    #             # code will go here for selecting a start and end position, making sure that no invalid input is given
    #             pass
    #     except ValueError:
    #         print('Invalid user input')
    #         self.load_position()

    # def request_user_move(self):
    #     try:
    #         user_best_move = input('Best move:     ')
    #         if self.is_move_correct(user_best_move):
    #             print('Correct move!')
    #             self.make_moves_from_current_position([user_best_move])
    #             self.load_position()
    #         else:
    #             print('Wrong move')
    #             # code to send best move to buzz
    #             self.request_user_move()
    #     except:
    #         pass

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



#####