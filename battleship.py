import string
import os
import time

def get_board():
    board = []
    for row in range(5):
        board.append([])
        for column in range(5):
            board[row].append(0)
    return board        

def valid_input():
    while True:
        coordinate,direct = get_input()
        if len(coordinate) == 2:
            if (coordinate[0].upper() in string.ascii_uppercase[0:5] and int(coordinate[1]) in range(1,6)):
                break
        else:
            print('Invalid input!')
            continue 
    return coordinate,direct

def get_input():
    coordinate = input('Your coordinate: ')
    direct = input('Vertical or horizontal (v/h): ')  
    return coordinate,direct

def print_board(board):
    print('  ',end="")
    for number in range(1,6):
        print(str(number)+' ',end='')
    print('\r')    
    for row in range(len(board)):
        print(string.ascii_uppercase[row]+' ',end="") 
        for column in range(len(board[row])):  
            if board[row][column] == 1:
                print('X ',end="")
            else:
                print('0 ',end="") 
        print('\r')


def place_ship(ships,board,coordinate,direct):
    if ships[0] == 1:
        letter = coordinate[0].upper()
        row=string.ascii_uppercase.index(letter)
        column = int(coordinate[1])-1
        board[row][column] = 1
    else:
        if direct == 'v':
            letter = coordinate[0].upper()
            row=string.ascii_uppercase.index(letter)
            column = int(coordinate[1])-1
            board[row][column] = 1
            board[row+1][column] = 1
        else:
            letter = coordinate[0].upper()
            row=string.ascii_uppercase.index(letter)
            column = int(coordinate[1])-1
            board[row][column] = 1
            board[row][column+1] = 1    

def player1_place():
    os.system('clear')
    player1 = get_board()
    ships = [1,1,1,2,2]
    while len(ships) != 0:
        print_board(player1)
        coordinate,direct = valid_input()
        place_ship(ships,player1,coordinate,direct)
        del ships[0]
        time.sleep(1)
        os.system('clear')         

def main():
    os.system('clear')
    player1_place()

if __name__ == "__main__":
    main()                
