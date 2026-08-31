# Assignment 9.1 "sudoku.py"
# by Weicheng Huang

# Libraries

# Global Variables
RED = '\033[91m'

# Functions
def solution(filename):
    try:
        sudoku_grid = []
        sudoku_grid_row = []
        with open(filename) as file:
            for line in file:
                for value in line:
                    sudoku_grid_row.append(value)
                sudoku_grid.append(sudoku_grid_row)
                sudoku_grid_row = []
            return sudoku_grid        
    except FileNotFoundError:
        return None
    
def print_sudoku_grid(sudoku_grid, row=-1, column=-1):
    count = 0
    count2 = 0
    if row == -1 and column == -1:
        for rowss in sudoku_grid:
            for value in rowss:
                count += 1
                if count == 3:
                    print("[", value, "]", sep = '', end ='  ')
                    count = 0
                else:
                    print("[", value, "]", sep = '', end =' ')
            print()
    elif row >= 0 and column >= 0:
        rows = 0
        cols = 0
        for rowss in sudoku_grid:
            count2 += 1
            for value in rowss:
                count += 1
                if count == 3:
                    if rows == row and cols == column:
                        print(f"\033[91m[", value, "]\033[0m", sep = '', end ='  ')
                        cols+=1
                        count = 0
                    else:
                        print("[", value, "]", sep = '', end ='  ')
                        cols+=1
                        count = 0
                else:
                    if rows == row and cols == column:
                        print(f"\033[91m[", value, "]\033[0m", sep = '', end =' ')
                        cols+=1
                    else:
                        print("[", value, "]", sep = '', end =' ')
                        cols+=1
            rows += 1
            print()
            if count2 == 3:
                print('\n', end = '')
                count2 = 0

def check_grid_validity(sudoku_grid):
    valid = True
    row = 0
    col = 0
    while valid == True:
        while row < len(sudoku_grid):
            row_set = set(sudoku_grid[row])
            row_value = sudoku_grid[row]
            while col < len(row_value):
                column_list = [sudoku_grid[0][col],sudoku_grid[1][col],sudoku_grid[2][col],sudoku_grid[3][col],sudoku_grid[4][col],sudoku_grid[5][col],sudoku_grid[6][col],sudoku_grid[7][col], sudoku_grid[8][col]]
                column_set = set(column_list)
                # row 0-3 col 0-3
                if row >= 0 and row < 3 and col >= 0 and col < 3:
                    region_list = [sudoku_grid[0][0],sudoku_grid[0][1],sudoku_grid[0][2],sudoku_grid[1][0],sudoku_grid[1][1],sudoku_grid[1][2],sudoku_grid[2][0],sudoku_grid[2][1], sudoku_grid[2][2]]
                    region_set = set(region_list)
                # row 3-5 col 0-3
                if row >= 3 and row < 6 and col >= 0 and col < 3:
                    region_list = [sudoku_grid[3][0],sudoku_grid[3][1],sudoku_grid[3][2],sudoku_grid[4][0],sudoku_grid[4][1],sudoku_grid[4][2],sudoku_grid[5][0],sudoku_grid[5][1], sudoku_grid[5][2]]
                    region_set = set(region_list)
                # row 6-8 col 0-3
                if row >= 6 and row < 9 and col >= 0 and col < 3:
                    region_list = [sudoku_grid[6][0],sudoku_grid[6][1],sudoku_grid[6][2],sudoku_grid[7][0],sudoku_grid[7][1],sudoku_grid[7][2],sudoku_grid[8][0],sudoku_grid[8][1], sudoku_grid[8][2]]
                    region_set = set(region_list)
                # row 0-3 col 3-5
                if row >= 0 and row < 3 and col >= 3 and col < 6:
                    region_list = [sudoku_grid[0][3],sudoku_grid[0][4],sudoku_grid[0][5],sudoku_grid[1][3],sudoku_grid[1][4],sudoku_grid[1][5],sudoku_grid[2][3],sudoku_grid[2][4], sudoku_grid[2][5]]
                    region_set = set(region_list)
                # row 3-5 col 3-5
                if row >= 3 and row < 6 and col >= 3 and col < 6:
                    region_list = [sudoku_grid[3][3],sudoku_grid[3][4],sudoku_grid[3][5],sudoku_grid[4][3],sudoku_grid[4][4],sudoku_grid[4][5],sudoku_grid[5][3],sudoku_grid[5][4], sudoku_grid[5][5]]
                    region_set = set(region_list)
                # row 6-8 col 3-5
                if row >= 6 and row < 9 and col >= 3 and col < 6:
                    region_list = [sudoku_grid[6][3],sudoku_grid[6][4],sudoku_grid[6][5],sudoku_grid[7][3],sudoku_grid[7][4],sudoku_grid[7][5],sudoku_grid[8][3],sudoku_grid[8][4], sudoku_grid[8][5]]
                    region_set = set(region_list)
                # row 0-3 col 6-8
                if row >= 0 and row < 3 and col >= 6 and col < 9:
                    region_list = [sudoku_grid[0][6],sudoku_grid[0][7],sudoku_grid[0][8],sudoku_grid[1][6],sudoku_grid[1][7],sudoku_grid[1][8],sudoku_grid[2][0],sudoku_grid[2][1], sudoku_grid[2][8]]
                    region_set = set(region_list)
                # row 3-5 col 6-8
                if row >= 3 and row < 6 and col >= 6 and col < 9:
                    region_list = [sudoku_grid[3][6],sudoku_grid[3][7],sudoku_grid[3][8],sudoku_grid[4][6],sudoku_grid[4][7],sudoku_grid[4][8],sudoku_grid[5][0],sudoku_grid[5][1], sudoku_grid[5][8]]
                    region_set = set(region_list)
                # row 6-8 col 6-8
                if row >= 6 and row < 9 and col >= 6 and col < 9:
                    region_list = [sudoku_grid[6][6],sudoku_grid[6][7],sudoku_grid[6][8],sudoku_grid[7][6],sudoku_grid[7][7],sudoku_grid[7][8],sudoku_grid[8][0],sudoku_grid[8][1], sudoku_grid[8][8]]
                    region_set = set(region_list)

                if 1 in row_set and 2 in row_set and 3 in row_set and 4 in row_set and 5 in row_set and 6 in row_set and 7 in row_set and 8 in row_set and 9:
                        valid = True
                elif 1 in column_set and 2 in column_set and 3 in column_set and 4 in column_set and 5 in column_set and 6 in column_set and 7 in column_set and 8 in column_set and 9:
                        valid = True
                elif 1 in region_list and 2 in region_list and 3 in region_list and 4 in region_list and 5 in region_list and 6 in region_list and 7 in region_list and 8 in region_list and 9:
                        valid = True
                else:
                    valid = False
                    print_sudoku_grid(sudoku_grid, row, col)
                col += 1
            row += 1

    return valid

# main
def main():
    sudoku_grid = solution("data/invalid_001.sud")
    for row in sudoku_grid:
        row.pop()
    #print(sudoku_grid)
    print_sudoku_grid(sudoku_grid)
    check_grid_validity(sudoku_grid)

main()