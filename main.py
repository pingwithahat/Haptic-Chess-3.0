# # This code tests to see if you can define a class as an input to another class.
#
#
# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#
#         def get_grade(self):
#             return self.grade
#
#
# class Course:
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []
#
#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False
#
#     def get_average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()
#
#         return value / len(self.students)
#
# MechENG = Course('Mechanical Engineering', 7)
# MechENG.add_student(Student('Emanuel', 24, '2:1'))
# print(MechENG.students[0].name)

#######################################################################################################################

# This code tests if it is best to store the arrays of positions in each instance or in the class in general

from stockfish import Stockfish


class Position(Stockfish):
    number_of_positions = 0

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
        user_input = input("What position type? Single position analysis [S] or Multi-position analysis [M]?")
        if user_input == 'S' or 's':
            user_input = input("Please enter position number you would like:    ['M' for Multi-position analysis]")
            if int(user_input) >= 0 & int(user_input) <= Position.number_of_positions:
                self.set_fen_position(Position.tactics_list_in_Position[int(user_input)])
                self.bm()
                print(self.get_board_visual())
                # code will go here to prepare for move to be transmitted over BLE to Buzz
                # how to check if user input is a valid move?
                # input("Please enter your move:")
            if int(user_input) < 0 | int(user_input) > Position.number_of_positions:
                # have code here that loops back to asking what position number you would like and a prompt to choose a
                # higher number or a lower number, respectfully
                pass

            elif user_input == 'M':
                self.SF()  # will this make the code loop successfully when a user tries to change from S to M
                pass

        # This is code in this function that was working on [2021/06/19]

        # self.position_number = input("What position number to start?")
        # if int(self.position_number) < len(Position.tactics_list_in_Position):
        #     self.set_fen_position(Position.tactics_list_in_Position[int(self.position_number)])
        #     # Doesn't yet do anything with the chosen position.
        #     self.is_SF = True
        #     self.bm()
        #     self.position_number_end = input("What position number to end?")
        #     if int(self.position_number_end) < len(Position.tactics_list_in_Position) & int(self.position_number_end) > int(self.position_number):
        #
        #         pass
        #     # Also needs an option for just the single position - otherwise needs to cycle to the chosen number unless
        #     # the end number is too high. Either cycle to highest possible number or ask for new number.
        # elif int(self.position_number) >= len(Position.tactics_list_in_Position):
        #     print("Position value not found.")
        #     self.is_SF = False
        #     return

    def bm(self):
        if self.is_SF:  # if it is true then it check ' == True' anyway, same with False
            print(self.get_best_move())
        else:
            return


iop = Position()
print(iop.SF())
# iop.bm()


# Working but could run into trouble with '.is_SF()' needing to be 'True' for '.bm()' to work.
# Below will manually input instances of each 'Position' class in a list to be called upon (e.g. to find the best move).

# array_of_instances = []
#
# array_of_instances2 = []
#
# array_of_instances.append(Position("",0))
# array_of_instances.append(Position("",1))
# array_of_instances.append(Position("",2))
#
# print(array_of_instances)
# for instances in array_of_instances:
#     instances.bm()


#
# array_of_instances[0].set_fen_position(Position.tactics_list_in_Position[0])
# print(array_of_instances[0].get_best_move())


# Will print the FEN positions and the 'best move' of each position in 'Position.tactics_list_in_Position'.
# for positions in Position.tactics_list_in_Position:
#     iop.set_fen_position(positions)
#     print(positions)
#     iop.bm()
#     array_of_instances2.append(Position(positions))

# print(array_of_instances2)
# This will save an instance of each 'Position' class which can be called upon in the list 'array_of_instances2'.
