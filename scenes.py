import pygame
import time
from pygame.locals import *
from mechanics import battle_phase
from ship import Ship
import random


class scene_handler:
    
    def __init__(self,initial_scene,screen):
        self.current_scene = initial_scene
        self.screen = screen
        self.buttons = []

        self.ships = ["assets/ship1_inPixio.png", "assets/ship2_inPixio.png", "assets/ship3_inPixio.png","assets/ship4_inPixio.png",
                 "assets/ship5_inPixio.png","assets/ship6_inPixio.png","assets/ship7_inPixio.png","assets/ship8_inPixio.png"]
        self.shipnum = 0
        self.ship = Ship(0,0,0)
        crews = []
        num_crews = 8
        for i in range(1,num_crews+1):
            crews += [Ship(random.randrange(1, 31), random.randrange(1, 21), random.randrange(0, 1001))]
        self.crews = crews

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
            self.scene_lose()

    def scene_start(self):
        bg = pygame.image.load("assets/start.png")
        self.screen.blit(pygame.transform.scale(bg, (800, 800)), (0, 0))

        start_button = Button(self.screen, 400, 700, 80, 80, "Start", action=lambda: self.change_scene(1))
        self.buttons.append(start_button)
        start_button.draw()

        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                for button in self.buttons:
                    button.handle_event(event)
            if self.current_scene != 0:
                running = False
                self.buttons.clear()
            pygame.display.flip()
                
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                running = False

   
 
    def scene_setup(self):
        bg = pygame.image.load("assets/oceanMap.png")
        
        self.screen.blit(pygame.transform.scale(bg, (800, 800)), (0, 0))
        
        x=50
        y=150
        counter = 0
        text = []
        count = 0
        for ship in self.ships:
            if counter == 4:
                x = 670
                y = 150

            ship_button = Button(self.screen, x, y, 80, 80, image=ship,action=lambda:self.ship_chooser(ship))
            self.buttons.append(ship_button)
            ship_button.draw()
            y+=150
            counter += 1
        #textboxes hehe
        font = pygame.font.Font(None, 36)
        x = 80
        y = 3
        counter2 = 0
        text = ['','','','','','','','']
        for i in range(8):
            int1 = random.randrange(1, 31)
            int2 = random.randrange(1, 21)
            int3 = random.randrange(0, 1001)
            text[i] = str(int1) + ' ' + str(int2) + ' ' + str(int3)
            if counter2 == 4:
                x = 350
                y = 3
            textbox = pygame.image.load("assets/setup_box.png")
            pygame.transform.scale(textbox, (5,5)) #idk how to change its size
            self.screen.blit(textbox, (x, y))
            # Render the text
            text_surface = font.render(text[i], True, (0, 0, 0))

            # Blit the text onto the screen
            text_rect = text_surface.get_rect(center=(x+225 , y+180))
            self.screen.blit(text_surface, text_rect)
            y+=150
            counter2+=1

        crews = []
        num_crews = 8

        for i in range(1, num_crews+1):
            crews += [Ship(random.randrange(1, 31), random.randrange(1, 21), random.randrange(0, 1001))]

        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                for button in self.buttons:
                    button.handle_event(event)
            if self.current_scene != 1:
                running = False
                self.buttons.clear()
            
            pygame.display.flip()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                running = False
            
    def ship_chooser(self,ship):
        self.change_scene(2)
        self.shipnum = self.ships.index(ship)
        self.ship = self.crews[self.shipnum]

    def scene_main(self):   
        bg = pygame.image.load("assets/oceanMap.png")
        self.screen.blit(pygame.transform.scale(bg, (800, 800)), (0, 0))
        ship_margin = 50

        ship_x = 150
        ship_y = 250

        b1 = Button(self.screen,400,700,80,80,"Battle",action=lambda:self.change_scene(3))
        b1.draw()
        self.buttons.append(b1)

        for i in range(1, 9):
            
            ship_image = pygame.image.load(f"assets/ship{i}_inPixio.png")

            resized_ship = pygame.transform.scale(ship_image, (100, 100))

            self.screen.blit(resized_ship, (ship_x, ship_y))

            ship_x += 100 + ship_margin

            if i % 4 == 0:
                ship_x = 150
                ship_y += 150 + ship_margin
        
        running = True
        while running:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        running = False
                    for button in self.buttons:
                        button.handle_event(event)
                if self.current_scene != 2:
                    running = False
                    self.buttons.clear()
                
                pygame.display.flip()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    running = False
            

    def scene_battle(self):

        font = pygame.font.Font(None, 36)
        value = 0
        active = False
      
        bg = pygame.image.load("assets/battle.png")

        
        textbox = pygame.image.load("assets/textbox.png")

        self.screen.blit(pygame.transform.scale(bg, (800, 800)), (0, 0))
        textbox = pygame.image.load("assets/textbox.png")
        self.screen.blit(pygame.transform.scale(textbox, (400, 400)), (0, 0))
        b2 = Button(self.screen,400,700, 80, 80, text="FINISH", color=(100,100,100),action=lambda:self.change_scene(4))

        #text1
        text1 = ["TIME TO FIGHT!!!! Well, almost..." ,
                 "First you need to assemble ",
                "the crew! You only have a ",
                "certain amount of crew members",
                "so make sure you allocate accordingly",
                "with your power level!"]
        
        text2 = ["You have to allocate your crew to",
                 "four different stations. The more you",
                 "allocate to any one station, the more ",
                 "likely you are to win that part of the",
                 "battle, but the more likley you are to",
                 "lose the others, so be strategic!!",
                 "Your total crew members and power level",
                 "are shown below, so good luck!!!"
                 ]
       
        font = pygame.font.Font('freesansbold.ttf', 15)
        fade_rate = 1
        fade = 0


        b1 = Button(self.screen, 20,500, 80, 80, text="OK", color=(100,100,100))
        b1.draw()
        self.buttons.append(b1)

        running = True


        inputs = []
        ystart = 340
        for x in range(4):
            inputs.append(pygame.Rect(400, ystart, 100, 40))
            ystart += 100
       
        values = [0,0,0,0]
        active = [False] * 4
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                for button in self.buttons:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if button.rect.collidepoint(event.pos):
                            if text1 == text2:
                                self.screen.blit(pygame.transform.scale(bg, (800, 800)), (0, 0))
                                text1 = ""
                                self.buttons.clear()
                            elif text1 == "":
                                self.screen.blit(pygame.transform.scale(bg, (800, 800)), (0, 0))
                                b2.draw()
                                enemy = random.choice(self.crews)
                                enemy_pos = self.generate_list_with_sum(int(enemy.crew))
                                result = battle_phase(self.ship,values,enemy,enemy_pos)
                                if result == 1:
                                    self.change_scene(4)
                                elif result == -1:
                                    self.change_scene(5)
                                else:
                                    self.change_scene(2)
                            else:
                                text1 = text2
                                self.screen.blit(pygame.transform.scale(bg, (800, 800)), (0, 0))
                                self.screen.blit(pygame.transform.scale(textbox, (500, 500)), (0, 0))
                                button.draw()


                for input in range(len(inputs)):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if inputs[input].collidepoint(event.pos):
                            active[input] = not active[input]  # Update the active status for the specific input
                        else:
                            active[input] = False  # Deactivate other inputs

                    if active[input] and event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            active[input] = False
                        elif event.key == pygame.K_BACKSPACE:
                            if values[input] > 0:
                                values[input] = int(values[input] // 10)  # Remove the last digit
                                self.screen.blit(pygame.transform.scale(bg, (800, 800)), (0, 0))
                        elif event.key in [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                            digit = int(event.unicode)
                            values[input] = values[input] * 10 + digit
                            self.screen.blit(pygame.transform.scale(bg, (800, 800)), (0, 0))
                            

                yvals = [340 + (100 * x) for x in range(4)]
                input_names = ["Attack", "Defend", "Sail", "Medic"]
                if text1 == "":
                    for input in range(len(inputs)):
                        value_text = font.render(str(values[input]), True, (0, 0, 0))
                        self.screen.blit(value_text, (400, yvals[input]))
                        pygame.draw.rect(self.screen, (255, 255, 255), (397, yvals[input] - 3, 100, 40), 2)
                        label_text = font.render(input_names[input], True, (0, 0, 0))
                        self.screen.blit(label_text, (400, yvals[input] - 15))


            if text1 == "":
                self.buttons.clear()  # Clear all buttons
                b2.draw()
                self.buttons.append(b2)
                
            current_y = -10
            for line in text1:
                text = font.render(line, True,(0,0,0))
                text.set_alpha(fade)
                print(text.get_alpha())
                textRect = text.get_rect()
                current_y+=50
                textRect.topleft = (35,current_y)
                self.screen.blit(text,textRect)
            
                
            if fade != 100:
                fade+= fade_rate
                pygame.time.delay(50)


            pygame.display.flip()

            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                running = False
            
            if self.current_scene != 3:
                running = False
                self.buttons.clear()
                print(values)
        
    def generate_list_with_sum(self, target_sum):
        if target_sum < 4:
            return None  # It's impossible to create a list of 4 numbers that add up to the target sum.

        while True:
            numbers = []
            remaining_sum = target_sum

            for _ in range(3):  # Choose 3 random numbers first
                if remaining_sum <= 0:
                    break

                # Generate a random number between 1 and the remaining sum
                num = random.randint(1, remaining_sum)
                numbers.append(num)
                remaining_sum -= num

            # The last element is calculated to ensure the sum is exactly equal to the target_sum
            last_num = target_sum - sum(numbers)
            numbers.append(last_num)

            if sum(numbers) == target_sum:
                return numbers

    def scene_win(self):
        bg = pygame.image.load("assets/win.png")
        self.screen.blit(pygame.transform.scale(bg, (820, 820)), (0, 0))
        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False


            pygame.display.flip()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                running = False
                
                pygame.display.flip()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    running = False
                    
    def scene_lose(self):
        bg = pygame.image.load("assets/lose.png")
        self.screen.blit(pygame.transform.scale(bg, (800, 800)), (0, 0))

        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False


            pygame.display.flip()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                running = False

class Button:
    
    def __init__(self, surface, x, y, width, height, text, color, text_color, action=None):
        self.surface = surface
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.text_color = text_color

    def __init__(self, surface, x, y, width, height, text=None, image=None, color=None, text_color=None, font=None, action=None):
        self.surface = surface
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.image = None
        if image:
            self.image = pygame.image.load(image)
            self.image = pygame.transform.scale(self.image, (width, height))
        self.color = color if color else (0, 0, 0,0)  # Default color
        self.text_color = text_color if text_color else (255, 255, 255)  # Default text color

        self.font = pygame.font.Font(None, 36)
        self.action = action

    def draw(self):        
        if self.image:
            self.surface.blit(self.image, self.rect.topleft)
        else:
            pygame.draw.rect(self.surface, self.color, self.rect)

        if self.text:
            pygame.draw.rect(self.surface, self.color, self.rect)
            text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            self.surface.blit(text_surface, text_rect)
            text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            self.surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if self.rect.collidepoint(event.pos):
                    if self.action is not None:
                        self.action()

