#sử dụng pygame, tkinter 

import tkinter, pygame, time,sys, random
from tkinter import messagebox
pygame.init()
#tạo của sổ 
gameSurface = pygame.display.set_mode((735,475))   #khởi tạo cửa sổ game 
pygame.display.set_caption('My Little Snake!')     #tạo tên cho bé! 
#hình ảnh
m = 20 #cchiều cao chiều rộng 
imgbody = pygame.transform.scale(pygame.image.load('Snacksbody.jpg'), (m,m))
imgface= pygame.transform.scale(pygame.image.load('face.jpg'), (m,m))
imgfood = pygame.transform.scale(pygame.image.load('moi.jpg'), (m,m))
#khởi tạo biến 
snakepos = [100,60]
snakebody = [[100,60],[80,60],[60,60]]
foodx = random.randrange(1,71)
foody = random.randrange(1,45)

if foodx % 2 !=0 : foodx +=1     #do m là số chẵn
if foody %2 != 0 : foody +=1

foodpos = [foodx*10, foody*10]
foodflat = True
direction = 'RIGHT'
changeto = direction
score = 0 
#màu sắc :
red = pygame.Color(255,0,0)
blue = pygame.Color(65,105,255)
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255) 
gray = pygame.Color(128,128,128)

# hàm GAMEOVER
def gameover():
	gfont = pygame.font.SysFont('consolas', 40 )
	gsurf = gfont.render('GAME OVER', True, red)
	grect = gsurf.get_rect()
	grect.midtop = (360,150)
	gameSurface.blit(gsurf, grect)
	showScore(0)
	pygame.display.flip()
	time.sleep(5) 
	pygame.quit()
	sys.exit()

def showScore(choice = 1):
    sfont = pygame.font.SysFont('consolas',20)
    ssurf = sfont.render('Score: {0}'.format(score),True,black)
    srect = ssurf.get_rect()
    if choice == 1:
        srect.midtop = (70,20)
    else:
        srect.midtop = (360,230)
    gameSurface.blit(ssurf,srect)

#vòng lặp chính : 
while True:
    pygame.time.delay(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # xử lí phím    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT:
                changeto = 'LEFT'
            if event.key == pygame.K_UP:
                changeto = 'UP'
            if event.key == pygame.K_DOWN:
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:    
                pygame.event.post(pygame.event.Event(pygame.QUIT))
	# huong di : có 3 hướng thôi 
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN' 
	#cập nhật tọa độ
    if direction == 'RIGHT':
        snakepos[0] += m
    if direction == 'LEFT':
        snakepos[0] -= m
    if direction == 'UP':
        snakepos[1]  -= m
    if direction == 'DOWN': 
        snakepos[1]  += m
    # ăn mồi 
    snakebody.insert(0,list(snakepos))
    if snakepos[0] == foodpos[0] and snakepos[1] == foodpos[1]:
    	score +=10
    	foodflat = False
    else:
    	snakebody.pop()

	#sinh mồi:
    if foodflat == False:
        foodx = random.randrange(1,71)
        foody = random.randrange(1,45)
        if foodx %2 != 0: foodx += 1
        if foody %2 != 0: foody += 1
        foodpos = [foodx * 10, foody * 10]
    foodflat = True
	# cập nhật 
    gameSurface.fill(white)
    for pos in snakebody:
    	gameSurface.blit(imgbody, pygame.Rect(pos[0], pos[1], m, m))
    gameSurface.blit(imgface, pygame.Rect(snakebody[0][0], snakebody[0][1], m, m))
    gameSurface.blit(imgfood, pygame.Rect(foodpos[0], foodpos[1], m, m))
	# đụng biên :
    if snakepos[0]>710 or snakepos[0]<10:
    	gameover()
    if snakepos[1]>450 or snakepos[1]<10:
    	gameover()
	#an chinh minh:
    for b in snakebody[1:]:
    	if snakepos[0] == b[0] and snakepos[1] == b[1]:  #đầu chạm vào các phần còn lại của thân 
    	    gameover()
	# duong vien :
    pygame.draw.rect(gameSurface,gray,(10,10,715,455),3)
    showScore()
    pygame.display.flip()
	

