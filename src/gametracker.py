class Game:
        """
        Stores all of the information for a given tic-tac-toe game
        """
        def __init__(self) -> None:
                self.top_left = Square(0,0)
                self.top_middle = Square(0,1)
                self.top_right = Square(0,2)
                self.middle_left = Square(1,0)
                self.middle_middle = Square(1,1)
                self.middle_right = Square(1,2)
                self.bottom_left = Square(2,0)
                self.bottom_middle = Square(2,1)
                self.bottom_right = Square(2,2)
                self.squares = [
                        self.top_left,
                        self.top_middle,
                        self.top_right,
                        self.middle_left,
                        self.middle_middle,
                        self.middle_right,
                        self.bottom_left,
                        self.bottom_middle,
                        self.bottom_right
                ]

                self.top_squares = [self.top_left, self.top_middle, self.top_right]
                self.middle_squares = [self.middle_left, self.middle_middle, self.middle_right]
                self.bottom_squares = [self.bottom_left, self.bottom_middle, self.bottom_right]
                self.left_squares = [self.top_left, self.middle_left, self.bottom_left]
                self.center_squares = [self.top_middle, self.middle_middle, self.bottom_middle]
                self.right_squares = [self.top_right, self.middle_right, self.bottom_right]
                self.left_right_diagonal = [self.top_left, self.middle_middle, self.bottom_right]
                self.right_left_diagonal = [self.top_right, self.middle_middle, self.bottom_left]
                self.winner = None
        
        def update_square(self, vertical_location: int, horizontal_location: int, value: bool) -> None:
                if((vertical_location < 0) and (vertical_location > 2)): raise ValueError("The vertical location argument has an invalid value")
                if((horizontal_location < 0) and (horizontal_location > 2)): raise ValueError("The horizontal location argument has an invalid value")
                row = None
                match vertical_location:
                        case 0:
                                row = self.top_squares
                        case 1:
                                row = self.middle_squares
                        case 2:
                                row = self.bottom_squares
                row[horizontal_location].update(value)
        
        def check_for_winner(self) -> int:
                if(all(square.used == True for square in self.squares)): return 2
                checks = []
                checks.append(self.__check_line(self.top_squares))
                checks.append(self.__check_line(self.middle_squares))
                checks.append(self.__check_line(self.bottom_squares))
                checks.append(self.__check_line(self.left_squares))
                checks.append(self.__check_line(self.center_squares))
                checks.append(self.__check_line(self.right_squares))
                checks.append(self.__check_line(self.left_right_diagonal))
                checks.append(self.__check_line(self.right_left_diagonal))

                if(all(check == -1 for check in checks)):
                        return -1

                else:
                        if(any((check == 0) for check in checks)):
                                self.winner = True
                                return 0
                        if(any((check == 1) for check in checks)):
                                self.winner = False
                                return 1 # O won

        def __check_line(self, line: list) -> int:
                if(all(square.value == True for square in line)): return 0
                if(all(square.value == False for square in line)): return 1
                return -1

        def print_game(self) -> str:
                out = ""
                out = out + self.__print_row(self.top_squares) + '\n'
                out = out + self.__print_row(self.middle_squares) + '\n'
                out = out + self.__print_row(self.bottom_squares)
                return out
       
        def __print_row(self, row_list: list) -> str:
                out = ""
                for i in range(0,5):
                        out = out + row_list[0].lines[i].value
                        out = out + row_list[1].lines[i].value
                        out = out + row_list[2].lines[i].value
                        if(i != 4):
                                out = out + '\n'
                return out

class Square:
        """
        Stores the information for a square in a game
        """
        def __init__(self, vert_location: int, hor_location: int) -> None:
                if((vert_location < 0) and (vert_location > 2)): raise ValueError("The vertical location value is invalid")
                if((hor_location < 0) and (hor_location > 2)): raise ValueError("The horizontal location value is invalid")
                self.used = False
                self.value = None #True is X, False is O
                self.vertical_location = vert_location
                self.horizontal_location = hor_location
                self.lines = [
                        Line(),
                        Line(),
                        Line(),
                        Line(),
                        Line()
                ]
                        
                self.__set_borders()

        def __set_borders(self) -> None:
                """
                Private method that sets the border strings of the square
                """
                if(self.vertical_location == 1):
                        self.lines[0].update_value(True, False, False)
                        self.lines[4].update_value(True, False, False)
                if(self.horizontal_location == 1):
                        self.lines[0].update_value(False, True, True)
                        self.lines[1].update_value(False, True, True)
                        self.lines[2].update_value(False, True, True)
                        self.lines[3].update_value(False, True, True)
                        self.lines[4].update_value(False, True, True) 

        def update(self, value: bool) -> None:
                """
                Method that updates the value of the square

                Args:
                    type (int): Set to 1 to use X, set to 2 to use O

                Raises:
                    Exception: Raised if the square has already been used
                """
                if(self.used == True): raise Exception("The square has already been used")
                self.used = True
                if(value):
                        self.value = True
                        #set to X
                        self.lines[2].update_value(False, False, False, True)
                else: 
                        self.value = False
                        #set to O
                        self.lines[2].update_value(False, False, False, False)
class Line:
        def __init__(self) -> None:
                self.value = "           "
        def update_value(self, vertical: bool, left: bool, right: bool, value: bool = None) -> None:
                value_string = list(self.value)
                if(vertical == True):
                        value_string = ["-" for i in value_string]
                if(left == True): value_string[0] = "|"
                if(right == True): value_string[-1] = "|"
                if(value != None):
                        if(value):
                                value_string[5] = "X"
                        else:
                                value_string[5] = "O"
                out = ""
                for i in value_string:
                        out = out + i
                self.value = out
        

                