"""
Author:Kamal Nayan
Title: Pasha The Racer
Copyright: KamalPashaSoft Pvt.Ltd. @2017 
"""



import pygame
import time 
import random


pygame.init()
display_width=1200
display_height=1000

black= (0,0,0)
white= (255,255,255)
red=(255,0,0)


 


gameDisplay=pygame.display.set_mode((display_width,display_height ))
pygame.display.set_caption('Pasha the racer')
clock=pygame.time.Clock()

 



raceimage=pygame.image.load('raceimage.png')

start_button1=pygame.image.load('start_button.png')
start_button2=pygame.image.load('START2.png')
quit_button1=pygame.image.load('quit_button.png')
quit_button2=pygame.image.load('QUIT2.png')
nh=pygame.image.load('nh.png')


lImg=pygame.image.load('Police.png')
borImg=pygame.image.load('normalline.png')
rdImg=pygame.image.load('hoverline.png')
iImg=pygame.image.load('Audi.png')
jImg=pygame.image.load('Ambulance.png')
kImg=pygame.image.load('Black_viper.png')






"""

def ran():
        t=random.randint(2,6)
	if(t==2):
		   carImg=iImg
	elif(t==3 or 4):
		   carImg==jImg
	else:
		   carImg=kImg

"""











def write_to(txt):
        fout=open("tes.txt",'w') #opens test.txt file in WRITE mode
	print fout
	line=txt      #line variable stores string 'anything' 
	fout.write(line)      #writes to fout
	fout.close 






     
def high_score(highscore):
	font=pygame.font.SysFont(None,30)
		
	hs=highscore
        text=font.render("             : "+str(hs),True,white)
	gameDisplay.blit(text,(20,25))










def car(x,y):
  
        gameDisplay.blit(lImg,(x,y))
        

def nh80(n,y_b):
	gameDisplay.blit(nh,(n,y_b))
     



def message_display(text):
      myfont =pygame.font.SysFont("monospace",115)
 
      label=myfont.render("YOU CRASHED!!!!",2,(white))

      gameDisplay.blit(label,(100,100))
    
      time.sleep(5)
      pygame.display.update()




def pass_obs(count):
    font=pygame.font.SysFont(None,30)
    text=font.render("Score: " +str(count),True,white)
    text1=font.render("HighScore:",True,white)
    gameDisplay.blit(text,(0,0))
    gameDisplay.blit(text1,(0,25))



    
   
   
    






def crash():
	
	pygame.init()
	pygame.mixer.music.load('crashs.wav')
	pygame.mixer.music.play(0)	
	message_display('you Crashed!!')




def border(x_b,y_b):
	gameDisplay.blit(rdImg,(x_b,y_b))


def icars(ob_x,ob_y):
    
	      
	gameDisplay.blit(iImg,(ob_x,ob_y))	
def icars1(ob_x,ob_y):
	gameDisplay.blit(jImg,(ob_x,ob_y))		


def sound():
        pygame.init()
	pygame.mixer.music.load('hammer_intro.mp3')
        pygame.mixer.music.play(0)

	
	

def game_intro():
	






	intro=True
	while intro:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.fill(black)
		font=pygame.font.SysFont(None,50)
		
		font1=pygame.font.SysFont(None,35)
		text=font.render("PASHA THE RACER",True,white)
		text1=font1.render("   a kamalpashaSoft production",True,white)
		text2=font1.render("All copyrights reserved @kamalpashaSoft Pvt. Ltd. 2017",True,white)
		gameDisplay.blit(text,(display_height/2.4,display_width/2.9))
		gameDisplay.blit(text1,(display_height/2.4,display_width/2.7))
		gameDisplay.blit(text2,(display_height/3,display_width/1.3))
		
		gameDisplay.blit(start_button1,(display_height/2.5,display_width/2))
		gameDisplay.blit(quit_button1,(display_height/1.5,display_width/2))
		


		gameDisplay.blit(raceimage,(385,-60))

		
		mouse=pygame.mouse.get_pos()
		click=pygame.mouse.get_pressed()
		print click
		
		if (400< mouse[0]<570) and (600<mouse[1]<660):
			gameDisplay.blit(start_button2,(display_height/2.5,display_width/2))
			if click[0]==1 :
		
					game_loop()

		if (667<mouse[0]<811) and (600<mouse[1]<661):
			gameDisplay.blit(quit_button2,(display_height/1.5,display_width/2))
			if click[0]==1:
					pygame.quit()
					quit()

		
		pygame.display.update()
		clock.tick(15)
	






