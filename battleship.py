import string

def get_board():
    board = []
    for row in range(5):
        board.append([])
        for column in range(5):
            board[row].append(0)
    return board        

def valid_input():
    while True:
        coordinate,direct=get_input()
        if len(coordinate) == 2:
            if (coordinate[0].upper() in string.ascii_uppercase[0:5] and int(coordinate[1]) in range(1,6)):
                break
        else:
            print('Invalid input!')
            continue 
    return coordinate,direct

def print_board(board):
    print('  ',end="")
    for number in range(1,6):
        print(str(number)+' ',end='')
    print('\r')    
    for row in range(len(board)):
        print(string.ascii_uppercase[row]+' ',end="") 
        for column in range(len(board[row])):  
            if board[row][column]==1:
                print('X ',end="")
            else:
                print('0 ',end="") 
        print('\r')

def get_input():
    coordinate=input('Your coordinate: ')
    direct=input('Vertical or horizontal (v/h): ')  
    return coordinate,direct

def main():
    board=get_board()
    board[0][0]=1
    coordinate,direct=valid_input()
    print_board(board)

if __name__ == "__main__":
    main()                
