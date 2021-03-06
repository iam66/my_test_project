import sys
import pygame
from settings import Settings

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    al_settings = Settings()
    screen = pygame.display.set_mode(
        (al_settings.screen_height, al_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 开始游戏的主循环
    while True:
        # 监视鼠标和键盘事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环时都会重绘屏幕
        screen.fill(al_settings.bg_color)

        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()
