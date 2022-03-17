import os
import pygame
from pygame import image

######################################################################################
# 기본 초기화 ( 반드시 해야 하는 것 )
pygame.init() 

# 화면 크기 설정
screen_width = 640  # 가로 크기
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))


# 화면 타이틀 설정
pygame.display.set_caption("S_H_ Pang") # 게임 이름

# FPS
clock = pygame.time.Clock()

######################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 이미지, 좌표, 폰트, 속도 등)
current_path = os.path.dirname(__file__) # 현재 파일의 위치 변환
image_path = os.path.join(current_path, "images")

# 배경 이미지 불러오기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해 사용


# 캐릭터(스프라이트) 불러오기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

# 이동 속도
character_speed = 0.5

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한번에 여러 발 발사 가능
weapons = []

# 무기 이동 속도
weapon_spead = 10

# 적 enemy 캐릭터


# # 폰트 정의
# game_font = pygame.font.Font(None, 40) # 폰트 객체 생성( 폰트, 크기)

# # 총 시간
# total_time = 10

# # 시작 시간
# start_ticks = pygame.time.get_ticks() # 시작 tick을 받아옴

# 캐릭터 이동 방향
character_to_x = 0

# 캐릭터 이동 속도
character_speed = 5

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(30) # 게임화면의 초당 프레임 수 설정

    print(("fps : "+ str(clock.get_fps())))

######################################################################################

    # 2. 이벤트 처리 ( 키보드, 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님
        
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

######################################################################################

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    # 무기 위치 조정
    # 100, 200 -> 180, 160, 140, ...
    # 500, 200 -> 180, 160, 140, ...
    weapons = [ [w[0], w[1] - weapon_spead ] for w in weapons ]

    # 천장에 닿은 무기 없애기
    weapons = [ [w[0], w[1] ] for w in weapons if w[1] > 0]
######################################################################################

    # 4. 충돌 처리

    # # 충돌 처리를 위한 rect 정보 없데이트
    # character_rect = character.get_rect()
    # character_rect.left = character_x_pos
    # character_rect.top = character_y_pos

    # enemy_rect = enemy.get_rect()
    # enemy_rect.left = enemy_x_pos
    # enemy_rect.top = enemy_y_pos

    # # 충돌 체크
    # if character_rect.colliderect(enemy_rect):
    #     print("충돌했습니다.")
    #     running = False

######################################################################################

    # 5. 화면에 그리기
    screen.blit(background, (0, 0)) # 배경 그리기
        
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    screen.blit(stage, (0, screen_height - stage_height))

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    # screen.blit(enemy, (enemy_x_pos,enemy_y_pos)) # 적 그리기

    pygame.display.update() # 게임화면을 다시 그리기!

######################################################################################

pygame.time.delay(2000)

# pygame 종료
pygame.quit()