def game_loop():
	
	fin=open("tes.txt",'r')
	print  fin
	fin.readline
	highscore=int(fin.readline())
	fin.close()
	
	
	
	
	
	crashed = False
	x= (display_width * 0.40)
	y= (display_height * 0.75)
	x_change=0
	ob_startx1=random.randrange(0,display_width*0.49) 
	ob_startx2=random.randrange(display_width*0.50,display_width*0.93)
	
		
		
		
		
	ob_posy=-300
	ob_posy1=-200
	ob_speed=+10
	ob_speed1=+6
	paso=0
	gear_change=0
	gear=0
	y_b=0
	x_b=0
	y_b_speed=+4.5






        while not crashed:
		    
		     for event in pygame.event.get():
			  if event.type ==pygame.QUIT:
			      crashed = True
			  
			  elif event.type==pygame.KEYDOWN:
			      if event.key==pygame.K_LEFT or event.key==pygame.K_a:
				  x_change=-5
		 	      elif event.key==pygame.K_RIGHT or event.key==pygame.K_d:
				  x_change=+5
			      if event.key==pygame.K_UP or event.key==pygame.K_w:
				  gear_change+=1
			      if event.key==pygame.K_DOWN or event.key==pygame.K_s:
				  gear_change-=1
			 

			  elif event.type==pygame.KEYUP:
			      if event.key==pygame.K_LEFT or event.key ==pygame.K_RIGHT:
		                  x_change=0
		              elif event.key==pygame.K_a or event.key==pygame.K_d:
			            x_change=0
			      if event.key==pygame.K_UP or event.key==pygame.K_w:
					gear_change=0
		      	      if event.key==pygame.K_DOWN or event.key==pygame.K_s:
					gear_change=0
		     
		      

		    # sound()	 
		     x+=x_change
		     gear+=gear_change
		     if gear==1:
			y_b_speed=+5
			ob_speed+=0.25
			ob_speed1+=0.25
		     if gear==2:
			y_b_speed=+7
			ob_speed+=0.50
			ob_speed1+=0.45
		     if gear==3:
			y_b_speed=+10
			ob_speed+=0.65
			ob_speed1+=0.60
		     if gear==4:
			y_b_speed=+15
			ob_speed+=0.95
			ob_speed1+=0.95
		     y_b+=y_b_speed

			






		    
		     
		     gameDisplay.fill(black) 
		     ob_posy+=ob_speed
		     ob_posy1+=ob_speed1
		     border(0,y_b)
		     border(0,y_b+200)
		     border(0,y_b+400)
	             border(0,y_b+600)
		     border(0,y_b+800)
		     border(600,y_b)
		     border(1195,y_b)
		     border(1195,y_b+200)
		     border(1195,y_b+400)
		     border(1195,y_b+600)
		     border(1195,y_b+800)
						
						
			
			
		     border(600,y_b+200)
		     border(600,y_b+400)
		     border(600,y_b+600)
		     border(600,y_b+800)
	             """
		     nh80(40,(ob_posy+100))
		     nh80(640,(ob_posy+100)) 
		     nh80(40,(ob_posy+600))
		     nh80(640,(ob_posy+600))
		     nh80(40,(ob_posy+900))
		     nh80(640,(ob_posy+900))	
	             """
		     car(x,y)
		     pass_obs(paso)
		     
		     

		     icars(ob_startx1,ob_posy)
		     icars1(ob_startx2,ob_posy1)
		    
		    
		     pygame.display.update()            
		    
		     


	             if y_b+800>900:
				y_b=0-7



		     if x<-70 or x>display_width*0.89:
		        write_to(str(highscore))
		        crash()
		        crashed= True
			

		     if ob_posy> display_height:  
		           ob_posy= 0-ob_posy
			   ob_startx1=random.randrange(0,display_width*0.49)
			   paso+=1
			   
		     if ob_posy1>display_height:
			   ob_posy1=0-ob_posy1
			   ob_startx2=random.randrange(display_width*0.60,display_width*0.95)
			   paso+=1
			   
		          
		     if paso>highscore:
		           highscore=paso
		        
		     



		     if (y<ob_posy+196):
		        if ((x>=ob_startx1 and x<=ob_startx1+96) or (x+92>ob_startx1 and x+96<ob_startx1+96)):
			     write_to(str(highscore))
		             crash()
		             crashed=True
		     if (y<ob_posy1+196):
		         if((x>=ob_startx2 and x<=ob_startx2+96) or (x+92>ob_startx2 and x+96<ob_startx2+96)):
			     write_to(str(highscore))
		             crash()
		             crashed=True

		     high_score(highscore)
		     
		 
		     pygame.display.update()
		     clock.tick(60)









sound()
game_intro()

#game_loop()
pygame.quit()
quit()
