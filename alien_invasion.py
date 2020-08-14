
import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_function as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	ship = Ship(ai_settings,screen)
	bullets = Group()
	aliens = Group()
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)
	play_button = Button(ai_settings,screen,"Play")

	gf.create_fleet(ai_settings,screen,ship,aliens)

	while True:
		gf.check_events(ai_settings,screen,stats,play_button,ship,sb,aliens,
						bullets)


		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,stats,sb,
							  ship,aliens,bullets)
			gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)

		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,
						 play_button)
run_game()