package ColorLand;


import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.scene.Group;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;

public class View extends Group {
    public final static double CELL_WIDTH = 20.0;
    @FXML private int rowCount;
    @FXML private int columnCount;
    private Rectangle[][] cellViews;

    public View() {
    }


    /**
     * Returns the number of rows in the visual gameboard
     * @return this.rowCount: rows in the gameboard
     */
    public int getRowCount(){
        return this.rowCount;
    }


    /**
     * Returns the number of columns in the visual gameboard
     * @return this.columnCount: columns in the gameboard
     */
    public int getColumnCount(){
        return this.columnCount;
    }


    /**
     * Sets the number of rows in the visual gameboard
     * @param rowCount: number of rows desired
     */
    public void setRowCount(int rowCount){
        this.rowCount = rowCount;
        this.initializeGrid();
    }


    /**
     * Sets the number of columns in the visual gameboard
     * @param columnCount: number of columns desired
     */
    public void setColumnCount(int columnCount){
        this.columnCount = columnCount;
        this.initializeGrid();
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
    public void refresh(Model model) {
        for (int row = 0; row < this.rowCount; row++) {
            for (int column = 0; column < this.columnCount; column++) {
                GameBoard.CellValue cellValue = model.board.getCellValue(row, column);
                if (cellValue == GameBoard.CellValue.USER_HEAD) {
                    this.cellViews[row][column].setFill(Color.RED);
                } else if (cellValue == GameBoard.CellValue.USER_TRAIL){
                    this.cellViews[row][column].setFill(Color.ORANGE);
                } else if (cellValue == GameBoard.CellValue.USER_TERR){
                    this.cellViews[row][column].setFill(Color.PINK);
                } else if (cellValue == GameBoard.CellValue.EMPTY) {
                    this.cellViews[row][column].setFill(Color.WHITE);
                } else if (cellValue == GameBoard.CellValue.BOT_HEAD) {
                    this.cellViews[row][column].setFill(Color.BLUE);
                } else if (cellValue == GameBoard.CellValue.BOT_TRAIL) {
                    this.cellViews[row][column].setFill(Color.ALICEBLUE);
                } else if (cellValue == GameBoard.CellValue.BOT_TERR){
                    this.cellViews[row][column].setFill(Color.LIGHTBLUE);
                } else {
                    this.cellViews[row][column].setFill(Color.BLACK);
                }
            }
        }
    }
}
