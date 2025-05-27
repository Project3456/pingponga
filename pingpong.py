import arcade
import random

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
WINDOW_TITLE = "PINGPONG"


class Ball(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.right > WINDOW_WIDTH:
            self.change_x = -self.change_x
        elif self.left < 0:
            self.change_x = -self.change_x



class Game(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        self.ball = Ball("PingPong/ball.png",0.1)
        self.ball.change_x = 2
        self.ball.center_y = WINDOW_HEIGHT / 2
        self.ball.center_x = WINDOW_WIDTH / 2




    def on_draw(self):
        self.clear((250, 250, 250))
        self.ball.draw()

    def update(self, delta_time):
        self.ball.update()





window = Game(WINDOW_WIDTH,WINDOW_HEIGHT,WINDOW_TITLE)
arcade.run()

