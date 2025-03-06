# import random
# #Algorithm
# GRID_SIZE = 9
# def checkValidNumInRow(board,num,row):
#     for i in range(0,GRID_SIZE):
#         if board[row][i] == num:
#             return True
#     return False
#
# def checkValidNumInCol(board,col,num):
#     for i in range(0,GRID_SIZE):
#         if board[i][col] == num:
#             return True
#     return False
#
# def checkValidNumInBox(board,num,row,col):
#     currentBoxRow = row - row % 3
#     currentBoxCol = col - col % 3
#     for i in range(currentBoxRow,currentBoxRow + 3):
#         for j in range(currentBoxCol,currentBoxCol + 3):
#             if board[i][j] == num:
#                 return True
#     return False
#
#
# def checkValidPlacement(board, num, row, col):
#     return not checkValidNumInRow(board, num, row) and not checkValidNumInCol(board, col, num) and not checkValidNumInBox(board, num, row, col)
#
#
# def backtracking(board):
#     for row in range(0,GRID_SIZE):
#         for col in range(0,GRID_SIZE):
#             if board[row][col] == 0:
#                 for num in range(1,10):
#                     if checkValidPlacement(board,num,row,col):
#                         board[row][col] = num
#
#                         if backtracking(board):
#                             return True
#                         else:
#                             board[row][col] = 0
#                 return False
#     return True
#
# def printBoard(board):
#     for row in range(0, GRID_SIZE):
#         if row % 3 == 0 and row != 0:
#             print("-----------")
#         for col in range(0, GRID_SIZE):
#             if col % 3 == 0 and col != 0:
#                 print("|", end=" ")
#             print(board[row][col], end=" ")
#         print()
#
#
# if __name__ == "__main__":
#     board = [[7,0,2,0,5,0,6,0,0],
#              [0,0,0,0,0,3,0,0,0],
#              [1,0,0,0,0,9,5,0,0],
#              [8,0,0,0,0,0,0,9,0],
#              [0,4,3,0,0,0,7,5,0],
#              [0,9,0,0,0,0,0,0,8],
#              [0,0,9,7,0,0,0,0,5],
#              [0,0,0,2,0,0,0,0,0],
#              [0,0,7,0,4,0,2,0,3]]
#     print("Game trước khi giải")
#     for row in range(0, GRID_SIZE):
#         if row % 3 == 0 and row != 0:
#             print("-----------")
#         for col in range(0, GRID_SIZE):
#             if col % 3 == 0 and col != 0:
#                 print("|", end=" ")
#             print(board[row][col], end=" ")
#         print()
#     if(backtracking(board)):
#         print("Giai thanh cong")
#     else:
#         print("Khong giai duoc")
#     printBoard(board)
#
# #--------------------------------------------------------
# #PyGame
import pygame
import random

# Constants
GRID_SIZE = 9
CELL_SIZE = 60
WINDOW_SIZE = CELL_SIZE * GRID_SIZE
BUTTON_HEIGHT = 50
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + BUTTON_HEIGHT))
pygame.display.set_caption("Sudoku Solver")
font = pygame.font.SysFont('Arial', 40)
button_font = pygame.font.SysFont('Arial', 20)

# Sudoku functions
def checkValidNumInRow(board, num, row):
    for i in range(0, GRID_SIZE):
        if board[row][i] == num:
            return True
    return False

def checkValidNumInCol(board, col, num):
    for i in range(0, GRID_SIZE):
        if board[i][col] == num:
            return True
    return False

def checkValidNumInBox(board, num, row, col):
    currentBoxRow = row - row % 3
    currentBoxCol = col - col % 3
    for i in range(currentBoxRow, currentBoxRow + 3):
        for j in range(currentBoxCol, currentBoxCol + 3):
            if board[i][j] == num:
                return True
    return False

def checkValidPlacement(board, num, row, col):
    return not checkValidNumInRow(board, num, row) and not checkValidNumInCol(board, col, num) and not checkValidNumInBox(board, num, row, col)

def backtracking(board):
    for row in range(0, GRID_SIZE):
        for col in range(0, GRID_SIZE):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if checkValidPlacement(board, num, row, col):
                        board[row][col] = num
                        if backtracking(board):
                            return True
                        else:
                            board[row][col] = 0
                return False
    return True

def generate_random_board():
    board = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    for _ in range(20):  # Fill 20 random cells
        row, col = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        num = random.randint(1, 9)
        if checkValidPlacement(board, num, row, col):
            board[row][col] = num
    return board

def draw_board(board):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            cell_value = board[row][col]
            if cell_value != 0:
                text = font.render(str(cell_value), True, BLACK)
                screen.blit(text, (col * CELL_SIZE + 20, row * CELL_SIZE + 10))
    for i in range(GRID_SIZE + 1):
        thickness = 4 if i % 3 == 0 else 1
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_SIZE), thickness)
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WINDOW_SIZE, i * CELL_SIZE), thickness)

def draw_buttons():
    pygame.draw.rect(screen, GRAY, (0, WINDOW_SIZE, WINDOW_SIZE // 2, BUTTON_HEIGHT))
    pygame.draw.rect(screen, GRAY, (WINDOW_SIZE // 2, WINDOW_SIZE, WINDOW_SIZE // 2, BUTTON_HEIGHT))
    solve_text = button_font.render("Solve", True, BLACK)
    new_text = button_font.render("New", True, BLACK)
    screen.blit(solve_text, (WINDOW_SIZE // 4 - 20, WINDOW_SIZE + 15))
    screen.blit(new_text, (3 * WINDOW_SIZE // 4 - 20, WINDOW_SIZE + 15))

def draw_message(message):
    if message:
        text = button_font.render(message, True, RED)
        screen.blit(text, (WINDOW_SIZE//2 - 70, WINDOW_SIZE + 15))

# Main function
if __name__ == "__main__":
    board = generate_random_board()
    message = ""
    running = True
    while running:
        screen.fill(WHITE)
        draw_board(board)
        draw_buttons()
        draw_message(message)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if y > WINDOW_SIZE:
                    if x < WINDOW_SIZE // 2:
                        # Solve button
                        temp_board = [row[:] for row in board]  # Tạo bản sao
                        if backtracking(temp_board):
                            board[:] = temp_board
                            message = ""
                        else:
                            message = "Không có cách giải"
                    else:
                        # New button
                        board = generate_random_board()
                        message = ""
        pygame.display.flip()
    pygame.quit()

