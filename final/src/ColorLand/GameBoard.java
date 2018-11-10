package ColorLand;

public class GameBoard{
    public enum CellValue{
        EMPTY,
        BOT_TERR, BOT_TRAIL, BOT_HEAD,
        USER_TERR, USER_TRAIL, USER_HEAD
    };

    public CellValue[][] cells;
    public int botCount;

    public int userLandSize;
    public int botLandSize;

    public GameBoard(int rowCount, int columnCount){
        assert rowCount > 0 && columnCount > 0;
        this.cells = new CellValue[rowCount][columnCount];
        this.userLandSize = 0;
        this.botLandSize = 0;
        this.botCount = 2;
    }

    public CellValue getCellValue(int row, int column){
        return this.cells[row][column];
    }

    public boolean isRoundComplete(){
        return botCount == 0 || userLandSize == 100;
    }
}