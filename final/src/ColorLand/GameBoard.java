package ColorLand;

public class GameBoard{
    public enum CellValue{
        EMPTY,
        BOT_TERR, BOT_TRAIL, BOT_HEAD,
        USER_TERR, USER_TRAIL, USER_HEAD
    };

    public CellValue[][] cells;

    public int userLandSize;
    public int botLandSize;

    public GameBoard(int rowCount, int columnCount){
        assert rowCount > 0 && columnCount > 0;
        this.cells = createEmptyBoard(rowCount, columnCount);
        this.userLandSize = 0;
        this.botLandSize = 0;
    }

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

    public int getUserLandSize(){
        return this.userLandSize;
    }
}