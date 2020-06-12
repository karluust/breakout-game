import pygame
from paddle import Paddle
from ball import Ball
from brick import Brick

pygame.init()

# Variables
WIDTH = 1600
HEIGHT = 900
FPS = 60
SPEED = 10
WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (34,34,34)
LIGHTGRAY = (153, 153, 153)
BRICKS = [red, green, blue, yellow] = [(255,0,0),(0,255,0),(0,0,255),(255,255,0)]

# Initializing the screen
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

# Initializing the clock and setting the caption
clock = pygame.time.Clock()
pygame.display.set_caption('Breakout')

# All sprites group
sprites = pygame.sprite.Group()
 
# Paddle Object
paddle = Paddle(WHITE, int((WIDTH / 8)), int((HEIGHT / 50)))
paddle.rect.x = int((WIDTH / 2)-100)
paddle.rect.y = int(HEIGHT * 0.8)
sprites.add(paddle)

# Ball Object
ball = Ball(LIGHTGRAY, 10, 10)
ball.rect.x = int(WIDTH / 2)
ball.rect.y = int(HEIGHT * 0.7)
sprites.add(ball)

# Brick Objects
bricks = pygame.sprite.Group()
for i in range(15):
    brick = Brick(red, 80, 30)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 140
    sprites.add(brick)
    bricks.add(brick)
for i in range(15):
    brick = Brick(yellow, 80, 30)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 180
    sprites.add(brick)
    bricks.add(brick)
for i in range(15):
    brick = Brick(green, 80, 30)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 220
    sprites.add(brick)
    bricks.add(brick)


# Main function for game
def main():
    gameOn = True
    lives = 3
    score = 0
    while gameOn:
        # Quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOn = False
        
        # Moving the paddle left or right
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.moveLeft(SPEED)
        if keys[pygame.K_RIGHT]:
            paddle.moveRight(SPEED)

        sprites.update()

        # Ball logic
        if ball.rect.x>=WIDTH:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x<=0:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y>HEIGHT:
            ball.velocity[1] = -ball.velocity[1]
            lives -= 1
            if lives == 0:
                font = pygame.font.Font(None, 74)
                text = font.render("GAME OVER", 1, WHITE)
                screen.blit(text, (int((WIDTH/2)-174), int(HEIGHT/2)))
                pygame.display.flip()
                pygame.time.wait(3000)

                gameOn = False
        if ball.rect.y<1:
            ball.velocity[1] = -ball.velocity[1]
        
        # Collision detection with paddle
        if pygame.sprite.collide_rect(ball, paddle):
            ball.rect.x -= ball.velocity[0]
            ball.rect.y -= ball.velocity[1]
            ball.bounce()

        # Collision detection with bricks
        brick_collision_list = pygame.sprite.spritecollide(ball, bricks, False)
        for brick in brick_collision_list:
            ball.bounce()
            brick.kill()
            score += 10
            if len(bricks) == 0:
                font = pygame.font.Font(None, 74)
                text = font.render("YOU WIN!", 1, WHITE)
                screen.blit(text, (int((WIDTH/2)-174), int(HEIGHT/2)))
                pygame.display.flip()
                pygame.time.wait(3000)
                gameOn = False

        # Background color
        screen.fill(GRAY)

        # Display score and lives on screen
        font = pygame.font.Font(None, 34)
        text = font.render("Score: " + str(score), 1, WHITE)
        screen.blit(text, (20,10))
        text = font.render("Lives: " + str(lives), 1, WHITE)
        screen.blit(text, (WIDTH-120,10))

        # Draw the sprites and update screen 
        sprites.draw(screen)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

main()