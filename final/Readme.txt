Johnny and Muyang

DESCRIPTION:
ColorLand
Turn your trail (orange) into territory (red) by returning to red grids.
Avoid blue crocodiles which live in the blue lakes and eat your trail.
The crocodiles also expand their lake.
Capture the goal amount of the territory (shown on the lower right corner).

MVC -- Players change the direction of movement using keyboard (keyEvent in CONTROLLER)
	that means the user take action in the view
	which modifies the positions/trails/territories in the MODEL
	then the view gets updated

MODEL contains a GameBoard board, a Box user, and a list of bots Box[] bots.
	The GameBoard consists of 2D array of cells, and the size of user's coverage of the map
	The Box contains the position, velocity, and lists of trailPositions and territory.
	
	The Model class contains the rules of movement for the boxes, and methods used to update
	the boxes and gameboard

VIEW would be showing
	- the game board
	- each color box's position
	- each color's territory
	- each color box's trail
	a scoreboard showing
	- the percentage of the area that belong to the user
	- levels
Core Classes:
	Model
		-Box
		-GameBoard
	View
	Controller
	Main
	






