package ColorLand;

import java.util.*;
import java.lang.*;

public class Model{
    public GameBoard board;
    private Box user;
    private Box[] bots;
    private Timer timer;
    private Float percentageUser;
    private Float percentageBot;
    private Boolean pause;

    /**
     * Constructor
     * instantiate a new model, which consists of a GameBoard board, a Box user, and
     * a list of CPU boxes Box[] bots.
     * @param rowCount the number of rows
     * @param columnCount the number of columns
     * @param numBots the number of bots
     */
    public Model(int rowCount, int columnCount, int numBots){
        this.board = new GameBoard(rowCount, columnCount);
        this.user = this.initializeUser(rowCount, columnCount);
        this.bots = this.initializeBots(numBots, rowCount, columnCount);
    }


    private Box initializeUser(int rowCount, int columnCount){
        Box user = new Box("user", rowCount, columnCount);
        return user;
    }

    /**
     * a helper method used to initialize the Bots
     * @param numBots number of bots
     * @return the initialized Box[] bots
     */
    public Box[] initializeBots(int numBots, int rowCount, int columnCount){
        Box[] bots = new Box[numBots];
        for (int i = 0; i < numBots; i++){
            bots[i] = new Box("bot", rowCount, columnCount);
            int columnPosition = bots[i].getHeadPosition().get("X-coordinate");
            int rowPosition = bots[i].getHeadPosition().get("Y-coordinate");
            this.board.updateCellValue(GameBoard.CellValue.BOT_HEAD, rowPosition, columnPosition);
        }
        return bots;
    }

    /**
     * Update the Model --
     * update the board
     * update the user box and CPU boxes
     * update the percent area that the user box and bot boxes covered
     * update the time
     * @param button the key pressed, passed from the controller
     */
    public void update(String button){
        updateGameBoard();
        this.checkCapture();
        updateUserBox(button);
        updateCPUBox();
        updatePercentage();
        updateTime();

    }


    public void checkCapture(){
        if(this.board.cells[this.user.getHeadY()][this.user.getHeadX()] == GameBoard.CellValue.USER_TERR){
            for(int x = 0; x < this.board.getBoardLength(); x++){
                for(int y = 0; y < this.board.getBoardHeight(); y++){
                    if(this.board.cells[y][x] == GameBoard.CellValue.USER_TRAIL){
                        this.capture(x,y);
                        this.user.removeTrailPosition(x,y);
                    }
                }
            }
        }
    }


    public void capture(int x, int y){
        this.board.updateCellValue(GameBoard.CellValue.USER_TERR, y, x);
    }

    /**
     * Update the cellvalues, botLandSize, userLandSize,
     * number of Bots,
     * and check if Round is complete
     */
    public void updateGameBoard(){
        ArrayList<HashMap<String, Integer>> userTrailPosition = this.user.getTrailPosition();
        ArrayList<HashMap<String, Integer>> userTerrPosition = this.user.getTerrPosition();
        for (HashMap<String, Integer> trailGrid : userTrailPosition){
            int trailRow = trailGrid.get("Y-coordinate");
            int trailColumn = trailGrid.get("X-coordinate");
            this.board.updateCellValue(GameBoard.CellValue.USER_TRAIL, trailRow, trailColumn);
        }
        userTerrPosition.forEach(terrGrid -> {
            int terrRow = terrGrid.get("Y-coordinate");
            int terrColumn = terrGrid.get("X-coordinate");
            this.board.updateCellValue(GameBoard.CellValue.USER_TERR, terrRow, terrColumn);
        });

    }

    /**
     * Update the position, velocity, and trailPosition list and territoryPosition list
     * of the user box.
     * @param button the button pressed, passed from the controller
     */
    public void updateUserBox(String button){
        this.user.updateVelocity(button);
        this.user.updatePosition();
        int columnPosition = user.getHeadPosition().get("X-coordinate");
        int rowPosition = user.getHeadPosition().get("Y-coordinate");
        this.board.updateCellValue(GameBoard.CellValue.USER_HEAD, rowPosition, columnPosition);



    }

    /**
     * Update the position, velocity, and trailPosition list and territoryPosition list
     * of the CPU boxes (bots).
     */
    public void updateCPUBox(){

    }

    /**
     * update and increment the time
     */
    public void updateTime(){

    }

    /**
     * update the percent area covered by each the user/bot boxes
     */
    public void updatePercentage(){

    }

    /**
     * Check if this round is complete
     * @return if there is no bot left or the size of user's territory is 100
     */
    public boolean isRoundComplete(){
        return bots.length == 0 || board.getUserLandSize() >= 100;
    }

    public Box getUser(){
        return this.user;
    }
}
