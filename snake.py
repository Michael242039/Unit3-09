from scene import *

class GameScene(Scene):
	def setup(self):
		self.size_of_screen_x = self.size.x
		self.size_of_screen_y = self.size.y
		self.screen_center_x = self.size_of_screen_x/2
		self.screen_center_y = self.size_of_screen_y/2
		
		self.square_size = 32
		
		self.snake = []
		self.snake.append(self.add_square(self.screen_center_x, self.screen_center_y, self.square_size))
		
	def update(self):
			self.move_snake()
	
	def add_square(self, x, y, size):
		#Creates sqaure
		square_path = ui.Path().rect(0, 0, size, size)
		square_path.fill()
		square_path.line_width = 4
		square_path.close()
		self.square = ShapeNode(square_path, fill_color='white', size = (40, 40), position = (x, y), stroke_color = 'black')
		self.add_parent(self.snake[0])
		
	def move_snake(self):
		move_left = Action.move_by(-10, 0)
		for i in range(0, int(len(self.snake))):
			self.snake[i].run_action(move_left)
		#self.snake.run_action(move_left)
			
		
run(GameScene(), show_fps = True)
