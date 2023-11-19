import pygame
pygame.init()  # Initialize pygame

WIDTH, HEIGHT = 800, 800  # Window dimensions
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the game window
pygame.display.set_caption("PonG")  # Set the window title

FPS = 60  # Frame rate
WHITE = (255, 255, 255)  # White color
BLACK = (0, 0, 0)  # Black color
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100  # Paddle dimensions
BALL_RADIUS = 7  # Ball radius
SCORE_FONT = pygame.font.SysFont("comicsans", 50)  # Font for the score
WINNING_SCORE = 10  # Score to win the game

class Paddle:
    COLOR = WHITE  # Paddle color
    VEL = 4  # Paddle velocity

    def __init__(self, x, y, width, height):  # Initialize paddle with position and dimensions
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height

    def draw(self, win):  # Draw the paddle on the window
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):  # Move the paddle up or down
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

    def reset(self):  # Reset the paddle to its original position
        self.x = self.original_x
        self.y = self.original_y


class Ball:
    MAX_VEL = 5  # Maximum ball velocity
    COLOR = WHITE  # Ball color

    def __init__(self, x, y, radius):  # Initialize ball with position and radius
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def draw(self, win):  # Draw the ball on the window
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move(self):  # Move the ball
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):  # Reset the ball to its original position and reverse its direction
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1

def draw(win, paddles, ball, left_score, right_score):  # Draw the game state
    # Fill the window with black color
    win.fill(BLACK)

    # Create and position the score texts
    left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
    win.blit(left_score_text, (WIDTH//4 - left_score_text.get_width()//2, 20))
    win.blit(right_score_text, (WIDTH * (3/4) - right_score_text.get_width()//2, 20))

    # Draw the paddles
    for paddle in paddles:
        paddle.draw(win)

    # Draw the dashed line in the middle
    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//20))

    # Draw the ball
    ball.draw(win)

    # Update the window
    pygame.display.update()

# The rest of the code here...
