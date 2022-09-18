"@credit https://stackoverflow.com/a/20183823/13903942 for more check --> https://github.com/furas/python-examples/tree/master/pygame/collisions"
import pygame

WHITE = (255,255,255)
BLACK = (0  ,0  ,0  )
RED   = (255,0  ,0  )
GREEN = (0  ,255,0  )
BLUE  = (0  ,0  ,255)

class Player():

    def __init__(self, x=0, y=0, width=150, height=150):

        self.rect = pygame.Rect(x, y, width, height)

        self.speed_x = 5
        self.speed_y = 5

        self.move_x = 0
        self.move_y = 0

        self.collision = [False] * 9

        self.font = pygame.font.SysFont("", 32)
        self.text = "";

    def set_center(self, screen):
        self.rect.center = screen.get_rect().center

    def event_handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.move_x -= self.speed_x
            elif event.key == pygame.K_RIGHT:
                self.move_x += self.speed_x
            elif event.key == pygame.K_UP:
                self.move_y -= self.speed_y
            elif event.key == pygame.K_DOWN:
                self.move_y += self.speed_y

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.move_x += self.speed_x
            elif event.key == pygame.K_RIGHT:
                self.move_x -= self.speed_x
            elif event.key == pygame.K_UP:
                self.move_y += self.speed_y
            elif event.key == pygame.K_DOWN:
                self.move_y -= self.speed_y

    def update(self):
        self.rect.x += self.move_x
        self.rect.y += self.move_y

    def draw(self, screen):

        pygame.draw.rect(screen, WHITE, self.rect, 2)
        self.draw_point(screen, self.rect.topleft, self.collision[0])
        self.draw_point(screen, self.rect.topright, self.collision[1])
        self.draw_point(screen, self.rect.bottomleft, self.collision[2])
        self.draw_point(screen, self.rect.bottomright, self.collision[3])

        self.draw_point(screen, self.rect.midleft, self.collision[4])
        self.draw_point(screen, self.rect.midright, self.collision[5])
        self.draw_point(screen, self.rect.midtop, self.collision[6])
        self.draw_point(screen, self.rect.midbottom, self.collision[7])

        self.draw_point(screen, self.rect.center, self.collision[8])

    def draw_point(self, screen, pos, collision):
        if not collision:
            pygame.draw.circle(screen, GREEN, pos, 5)
        else:
            pygame.draw.circle(screen, RED, pos, 5)

    def check_collision(self, rect):
        self.collision[0] = rect.collidepoint(self.rect.topleft)
        self.collision[1] = rect.collidepoint(self.rect.topright)
        self.collision[2] = rect.collidepoint(self.rect.bottomleft)
        self.collision[3] = rect.collidepoint(self.rect.bottomright)

        self.collision[4] = rect.collidepoint(self.rect.midleft)
        self.collision[5] = rect.collidepoint(self.rect.midright)
        self.collision[6] = rect.collidepoint(self.rect.midtop)
        self.collision[7] = rect.collidepoint(self.rect.midbottom)

        self.collision[8] = rect.collidepoint(self.rect.center)

    def render_collision_info(self):

        text = "collision: "
        print( "collision:"),

        if self.collision[0] or self.collision[2] or self.collision[4]:
            text += "left "
            print( "left")

        if self.collision[1] or self.collision[3] or self.collision[5]:
            text += "right "
            print( "right")

        if self.collision[0] or self.collision[1] or self.collision[6]:
            text += "top "
            print( "top")

        if self.collision[2] or self.collision[3] or self.collision[7]:
            text += "bottom "
            print( "bottom",)

        if self.collision[8]:
            text += "center "
            print( "center",)

        print("")
        self.text = self.font.render(text, 1, WHITE)

    def draw_collision_info(self, screen, pos):
        screen.blit(self.text, pos)

#----------------------------------------------------------------------

class Game():

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode( (800,600) )
        pygame.display.set_caption("Side Collision")

        self.player = Player()
        self.enemy  = Player()
        self.enemy.set_center(self.screen)


    def run(self):
        clock = pygame.time.Clock()

        RUNNING = True

        while RUNNING:

            # --- events ----

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUNNING = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        RUNNING = False

                self.player.event_handler(event)

            # --- updates ---

            self.player.update()
            self.enemy.update()

            self.player.check_collision(self.enemy.rect)
            self.enemy.check_collision(self.player.rect)
            self.player.render_collision_info()
            self.enemy.render_collision_info()

            # --- draws ----

            self.screen.fill(BLACK)

            self.player.draw(self.screen)
            self.enemy.draw(self.screen)

            self.player.draw_collision_info(self.screen, (0,0))
            self.enemy.draw_collision_info(self.screen, (0,32))

            pygame.display.update()

            # --- FPS ---

            clock.tick(30)

        pygame.quit()

#----------------------------------------------------------------------

if __name__ == '__main__':
    Game().run()