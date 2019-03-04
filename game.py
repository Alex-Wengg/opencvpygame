
import random
import pygame

class Osuball(pygame.sprite.Sprite):
    '''the method for the labels where we will place the scores the player
    hitting the brick'''
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        # Set the image and rect attributes for the bricks
        self.image = pygame.image.load("images/mouse.jpg")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

class Circle(pygame.sprite.Sprite):
    '''Our Bricks class inherits from the Sprite class'''
    def __init__(self, x, y):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)

        # Set the image and rect attributes for the bricks
        self.image = pygame.image.load("images/ball3.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.time = 0
    def update(self):
        self.time+=1
        if self.time ==50:
            self.image = pygame.image.load("images/ball2.png")
        elif self.time > 100:
            self.image = pygame.image.load("images/ball1.png")


class Points(pygame.sprite.Sprite):
    '''the method for the labels where we will place the scores the player
    hitting the brick'''
    def __init__(self, message, x_y_center):
        pygame.sprite.Sprite.__init__(self)
        self.__font = pygame.font.SysFont("None", 30)
        self.__text = message
        self.__center = x_y_center
    #set the message
    def set_text(self, message):
        self.__text = message
    #constanting displaying the message
    def update(self):

        self.image = self.__font.render(self.__text, 1, (0, 225, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.__center
