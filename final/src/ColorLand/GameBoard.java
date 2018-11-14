package ColorLand;

public class GameBoard{

    public enum CellValue{
        EMPTY,
        BOT_TERR, BOT_TRAIL, BOT_HEAD,
        USER_TERR, USER_TRAIL, USER_HEAD
    }

    public CellValue[][] cells;

    public int userLandSize;
    public int botLandSize;
    private int boardLength;
    private int boardHeight;

    /**
     * Constructor, instantiate an empty game board
     * initialized the value of userLandSize and botLandSize to be 0
     * @param rowCount the number of rows of the game board
     * @param columnCount the number of column of the game board
     */
    public GameBoard(int rowCount, int columnCount){
        assert rowCount > 0 && columnCount > 0;
        this.cells = createEmptyBoard(rowCount, columnCount);
        this.userLandSize = 0;
        this.botLandSize = 0;
        this.boardLength = columnCount;
        this.boardHeight = rowCount;
    }

    /**
     * a helper method called in the constructor
     * create a gameboard and set all cell values to be EMPTY
     * @param rowCount the number of rows of the game board
     * @param columnCount the number of columns of the game board
     * @return the created board/cells
     */
    public CellValue[][] createEmptyBoard(int rowCount, int columnCount){
        CellValue[][] returnCells = new CellValue[rowCount][columnCount];
        for (int row = 0; row < rowCount; row++){
            for (int column = 0; column < columnCount; column++){
                returnCells[row][column] = CellValue.EMPTY;
            }
        }
        return returnCells;
    }

    /**
     * get the value of a cell on a specific position
     * @param row the position of the row
     * @param column the position of the column
     * @return the value of the cell
     */
    public CellValue getCellValue(int row, int column){
        return this.cells[row][column];
    }

    /**
     * get the value of the user's land size
     * @return the size of the user's land size
     */
    public int getUserLandSize(){
        return this.userLandSize;
    }

    public void updateCellValue(CellValue cellvalue, int rowPosition, int columnPosition) {
        this.cells[rowPosition][columnPosition] = cellvalue;

    }


    public int getBoardLength() {return this.boardLength;}

    public int getBoardHeight() {return this.boardHeight;}
}

