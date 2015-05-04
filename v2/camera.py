
class Camera:
	def __init__(screen, background, pos, zoomScale, world):
		self.screen = screen
		self.background = background
		self.world = world

		self.pos = pos
		self.zoomScale = zoomScale

	def draw(self):
		gameMap = self.world.gameMap	
		entList = self.world.entityList
		
		for tile in gameMap.data:
			pass # Draw each tile

		for entity in entList:
			pass # Draw each entity

		pygame.display.flip()
