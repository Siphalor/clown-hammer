##########
# ASSETS #
##########
# Images created by myself with GIMP: https://www.gimp.org
# Sounds created with Bfxr: http://www.bfxr.net
# Music created with BeepBox: http://www.beepbox.co
# Font ModerDOS created by Jayvee Enaguas: https://http://www.dafont.com/moder-dos-437.font


import sys, pygame, random, math, platform, os
from pygame.locals import *

_event_counter = pygame.USEREVENT
def get_next_event_id():
	global _event_counter
	_event_counter += 1
	return _event_counter


############################################
# Important global variables and constants #
############################################

game_grid = (5, 4)
TICK_EVENT = get_next_event_id()
tick_delay = 250
waiter = 0

WINDOWS = 1

def main():
	global size, tile_size, spawn_delay, tick_delay, lifes, game_state, score, WINDOWS, background, table, can_idle, game_grid, game_matrix, spawn_accelaretor
	
	if platform.system() == 'Windows':
		WINDOWS = 1
	else:
		WINDOWS = 0
	
	# Story
	print('The ex friend of your partner wants to celebrate his birthday.\nBut you don\'t like him. And you don\'t like parties.\n')
	c_pause()
	print('\nTo prevent your girl friend from getting amused by her old one \033[1myou have to stop the clown which should come to the party\033[0m.\n')
	c_pause()
	print('\nOr should I say, the clown \033[1mARMY\033[0m?\n')
	c_pause()
	
	# Init
	pygame.init()
	infoObj = pygame.display.Info()
	hammer_pos = [0,0]
	pygame.mouse.set_visible(False)
	pygame.time.set_timer(TICK_EVENT, tick_delay)
	
	# music
	pygame.mixer.music.load('assets/loop.wav')
	pygame.mixer.music.play(-1)
	
	# Calculate stuff for tiles
	size = (infoObj.current_w // 2, infoObj.current_w // 2 // game_grid[0] * game_grid[1])
	print(size)
	if size[0] / game_grid[0] < size[1] / game_grid[1]:
		tile_size = (size[0] - size[0] // 5) // game_grid[0]
	else:
		tile_size = (size[1] - size[1] // 5) // game_grid[1]
	
	# Load font
	font = pygame.font.Font('assets/ModernDOS.ttf', tile_size)
	
	# Load sounds
	confetti_sound = pygame.mixer.Sound('assets/confetti.wav')
	confetti_sound.set_volume(0.3)
	explosion_sound = pygame.mixer.Sound('assets/explosion.wav')
	explosion_sound.set_volume(0.2)
	hammer_sound = pygame.mixer.Sound('assets/hammer.wav')
	hammer_sound.set_volume(0.4)
	
	# Load images
	table = pygame.image.load('assets/table.png')
	table = pygame.transform.scale(table, size)
	
	hammer = pygame.image.load('assets/hammer.png')
	hammer = pygame.transform.scale(hammer, (tile_size, tile_size))
	hammer_1 = pygame.image.load('assets/hammer_use_1.png')
	hammer_1 = pygame.transform.scale(hammer_1, (tile_size, tile_size))
	hammer_2 = pygame.image.load('assets/hammer_use_2.png')
	hammer_2 = pygame.transform.scale(hammer_2, (tile_size, tile_size))
	
	can_idle = pygame.image.load('assets/can_idle.png')
	can_idle = pygame.transform.scale(can_idle, (tile_size, tile_size))
	
	can_clown = pygame.image.load('assets/can_clown.png')
	can_clown = pygame.transform.scale(can_clown, (tile_size, tile_size))
	can_clown_up_1 = pygame.image.load('assets/can_clown_up_1.png')
	can_clown_up_1 = pygame.transform.scale(can_clown_up_1, (tile_size, tile_size))
	can_clown_up_2 = pygame.image.load('assets/can_clown_up_2.png')
	can_clown_up_2 = pygame.transform.scale(can_clown_up_2, (tile_size, tile_size))
	can_clown_up_3 = pygame.image.load('assets/can_clown_up_3.png')
	can_clown_up_3 = pygame.transform.scale(can_clown_up_3, (tile_size, tile_size))
	
	can_explode_1 = pygame.image.load('assets/can_explode_1.png')
	can_explode_1 = pygame.transform.scale(can_explode_1, (tile_size, tile_size))
	can_explode_2 = pygame.image.load('assets/can_explode_2.png')
	can_explode_2 = pygame.transform.scale(can_explode_2, (tile_size, tile_size))
	can_explode_3 = pygame.image.load('assets/can_explode_3.png')
	can_explode_3 = pygame.transform.scale(can_explode_3, (tile_size, tile_size))
	can_explode_4 = pygame.image.load('assets/can_explode_4.png')
	can_explode_4 = pygame.transform.scale(can_explode_4, (tile_size, tile_size))
	
	can_confetti_1 = pygame.image.load('assets/can_confetti_1.png')
	can_confetti_1 = pygame.transform.scale(can_confetti_1, (tile_size, tile_size))
	can_confetti_2 = pygame.image.load('assets/can_confetti_2.png')
	can_confetti_2 = pygame.transform.scale(can_confetti_2, (tile_size, tile_size))
	can_confetti_3 = pygame.image.load('assets/can_confetti_3.png')
	can_confetti_3 = pygame.transform.scale(can_confetti_3, (tile_size, tile_size))
	
	confetti_1 = pygame.image.load('assets/confetti_1.png')
	confetti_1 = pygame.transform.scale(confetti_1, size)
	confetti_2 = pygame.image.load('assets/confetti_2.png')
	confetti_2 = pygame.transform.scale(confetti_2, size)
	confetti_3 = pygame.image.load('assets/confetti_3.png')
	confetti_3 = pygame.transform.scale(confetti_3, size)
	confetti_4 = pygame.image.load('assets/confetti_4.png')
	confetti_4 = pygame.transform.scale(confetti_4, size)
	confetti_5 = pygame.image.load('assets/confetti_5.png')
	confetti_5 = pygame.transform.scale(confetti_5, size)
	
	can_gift = pygame.image.load('assets/can_gift.png')
	can_gift = pygame.transform.scale(can_gift, (tile_size, tile_size))
	can_gift_1 = pygame.image.load('assets/can_gift_1.png')
	can_gift_1 = pygame.transform.scale(can_gift_1, (tile_size, tile_size))
	can_gift_2 = pygame.image.load('assets/can_gift_2.png')
	can_gift_2 = pygame.transform.scale(can_gift_2, (tile_size, tile_size))
	can_gift_3 = pygame.image.load('assets/can_gift_3.png')
	can_gift_3 = pygame.transform.scale(can_gift_3, (tile_size, tile_size))
	
	
	# Items		0			1				2				3			4				5				6			7				8				9				10			11				12			13			14			15
	items = (can_idle, can_clown_up_1, can_clown_up_2, can_clown_up_3, can_clown, can_explode_1, can_explode_2, can_explode_3, can_explode_4, can_confetti_1, can_confetti_2, can_confetti_3, can_gift_1, can_gift_2, can_gift_3, can_gift, can_gift_3, can_gift_2, can_gift_1)
	
	# Hammer frames
	hammer_frames = (hammer, hammer_2, hammer_2, hammer_1)
	hammer_state = 0
	
	# Confetti		0			1			2			3			4
	confetti = (confetti_5, confetti_4, confetti_3, confetti_2, confetti_1)
	
	# Create window
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption('Clown Hammer')
	
	start_game()
	
	# First blit
	screen.blit(background, (0, 0))
	pygame.display.flip()
	
	# Start!
	last_tick_time = pygame.time.get_ticks()
	
	while 1:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
			if game_state:
				if event.type == TICK_EVENT:
					if hammer_state != 0 and hammer_state < len(hammer_frames):
						hammer_state += 1
					if hammer_state == len(hammer_frames):
						hammer_state = 0
					for i in range(len(game_matrix)):
						if(game_matrix[i] == 0.0):
							continue
						if game_matrix[i] >= 12.0:
							game_matrix[i] += 1.0
						if game_matrix[i] >= 19.0:
							game_matrix[i] = 0.0
							continue
						if game_matrix[i] >= 9.0 and game_matrix[i] < 12.0:
							game_matrix[i] += 1.0
						if(game_matrix[i] == 12.0):
							game_matrix[i] = 0.0
							continue
						if(game_matrix[i] >= 5.0 and game_matrix[i] < 9.0):
							game_matrix[i] += 1.0
						if(game_matrix[i] == 9.0):
							game_matrix[i] = 0.0
							continue
						if(game_matrix[i] >= 4.0 and game_matrix[i] < 5.0):
							game_matrix[i] += 0.125
						if(game_matrix[i] == 5.0):
							game_matrix[i] = 9.0
							confetti_sound.play()
							lose()
						if(game_matrix[i] < 4.0):
							game_matrix[i] += 1.0
				if event.type == MOUSEBUTTONDOWN:
					if hammer_state == 0:
						hammer_state = 1
						tile = tile_for_pos(pygame.mouse.get_pos())
						tile = tile[0] + game_grid[0] * tile[1]
						if tile >= 0 and tile < len(game_matrix):
							if game_matrix[tile] > 1 and game_matrix[tile] < 12.0:
								game_matrix[tile] = 5
								explosion_sound.play()
								score += 1
								if spawn_delay <= 640:
									spawn_delay -= 6
								else:
									spawn_delay = math.floor(spawn_delay * spawn_accelaretor)
									spawn_accelaretor = spawn_accelaretor + (1 - spawn_accelaretor) * 0.3
							elif game_matrix[tile] > 11.0:
								game_matrix[tile] = 9.0
								confetti_sound.play()
								lose()
							else:
								hammer_sound.play()
						else:
							hammer_sound.play()
			elif waiter + 1000 <= pygame.time.get_ticks():
				if event.type == MOUSEBUTTONDOWN:
					start_game()
					if hammer_state == 0:
						hammer_state = 1
						explosion_sound.play()
		
		
		screen.blit(background, (0, 0))
		
		if game_state:
			# tick
			if pygame.time.get_ticks() - last_tick_time >= spawn_delay:
				# choose random position
				pos = random.randint(0,len(game_matrix) - 1)
				# choose clown / gift
				if game_matrix[pos] == 0.0:
					if random.random() < 0.8:
						game_matrix[pos] = 1.0
					else:
						game_matrix[pos] = 12.0
				last_tick_time = pygame.time.get_ticks()
		
		# Blit items
		pos = 0
		for item in game_matrix:
			if(item != 0.0):
				screen.blit(items[math.floor(item)], pos_of_tile(pos % game_grid[0], pos // game_grid[0]))
			pos += 1
		
		# Confetti
		if lifes != 5:
			screen.blit(confetti[lifes], (0, 0))
		
		# Game Over
		if lifes == 0:
			text = font.render('GAME OVER', False, (255, 255, 255))
			screen.blit(text, (size[1] // 5, size[0] // 2 - text.get_width() // 2))
			text = None
			text = font.render(str(score), False, (255, 255, 255))
			screen.blit(text, (size[1] // 5 * 3, size[0] // 2 - text.get_width() // 2))
		
		hammer_pos[0] = pygame.mouse.get_pos()[0] - math.floor(tile_size / 16 * 2.5)
		hammer_pos[1] = pygame.mouse.get_pos()[1] - math.floor(tile_size / 16 * 13.5)
		screen.blit(hammer_frames[hammer_state], hammer_pos)
		
		pygame.display.flip()


def pos_of_tile(x, y):
	global size, tile_size
	return ((size[0] - game_grid[0] * tile_size) // 4 + (size[0] - game_grid[0] * tile_size) // 2 // (game_grid[0] - 1) * x + tile_size * x, (size[1] - game_grid[1] * tile_size) // 4 + (size[1] - game_grid[1] * tile_size) // 2 // (game_grid[1] - 1) * y + tile_size * y)

def tile_for_pos(pos):
	global size, tile_size
	return ((pos[0] - (size[0] - game_grid[0] * tile_size) // 4) // ((size[0] - game_grid[0] * tile_size) // 2 // (game_grid[0] - 1) + tile_size), (pos[1] - (size[1] - game_grid[1] * tile_size) // 4) // ((size[1] - game_grid[1] * tile_size) // 2 // (game_grid[1] - 1) + tile_size))

def lose():
	global lifes, game_state, waiter
	lifes -= 1
	if lifes <= 0:
		game_state = 0
		waiter = pygame.time.get_ticks()
		lifes = 0

def c_pause():
	global WINDOWS
	if WINDOWS:
		os.system('pause')
	else:
		os.system('read -n1 -r -p "Press any key to continue..." key')

def start_game():
	global spawn_delay, score, game_state, background, table, lifes, game_grid, can_idle, game_matrix, spawn_accelaretor
	game_matrix = [0.0] * game_grid[0] * game_grid[1]
	spawn_delay = 3000
	spawn_accelaretor = 0.6
	score = 0
	lifes = 5
	game_state = 1
	background = table
	background.convert()
	for x in range(game_grid[0]):
		for y in range(game_grid[1]):
			background.blit(can_idle, (pos_of_tile(x, y)))

if __name__ == '__main__': main()