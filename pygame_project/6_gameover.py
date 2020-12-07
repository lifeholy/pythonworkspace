# 1.모든 공을 없애면 게임 종료(성공)
# 2.캐릭터는 공에 닿으면 게임종료(실패)
# 3.시간 제한 99초 초과시 게임종료(실패)

import pygame
#import random
import os
#####################################################################
#0. 기본사항
pygame.init() 

#화면크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("PANG")  

#FPS
clock = pygame.time.Clock()
#####################################################################

#1. 사용자 게임 초기화(배경화면, 게임이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__) #현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") #images 폴더위치 반환


#배경 이미지 불러오기
background = pygame.image.load(os.path.join(image_path, "background.png"))

#스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] #스테이지의 높이 위에 캐릭터를 두기위해 사용


#캐릭터 만들기,불러오기
charactor = pygame.image.load(os.path.join(image_path, "charactor.png"))
charactor_size = charactor.get_rect().size  #이미지의 크기를 구해옴
charactor_width = charactor_size[0]
charactor_height = charactor_size[1]
charactor_x_pos = (screen_width) - (charactor_width / 2) #화면 가로크기의 절반에 위치
charactor_y_pos = screen_height - charactor_height - stage_height /10 #화면 세로크기에 캐릭터 높이만큼 뺀 위치


#캐릭터 이동할 좌표
charactor_to_x = 0
#to_y = 0

#이동 속도
charactor_speed = 5


#무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size  #이미지의 크기를 구해옴
weapon_width = weapon_size[0]

#무기는 한번에 여러발 발사 가능
weapons = []

#무기 이동 속도
weapon_speed = 3

#공 만들기 (4개 크기에 대해 따로 처리)
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))]

#공 크기에 따른 최초 스피드
ball_speed_y = [-18, -15, -12, -9] #index 0, 1, 2, 3 에 해당하는 값


#공들
balls = []

#최초 발생하는 큰 공 추가
balls.append({
    "pos_x" : 50, #공의 x좌표
    "pos_y" : 50, #공의 y좌표
    "img_idx" : 0, #공의 이미지 인덱스
    "to_x":3, #x축 이동방향, -3이면 왼쪽으로, 3이면 오른쪽으로
    "to_y": -6, #y축 이동방향,
    "init_spd_y": ball_speed_y[0]}) #y 최초 속도

#사라질 무기와 공 정보 저장 변수
weapon_to_remove = -1
ball_to_remove = -1

# 적캐릭터(똥) 만들기
#enermy = pygame.image.load("D:/pythonworkspace/pygame_basic/ddong.png")
#enermy_size = enermy.get_rect().size  #이미지의 크기를 구해옴
#enermy_width = enermy_size[0]
#enermy_height = enermy_size[1]
#enermy_x_pos = random.randint(0, screen_width - enermy_width) #(screen_width / 2) - (enermy_width / 2) #화면 가로크기의 절반에 위치
#enermy_y_pos = 0 #screen_height /2 - enermy_height / 2  #화면 세로크기에 캐릭터 높이만큼 뺀 위치
#enermy_speed = 7

#폰트 정의
game_font = pygame.font.Font(None, 40)  #폰트객체생성 폰트,크기

#게임종료 메세지
game_result = "Game Over"

#총 시간
total_time = 100

#시작시간 정보
start_ticks = pygame.time.get_ticks() #시작 tick을 받아옴




#이벤트 루프
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(30) #게임화면의 초당 프레임수를 설정

    #print(("fps : " ) + str(clock.get_fps())) #프레임수를 출력함

    #2. 이벤트처리(키보드, 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 화면나가기 클릭하였는가?
            running = False

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                charactor_to_x -= charactor_speed
            elif event.key == pygame.K_RIGHT:
                charactor_to_x += charactor_speed 
            elif event.key == pygame.K_SPACE: #무기 발사
                weapon_x_pos = charactor_x_pos + (charactor_width / 2) - (weapon_width / 2)
                weapon_y_pos = charactor_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
            #if event.key == pygame.K_UP:
            #    to_y -= charactor_speed 
            #if event.key == pygame.K_DOWN:
            #    to_y += charactor_speed 

        if event.type == pygame.KEYUP: #키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                charactor_to_x = 0
            #elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            #    to_y = 0

    #3. 게임캐릭터 위치 정의
    charactor_x_pos += charactor_to_x
    #charactor_y_pos += to_y * dt

    #가로 경계값 처리
    if charactor_x_pos < 0:
        charactor_x_pos = 0
    elif charactor_x_pos > screen_width - charactor_width:
        charactor_x_pos = screen_width - charactor_width

    #무기 위치 조정
    #x,y 100,200 -> 100,190 ...
    #500,200 -> 190, 180, 170 ...
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons]
    
    #천정에 닿은 무기 없애기
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]

    #공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        #가로벽에 닿았을 때 공 이동 위치 변경(튕겨 나오는 효과)
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1

        #세로 위치
        #스테이지에 튕겨서 올라가는 처리
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]

        else:  #그 외의 모든 경우에는 속도를 증가
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

