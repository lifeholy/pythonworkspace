import pygame

pygame.init() 

#화면크기 설정 초기설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("처음 게임")

#FPS
clock = pygame.time.Clock()

#배경 이미지 불러오기
background = pygame.image.load("F:/pythonworkspace/pygame_basic/background.png")

#캐릭터 불러오기
charactor = pygame.image.load("F:/pythonworkspace/pygame_basic/charactor.png")
charactor_size = charactor.get_rect().size  #이미지의 크기를 구해옴
charactor_width = charactor_size[0]
charactor_height = charactor_size[1]
charactor_x_pos = (screen_width / 2) - (charactor_width / 2) #화면 가로크기의 절반에 위치
charactor_y_pos = screen_height - charactor_height #화면 세로크기에 캐릭터 높이만큼 뺀 위치


#이동할 좌표
to_x = 0
to_y = 0

#이동 속도
charactor_speed = 0.6

# 적캐릭터
enermy = pygame.image.load("F:/pythonworkspace/pygame_basic/enermy.png")
enermy_size = enermy.get_rect().size  #이미지의 크기를 구해옴
enermy_width = enermy_size[0]
enermy_height = enermy_size[1]
enermy_x_pos = (screen_width / 2) - (enermy_width / 2) #화면 가로크기의 절반에 위치
enermy_y_pos = screen_height /2 - enermy_height / 2  #화면 세로크기에 캐릭터 높이만큼 뺀 위치

#폰트 정의
game_font = pygame.font.Font(None, 40)  #폰트객체생성 폰트,크기

#총 시간
total_time = 10

#시작시간 정보
start_ticks = pygame.time.get_ticks() #시작 tick을 받아옴




#이벤트 루프
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(60) #게임화면의 초당 프레임수를 설정

    #print(("fps : " ) + str(clock.get_fps())) #프레임수를 출력함

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 화면나가기 클릭하였는가?
            running = False

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= charactor_speed
            if event.key == pygame.K_RIGHT:
                to_x += charactor_speed 
            if event.key == pygame.K_UP:
                to_y -= charactor_speed 
            if event.key == pygame.K_DOWN:
                to_y += charactor_speed 

        if event.type == pygame.KEYUP: #키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    charactor_x_pos += to_x * dt
    charactor_y_pos += to_y * dt

    #가로 경계값 처리
    if charactor_x_pos < 0:
        charactor_x_pos = 0
    elif charactor_x_pos > screen_width - charactor_width:
        charactor_x_pos = screen_width - charactor_width

    #세로 경계값 처리
    if charactor_y_pos < 0:
        charactor_y_pos = 0
    elif charactor_y_pos > screen_height - charactor_height:
        charactor_y_pos = screen_height - charactor_height

    #충돌 처리를 위한 rect 정보 업데이트
    charactor_rect = charactor.get_rect()
    charactor_rect.left = charactor_x_pos
    charactor_rect.top = charactor_y_pos 

    enermy_rect = enermy.get_rect()
    enermy_rect.left = enermy_x_pos
    enermy_rect.top = enermy_y_pos 

    #충돌 처리
    if charactor_rect.colliderect(enermy_rect):
        print("충돌했어요")
        running = False



    #screen.fill((255,255,0)) #RGB값을 채워 넣음
    screen.blit(background, (0,0)) #x좌표, y좌표에 백그라운드그림을 띄운다
    screen.blit(charactor, (charactor_x_pos, charactor_y_pos)) 
    screen.blit(enermy, (enermy_x_pos, enermy_y_pos)) #적그리기

    #타이머 삽입
    #경과시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #경과시간을 1000으로 나누어 초단위
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,0,0)) #int형으로 바꾸고
    #출력할 글자, True, 글자색상
    screen.blit(timer, (10,10))

    pygame.display.update() #게임화면을 다시 그리기!  반드시 필요

# 종료
pygame.quit()