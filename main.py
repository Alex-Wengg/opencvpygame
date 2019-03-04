import pygame
from pygame.locals import *
import cv2
import numpy as np
import sys,random
from game import *
camera = cv2.VideoCapture(0)
pygame.init()
pygame.display.set_caption("OpenCV camera stream on Pygame")
screen = pygame.display.set_mode([1280,720])
face_cascade = cv2.CascadeClassifier('/Users/hanweng/Desktop/programs/opencvgame/cascademaker/data/cascade.xml')

score = 0
width, height = screen.get_size()
circles =[]
osuball = Osuball( 50,60)
circle = Circle( 20,20)
circleGroup = pygame.sprite.Group(circle)
time = 0
try:
    #to make it a video
    while True:

        #the text from pygame to be in video
        #screenshot the pic from video
        ret, frame = camera.read()
        #print(frame)
        #fill the screen with whiteness
        screen.fill([0,0,0])

        #convert the vid piv to rgb for pygame to read
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #the frame is now an array from above to be rotated
        frames = np.rot90(frame)
        #convert the arrays for pygame to be added in the image
        pygameframe = pygame.surfarray.make_surface(frames)
        #update the screen with new images basically

        points = Points(str(score),(30,30))
        time += 1
        x= random.randrange(1,width)
        y= random.randrange(1, height)
        if time >50:
            circle = Circle(x,y)
            time = 0
            circles.append(circle)
            circleGroup = pygame.sprite.Group(circles)
        faces = face_cascade.detectMultiScale(gray, 1.4, 5)

        if pygame.sprite.spritecollide(osuball, circleGroup, True):
            for circle in circles:
                circles.remove(circle)
            score +=1

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        osuball = Osuball(width-x,(2*y+h)/2)

        testing = pygame.sprite.Group(osuball,circleGroup, points)

        screen.blit(pygameframe, (30,30))

        testing.clear(screen, pygameframe)
        testing.update()
        testing.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if (event.type == KEYDOWN):
                sys.exit(0)


except (KeyboardInterrupt,SystemExit):
    pygame.quit()
    cv2.destroyAllWindows()
