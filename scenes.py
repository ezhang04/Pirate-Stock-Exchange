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
            self.scene_lose

    def scene_start(self):
        self.screen.fill((255, 255, 255))
        time.sleep(1)

    def scene_setup(self):
        pass

    def scene_main(self):   
        self.screen.clear()
        self.screen.fill((255, 255, 255))
        pass

    def scene_battle(self):
        pass

    def scene_win(self):
        pass

    def scene_lose(self):
        pass

class Button:
    def __init__(self, surface, x, y, width, height, text, color, text_color, action=None):
        self.surface = surface
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.text_color = text_color
        self.font = pygame.font.Font(None, 36)
        self.action = action

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if self.rect.collidepoint(event.pos):
                    if self.action is not None:
                        self.action()