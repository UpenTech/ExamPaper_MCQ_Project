from colorama import Fore, Back

COLORATION = Fore.YELLOW + Back.BLUE
COLOR_RESET = Fore.RESET + Back.RESET

#Header Page of Test Paper
TITLE = COLORATION + "Class Test".upper().center(80)
HEAD = "Psychology mcq questions".upper().center(80) + COLOR_RESET

MARKS_F = "Full Marks: 100".rjust(80)
MARKS_P = "Pass Marks: 35".rjust(80)

print(TITLE)
print(HEAD)
print(MARKS_F)
print(MARKS_P)
