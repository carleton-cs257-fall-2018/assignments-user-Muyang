Johnny and Muyang

DESCRIPTION:
ColorLand
Player's goal is to cover the whole map with the color of your box. When your box move, it leaves a trail. The trail should go back to the player's territory to obtain the area enclosed by your trail. If other player touches your trail, you die. You can kill other player
by touching their trial. Once a player dies, it loses all of its area (become blank). One can steal territory from other players. When the player covers the whole map, the player wins.

MVC -- Players change the direction of movement using keyboard (keyEvent in CONTROLLER)
	that means the user take action in the view
	which modifies the positions/trails/territories in the MODEL
	then the view gets updated

MODEL contains a GameBoard board, a Box user, and a list of bots Box[] bots.
	The GameBoard consists of 2D array of cells, and the size of user's coverage of the map
	The Box contains the position, velocity, and lists of trailPositions and territory.
	
	The Model class contains the rules of movement for the boxes, and methods used to update
	the boxes and gameboard; also keeps track of the timer.

VIEW would be showing
	- the game board
	- each color box's position
	- each color's territory
	- each color box's trail
	a scoreboard showing
	- the percentage of the area that belong to each color
	- time played
	- rounds
Core Classes:
	Model
		-Box
		-GameBoard
	View
	Controller
	Main
	






