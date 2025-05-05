import pygame
import random 
import sys 

#pygame baslatt
pygame.init()

import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("12. Ground Theme (Hurry!).mp3")
pygame.mixer.music.set_volume(0.2)  # Ses seviyesi: 0.0 ile 1.0 arasında
pygame.mixer.music.play(-1)  # -1: müziği döngüde çalar


#Ekran boyutu
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Yılan oyunu")

# renkler 
white = (255, 255, 255)
green = (0, 200, 0)
red = (200, 0, 0)
black = (0, 0, 0)
light_green = (144, 238, 144)  # açık yeşil


#saat ve yılan hızı
clock = pygame.time.Clock()




#Yılan bloğu boyutu 
block_size = 20

#yazı fontu 
font = pygame.font.Font("PressStart2P-Regular.ttf", 15)





def draw_snake(snake_list):
    for i, x in enumerate(snake_list):
        color = white if i == len(snake_list) - 1 else green  # son parça baştır
        pygame.draw.rect(screen, color, [x[0], x[1], block_size, block_size])


def show_score_and_speed(score, speed):
    text = font.render(f"Skor: {score}  Hız: {speed}", True, white)
    screen.blit(text, [10, 10])  # Sol üst köşeye yaz


def message(msg, color):
    text = font.render(msg, True, color)
    # Ekranın tam ortasına konumlandırmak için
    text_width = text.get_width()
    text_height = text.get_height()
    x_pos = (width - text_width) // 2
    y_pos = (height - text_height) // 2
    screen.blit(text, [x_pos, y_pos])


def game_loop():
    game_over = False
    game_close = False
    snake_speed = 5

    x = width // 2 
    y = height // 2

    dx = 0
    dy = 0

    snake_list = []
    snake_length = 1

 


    #yem konumu

    foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    foody = round(random.randrange(0,height - block_size)/ 20.0) * 20.0 

   


    while not game_over:
        
        while game_close:
            pygame.mixer.music.stop()
            screen.fill(light_green)

            
            message("Kaybettin! Q ile çık, C ile devam", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        pygame.mixer.music.play(-1)
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -block_size
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = block_size
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dy = -block_size
                    dx = 0
                elif event.key == pygame.K_DOWN and dy == 0:
                    dy = block_size
                    dx = 0


        x += dx
        y += dy

        # Kendine çarpma veya ekran dışına çıkma kontrolü
        if x >= width or x < 0 or y >= height or y < 0:
            pygame.mixer.music.stop()  # 🎵 Müzik burada durur
            game_close = True

        # Kendine çarpma kontrolü
        for segment in snake_list[:-1]:
            if segment == snake_head:
                pygame.mixer.music.stop()  # 🎵 Müzik burada durur
                game_close = True


        # Ekran dışına çıkma kontrolü
            if x >= width or x < 0 or y >= height or y < 0:
                game_close = True

        screen.fill(light_green)
        
        pygame.draw.circle(screen, red, (int(foodx + block_size / 2), int(foody + block_size / 2)), block_size // 2)


        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # Kendine çarpma kontrolü
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_list)
        show_score_and_speed(snake_length - 1, snake_speed)
        pygame.display.update()
       

        # Yem yeme kontrolü
        if x == foodx and y == foody:
            snake_length += 1
            snake_speed = min(snake_speed + 1, 15)
            foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0

        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()

game_loop()    

