import arcade
import random

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
WINDOW_TITLE = "PINGPONG"


class Ball(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right > WINDOW_WIDTH:
            self.change_x = -self.change_x
        elif self.left < 0:
            self.change_x = -self.change_x
        if self.top > WINDOW_HEIGHT or self.bottom < 0:
            self.change_y = -self.change_y

class Rocket(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        
    





class Game(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        self.ball = Ball("PingPong/ball.png",0.1)
        self.rocket = Rocket("PingPong/bar.png",0.1)
        self.ball.change_x = 2
        self.ball.center_y = WINDOW_HEIGHT / 2
        self.ball.center_x = WINDOW_WIDTH / 2
        self.ball.change_y = 4
        self.rocket.center_y = WINDOW_HEIGHT / 5
        self.rocket.center_x = WINDOW_WIDTH / 2




    def on_draw(self):
        self.clear((250, 250, 250))
        self.ball.draw()
        self.rocket.draw()

    def update(self, delta_time):
        self.ball.update()
        self.rocket.update()


    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.rocket.change_x = 10





window = Game(WINDOW_WIDTH,WINDOW_HEIGHT,WINDOW_TITLE)
arcade.run()



