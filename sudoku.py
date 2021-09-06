
BOARD = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(bo):
    """Print the board on the screen"""
    for i in range(len(bo)):
        if i%3==0 and i!=0:
            print("-".center(22, '-'))
        for j in range(len(bo[0])):
            if j%3==0 and j!=0:
                print("|", end=" ")
            if j==8:
                print(str(bo[i][j]))
            else:
                print(str(bo[i][j]), end=" ")


def find_empty(bo):
    """find the blank space in sudoku table"""
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j]==0:
                return (i,j)

def validator(bo, pos, num):
    """Assume i as row and j as coloumn"""
    # check rows
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[0]!=i:
            return False
    # check columns
    for i in range(len(bo)):
        if bo[i][pos[1]]==num and pos[1]!=i:
            return False
    #check square
    box_x = pos[0]//3
    box_y = pos[1]//3
    for i in range(box_x*3, box_x*3+3):
        for j in range(box_y*3, box_y*3+3):
            if bo[i][j]==num and (i,j)!=pos:
                return False
    return True

def sudoku_solve(bo):
    found = find_empty(bo)
    if found is None:
        return True
    
    for k in range(1, 10):
        if validator(bo, found, k):
            bo[found[0]][found[1]]=k
            if sudoku_solve(bo):
                return True
            
            bo[found[0]][found[1]] = 0
    
    return False


if __name__ == "__main__":
    sudoku_solve(BOARD)
    print_board(BOARD)
    
    

