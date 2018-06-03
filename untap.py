class Rover:
	#Rover initial variables
	def __init__(self,x0, y0, bearing, board_size):
		#set Initial x0
		self._x0 = x0
		#compas list will be used determine which side rover is facing 
		self.__compass = ["N", "E", "S", "W"]
		#set Initial y0
		self._y0 = y0
		#Store the bearing and the position of it in the list for truns
		self._bearing = [bearing, self.__compass.index(bearing)]
		#Initialize board size to determine wether we will move out of the board or not
		self._board_size = board_size
	"""move method will move the rover on the board based on the command"""
	def move(self,command):
		#If the command is left we will pull the elements from the left side of the list
		if command.lower() == "l":
			#Get the bearing of the rover after left turn
			self._bearing[0] = self.__compass[self._bearing[1]-1]
			#Store index of that bearing for further calculations
			self._bearing[1] = self.__compass.index(self._bearing[0])
		#If the rover turns right we will iterate to the right side of the list
		elif command.lower() == 'r':
			#Get the index of the list
			index_turn = self._bearing[1] + 1
			#Check to see if we are out of bound
			if index_turn >= len(self.__compass):
				#We are so we iterate from the start
				index_turn = 0
			#Get the bearing of the rover after right turn
			self._bearing[0] = self.__compass[index_turn]
			#Store the index of the bearing for further calculations
			self._bearing[1] = self.__compass.index(self._bearing[0])
		#If the comand is move than we move the rover based on the direction it faces
		elif command.lower() == 'm':
			#Call __advance method to move the rover
			self.__advance(self._bearing[0])
			#Check to see if the rover is moved out of the board by x axis
			if self._x0 > self._board_size[0] or self._x0 <= -1:
				#It moved out so we raise an Error
				raise ValueError("Your Mars Rover just died in a tragic accident")
			#Check t see if the rover moved out of the board by y axis
			elif self._y0 > self._board_size[1] or self._y0 <= -1:
				#It moved so we raise an error
				raise ValueError("Your Mars Rover just died a tragic accident")
	"""__advance method will calculate the rover position based on the bearing its facing"""
	def __advance(self, direction):
		#If the bearing is North
		if direction.lower() == 'n':
			#We move up by 1 on y axis
			self._y0 = self._y0 + 1 
		#Otherwise the bearing is South
		elif direction.lower() == 's':
			#We move down by 1 on y axis
			self._y0 = self._y0 - 1
		#Otherwise the bearing is E
		elif direction.lower() == 'e':
			#We move by one to the rright by x axis
			self._x0 = self._x0 + 1
		#Otherwise the bearing is W 
		elif direction.lower() == 'w':
			#We move left by one to the left by x axist
			self._x0 = self._x0 - 1

	def result(self):
		return "{} {} {}".format(
			self._x0, self._y0, self._bearing[0]
		)



if __name__ == '__main__':
	rover = Rover(3,3,"E", [5,5])
	# rover = Rover(1,2,"N")
	# command_list = ["L","M","L","M","L","M","L","M","M"]
	command_list = ["M","M","R","M","M","R","M","R","R","M",]
	
	for command in command_list:
		try:
			rover.move(command)
		except ValueError as val:
			print(val)
	print(rover.result())

