
class Parachute:
    """The role of this class is to show the parachute picture
    based on how well the user responds correctly"""

    def __init__(self):
        """constructor: a list of lines, the line1 to line8 are symbols to draw the parachute, the details are shown in the show method how they will be displayed"""
        #Issue solved by the team initiated by Yves Cyril
    
        self._line1 = " / \ "
        self._line2 = " /!\ "
        self._line3 = "  o  "
        self._line4 = " \ / "
        self._line5 = "\   /"
        self._line6 = " ___ "
        self._line7 = "/   \ "
        self._line8 = " ___ "
        self._line = [self._line8, self._line7, self._line6, self._line5, self._line4, self._line3, self._line2, self._line1] 

    def _show(self,check):
        """to print the list of lines depending on the parameter called check,
        this check is an imaginary score or result of how well the user respond correctly, 
        if the answer is correct, the parachute will print a new line at the top unless that imaginary score is still equal to 8,
        if the answer is not correct, the parachute will not print the top line"""

        #when the check is equal to 3, it will be game over and the self._line3 will turns into "  x  "
        if check == 3:
            self._line[5] = "  x  "
        for i in range(8):
            if i <= (7 - check):
                continue
            parachute_img =f'\033[1;30;43m {self._line[i]} \033[0m' 
            print(parachute_img)

            


