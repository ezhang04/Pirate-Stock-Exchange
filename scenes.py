import pygame
import time

class scene_handler:
    
    def __init__(self,initial_scene,screen):
        self.current_scene = initial_scene
        self.screen = screen
        self.buttons = []
    def change_scene(self,scene):
        self.current_scene = scene
    def scene_setup(screen):
      pass

    def present_scene(self):
        if self.current_scene == 0:
            self.scene_start()
        if self.current_scene == 1:
            self.scene_setup()
        if self.current_scene == 2:
            self.scene_main()
        if self.current_scene == 3:
            self.scene_battle()
        if self.current_scene == 4:
            self.scene_win()
        if self.current_scene == 5:
            self.scene_lose()

    def scene_start(self):
        bg = pygame.image.load("assets/start.png")
        self.screen.blit(pygame.transform.scale(bg, (820, 820)), (0, 0))
        
        bg = pygame.image.load("assets/oceanMap.png")
        self.screen.blit(pygame.transform.scale(bg, (800, 800)), (0, 0))



    def scene_setup(self):
        bg = pygame.image.load("assets/oceanMap.png")
        self.screen.blit(pygame.transform.scale(bg, (800, 800)), (0, 0))

        ships = ["assets/ship1_inPixio.png", "assets/ship2_inPixio.png", "assets/ship3_inPixio.png","assets/ship4_inPixio.png",
                 "assets/ship5_inPixio.png","assets/ship6_inPixio.png","assets/ship7_inPixio.png","assets/ship8_inPixio.png"]

        x=50
        y=150
        counter = 0

        for ship in ships:
            if counter == 4:
                x = 670
                y = 150
            ship_button = Button(self.screen, x, y, 80, 80, image=ship)
            self.buttons.append(ship_button)
            ship_button.draw()
            y+=150
            counter += 1

    def scene_main(self):   
        bg = pygame.image.load("assets/oceanMap.png")
        self.screen.blit(pygame.transform.scale(bg, (820, 820)), (0, 0))
        ship_margin = 50

        ship_x = 150
        ship_y = 250

        for i in range(1, 9):
            
            ship_image = pygame.image.load(f"assets/ship{i}_inPixio.png")

            resized_ship = pygame.transform.scale(ship_image, (100, 100))

            self.screen.blit(resized_ship, (ship_x, ship_y))

            ship_x += 100 + ship_margin

            if i % 4 == 0:
                ship_x = 150
                ship_y += 150 + ship_margin

    def scene_battle(self):
        pass

    def scene_win(self):
        bg = pygame.image.load("assets/win.png")
        self.screen.blit(pygame.transform.scale(bg, (820, 820)), (0, 0))

    def scene_lose(self):
        bg = pygame.image.load("assets/lose.png")
        self.screen.blit(pygame.transform.scale(bg, (820, 820)), (0, 0))

class Button:

    def __init__(self, surface, x, y, width, height, text, color, text_color, action=None):
        self.surface = surface
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.text_color = text_color

    def __init__(self, surface, x, y, width, height, text=None, image=None, color=None, text_color=None, action=None):
        self.surface = surface
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.image = None
        if image:
            self.image = pygame.image.load(image)
            self.image = pygame.transform.scale(self.image, (width, height))
        self.color = color if color else (0, 128, 255)  # Default color
        self.text_color = text_color if text_color else (255, 255, 255)  # Default text color

        self.font = pygame.font.Font(None, 36)
        self.action = action

    def draw(self):

        pygame.draw.rect(self.surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.surface.blit(text_surface, text_rect)
        
        if self.image:
            self.surface.blit(self.image, self.rect.topleft)
        else:
            pygame.draw.rect(self.surface, self.color, self.rect)

        if self.text:
            text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            self.surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if self.rect.collidepoint(event.pos):
                    if self.action is not None:
                        self.action()

