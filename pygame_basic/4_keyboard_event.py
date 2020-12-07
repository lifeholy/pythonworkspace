import pygame

pygame.init() 

#화면크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("처음 게임")

#배경 이미지 불러오기
background = pygame.image.load("D:/pythonworkspace/pygame_basic/background.png")

#캐릭터 불러오기
charactor = pygame.image.load("D:/pythonworkspace/pygame_basic/charactor.png")
charactor_size = charactor.get_rect().size  #이미지의 크기를 구해옴
charactor_width = charactor_size[0]
charactor_height = charactor_size[1]
charactor_x_pos = (screen_width / 2) - (charactor_width / 2) #화면 가로크기의 절반에 위치
charactor_y_pos = screen_height - charactor_height #화면 세로크기에 캐릭터 높이만큼 뺀 위치


#이동할 좌표
to_x = 0
to_y = 0

#이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 화면나가기 클릭하였는가?
            running = False

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= 5 
            if event.key == pygame.K_RIGHT:
                to_x += 5 
            if event.key == pygame.K_UP:
                to_y -= 5 
            if event.key == pygame.K_DOWN:
                to_y += 5 

        if event.type == pygame.KEYUP: #키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    charactor_x_pos += to_x
    charactor_y_pos += to_y

    #가로 경계값 처리
    if charactor_x_pos < 0:
        charactor_x_pos = 0
    elif charactor_x_pos > screen_width - charactor_width:
        charactor_x_pos = 0

    #세로 경계값 처리
    if charactor_y_pos < 0:
        charactor_y_pos = 0
    elif charactor_y_pos > screen_height - charactor_height:
        charactor_y_pos = 0

    #screen.fill((255,255,0)) #RGB값을 채워 넣음
    screen.blit(background, (0,0)) #x좌표, y좌표에 백그라운드그림을 띄운다

    screen.blit(charactor, (charactor_x_pos, charactor_y_pos))

    pygame.display.update() #게임화면을 다시 그리기!  반드시 필요

# 종료
pygame.quit()