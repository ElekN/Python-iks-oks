from sys import exit

 # Empty table
table = [" "," "," "," "," "," "," "," "," "]
player = 1

    # Prints table
def printTable():
    print(table[0] + "|" + table[1] + "|" + table[2])
    print("-----")
    print(table[3] + "|" + table[4] + "|" + table[5])
    print("-----")
    print(table[6] + "|" + table[7] + "|" + table[8])

    # Win checking system
def checkWin():
    for i in range(2):
        if i == 0:
            xo = "X"
        elif i == 1:
            xo = "O"
        if table[0] == table[1] == table[2] == xo:
            print("WIN!")
            exit()
        if table[3] == table[4] == table[5] == xo:
            print("WIN!")
            exit()
        if table[6] == table[7] == table[8] == xo:
            print("WIN!")
            exit()
        if table[0] == table[3] == table[6] == xo:
            print("WIN!")
            exit()
        if table[1] == table[4] == table[7] == xo:
            print("WIN!")
            exit()
        if table[2] == table[5] == table[8] == xo:
            print("WIN!")
            exit()
        if table[0] == table[4] == table[8] == xo:
            print("WIN!")
            exit()
        if table[2] == table[4] == table[6] == xo:
            print("WIN!")
            exit()

printTable()

for i in range(9):
    choice = int(input("Enter field: "))
    # Player chooser
    if player == 1:
        table[choice - 1] = "X"
        player = 2
    else
        table[choice -1] = "O"
        player = 1
    printTable()
    checkWin()
