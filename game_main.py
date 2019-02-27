import pygame
from game_sprites import *


class game():

    def __init__(self):
        print("游戏初始化")

        # 1.创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)

        self.__create_sprites()

        # 2.创建游戏的时钟
        self.clock = pygame.time.Clock()

        # 设置定时器事件 - 创建敌机1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

    def __create_sprites(self):

        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

    def start_game(self):
        print("游戏开始...")

        while True:

            # 1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)

            # 2.事件监听
            self.__event_handler()

            # 4.更新/绘制精灵组
            self.__update_sprites()

            self.__hit_enemy()

            self.__enemy_alive()

            # 5.更新屏幕显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():

            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                self.__game_over()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.hero.fire()
            elif event.type == CREATE_ENEMY_EVENT:
                self.enemy_group.add(Enemy())

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

    def __hit_enemy(self):
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

    def __enemy_alive(self):
        if len(pygame.sprite.spritecollide(self.hero, self.enemy_group, False)):
            self.hero.die()
            pygame.time.set_timer(CREATE_ENEMY_EVENT, 0)

    def __game_over(self):
        print("游戏结束")

        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = game()

    # 启动游戏
    game.start_game()
