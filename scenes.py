import pygame
import time

class scene_handler:
    
    def __init__(self,initial_scene,screen):
        self.current_scene = initial_scene
        self.screen = screen
        self.buttons = []

    def change_scene(self,scene):
        self.current_scene = scene

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
