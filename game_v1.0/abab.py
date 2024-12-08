import pgzrun
import random
a = ''#方向
point = 0#分数
speed = 4#速度

WIDTH = 500
HEIGHT = 700

bobo = Actor('bobo')
bobo.y = 350
bobo.x = 250
douzi = Actor('douzi')
douzi.y = random.randint(douzi.height//2,HEIGHT-douzi.height)
douzi.x = random.randint(douzi.width//2,WIDTH-douzi.width)

def change():
    douzi.y = random.randint(douzi.height//2,HEIGHT-douzi.height)
    douzi.x = random.randint(douzi.width//2,WIDTH-douzi.width)
    if random.randint(1,10) == 5:
        douzi.image = 'boom'
    else:
        douzi.image = 'douzi'

clock.schedule_interval(change,5)

def draw():
    screen.blit('bg',(0,0))
    bobo.draw()
    douzi.draw()
    screen.draw.text(str(point),(0,0))

def on_key_down(key):
    global a
    if key == keys.RIGHT:
        a = 'R'
    if key == keys.LEFT:
        a = 'L'
    if key == keys.DOWN:
        a = 'D'
    if key == keys.UP:
        a = 'U'

def update():
    global a
    global point
    global speed
    if douzi.colliderect(bobo):
        if douzi.image == 'boom':
            point = 0
        else:
            point += 1
        douzi.y = random.randint(douzi.height//2,HEIGHT-douzi.height)
        douzi.x = random.randint(douzi.width//2,WIDTH-douzi.width)
        if random.randint(2,3) == 2:
            douzi.image = 'boom'
        else:
            douzi.image = 'douzi'
    if a == 'R':
        bobo.x += speed
        if bobo.right > WIDTH:
            a = 'L'
    if a == 'L':
        bobo.x -= speed
        if bobo.left < 0:
            a = 'R'
    if a == 'U':
        bobo.y -= speed
        if bobo.top < 0:
            a = 'D'
    if a == 'D':
        bobo.y += speed
        if bobo.bottom > HEIGHT:
            a = 'U'

pgzrun.go()

print('您的分数是：',point)