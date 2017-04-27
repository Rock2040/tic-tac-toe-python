boardSize = 3

matrix = [
	[(1, 1), (2, 1), (3, 1)],
	[(1, 2), (2, 2), (3, 2)],
	[(1, 3), (2, 3), (3, 3)]
]

filledPositions = {
	1 : [],
	2 : [],
	"all_positions" : []
}

def checkHorizontalRowComplete(lst):
	# Horizontal row completion check
	for row in matrix:
		rowComplete = True
		for point in row:
			if point in lst:
				continue
			else:
				rowComplete = False
				break
		else:
			return rowComplete
	else:
		return False

def checkVerticalRowComplete(lst):
	# Vertical row completion check
	for x in xrange(0, boardSize):
		rowComplete = True
		verticalRow = [row[x] for row in matrix]
		for point in verticalRow:
			if point in lst:
				continue
			else:
				rowComplete = False
				break
		else:
			return rowComplete
	else:
		return False

def checkDiagonalRowComplete(lst):
	# Diagonal row completion check
	diagonalRow = [];
	oppositeDiagonalRow = []
	bs = boardSize

	for x in range(0, boardSize):
		diagonalRow.append(matrix[x][x])

	for x in range(0, boardSize):
		oppositeDiagonalRow.append(matrix[x][bs - 1])
		bs -= 1

	rowComplete = True
	for point in diagonalRow:
		if point in lst:
			continue
		else:
			rowComplete = False
			break
	else:
		return rowComplete

	rowComplete = True
	for point in oppositeDiagonalRow:
		if point in lst:
			continue
		else:
			rowComplete = False
			break
	else:
		return rowComplete

def positionFilled(tup):
	return tup in filledPositions["all_positions"]

def positionExists(position):
	for row in matrix:
		if position in row:
			return True
	else:
		return False


def allPositionsFilled():
	return len(filledPositions["all_positions"]) == len([item for item in [row for row in matrix]])

def checkRowComplete(lst):
	if checkHorizontalRowComplete(lst) or checkVerticalRowComplete(lst) or checkDiagonalRowComplete(lst):
		return True
	else:
		return False


def start():
	inProgress = True
	print "Welcome to Tic-Tac-Toe!!", "\n", "-" * 10
	playerOne = { "name" : "", "symbol" : "X", "player_number" : 1 }
	playerTwo = { "name" : "", "symbol" : "O", "player_number" : 2 }
	playerOne["name"] = raw_input("Enter Player 1 Name: ").capitalize()
	playerTwo["name"] = raw_input("Enter Player 2 Name: ").capitalize()
	currentPlayer = playerOne

	def switchCurrentPlayer():
		if currentPlayer == playerOne:
			return playerTwo
		else:
			return playerOne

	def isStalemate():
		positionsInMatrix = [item for l in matrix for item in l]
		
		for p in positionsInMatrix:
			if p in filledPositions["all_positions"]:
				continue
			else:
				return False
		else:
			return True

	def drawBoard():
		board = ""
		emptyPosition = "*"
		delimiter = " "
		for row in matrix:
			x = 0
			for element in row:
				if element in filledPositions[playerOne["player_number"]]:
					board += playerOne["symbol"] + delimiter
				elif element in filledPositions[playerTwo["player_number"]]:
					board += playerTwo["symbol"] + delimiter
				else:
					board += emptyPosition + delimiter

				if x == boardSize - 1:
					board += "\n"

				x += 1
		else:
			print "Current Board:\n", ("-" * 10) + "\n", board

	drawBoard()

	def victory():
		print currentPlayer["name"], "got", boardSize, "in a row!", currentPlayer["name"], "wins!"
		return True

	def reset():
		global filledPositions
		filledPositions[1] = []
		filledPositions[2] = []
		filledPositions["all_positions"] = []
		print "Resetting..."
		start()

	while inProgress:
		user_input = raw_input("{cp} picks position: ".format(cp=currentPlayer["name"]))
		position = tuple([int(coord) for coord in user_input.split(",")])
		if positionFilled(position):
			print "Position", position, "is already filled."
			continue
		else:
			if positionExists(position):
				filledPositions[currentPlayer["player_number"]].append(position)
				filledPositions["all_positions"].append(position)
				if isStalemate():
					drawBoard()
					print "STALEMATE. NOBODY WINS."
					reset()
			else:
				print position, "is not a valid position"
				continue
			if checkRowComplete(filledPositions[currentPlayer["player_number"]]):
				drawBoard()
				victory()
				reset()
			else:
				drawBoard()
				print currentPlayer["name"], "filled position", position
				currentPlayer = switchCurrentPlayer()


	
start()