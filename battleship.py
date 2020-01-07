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
        if (coordinate[0].upper() in string.ascii_uppercase[0:5] and int(coordinate[1]) in range(1,6)):
            break
        else:
            print('Invalid input!')
            continue 
    return coordinate,direct   

def get_input():
    coordinate=input('Your coordinate: ')
    direct=input('Vertical or horizontal (v/h): ')  
    return coordinate,direct

def main():
    board=get_board()
    coordinate,direct=valid_input()

if __name__ == "__main__":
    main()                
