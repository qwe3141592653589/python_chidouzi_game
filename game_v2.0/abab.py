import pgzrun
import random
a = ''#方向
point = 0#分数
speed = 20#速度
time = 0#时间
after = 5#豆子刷新时间(不影响全局)
Lv = 0#豆子等级
KeyboardInput = ''#已按下的按钮

WIDTH = 500
HEIGHT = 700

bobo = Actor('bobo')
bobo.y = 350
bobo.x = 250
douzi = Actor('douzi')
douzi.y = random.randint(douzi.height//2,HEIGHT-douzi.height)
douzi.x = random.randint(douzi.width//2,WIDTH-douzi.width)

def change():
    #豆子刷新
    global after
    douzi.y = random.randint(douzi.height//2,HEIGHT-douzi.height)
    douzi.x = random.randint(douzi.width//2,WIDTH-douzi.width)
    if random.randint(1,2) == 2:
        douzi.image = 'boom'
    else:
        douzi.image = 'douzi'
    after = 5

def t():
    global time
    global after
    #时间
    time += 1
    after -= 1

clock.schedule_interval(change,5)
clock.schedule_interval(t,1)

def draw():
    screen.blit('bg',(0,0))
    bobo.draw()
    douzi.draw()
    screen.draw.text('point:'+str(point),(0,0))
    screen.draw.text('time:'+str(time),(0,40))
    screen.draw.text('after:'+str(after),(440,0))
    screen.draw.text('Lv:'+str(Lv),(0,20))


def on_key_down(key):
    global a
    global KeyboardInput
    #方向
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
    global Lv
    #豆子一次刷新
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
    #移动
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
    #升级判断
    if point == 0:
        Lv = 0
    if point == 5:
        Lv = 1
    if point == 10:
        Lv = 2
    if point == 15:
        Lv = 3
    if point == 20:
        Lv = 4
    if point == 25:
        Lv = 5
    if point == 30:
        Lv = 6
    if point == 35:
        Lv = 7
    #升级换样子
    if Lv == 0:
        bobo.image = 'bobo'
    if Lv == 1:
        bobo.image = 'bobo_v1'
    if Lv == 2:
        bobo.image = 'bobo_v2'
    if Lv == 3:
        bobo.image = 'bobo_v3'
    if Lv == 4:
        bobo.image = 'bobo_v4'
    if Lv == 5:
        bobo.image = 'bobo_v5'
    if Lv == 6:
        bobo.image = 'bobo_v6'
    if Lv == 7:
        bobo.iamge = 'bobo_max'

pgzrun.go()

print('您的分数是：',point)