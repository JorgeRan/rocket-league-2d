import cocos
from cocos.layer import ColorLayer
from cocos.sprite import Sprite
from pyglet.window import key

class GameLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super().__init__()
        self.square = Sprite('assets/green_square.png')
        self.square.position = 320, 240
        self.add(self.square)

        self.keys_held = set()
        self.schedule(self.update)

    def on_key_press(self, symbol, modifiers):
        self.keys_held.add(symbol)

        if symbol == key.R:  
            cocos.director.director.replace(Game())

    def on_key_release(self, symbol, modifiers):
        self.keys_held.discard(symbol)

    def update(self, dt):
        move = 200 * dt

        if key.LEFT in self.keys_held:
            self.square.x -= move
        if key.RIGHT in self.keys_held:
            self.square.x += move
        if key.UP in self.keys_held:
            self.square.y += move
        if key.DOWN in self.keys_held:
            self.square.y -= move
    
    def layer_size(self):
        width, height = cocos.director.get_window_size()
        x, y = self.square.position

class Game(cocos.scene.Scene):
    def __init__(self):
        background = ColorLayer(0, 0, 255, 255)
        background.scale_x = 640
        background.scale_y = 480
        background.position = 0, 0
        game = GameLayer()
        super().__init__(background, game)
    
        

if __name__ == "__main__":
    cocos.director.director.init(width=640, height=480, caption="Hold-to-Move")
    cocos.director.director.run(Game())
