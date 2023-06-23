import random

board = ["_" , "_" , "_" ,
        "_" , "_" , "_" , 
        "_" , "_" , "_"]
currentplayer = "X"
winner = None
gamerunning = True

#printing the game board

def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

#take player input
def playerinput(board):
    inp = int(input("Enter a Spot 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] =="_":
        board[inp-1] = currentplayer
    else:
        print("ooops players already occupied the spot you can choose differnt one")

#check for win and tie
def checkhorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "_":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "_":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "_":
        winner = board[6]
        return True

def checkrow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "_":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "_":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "_":
        winner = board[2]
        return True

def checkdiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "_":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "_":
        winner = board[2]
        return True

def checktie(board):
    global gamerunning
    if "_" not in board:
        printboard(board)
        print(" its a tie as usual!")
        gamerunning = False

def checkwin():
    if checkdiag(board) or checkhorizontle(board) or checkrow(board):
        print(f"the winner is {winner}")

#switch theplayer

def switchplayer():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    else:
        currentplayer = "X"


# computer
def computer(board):
    while currentplayer == "O":
        position = random.randint(0, 8)
        if board[position] == "_":
            board[position] = "O"
            switchplayer()


#check for win or tie

while gamerunning:
    printboard(board)
    playerinput(board)
    checkwin()
    checktie(board)
    switchplayer()
    computer(board)
    checkwin()
    checktie(board)
  