import string
import os
import time
import random

def get_board(boardSize):
    board = []
    for row in range(boardSize+2):
        board.append([])
        for column in range(boardSize+2):
            board[row].append(0)
    return board        

def valid_input(boardSize):
    while True:
        coordinate,direct = get_input()
        if len(coordinate) == 2:
            if (coordinate[0].upper() in string.ascii_uppercase[0:boardSize] and int(coordinate[1]) in range(1,boardSize+1)) and (direct == 'v' or direct == 'h'):
                break
            else:
                print('Invalid input!')
                continue 
        elif len(coordinate)==3 and coordinate[0].upper() in string.ascii_uppercase[0:boardSize] and int(coordinate[1]) == 1 and int(coordinate[2]) == 0 and (direct == 'v' or direct == 'h'):
                break    
        else:
            print('Invalid input!')
            continue 
    return coordinate,direct

def get_input():
    coordinate = input('Your coordinate: ')
    direct = input('Vertical or horizontal (v/h): ')  
    return coordinate,direct

def print_board(board,boardSize):
    print('  ',end="")
    for number in range(1,boardSize+1):
        print(str(number)+' ',end='')
    print('\r')    
    for row in range(1,len(board)-1):
        print(string.ascii_uppercase[row-1]+' ',end="") 
        for column in range(1,len(board[row])-1):  
            if board[row][column] == 1:
                print('X ',end="")
            else:
                print('0 ',end="") 
        print('\r')

def get_coordinates(coordinate):
    if len(coordinate) == 2:
        letter = coordinate[0].upper()
        row=string.ascii_uppercase.index(letter)+1
        column = int(coordinate[1])
        return row,column
    else:
        letter = coordinate[0].upper()
        row=string.ascii_uppercase.index(letter)+1
        column = 10
        return row,column

def placing(board,row,column,ships,direct):  
    board[row][column] = 1
    if ships[0] == 2 and direct == 'v':
        board[row+1][column] = 1
    elif ships[0] == 2 and direct == 'h':
        board[row][column+1] = 1
           
def place(ships,board,coordinate,direct,boardSize):
    row,column=get_coordinates(coordinate)
    while True:
        if board[row][column] == 1:
            print('This place is taken!')
            coordinate,direct=valid_input(boardSize)
            row,column=get_coordinates(coordinate)
            continue      
        elif board[row+1][column] == 0 and board[row-1][column] == 0  and board[row][column+1] == 0 and board[row][column-1] == 0:
            placing(board,row,column,ships,direct)  
            break
        else:
            print('Ships are too close!')
            coordinate,direct=valid_input(boardSize)
            row,column=get_coordinates(coordinate)
            continue      

def place_horizontal(ships,board,coordinate,direct,boardSize):
    row,column=get_coordinates(coordinate)
    while True:
        if board[row][column] == 1 or board[row][column+1] == 1:
            print('This place is taken!')
            coordinate,direct=valid_input(boardSize)
            row,column=get_coordinates(coordinate)
            continue   
        elif column == boardSize:
            print('Ship is out of board!')
            coordinate,direct=valid_input(boardSize)
            row,column=get_coordinates(coordinate)
            continue  
        elif board[row][column-1] == 0 and board[row-1][column] == 0  and board[row-1][column+1] == 0 and board[row][column+2] == 0 and board[row+1][column+1] == 0 and board[row+1][column] == 0:
            board[row][column] = 1
            board[row][column+1] = 1
            break
        else:
            print('Ships are too close!')
            coordinate,direct=valid_input(boardSize)
            row,column=get_coordinates(coordinate)
            continue 

def place_vertical(ships,board,coordinate,direct,boardSize):
    row,column=get_coordinates(coordinate)
    while True:
        if board[row][column] == 1 or board[row+1][column] == 1:
            print('This place is taken!')
            coordinate,direct=valid_input(boardSize)
            row,column=get_coordinates(coordinate)
            continue   
        elif row == boardSize:
            print('Ship is out of board!')
            coordinate,direct=valid_input(boardSize)
            row,column=get_coordinates(coordinate)
            continue  
        elif board[row][column-1] == 0 and board[row+1][column-1] == 0  and board[row+2][column] == 0 and board[row+1][column+1] == 0 and board[row][column+1] == 0 and board[row-1][column] == 0:
            board[row][column] = 1
            board[row+1][column] = 1
            break
        else:
            print('Ships are too close!')
            coordinate,direct=valid_input(boardSize)
            row,column=get_coordinates(coordinate)
            continue 

def place_ship(ships,board,coordinate,direct,boardSize):
    if ships[0] == 1:
       place(ships,board,coordinate,direct,boardSize)
    else:
        if direct == 'v':
            place_vertical(ships,board,coordinate,direct,boardSize)
        else:
            place_horizontal(ships,board,coordinate,direct,boardSize)

def board_size():
    boardSize=int(input('Your board size: '))
    while True:
        if boardSize in range(1,11):
            break
        else:
            print('Invalid input! (must be between 5-10)')
            boardSize=int(input('Your board size: '))
            continue
    return boardSize    
    
