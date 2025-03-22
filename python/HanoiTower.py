import pygame
import random
import sys
import math

pygame.init()

# Kích thước bảng và các thông số khác
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 5
ROWS, COLS = 5, 5  # Thay đổi kích thước bảng thành 5x5
CELL_SIZE = WIDTH // COLS
CIRCLE_RADIUS = CELL_SIZE // 3
CIRCLE_WIDTH = 5
CROSS_WIDTH = 5
SPACE = CELL_SIZE // 4

# Màu sắc
BG_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
CIRCLE = (255, 0, 0)
CROSS = (0, 255, 0)

# Màn hình
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)

class TicTacToe:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [" " for _ in range(rows * cols)]
        self.human_player = "O"
        self.ai_player = "X"
        self.game_over = False
        self.winner = None
        self.max_depth = 3  # Giới hạn độ sâu của Minimax

    def print_board(self):
        """In trạng thái hiện tại của bảng"""
        for i in range(0, self.rows * self.cols, self.cols):
            print(" | ".join(self.board[i:i + self.cols]))
            if i < self.rows * (self.cols - 1):
                print("-" * (self.cols * 4 - 1))

    def available_moves(self):
        """Trả về danh sách các nước đi có sẵn (chỉ số của các ô trống)"""
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def make_move(self, position, player):
        """Thực hiện một nước đi trên bảng"""
        if self.board[position] == " ":
            self.board[position] = player
            return True
        return False

    def is_board_full(self):
        """Kiểm tra xem bảng đã đầy chưa"""
        return " " not in self.board

    def check_winner(self):
        """Kiểm tra xem có người chiến thắng không. Trả về ký hiệu người chiến thắng hoặc None"""
        # Kiểm tra hàng
        for i in range(0, self.rows * self.cols, self.cols):
            if all(self.board[i + j] == self.board[i] != " " for j in range(self.cols)):
                return self.board[i]

        # Kiểm tra cột
        for i in range(self.cols):
            if all(self.board[i + j * self.cols] == self.board[i] != " " for j in range(self.rows)):
                return self.board[i]

        # Kiểm tra đường chéo chính
        if all(self.board[i * (self.cols + 1)] == self.board[0] != " " for i in range(self.rows)):
            return self.board[0]

        # Kiểm tra đường chéo phụ
        if all(self.board[(i + 1) * (self.cols - 1)] == self.board[self.cols - 1] != " " for i in range(self.rows)):
            return self.board[self.cols - 1]

        return None

    def minimax(self, depth, is_maximizing, alpha, beta):
        # Các trường hợp cơ bản
        winner = self.check_winner()
        if winner == self.ai_player:
            return 1
        if winner == self.human_player:
            return -1
        if self.is_board_full() or depth == self.max_depth:
            return 0

        if is_maximizing:
            best_score = -math.inf
            for move in self.available_moves():
                self.board[move] = self.ai_player
                score = self.minimax(depth + 1, False, alpha, beta)
                self.board[move] = " "
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
            return best_score
        else:
            best_score = math.inf
            for move in self.available_moves():
                self.board[move] = self.human_player
                score = self.minimax(depth + 1, True, alpha, beta)
                self.board[move] = " "
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
            return best_score

    def get_best_move(self):
        """Tìm nước đi tốt nhất cho AI sử dụng Minimax với cắt tỉa Alpha-Beta"""
        best_score = -math.inf
        best_move = None

        for move in self.available_moves():
            self.board[move] = self.ai_player
            score = self.minimax(0, False, -math.inf, math.inf)
            self.board[move] = " "

            # Cập nhật điểm tốt nhất
            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def play_game(self):
        """Vòng lặp chính của trò chơi"""
        ai_turn = random.choice([True, False])

        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and not ai_turn and not self.game_over:
                    mouseX = event.pos[0] // CELL_SIZE
                    mouseY = event.pos[1] // CELL_SIZE
                    move = mouseY * self.cols + mouseX

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
        """Vẽ bảng và các nước đi"""
        screen.fill(BG_COLOR)

        # Vẽ các đường kẻ ngang và dọc
        for i in range(1, self.cols):
            pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), LINE_WIDTH)
        for i in range(1, self.rows):
            pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), LINE_WIDTH)

        # Vẽ các nước đi
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i * self.cols + j] == "O":
                    pygame.draw.circle(screen, CIRCLE, (j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2), CIRCLE_RADIUS, CIRCLE_WIDTH)
                elif self.board[i * self.cols + j] == "X":
                    pygame.draw.line(screen, CROSS, (j * CELL_SIZE + SPACE, i * CELL_SIZE + CELL_SIZE - SPACE), (j * CELL_SIZE + CELL_SIZE - SPACE, i * CELL_SIZE + SPACE), CROSS_WIDTH)
                    pygame.draw.line(screen, CROSS, (j * CELL_SIZE + SPACE, i * CELL_SIZE + SPACE), (j * CELL_SIZE + CELL_SIZE - SPACE, i * CELL_SIZE + CELL_SIZE - SPACE), CROSS_WIDTH)

    def display_winner(self):
        """Hiển thị người chiến thắng hoặc thông báo hòa"""
        if self.winner == self.ai_player:
            message = "AI wins!"
        elif self.winner == self.human_player:
            message = "Congratulations! You win!"
        else:
            message = "It's a tie!"

        font = pygame.font.Font(None, 36)

        text = font.render(message, True, (0, 0, 0))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.update()

game = TicTacToe(ROWS, COLS)
game.play_game()