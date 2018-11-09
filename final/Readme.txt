Johnny and Muyang's ColorLand

Player's goal is to cover the whole map with the color of your box. When your box move, it leaves a trail. The trail should go back to the player's territory to obtain the area enclosed by your trail. If other player touches your trail, you die. You can kill other player
by touching their trial. Once a player dies, it loses all of its area (become blank). One can steal territory from other players. When the player covers the whole map, the player wins.

MVC -- Players change the direction of movement using keyboard (keyEvent in CONTROLLER)
	that means the user take action in the view
	which modifies the positions/trails/territories in the MODEL
	then the view gets updated

MODEL contains 
	- the position of the color-box, 
	- the territory of each color, 
	- the trail of each color,
	- the percentage of the area that belong to each color.
	- the bots and their rules of movements
VIEW would be a gameboard showing
	- each color box's position
	- each color's territory
	- each color box's trail
	a scoreboard showing
	- the percentage of the area that belong to each color
	- time played
	- rounds

Core Classes (methods?) for Model
-	a Box class, storing its position, territory(list of cell[][]), trail, head)

-	public enum CellValue {EMPTY, BOT_TERRITORY, BOT_TRAIL, BOT_HEAD,
					PLAYER_TERRITORY, PLAYER_TRAIL, PLAYER_HEAD};
	
	Constructor()
	startNewGame()
	startNextLevel() -- more bots
	isLevelComplete() {
		return this.botCount == 0;
	}
	isGameOver()
	initializeLevel
	numberOfBotsForLevel
	getRowCount()
	getColumnCount()
	getPercentageFor(param)
	getCellValue()
	moveBoxBy()
		checkDirection  -- listen from View
		changeCellValue	
		botMovement()
-	idea about movement:
	initialize territory, trail, head-position

	VIEW/CONTROLLER_Listen make a movement (do nothing/change direction)
	MODEL moveBoxBy according to movement
		store the old head position
		change the head position

		old head position -> trail
		
		if the new position of the head is empty||someone's territory -> mark it as this box's head
		if the new position of the head is trail -> the box of the trail's color dies
							 -> mark it as this box's head
		if the new position of the head is my territory -> for each row:
									for( start point: territory||first trail, end point: last trail||territory, i++)
										change cell value to territory
	