def player1_place(boardSize):
    os.system('clear')
    player1 = get_board(boardSize)
    ships = [random.randint(1,2) for i in range(boardSize)]
    countShips = sum(ships)
    while len(ships) != 0:
        print_board(player1,boardSize)
        print(f"Your ship size is {ships[0]}.")
        coordinate,direct = valid_input(boardSize)
        place_ship(ships,player1,coordinate,direct,boardSize)
        del ships[0]
        os.system('clear')        
    print_board(player1,boardSize)   
    print(countShips)
    return player1, countShips

def player2_place(boardSize):
    os.system('clear')
    player2 = get_board(boardSize)
    ships = [random.randint(1,2) for i in range(boardSize)]
    countShips=sum(ships) 
    while len(ships) != 0:
        print_board(player2,boardSize)
        print(f"Your ship size is {ships[0]}.")
        coordinate,direct = valid_input(boardSize)
        place_ship(ships,player2,coordinate,direct,boardSize)
        del ships[0]
        os.system('clear')        
    print_board(player2,boardSize)  
    print(countShips)
    return player2,countShips

def print_board_shoot(board,boardSize):
    print('  ',end="")
    for number in range(1,boardSize+1):
        print(str(number)+' ',end='')
    print('\r')    
    for row in range(1,len(board)-1):
        print(string.ascii_uppercase[row-1]+' ',end="") 
        for column in range(1,len(board[row])-1):  
            if board[row][column] == 0 or board[row][column] == 1:
                print('0 ',end="")
            elif board[row][column] == 2:
                print('M ',end="") 
            elif board[row][column] == 3:
                print('H ',end="")    
            else:
                print('S ',end="")    
        print('\r')   

def valid_shoot(boardSize):
    while True:
        coordinate = get_shoot()
        if len(coordinate) == 2:
            if (coordinate[0].upper() in string.ascii_uppercase[0:boardSize] and int(coordinate[1]) in range(1,boardSize+1)):
                break
            else:
                print('Invalid input!')
                continue 
        elif len(coordinate) == 3  and coordinate[0].upper() in string.ascii_uppercase[0:boardSize] and coordinate[1] == 1 and coordinate[2] ==0:
            break    
        else:
            print('Invalid input!')
            continue 
    return coordinate    

def get_shoot():
    coordinate = input('Your coordinate: ')
    return coordinate

def shooting(player,coordinate):
    row,column = get_coordinates(coordinate)
    while True:
        if player[row][column] == 0:
            print("You've missed!")
            player[row][column] = 2
            break
        elif player[row][column] == 1 and (player[row+1][column] == 1 or player[row][column+1] == 1 or player[row-1][column] == 1 or player[row][column-1] == 1):
            print('You\'ve hit a ship!')
            player[row][column] = 3
            break
        elif player[row][column] == 1 and player[row+1][column] == 3:
            print('You\'ve sunk a ship!')
            player[row][column] = 4
            player[row+1][column] = 4
            break
        elif player[row][column] == 1 and player[row-1][column] == 3:
            print('You\'ve sunk a ship!')
            player[row][column] = 4
            player[row-1][column] = 4
            break
        elif player[row][column] == 1 and player[row][column+1] == 3:
            print('You\'ve sunk a ship!')
            player[row][column] = 4
            player[row][column+1] = 4
            break
        elif player[row][column] == 1 and player[row][column-1] == 3:
            print('You\'ve sunk a ship!')
            player[row][column] = 4
            player[row][column-1] = 4
            break
        elif player[row][column] == 1 and (player[row+1][column] == 0 or player[row+1][column] == 2) and (player[row-1][column] == 0 or player[row-1][column] == 2) and (player[row][column+1] == 0 or player[row-1][column] == 2) and (player[row][column-1] == 0 or player[row][column-1] == 2):
            print('You\'ve sunk a ship!')
            player[row][column] = 4
            break

def check_win(player,countShips,playerNumber):
    countSunks=0
    for row in range(len(player)):
        for column in range(len(player[row])):
            if player[row][column] == 4:
                countSunks+=1
    if countSunks == countShips:
        os.system("clear")
        print(f"Player {playerNumber} wins!")
        print("Game over!")
        time.sleep(4)
        return True
    else:
        return False                
        
def shoot(player1,player2,countShips,boardSize):
    won=False
    count=1
    while won is False:
        if count % 2 == 1:
            os.system('clear')
            print_board_shoot(player2,boardSize)
            print('Player 1 turn.')
            coordinate=valid_shoot(boardSize)
            shooting(player2,coordinate)
            won=check_win(player2,countShips,1)
            time.sleep(2)
            os.system('clear')
        else:
            print_board_shoot(player1,boardSize)
            print('Player 2 turn.')
            coordinate=valid_shoot(boardSize)
            shooting(player1,coordinate)
            won=check_win(player1,countShips,2)
            time.sleep(2)
            os.system('clear')
        count += 1    

def main():
    os.system('clear')
    boardSize = board_size()
    os.system('clear')
    player1, countShips = player1_place(boardSize)
    os.system('clear')
    letter = input("Next player's placement phase") 
    player2, countShips = player2_place(boardSize)
    os.system('clear')
    letter = input("Shooting phase") 
    os.system('clear')
    shoot(player1,player2, countShips,boardSize)

if __name__ == "__main__":
    main()                
