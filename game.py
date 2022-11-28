from classes import *
import sys
import glob

import pygame


import constants as CONST

screen = pygame.display.set_mode(((CONST.SCREEN_WIDTH, CONST.SCREEN_HEIGHT)))


class Game():

    def __init__(self):
        self.objects = []
        self.player1 = None
        self.player2 = None
        self.winner = 0
        self.screen = screen
        self.background = None
        self.myfont = None


    def start_pygame(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(('Castles War!'))
        self.screen = screen
        background = pygame.transform.scale(pygame.image.load(('background_image.jpg')), (CONST.SCREEN_WIDTH, CONST.SCREEN_HEIGHT))
        self.background = background
        screen.blit(background, (0,0))
        pygame.draw.rect(screen, (76, 153, 0), [0, CONST.SCREEN_HEIGHT-CONST.GROUND_HEIGHT, CONST.SCREEN_WIDTH, CONST.GROUND_HEIGHT])

        

    


    def main(self):
        print('Start of the Game!')
        
        FPS = CONST.FPS
        clock = pygame.time.Clock()
        run = True
        while run:
            self.start_pygame()
            
            
            clock.tick(FPS)
            mine1= Mines(p=position(CONST.SCREEN_WIDTH*0+1*CONST.MINE_POS,CONST.SCREEN_HEIGHT-CONST.GROUND_HEIGHT), player=1)
            mine2= Mines(p=position(CONST.SCREEN_WIDTH*1+(-1)*CONST.MINE_POS,CONST.SCREEN_HEIGHT-CONST.GROUND_HEIGHT), player = 2)
            barracks1= Barracks(p=position(CONST.SCREEN_WIDTH*0+1*CONST.BARRACKS_POS,CONST.SCREEN_HEIGHT-CONST.GROUND_HEIGHT), player=1)
            barracks2 = Barracks(p=position(CONST.SCREEN_WIDTH*1+(-1)*CONST.BARRACKS_POS,CONST.SCREEN_HEIGHT-CONST.GROUND_HEIGHT), player=2)
            tower1= Towers(p=position(CONST.SCREEN_WIDTH*0+1*CONST.WALL_POS,CONST.SCREEN_HEIGHT-CONST.GROUND_HEIGHT), player=1)
            tower2= Towers(p=position(CONST.SCREEN_WIDTH*1+(-1)*CONST.WALL_POS,CONST.SCREEN_HEIGHT-CONST.GROUND_HEIGHT), player=2)
            wall1= Walls(p=position(CONST.SCREEN_WIDTH*0+1*CONST.WALL_POS,CONST.SCREEN_HEIGHT-CONST.GROUND_HEIGHT), player=1)
            wall2= Walls(p=position(CONST.SCREEN_WIDTH*1+(-1)*CONST.WALL_POS,CONST.SCREEN_HEIGHT-CONST.GROUND_HEIGHT), player=2)
            

            
            screen.blit(mine1.image, (((mine1.position.x-(mine1.image.get_width()/2),mine1.position.y-(mine1.image.get_height())))))
            screen.blit(mine2.image, (((mine2.position.x-(mine2.image.get_width()/2),mine2.position.y-(mine2.image.get_height())))))
            screen.blit(barracks1.image, (((barracks1.position.x-(barracks1.image.get_width()/2),barracks1.position.y-(barracks1.image.get_height())))))
            screen.blit(barracks2.image, (((barracks2.position.x-(barracks2.image.get_width()/2),barracks2.position.y-(barracks2.image.get_height())))))
            screen.blit(tower1.image, (((tower1.position.x-(tower1.image.get_width()/2),tower1.position.y-(tower1.image.get_height())))))
            screen.blit(tower2.image, (((tower2.position.x-(tower2.image.get_width()/2),tower2.position.y-(tower2.image.get_height())))))
            screen.blit(wall1.image, (((wall1.position.x-(wall1.image.get_width()/2),wall1.position.y-(wall1.image.get_height())))))
            screen.blit(wall2.image, (((wall2.position.x-(wall2.image.get_width()/2),wall2.position.y-(wall2.image.get_height())))))


            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
        


if __name__ == "__main__":
    GM = Game()
    GM.main()


#def create_a_player(self, n):
        #m1 = 0
        #m2 = 0
        
        #if n == 1:
            #m1 = 0
            #m2 = 1
        #elif n == 2:
            #m1 = 1
            #m2 = -1

        #p = { "mine": Mines(p = position(CONST.SCREEN_WIDTH*0+1*CONST.MINE_POS,CONST.SCREEN_HEIGHT-CONST.GROUND_HEIGHT), player = n)}
        #return p

    #def populate(self, P1, P2):
        #for x in (P1, P2):
            #x.create_images
       #for x in p
       #x.create_images

#create player, for i in player dictionary, i.create_images

#P1 = self.create_a_player(1)
#P2 = self.create_a_player(2)


    



            
            




        


    

    





    

        
        



if __name__ == "__main__":
    GAME = Game()
    GAME.main()
        

        
