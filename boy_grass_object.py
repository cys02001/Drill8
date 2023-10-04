from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self): pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = random.randint(0, 7)
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Big_Ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.frame = 0
        self.image = load_image('ball41x41.png')
        self.speed = random.randint(1, 5)

    def update(self):
        self.frame = random.randint(0, 0)
        if self.y > 70:
            self.y -= self.speed
        else:
            self.y = 70

    def draw(self):
        self.image.clip_draw(self.frame * 41, 0, 41, 41, self.x, self.y)


class Small_Ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.frame = 0
        self.image = load_image('ball21x21.png')
        self.speed = random.randint(1, 5)

    def update(self):
        self.frame = random.randint(0, 0)
        if self.y > 60:
            self.y -= self.speed
        else:
            self.y = 60

    def draw(self):
        self.image.clip_draw(self.frame * 21, 0, 21, 21, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    global team
    global big_balls
    global small_balls
    global world

    running = True
    world = []

    grass = Grass()
    world.append(grass)

    team = [Boy() for i in range(11)]
    big_balls = [Big_Ball() for i in range(10)]
    small_balls = [Small_Ball() for i in range(10)]
    world += team
    world += big_balls
    world += small_balls


def update_world():
    grass.update()
    for boy in world:
        boy.update()
    for big_ball in world:
        big_ball.update()
    for small_ball in world:
        small_ball.update()


def render_world():
    clear_canvas()
    for boy in world:
        boy.draw()
    for big_ball in world:
        big_ball.draw()
    for small_ball in world:
        small_ball.draw()
    update_canvas()


open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()  # game logic
    render_world()  # draw game world
    delay(0.05)

# finalization code

close_canvas()