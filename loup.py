alien = Actor('alien')
alien.topleft = (0, 0)

fantomas = Actor('creature-1')
fantomas.bottomright = (1800, 1200)  

WIDTH = 1800
HEIGHT = 1200

def draw():
    screen.clear()
    alien.draw()
    fantomas.draw()


def update():

    if keyboard.left:
        alien.x -= 8
    if keyboard.right:
        alien.x += 8
    if keyboard.up:
        alien.y -= 8
    if keyboard.down:
        alien.y += 8


    if keyboard.q:
        fantomas.x -= 3
    if keyboard.d:
        fantomas.x += 3
    if keyboard.z:
        fantomas.y -= 3
    if keyboard.s:
        fantomas.y += 3

def collision(fantomas, alien):

    if fantomas.colliderect(alien)
        print("Game Over !")