#    enermy_y_pos += enermy_speed

    #적캐릭터가 사라지면 새로 랜덤위치로 처리
#    if enermy_y_pos > screen_height:
#        enermy_y_pos = 0
#        enermy_x_pos = random.randint(0, screen_width - enermy_width)

    

    #세로 경계값 처리
    #if charactor_y_pos < 0:
    #    charactor_y_pos = 0
    #elif charactor_y_pos > screen_height - charactor_height:
    #    charactor_y_pos = screen_height - charactor_height

    #4. 충돌처리
    #충돌 처리를 위한 rect 정보 업데이트
    #캐릭터 rect정보 업데이트
    charactor_rect = charactor.get_rect()
    charactor_rect.left = charactor_x_pos
    charactor_rect.top = charactor_y_pos 

    #공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        #공 rect 정보 업데이트
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        #공과 캐릭터 충돌 처리
        if charactor_rect.colliderect(ball_rect):
            running = False
            break

        #공과 무기들 충돌 처리
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            #무기 rect 정보 업데이트
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            #충돌 체크
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx #해당무기 없애기 위한 값 설정
                ball_to_remove = ball_idx #해당공 없애기 위한 값 설정
                
                #가장 작은 크기의 공이 아니라면 다음단계의 공으로 나눠주기
                if ball_img_idx < 3:
                    #현재 공크기 정보를 가지고 옴
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    #나눠진 공 정보
                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]

                    #왼쪽으로 튕겨나가는 작은 공
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), #공의 x좌표
                        "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2), #공의 y좌표
                        "img_idx" : ball_img_idx + 1, #공의 이미지 인덱스
                        "to_x":-3, #x축 이동방향, -3이면 왼쪽으로, 3이면 오른쪽으로
                        "to_y": -6, #y축 이동방향,
                        "init_spd_y": ball_speed_y[ball_img_idx + 1]}) #y 최초 속도

                    #오른쪽으로 튕겨나가는 작은공
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), #공의 x좌표
                        "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2), #공의 y좌표
                        "img_idx" : ball_img_idx + 1, #공의 이미지 인덱스
                        "to_x":3, #x축 이동방향, -3이면 왼쪽으로, 3이면 오른쪽으로
                        "to_y": -6, #y축 이동방향,
                        "init_spd_y": ball_speed_y[ball_img_idx + 1]}) #y 최초 속도
                break #안쪽 for문 탈출
        else:  #이중 for문을 빠져나오기위한 트릭
            continue #안쪽 for문이 조건이 맞지 않으면 바깥 for문 계속 수행
        break #바깥쪽 for문 탈출 (단 안쪽 for문에 break가 있어야 수행됨)
     #충돌된 공과 무기를 없애기
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    #모든공을 없앤 경우 게임종료(성공)
    if len(balls) == 0:
        game_result = "Mission Complete"
        running = False

#    enermy_rect = enermy.get_rect()
#    enermy_rect.left = enermy_x_pos
#    enermy_rect.top = enermy_y_pos 

    #충돌 처리
#    if charactor_rect.colliderect(enermy_rect):
#        print("충돌했어요")
#        running = False


    #5. 화면에 그리기
    #screen.fill((255,255,0)) #RGB값을 채워 넣음
    screen.blit(background, (0,0)) #x좌표, y좌표에 백그라운드그림을 띄운다
    
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))
    
    screen.blit(stage, (0,screen_height - stage_height)) #x좌표, y좌표에 백그라운드그림을 띄운다
    screen.blit(charactor, (charactor_x_pos, charactor_y_pos)) 
#    screen.blit(enermy, (enermy_x_pos, enermy_y_pos)) #적그리기
 
    

    #타이머 삽입
    #경과시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #경과시간을 1000으로 나누어 초단위
    timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (255,0,0)) #int형으로 바꾸고
    #출력할 글자, True, 글자색상
    screen.blit(timer, (10,10))

    #시간 초과했다면
    if total_time - elapsed_time <= 0:
        game_result = "Time Over"
        running = False

    pygame.display.update() #게임화면을 다시 그리기!  반드시 필요

#종료메세지 출력
msg = game_font.render(game_result, True, (255,255,0)) #노란색
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()

#2초 대기
pygame.time.delay(2000)

# 종료
pygame.quit()