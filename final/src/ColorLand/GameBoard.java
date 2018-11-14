package ColorLand;

public class GameBoard{
    public enum CellValue{
        EMPTY,
        BOT_TERR, BOT_TRAIL, BOT_HEAD,
        USER_TERR, USER_TRAIL, USER_HEAD
    }
    protected CellValue[][] cells;
//    protected int userLandSize;
//    protected int botLandSize;
    protected int boardLength;
    protected int boardHeight;

    /**
     * Constructor, instantiate an empty game board
     * initialized the value of userLandSize and botLandSize to be 0
     * @param rowCount the number of rows of the game board
     * @param columnCount the number of column of the game board
     */
    public GameBoard(int rowCount, int columnCount){
        assert rowCount > 0 && columnCount > 0;
        this.cells = createEmptyBoard(rowCount, columnCount);
//        this.userLandSize = 0;
//        this.botLandSize = 0;
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


    public CellValue getCellValue(int row, int column){
        return this.cells[row][column];
    }

    public void updateCellValue(CellValue cellvalue, int row, int column) {
        this.cells[row][column] = cellvalue;

    }
//    /**
//     * get the value of the user's land size
//     * @return the size of the user's land size
//     */
//    public int getUserLandSize(){
//        return this.userLandSize;
//    }

//    public int getBoardLength() {return this.boardLength;}
//
//    public int getBoardHeight() {return this.boardHeight;}
}

