
import time
import sys
import numpy as np
import cv2
from mss import mss
from PIL import Image

import cv2
sys.path.append(r'/home/lpe/Desktop/Project_in_Artificial_Intelligence_PAC-MAN/Pacman_Game/') 
from Pacman_Game.run import *
import numpy as np
if __name__ == "__main__":
    game = GameController()
    game.startGame()
    i = 0
    print(game.screen)
    


    bounding_box = {'top': 170 , 'left': 100, 'width': 448, 'height': 576-16*4}

    sct = mss()

    game.pause.flip()
    counter = 1 
    while 100:
        sct_img = sct.grab(bounding_box)
        cv2.imshow('screen', np.array(sct_img))

        counter = counter + 1
        if(game.pause.paused):
            game.pause.flip()
        if game.flashBG:
            print(counter)
            game.restartGame()
        #print("score",game.score,"pacman pose" ,game.pacman.position,"Ghost", game.ghosts.ghosts[1].position,"ghost mode", game.ghosts.ghosts[1].mode.current)
        game.update()

        
                                                        


