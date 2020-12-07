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

#이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 화면나가기 클릭하였는가?
            running = False

    #screen.fill((255,255,0)) #RGB값을 채워 넣음
    screen.blit(background, (0,0)) #x좌표, y좌표에 백그라운드그림을 띄운다

    pygame.display.update() #게임화면을 다시 그리기!  반드시 필요

# 종료
pygame.quit()