import pygame
from sys import exit
from random import randint


def draw_snake(snake):
  for i, rect in enumerate(snake):
    screen.blit(snake_surf, rect)
    pygame.draw.rect(screen, "White", rect, 1)

def collision(snake):
  global ball_rect, score
  for rect in snake:
    if rect.colliderect(ball_rect):
      ball_rect = ball_surf.get_rect(topleft = (randint(1, 15) * 30, randint(1, 15) * 30))
      score += 1
      snake.append(snake_surf.get_rect(topleft = (snake[len(snake) - 1].x - x_pos, snake[len(snake) - 1].y - y_pos)))
      crunch = pygame.mixer.Sound("sounds/Sound_crunch.wav")
      crunch.set_volume(0.2)
      crunch.play()


pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake game")
clock = pygame.time.Clock()



text_font = pygame.font.Font("font/Pixeltype.ttf", 50)
name_surf = text_font.render("Snake Game", False, "White")
name_rect = name_surf.get_rect(midbottom = (250, 180))

instruction_surf = text_font.render("Press space to start", False, "White")
instruction_rect = instruction_surf.get_rect(midbottom = (250, 320))

snake_font = pygame.font.Font("font/Pixeltype.ttf", 150)
snake_sticker = snake_font.render("🐍", False, "Green", None)
snake_sticker_rect = snake_sticker.get_rect(center = (250, 250))

snake_surf = pygame.surface.Surface((30, 30))
snake_surf.fill("Green")

ball_surf = pygame.surface.Surface((24, 24))
ball_rect = ball_surf.get_rect(topleft = (randint(1, 15) * 30, randint(1, 15) * 30))
ball_surf.fill("Red")


snake = [
  snake_surf.get_rect(topleft = (90, 0)),
  snake_surf.get_rect(topleft = (60, 0)),
  snake_surf.get_rect(topleft = (30, 0)),
  snake_surf.get_rect(topleft = (0, 0)),
]
game_active = False
x_pos = 30
y_pos = 0
score = 0




piece_timer = pygame.USEREVENT + 1
pygame.time.set_timer(piece_timer, 100)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()  
    if game_active:  
      if event.type == piece_timer:
        snake.insert(0, snake_surf.get_rect(topleft = (snake[0].x + x_pos,snake[0].y + y_pos)))  
        snake.pop()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN and x_pos != 0 and y_pos != -30:
          x_pos = 0
          y_pos = 30
        if event.key == pygame.K_LEFT and x_pos != 30 and y_pos != 0:
          x_pos = -30  
          y_pos = 0
        if event.key == pygame.K_UP and x_pos != 0 and y_pos != 30:
          x_pos = 0  
          y_pos = -30
        if event.key == pygame.K_RIGHT and x_pos != -30 and y_pos != 0:
          x_pos = 30  
          y_pos = 0  


  for rect in snake[1:]:
    if snake[0].colliderect(rect):
      game_active = False
      break
  screen.fill("Black")
     
  if game_active:   
    pygame.draw.rect(screen, "Red", ball_rect, 0, 20)
    draw_snake(snake)  
    score_surf = text_font.render(f"Score: {score}", False, "White")
    score_rect = score_surf.get_rect(bottomright = (500, 500))
    screen.blit(score_surf, score_rect)
    pygame.draw.rect(screen, "White", score_rect, 1)

    head = snake[0]
    if head.x < 0 or head.x > 470 or head.y < 0 or head.y > 470:
      game_active = False 

    collision(snake)
  else:
    screen.blit(snake_sticker, snake_sticker_rect)        
    screen.blit(name_surf, name_rect)
    if score == 0:
      screen.blit(instruction_surf, instruction_rect)
    else:
      display_score = text_font.render(f"Your Score: {score}", False, "White")
      display_score_rect = display_score.get_rect(midbottom = (250, 320))
      screen.blit(display_score, display_score_rect)  
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
      snake = [
        snake_surf.get_rect(topleft = (90, 0)),
        snake_surf.get_rect(topleft = (60, 0)),
        snake_surf.get_rect(topleft = (30, 0)),
        snake_surf.get_rect(topleft = (0, 0)),
      ]
      x_pos = 30
      y_pos = 0
      game_active = True
      score = 0


  pygame.display.update()  
  clock.tick(60)  