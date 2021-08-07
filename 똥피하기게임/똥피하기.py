
import pygame
from random import *
pygame.init() 

#화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("똥 피하기")

# FPS
clock = pygame.time.Clock()

# 1. 사용자 게임 초기화 ( 배경화면, 게임이미지, 좌표, 폰트,속도 등 설정)
background = pygame.image.load("D:/github/pythonGame/똥피하기게임/background.png")

character = pygame.image.load("D:/github/pythonGame/똥피하기게임/character.png")
character_size = character.get_rect().size # rectangle의 약자,, 사이즈 알아내기
character_width = character_size[0] #캐릭터의 가로크기
character_height = character_size[1] #캐릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

#캐릭터 이동 좌표
character_to_x = 0
character_speed = 0.6

enemy = pygame.image.load("D:/github/pythonGame/똥피하기게임/enemy.png")
enemy_size = enemy.get_rect().size # rectangle의 약자,, 사이즈 알아내기
enemy_width = enemy_size[0] #캐릭터의 가로크기
enemy_height = enemy_size[1] #캐릭터의 세로크기
enemy_x_pos = randrange(0,screen_width-enemy_width) # 똥의 x 좌표 설정 (랜덤)
enemy_y_pos = 0
enemy_speed = random() 

# 점수
total_score = 0

# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 폰트와 크기 명시
game_over_font = pygame.font.Font(None, 100)

running = True 

while running:
    dt = clock.tick(30) # 게임 화면의 초당 프레임수 설정

    #2. 이벤트 처리 ( 키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed    

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                character_to_x = 0
            elif event.key == pygame.K_RIGHT:
                character_to_x = 0  

    character_x_pos += character_to_x * dt
    enemy_y_pos += character_speed * dt

    #캐릭터 경계값 정의
    if character_x_pos < 0: #왼쪽으로 벗어나면
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if enemy_y_pos > screen_height: # 똥피하기 성공시
        enemy_x_pos = randrange(0,screen_width-enemy_width)
        enemy_y_pos = 0
        total_score += 5
        enemy_speed = random()  # 속도 재설정
    
    # 충돌 처리

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌했습니다.")
        running = False

    # 5. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))

    score = game_font.render(str(total_score),True,(255,255,255))
    screen.blit(score,(10,10))   

    pygame.display.update()

# 잠시 대기
game_over_msg = game_over_font.render("GAME OVER",True,(255,255,255))
screen.blit(game_over_msg,(10,50))
pygame.display.update()
pygame.time.delay(2000) # 2초 정도 대기 (ms)

# 게임 종료
pygame.quit()