from untap import Rover


def test_sample_1():
	rover = Rover(3,3,"E", [5,5])
	command_list = ["M","M","R","M","M","R","M","R","R","M",]
	for command in command_list:
		try:
			rover.move(command)
		except ValueError as val:
			print(val)
	assert rover.result() == "5 1 E"

def test_sample_2():
	rover = Rover(1,2,"N", [5,5])
	command_list = ["L","M","L","M","L","M","L","M","M"]
	for command in command_list:
		try:
			rover.move(command)
		except ValueError as val:
			print(val)
	assert rover.result() == "1 3 N"

def test_sample_3():
	rover = Rover(3,3,"E", [5,5])
	command_list = ["M","M","R","M","M","R","M","R","R","M","M"]
	for command in command_list:
		try:
			rover.move(command)
		except ValueError as val:
			assert True


