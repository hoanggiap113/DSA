
import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 5
ROWS, COLS = 3, 3
CELL_SIZE = WIDTH // COLS
CIRCLE_RADIUS = CELL_SIZE // 3
CIRCLE_WIDTH = 5
CROSS_WIDTH = 5
SPACE = CELL_SIZE // 4

# Colors
BG_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
CIRCLE_COLOR = (255, 0, 0)
CROSS_COLOR = (0, 255, 0)

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)

# Board
board = [" " for _ in range(9)]

# Initialize the game
class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.human_player = "O"
        self.ai_player = "X"
        self.game_over = False
        self.winner = None

    def print_board(self):
        """Print the current state of the board"""
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}")
            if i < 6:
                print("---------")

    def available_moves(self):
        """Returns list of available moves (indices of empty squares)"""
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def make_move(self, position, player):
        """Make a move on the board"""
        if self.board[position] == " ":
            self.board[position] = player
            return True
        return False

    def is_board_full(self):
        """Check if the board is full"""
        return " " not in self.board

    def check_winner(self):
        """Check if there's a winner. Returns winner symbol or None"""
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] != " ":
                return self.board[i]

        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != " ":
                return self.board[i]

        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return self.board[2]

        return None

    def minimax(self, depth, is_maximizing):
        # Base cases
        winner = self.check_winner()
        if winner == self.ai_player:
            return 1
        if winner == self.human_player:
            return -1
        if self.is_board_full():
            return 0
        if is_maximizing:
            best_score = float("-inf")
            for move in self.available_moves():
                self.board[move] = self.ai_player
                score = self.minimax(depth + 1, False)
                self.board[move] = " "
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for move in self.available_moves():
                self.board[move] = self.human_player
                score = self.minimax(depth + 1, True)
                self.board[move] = " "
                best_score = min(score, best_score)
            return best_score

    def get_best_move(self):
        """Find the best move for AI using minimax"""
        best_score = float("-inf")
        best_move = None

        for move in self.available_moves():
            # Make a calculating move
            self.board[move] = self.ai_player
            # Recursively call minimax with the next depth and the minimizing player
            score = self.minimax(0, False)
            # Reset the move
            self.board[move] = " "

            # Update the best score
            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def play_game(self):
        """Main game loop"""
        ai_turn = random.choice([True, False])

        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and not ai_turn and not self.game_over:
                    mouseX = event.pos[0] // CELL_SIZE
                    mouseY = event.pos[1] // CELL_SIZE
                    move = mouseY * 3 + mouseX

                    if move in self.available_moves():
                        self.make_move(move, self.human_player)
                        if self.check_winner() == self.human_player:
                            self.winner = self.human_player
                            self.game_over = True
                        elif self.is_board_full():
                            self.game_over = True
                        ai_turn = True

            if ai_turn and not self.game_over:
                move = self.get_best_move()
                self.make_move(move, self.ai_player)
                if self.check_winner() == self.ai_player:
                    self.winner = self.ai_player
                    self.game_over = True
                elif self.is_board_full():
                    self.game_over = True
                ai_turn = False

            self.draw_board()
            pygame.display.update()

            if self.game_over:
                self.display_winner()
                pygame.time.wait(3000)
                sys.exit()

    def draw_board(self):
        """Draw the board and the moves"""
        screen.fill(BG_COLOR)
        # Draw vertical lines
        pygame.draw.line(screen, LINE_COLOR, (CELL_SIZE, 0), (CELL_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (2 * CELL_SIZE, 0), (2 * CELL_SIZE, HEIGHT), LINE_WIDTH)
        # Draw horizontal lines
        pygame.draw.line(screen, LINE_COLOR, (0, CELL_SIZE), (WIDTH, CELL_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, 2 * CELL_SIZE), (WIDTH, 2 * CELL_SIZE), LINE_WIDTH)

        for i in range(ROWS):
            for j in range(COLS):
                if self.board[i * 3 + j] == "O":
                    pygame.draw.circle(screen, CIRCLE_COLOR, (j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2), CIRCLE_RADIUS, CIRCLE_WIDTH)
                elif self.board[i * 3 + j] == "X":
                    pygame.draw.line(screen, CROSS_COLOR, (j * CELL_SIZE + SPACE, i * CELL_SIZE + CELL_SIZE - SPACE), (j * CELL_SIZE + CELL_SIZE - SPACE, i * CELL_SIZE + SPACE), CROSS_WIDTH)
                    pygame.draw.line(screen, CROSS_COLOR, (j * CELL_SIZE + SPACE, i * CELL_SIZE + SPACE), (j * CELL_SIZE + CELL_SIZE - SPACE, i * CELL_SIZE + CELL_SIZE - SPACE), CROSS_WIDTH)

    def display_winner(self):
        """Display the winner or a tie message"""
        if self.winner == self.ai_player:
            message = "AI wins!"
        elif self.winner == self.human_player:
            message = "Congratulations! You win!"
        else:
            message = "It's a tie!"

        font = pygame.font.Font(None, 36)
        text = font.render(message, True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

# Main
if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()