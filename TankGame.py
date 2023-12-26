import pygame
import random
import time


class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.current_win_streak = 0
        self.top_win_streak = 0
        self.best_attempts = float("inf")

        pygame.mixer.init()
        pygame.mixer.music.load("resources/a3be96e64e9ae64.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        self.display_width = 800
        self.display_height = 600

        self.game_layout_display = pygame.display.set_mode(
            (self.display_width, self.display_height)
        )

        self.splash_screen_background = pygame.image.load("resources/screen-13.jpg")
        self.background = pygame.image.load(
            "resources/f1adf3a5912cae1b6ec421796eec064a.png"
        )

        self.wheat = (245, 222, 179)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.blue = (0, 0, 255)
        self.red = (200, 0, 0)
        self.light_red = (255, 0, 0)
        self.yellow = (200, 200, 0)
        self.light_yellow = (255, 255, 0)
        self.green = (34, 177, 76)
        self.light_green = (0, 255, 0)

        self.clock = pygame.time.Clock()

        self.tnk_width = 40
        self.tnk_height = 20
        self.tur_width = 5
        self.whl_width = 5
        self.grnd_height = 35

        self.s_font = pygame.font.SysFont("Times New Roman", 25)
        self.m_font = pygame.font.SysFont("Times New Roman", 50)
        self.l_font = pygame.font.SysFont("Times New Roman", 85)
        self.vs_font = pygame.font.SysFont("Times New Roman", 25)

        self.top_win_streaks = self.load_win_streaks()

    def save_win_streaks(self):
        with open("win_streaks.txt", "w") as file:
            for streak in self.top_win_streaks:
                file.write(str(streak) + "\n")

    def load_win_streaks(self):
        try:
            with open("win_streaks.txt", "r") as file:
                return [int(line.strip()) for line in file.readlines()]
        except FileNotFoundError:
            return [0, 0, 0]

    def txt_object(self, txt, color, size="small"):
        if size == "small":
            txtSrfc = self.s_font.render(txt, True, color)
        elif size == "medium":
            txtSrfc = self.m_font.render(txt, True, color)
        elif size == "large":
            txtSrfc = self.l_font.render(txt, True, color)
        return txtSrfc, txtSrfc.get_rect()

    def txt_btn(self, message, color, btnx, btny, btnwidth, btnheight, size="small"):
        txtSrf, textRect = self.txt_object(message, color, size)
        textRect.center = ((btnx + (btnwidth / 2)), btny + (btnheight / 2))
        self.game_layout_display.blit(txtSrf, textRect)

    def msg_screen(self, message, color, y_displace=0, size="small"):
        txtSrf, textRect = self.txt_object(message, color, size)
        textRect.center = (
            int(self.display_width / 2),
            int(self.display_height / 2) + y_displace,
        )
        self.game_layout_display.blit(txtSrf, textRect)

    def tank(self, x, y, turret_position):
        x = int(x)
        y = int(y)

        pos_Turrets = [
            (x - 27, y - 2),
            (x - 26, y - 5),
            (x - 25, y - 8),
            (x - 23, y - 12),
            (x - 20, y - 14),
            (x - 18, y - 15),
            (x - 15, y - 17),
            (x - 13, y - 19),
            (x - 11, y - 21),
        ]

        pygame.draw.circle(
            self.game_layout_display, self.red, (x, y), int(self.tnk_height / 2)
        )
        pygame.draw.rect(
            self.game_layout_display,
            self.red,
            (x - self.tnk_height, y, self.tnk_width, self.tnk_height),
        )

        pygame.draw.line(
            self.game_layout_display,
            self.red,
            (x, y),
            pos_Turrets[turret_position],
            self.tur_width,
        )

        pygame.draw.circle(
            self.game_layout_display, self.red, (x - 15, y + 20), self.whl_width
        )
        pygame.draw.circle(
            self.game_layout_display, self.red, (x - 10, y + 20), self.whl_width
        )
        pygame.draw.circle(
            self.game_layout_display, self.red, (x - 5, y + 20), self.whl_width
        )
        pygame.draw.circle(
            self.game_layout_display, self.red, (x, y + 20), self.whl_width
        )
        pygame.draw.circle(
            self.game_layout_display, self.red, (x + 5, y + 20), self.whl_width
        )
        pygame.draw.circle(
            self.game_layout_display, self.red, (x + 10, y + 20), self.whl_width
        )
        pygame.draw.circle(
            self.game_layout_display, self.red, (x + 15, y + 20), self.whl_width
        )

        return pos_Turrets[turret_position]
        pass

    def computer_tank(self, x, y, turret_position):
        x = int(x)
        y = int(y)

        pos_Turrets = [
            (x + 27, y - 2),
            (x + 26, y - 5),
            (x + 25, y - 8),
            (x + 23, y - 12),
            (x + 20, y - 14),
            (x + 18, y - 15),
            (x + 15, y - 17),
            (x + 13, y - 19),
            (x + 11, y - 21),
        ]

        pygame.draw.circle(
            self.game_layout_display, self.blue, (x, y), int(self.tnk_height / 2)
        )
        pygame.draw.rect(
            self.game_layout_display,
            self.blue,
            (x - self.tnk_height, y, self.tnk_width, self.tnk_height),
        )

        pygame.draw.line(
            self.game_layout_display,
            self.blue,
            (x, y),
            pos_Turrets[turret_position],
            self.tur_width,
        )

        pygame.draw.circle(
            self.game_layout_display, self.blue, (x - 15, y + 20), self.whl_width
        )
        pygame.draw.circle(
            self.game_layout_display, self.blue, (x - 10, y + 20), self.whl_width
        )

        pygame.draw.circle(
            self.game_layout_display, self.blue, (x - 15, y + 20), self.whl_width
        )
        pygame.draw.circle(
            self.game_layout_display, self.blue, (x - 10, y + 20), self.whl_width
        )
        pygame.draw.circle(
            self.game_layout_display, self.blue, (x - 5, y + 20), self.whl_width
        )
        pygame.draw.circle(
            self.game_layout_display, self.blue, (x, y + 20), self.whl_width
        )
        pygame.draw.circle(
            self.game_layout_display, self.blue, (x + 5, y + 20), self.whl_width
        )
        pygame.draw.circle(
            self.game_layout_display, self.blue, (x + 10, y + 20), self.whl_width
        )
        pygame.draw.circle(
            self.game_layout_display, self.blue, (x + 15, y + 20), self.whl_width
        )

        return pos_Turrets[turret_position]
        pass

    def btn(
        self,
        txt,
        x,
        y,
        width,
        height,
        inactive_color,
        active_color,
        action=None,
        size="small",
    ):
        cursor = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > cursor[0] > x and y + height > cursor[1] > y:
            pygame.draw.rect(
                self.game_layout_display, active_color, (x, y, width, height)
            )
            if click[0] == 1 and action != None:
                if action == "quit":
                    pygame.quit()
                    quit()

                if action == "play":
                    self.gameLoop()

                if action == "main":
                    self.game_intro()

                if action == "win_streaks":
                    self.win_streak_menu()
        else:
            pygame.draw.rect(
                self.game_layout_display, inactive_color, (x, y, width, height)
            )

        self.txt_btn(txt, self.black, x, y, width, height)
        pass

    def pause(self):
        paused = True
        self.msg_screen("Paused", self.white, -100, size="large")
        self.msg_screen("Press P to continue playing or ESC to quit", self.wheat, 25)
        pygame.display.update()
        while paused:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        paused = False
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

            self.clock.tick(10)
        pass

    def barrier(self, x_loc, ran_height, bar_width):
        pygame.draw.rect(
            self.game_layout_display,
            self.green,
            [x_loc, self.display_height - ran_height, bar_width, ran_height],
        )
        pass

    def explosion(self, x, y, size=50):
        exp = True

        while exp:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            startPoint = x, y

            choice_colors = [self.red, self.light_red, self.yellow, self.light_yellow]

            mgntde = 1

            while mgntde < size:
                exploding_bit_x = x + random.randrange(-1 * mgntde, mgntde)
                exploding_bit_y = y + random.randrange(-1 * mgntde, mgntde)

                pygame.draw.circle(
                    self.game_layout_display,
                    choice_colors[random.randrange(0, 4)],
                    (exploding_bit_x, exploding_bit_y),
                    random.randrange(1, 5),
                )
                mgntde += 1

                pygame.display.update()
                self.clock.tick(100)

            exp = False
        pass

    def play_game(game_instance, current_win_streak):
        number_to_guess = random.randint(1, 100)
        attempts = 0

        while True:
            guess = int(input("Guess the number (1-100): "))
            attempts += 1

            if guess < number_to_guess:
                print("Слишком низко! Попробуйте снова.")
            elif guess > number_to_guess:
                print("Слишком высоко! Попробуйте снова.")
            else:
                print(f"Поздравляем!")
                if attempts < game_instance.best_attempts:
                    game_instance.best_attempts = attempts
                    print("Новая лучшая попытка!")
                if current_win_streak > game_instance.top_win_streak:
                    game_instance.top_win_streak = current_win_streak
                    print("Новый рекорд!")
                break

    def start_game(self):
        top_win_streak = 0
        current_win_streak = 0
        game_instance = Game()

        while True:
            print("Добро пожаловать в Мир Танков!")
            print("1. Играть")
            print("2. Выйти")

            choice = input("Ваш выбор: ")

            if choice == "1":
                self.play_game(game_instance, current_win_streak)
                current_win_streak += 1
            elif choice == "2":
                print("Спасибо за игру!")
                break
            else:
                print("Выбор неправильный! Выберите снова!")
        pass

    def playerfireShell(
        self,
        xy,
        tankx,
        tanky,
        turPost,
        gun_power,
        xloc,
        bar_width,
        ranHeight,
        eTankX,
        eTankY,
    ):
        fire = True
        damage = 0

        startShell = list(xy)

        while fire:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.draw.circle(
                self.game_layout_display, self.red, (startShell[0], startShell[1]), 5
            )

            startShell[0] -= (12 - turPost) * 2

            startShell[1] += int(
                (((startShell[0] - xy[0]) * 0.015 / (gun_power / 50)) ** 2)
                - (turPost + turPost / (12 - turPost))
            )

            if startShell[1] > self.display_height - self.grnd_height:

                hit_x = int(
                    (startShell[0] * self.display_height - self.grnd_height)
                    / startShell[1]
                )
                hit_y = int(self.display_height - self.grnd_height)

                if eTankX + 15 > hit_x > eTankX - 15:
                    print("Critical Hit!")
                    damage = 25
                elif eTankX + 20 > hit_x > eTankX - 20:
                    print("Hard Hit!")
                    damage = 15
                elif eTankX + 30 > hit_x > eTankX - 30:
                    print("Medium Hit")
                    damage = 10
                elif eTankX + 40 > hit_x > eTankX - 40:
                    print("Light Hit")
                    damage = 100

                self.explosion(hit_x, hit_y)
                fire = False

            check_x_1 = startShell[0] <= xloc + bar_width
            check_x_2 = startShell[0] >= xloc
            check_y_1 = startShell[1] <= self.display_height
            check_y_2 = startShell[1] >= self.display_height - ranHeight

            if check_x_1 and check_x_2 and check_y_1 and check_y_2:
                hit_x = int((startShell[0]))
                hit_y = int(startShell[1])
                self.explosion(hit_x, hit_y)
                fire = False

            pygame.display.update()
            self.clock.tick(60)
        return damage

    def win_streak_menu(self):
        in_menu = True
        while in_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.game_layout_display.blit(self.background, (0, 0))
            self.msg_screen("Top-3 Win Streaks", self.wheat, -100, size="medium")

            for i, streak in enumerate(self.top_win_streaks):
                self.msg_screen(f"{i + 1}. {streak} Wins", self.wheat, 30 * i)

            self.btn(
                "Menu", 350, 500, 100, 50, self.wheat, self.light_green, action="main"
            )

            pygame.display.update()
            self.clock.tick(5)
        pass

    def game_over(self):

        game_over = True

        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.game_layout_display.blit(self.background, (0, 0))
            self.msg_screen("Game Over", self.white, -100, size="large")
            self.msg_screen("Вы проиграли", self.wheat, -30)

            self.btn(
                "Играть снова",
                150,
                500,
                150,
                50,
                self.wheat,
                self.light_green,
                action="play",
            )
            self.btn(
                "Выйти", 550, 500, 100, 50, self.wheat, self.light_red, action="quit"
            )

            pygame.display.update()

            self.clock.tick(15)

        current_win_streak = 0

        current_win_streak += 1

        self.top_win_streaks.append(current_win_streak)
        top_win_streaks = sorted(self.top_win_streaks, reverse=True)[:3]

        win = True

        while win:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.game_layout_display.blit(self.background, (0, 0))
            self.msg_screen("You won!", self.white, -100, size="large")
            self.msg_screen("Congratulations!", self.wheat, -30)

            # Кнопки для выбора дальнейших действий
            self.btn(
                "Play again",
                150,
                500,
                150,
                50,
                self.wheat,
                self.light_green,
                action="play",
            )
            self.btn(
                "Quit", 550, 500, 100, 50, self.wheat, self.light_red, action="quit"
            )

            pygame.display.update()
            self.clock.tick(15)

        self.game_instance.game_over()

    def health_bars(self, p_health=None, e_health=None):
        if p_health > 75:
            p_health_color = self.green
        elif p_health > 50:
            p_health_color = self.yellow
        else:
            p_health_color = self.red

        if e_health > 75:
            e_health_color = self.green
        elif e_health > 50:
            e_health_color = self.yellow
        else:
            e_health_color = self.red

        pygame.draw.rect(
            p_health.game_layout_display, p_health_color, (680, 25, p_health, 25)
        )
        pygame.draw.rect(
            p_health.game_layout_display, e_health_color, (20, 25, e_health, 25)
        )

    def computerfireShell(
        self,
        xy,
        tankx,
        tanky,
        turPost,
        gun_power,
        xloc,
        bar_width,
        ranHeight,
        ptankx,
        ptanky,
    ):
        damage = 0
        cPower = 1
        pow_found = False

        while not pow_found:
            cPower += 1
            if cPower > 100:
                pow_found = True

            fire = True
            startShell = list(xy)

            while fire:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                check_x_1 = startShell[0] <= xloc + bar_width
                check_x_2 = startShell[0] >= xloc
                check_y_1 = startShell[1] <= self.display_height
                check_y_2 = startShell[1] >= self.display_height - ranHeight

                if check_x_1 and check_x_2 and check_y_1 and check_y_2:
                    hit_x = int((startShell[0]))
                    hit_y = int(startShell[1])
                    self.explosion(hit_x, hit_y)
                    fire = False

                startShell[0] += (12 - turPost) * 2
                startShell[1] += int(
                    (((startShell[0] - xy[0]) * 0.015 / (cPower / 50)) ** 2)
                    - (turPost + turPost / (12 - turPost))
                )

                if startShell[1] > self.display_height - self.grnd_height:
                    hit_x = int(
                        (startShell[0] * self.display_height - self.grnd_height)
                        / startShell[1]
                    )
                    hit_y = int(self.display_height - self.grnd_height)

                    if ptankx + 15 > hit_x > ptankx - 15:
                        print("target acquired!")
                        pow_found = True
                    fire = False

                check_x_1 = startShell[0] <= xloc + bar_width
                check_x_2 = startShell[0] >= xloc

                check_y_1 = startShell[1] <= self.display_height
                check_y_2 = startShell[1] >= self.display_height - ranHeight

                if check_x_1 and check_x_2 and check_y_1 and check_y_2:
                    hit_x = int((startShell[0]))
                    hit_y = int(startShell[1])

                    fire = False

        fire = True
        startShell = list(xy)
        print("FIRE!", xy)

        while fire:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.draw.circle(
                self.game_layout_display, self.red, (startShell[0], startShell[1]), 5
            )

            startShell[0] += (12 - turPost) * 2

            gun_power = random.randrange(int(cPower * 0.90), int(cPower * 1.10))

            startShell[1] += int(
                (((startShell[0] - xy[0]) * 0.015 / (gun_power / 50)) ** 2)
                - (turPost + turPost / (12 - turPost))
            )

            if startShell[1] > self.display_height - self.grnd_height:
                hit_x = int(
                    (startShell[0] * self.display_height - self.grnd_height)
                    / startShell[1]
                )
                hit_y = int(self.display_height - self.grnd_height)

                if ptankx + 15 > hit_x > ptankx - 15:
                    print("Critical Hit!")
                    damage = 25
                elif ptankx + 20 > hit_x > ptankx - 20:
                    print("Hard Hit!")
                    damage = 15
                elif ptankx + 30 > hit_x > ptankx - 30:
                    print("Medium Hit")
                    damage = 10
                elif ptankx + 40 > hit_x > ptankx - 40:
                    print("Light Hit")
                    damage = 5

                self.explosion(hit_x, hit_y)
                fire = False

            check_x_1 = startShell[0] <= xloc + bar_width
            check_x_2 = startShell[0] >= xloc

            check_y_1 = startShell[1] <= self.display_height
            check_y_2 = startShell[1] >= self.display_height - ranHeight

            pygame.display.update()
            self.clock.tick(60)
        return damage
        pass

    def you_win(self):
        global current_win_streak
        global top_win_streaks

        current_win_streak += 1

        top_win_streaks.append(current_win_streak)
        top_win_streaks = sorted(top_win_streaks, reverse=True)[:3]
        self.save_win_streaks(top_win_streaks)

        win = True

        while win:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.game_layout_display.blit(self.background, (0, 0))
            self.msg_screen("You won!", self.white, -100, size="large")
            self.msg_screen("Congratulations!", self.wheat, -30)

            # Кнопки для выбора дальнейших действий
            self.btn(
                "Play again",
                150,
                500,
                150,
                50,
                self.wheat,
                self.light_green,
                action="play",
            )
            self.btn(
                "Quit", 550, 500, 100, 50, self.wheat, self.light_red, action="quit"
            )

            pygame.display.update()
            self.clock.tick(15)
        pass

    def power(self, level):
        text = self.s_font.render("Power: " + str(level) + "%", True, self.wheat)
        self.game_layout_display.blit(text, [self.display_width / 2, 0])
        pass

    def game_intro(self):
        pygame.mixer.init()
        pygame.mixer.music.load("resources/a3be96e64e9ae64.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        intro = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()

            self.game_layout_display.blit(self.splash_screen_background, (-100, -300))
            self.msg_screen(
                "Добро пожаловать в Мир танков!", self.black, -250, size="medium"
            )
            self.msg_screen("Ваша цель - стрелять и уничтожить", self.black, -200)
            self.msg_screen(
                "вражеский танк быстрее, чем он уничтожит вас!", self.black, -160
            )
            self.msg_screen("Продолжить - P, выйти - ESC", self.black, 180)

            self.btn(
                "Играть",
                150,
                500,
                100,
                50,
                self.wheat,
                self.light_green,
                action="play",
                size="small",
            )
            self.btn(
                "Выйти",
                550,
                500,
                100,
                50,
                self.wheat,
                self.light_red,
                action="quit",
                size="small",
            )
            self.btn(
                "Top-3 Win Streaks",
                300,
                500,
                200,
                50,
                self.wheat,
                self.light_yellow,
                action="win_streaks",
            )

            pygame.display.update()
            self.clock.tick(15)
        pass

    def gameLoop(self):
        gExit = False
        gOver = False
        speed = 30

        p_health = 100
        e_health = 100

        bar_width = 50

        mTankX = self.display_width * 0.9
        mTankY = self.display_height * 0.9
        tnkMove = 0
        curTurPost = 0
        changeTurs = 0

        eTankX = self.display_width * 0.1
        eTankY = self.display_height * 0.9

        f_power = 50
        p_change = 0

        xloc = (self.display_width / 2) + random.randint(
            -0.1 * self.display_width, 0.1 * self.display_width
        )
        ranHeight = random.randrange(
            self.display_height * 0.1, self.display_height * 0.6
        )

        self.game_layout_display.blit(self.background, (0, 0))
        pygame.display.update()

        while not gExit:

            if gOver == True:

                self.msg_screen("Game Over", self.red, -50, size="large")
                self.msg_screen("Продолжить - P, выйти - ESC", self.black, 50)
                pygame.display.update()
                while gOver == True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            gExit = True
                            gOver = False

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_p:
                                self.gameLoop()
                            elif event.key == pygame.K_ESCAPE:

                                gExit = True
                                gOver = False

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    gExit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        tnkMove = -5

                    elif event.key == pygame.K_RIGHT:
                        tnkMove = 5

                    elif event.key == pygame.K_UP:
                        changeTurs = 1

                    elif event.key == pygame.K_DOWN:
                        changeTurs = -1

                    elif event.key == pygame.K_p:
                        self.pause()

                    elif event.key == pygame.K_SPACE:

                        damage = self.playerfireShell(
                            gun,
                            mTankX,
                            mTankY,
                            curTurPost,
                            f_power,
                            xloc,
                            bar_width,
                            ranHeight,
                            eTankX,
                            eTankY,
                        )
                        e_health -= damage

                        posMovement = ["f", "r"]
                        moveInd = random.randrange(0, 2)

                        for x in range(random.randrange(0, 25)):

                            if (
                                self.display_width * 0.3
                                > eTankX
                                > self.display_width * 0.03
                            ):
                                if posMovement[moveInd] == "f":
                                    eTankX += 5
                                elif posMovement[moveInd] == "r":
                                    eTankX -= 5

                                self.game_layout_display.blit(self.background, (0, 0))
                                self.health_bars(p_health, e_health)
                                gun = self.tank(mTankX, mTankY, curTurPost)
                                e_gun = self.computer_tank(eTankX, eTankY, 8)
                                f_power += p_change

                                self.power(f_power)

                                self.barrier(xloc, ranHeight, bar_width)
                                self.game_layout_display.fill(
                                    self.green,
                                    rect=[
                                        0,
                                        self.display_height - self.grnd_height,
                                        self.display_width,
                                        self.grnd_height,
                                    ],
                                )
                                pygame.display.update()

                                self.clock.tick(speed)

                        damage = self.computerfireShell(
                            e_gun,
                            eTankX,
                            eTankY,
                            8,
                            50,
                            xloc,
                            bar_width,
                            ranHeight,
                            mTankX,
                            mTankY,
                        )
                        p_health -= damage

                    elif event.key == pygame.K_a:
                        p_change = -1
                    elif event.key == pygame.K_d:
                        p_change = 1

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        tnkMove = 0

                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        changeTurs = 0

                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        p_change = 0

            self.game_layout_display.blit(self.background, (0, 0))

            mTankX += tnkMove

            curTurPost += changeTurs

            if curTurPost > 8:
                curTurPost = 8
            elif curTurPost < 0:
                curTurPost = 0

            if mTankX - (self.tnk_width / 2) < xloc + bar_width:
                mTankX += 5

            self.game_layout_display.blit(self.background, (0, 0))
            self.health_bars(p_health, e_health)
            gun = self.tank(mTankX, mTankY, curTurPost)
            e_gun = self.computer_tank(eTankX, eTankY, 8)

            f_power += p_change

            if f_power > 100:
                f_power = 100
            elif f_power < 1:
                f_power = 1

            self.power(f_power)

            self.barrier(xloc, ranHeight, bar_width)
            self.game_layout_display.fill(
                self.green,
                rect=[
                    0,
                    self.display_height - self.grnd_height,
                    self.display_width,
                    self.grnd_height,
                ],
            )
            pygame.display.update()

            if p_health < 1:
                self.game_over()
            elif e_health < 1:
                self.you_win()
            self.clock.tick(speed)

        pygame.quit()
        quit()
        pass


if __name__ == "__main__":
    game = Game()
    game.start_game()
