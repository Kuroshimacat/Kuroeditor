import os

clearConsole = lambda: os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear'
)
clearConsole()
path = input("where: ")
clearConsole()
def read(path):
    try:
        with open(path ,encoding='utf-8') as file_object:
#            lines = file_object.readlines()
            for line in file_object:
                print(line.rstrip())
    except OSError:
        print("Bad path")

read(path=path)