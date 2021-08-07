# ====== 캐릭터 ==========
# ========배경 설정=========

import pygame

pygame.init() # 초기화 작업 (필수)

#화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Python Game")

# 배경 이미지 불러오기
background = pygame.image.load("D:/github/pythonGame/pygame_basic/background.png")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load("D:/github/pythonGame/pygame_basic/character.png")
character_size = character.get_rect().size # rectangle의 약자,, 사이즈 알아내기
character_width = character_size[0] #캐릭터의 가로크기
character_height = character_size[1] #캐릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 이벤트 루프 ( 항상 돌고있어야 프로그램이 안꺼짐)
running = True # 게임이 진행중인가 체크

while running:
    for event in pygame.event.get(): # 동작이 들어오는지 체크
        if event.type == pygame.QUIT: # 창 닫기
            running = False

    screen.blit(background, (0,0)) # 사진을 넣고 좌표설정 0,0 은 x축 = 0 y축 = 0

    screen.blit(character,(character_x_pos,character_y_pos)) # 캐릭터 그리기

    pygame.display.update() # 파이게임은 계속 업데이트를 하면서 화면을 다시그려야함(필수)
# 게임 종료
pygame.quit()