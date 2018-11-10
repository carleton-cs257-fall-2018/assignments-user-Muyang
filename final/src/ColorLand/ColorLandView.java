package ColorLand;


import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.scene.Group;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;

public class ColorLandView extends Group {
    public final static double CELL_WIDTH = 20.0;

    @FXML private int rowCount;
    @FXML private int columnCount;
    private Rectangle[][] cellViews;

    public ColorLandView() {
    }

    public int getRowCount(){
        return this.rowCount;
    }
    public int getColumnCount(){
        return this.columnCount;
    }
    public void setRowCount(int rowCount){
        this.rowCount = rowCount;
        this.initializeGrid();
    }
    public void setColumnCount(int columnCount){
        this.columnCount = columnCount;
        this.initializeGrid();
    }


    /* Creates the initial grid
    *
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


    /* Updates the look of the grid/percentages to reflect the model
    * @param model: the model
    */
    public void refresh(Model model) {
        //assert model.getRowCount() == this.rowCount && model.getColumnCount() == this.columnCount;
        for (int row = 0; row < this.rowCount; row++) {
            for (int column = 0; column < this.columnCount; column++) {
                GameBoard.CellValue cellValue = model.board.getCellValue(row, column);
                if (cellValue == GameBoard.CellValue.USER_HEAD) {
                    this.cellViews[row][column].setFill(Color.RED);
                } else if (cellValue == GameBoard.CellValue.EMPTY) {
                    this.cellViews[row][column].setFill(Color.BLACK);
                } else if (cellValue == GameBoard.CellValue.BOT_HEAD) {
                    this.cellViews[row][column].setFill(Color.GREEN);
                } else {
                    this.cellViews[row][column].setFill(Color.WHITE);
                }
            }
        }
    }
}
