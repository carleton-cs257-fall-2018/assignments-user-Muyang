package ColorLand;

import javafx.fxml.FXML;
import javafx.scene.Group;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;

public class View extends Group {
    protected final static double CELL_WIDTH = 20.0;
    @FXML protected int rowCount;
    @FXML protected int columnCount;
    private Rectangle[][] cellViews;

    public View() {
    }

    /**
     * Creates the initial grid
     */
    private void initializeGrid() {
        if (this.rowCount > 0 && this.columnCount > 0) {
            this.cellViews = new Rectangle[this.rowCount][this.columnCount];
            for (int row = 0; row < this.rowCount; row++) {
                for (int column = 0; column < this.columnCount; column++) {
                    Rectangle rectangle = new Rectangle();
                    rectangle.setX((double)column * CELL_WIDTH);
                    rectangle.setY((double)row * CELL_WIDTH);
                    rectangle.setWidth(CELL_WIDTH);
                    rectangle.setHeight(CELL_WIDTH);
                    this.cellViews[row][column] = rectangle;
                    this.getChildren().add(rectangle);
                }
            }
        }
    }

    /**
     * Updates the look of the grid/percentages to reflect the model
     * @param model: the model
     */
    protected void refresh(Model model) {
        for (int row = 0; row < this.rowCount; row++) {
            for (int column = 0; column < this.columnCount; column++) {
                GameBoard.CellValue cellValue = model.getBoard().getCellValue(row, column);
                if (cellValue == GameBoard.CellValue.USER_HEAD) {
                    this.cellViews[row][column].setFill(Color.DARKRED);
                } else if (cellValue == GameBoard.CellValue.USER_TRAIL){
                    this.cellViews[row][column].setFill(Color.ORANGE);
                } else if (cellValue == GameBoard.CellValue.USER_TERR){
                    this.cellViews[row][column].setFill(Color.ORANGERED);
                } else if (cellValue == GameBoard.CellValue.EMPTY) {
                    this.cellViews[row][column].setFill(Color.DARKOLIVEGREEN);
                } else if (cellValue == GameBoard.CellValue.BOT_HEAD) {
                    this.cellViews[row][column].setFill(Color.BLUE);
                } else if (cellValue == GameBoard.CellValue.BOT_TRAIL) {
                    this.cellViews[row][column].setFill(Color.LIGHTBLUE);
                } else if (cellValue == GameBoard.CellValue.BOT_TERR){
                    this.cellViews[row][column].setFill(Color.LIGHTBLUE);
                } else {
                    this.cellViews[row][column].setFill(Color.BLACK);
                }
            }
        }
    }

    /**
     * Used for the FXML, don't delete
     * Returns the number of rows in the visual gameboard
     * @return this.rowCount: rows in the gameboard
     */
    public int getRowCount(){
        return this.rowCount;
    }
    /**
     * Used for the FXML, don't delete
     * Returns the number of columns in the visual gameboard
     * @return this.columnCount: columns in the gameboard
     */
    public int getColumnCount(){
        return this.columnCount;
    }
    /**
     * Used for the FXML, don't delete
     * Sets the number of rows in the visual gameboard
     * @param rowCount: number of rows desired
     */
    public void setRowCount(int rowCount){
        this.rowCount = rowCount;
        this.initializeGrid();
    }
    /**
     * Used for the FXML, don't delete
     * Sets the number of columns in the visual gameboard
     * @param columnCount: number of columns desired
     */
    public void setColumnCount(int columnCount){
        this.columnCount = columnCount;
        this.initializeGrid();
    }

}
