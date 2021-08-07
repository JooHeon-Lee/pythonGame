#======충돌 처리 ====
import pygame

pygame.init() # 초기화 작업 (필수)

#화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Python Game")

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("D:/github/pythonGame/pygame_basic/background.png")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load("D:/github/pythonGame/pygame_basic/character.png")
character_size = character.get_rect().size # rectangle의 약자,, 사이즈 알아내기
character_width = character_size[0] #캐릭터의 가로크기
character_height = character_size[1] #캐릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

#이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6


# 적 enemy 캐릭터 생성
enemy = pygame.image.load("D:/github/pythonGame/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size # rectangle의 약자,, 사이즈 알아내기
enemy_width = enemy_size[0] #캐릭터의 가로크기
enemy_height = enemy_size[1] #캐릭터의 세로크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) # 화면 가로의 절반크기에 해당하는 곳에 위치
enemy_y_pos = (screen_height / 2 ) - (enemy_height / 2) # 화면 세로 크기 가장 아래에 해당하는 곳에 위치



# 이벤트 루프 ( 항상 돌고있어야 프로그램이 안꺼짐)
running = True # 게임이 진행중인가 체크

while running:
    dt = clock.tick(60) # 게임 화면의 초당 프레임수 설정

    # 캐릭터가 100 만큼 이동해야함
    # 10 fps : 1초동안에 10번동작 1번에 10만큼 이동해야 100 만큼 이동
    # 20 fps : 1초동안에 20번 동작 1번에 5만큼 이동해야 100 만큼 이동
    # 즉 프레임 마다 이동하는게 달라져야함

    for event in pygame.event.get(): # 동작이 들어오는지 체크
        if event.type == pygame.QUIT: # 창 닫기
            running = False

        if event.type == pygame.KEYDOWN: # 키가 눌려졌는지 확인
            if event.key == pygame.K_LEFT: # 왼쪽 
                to_x -= character_speed # 5만큼 왼쪽 이동
            elif event.key == pygame.K_RIGHT: # 오른쪽
                to_x += character_speed
            elif event.key == pygame.K_UP: # 위쪽
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # 아래쪽
                to_y += character_speed
        
        if event.type == pygame.KEYUP: #방향키를 떼면 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #가로 경계값 처리
    if character_x_pos < 0: # 화면 왼쪽을 벗어남
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    #세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos # 실제 캐릭터의 x위치
    character_rect.top = character_y_pos # 실제 캐릭터의 y 위치

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect): # 캐릭터와 에너미가 충돌했는지
        print("충돌 했습니다.")
        running = False
            
    screen.blit(background, (0,0)) # 사진을 넣고 좌표설정 0,0 은 x축 = 0 y축 = 0
    screen.blit(character,(character_x_pos,character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy,(enemy_x_pos, enemy_y_pos)) # 적그리기

    pygame.display.update() # 파이게임은 계속 업데이트를 하면서 화면을 다시그려야함(필수)
# 게임 종료
pygame.quit()