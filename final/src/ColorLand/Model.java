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
        this.user = new Box("user");
        this.bots = initializeBots(numBots);
    }

    /**
     * a helper method used to initialize the Bots
     * @param numBots number of bots
     * @return the initialized Box[] bots
     */
    public Box[] initializeBots(int numBots){
        Box[] bots = new Box[numBots];
        for (int i = 0; i < numBots; i++){
            bots[i] = new Box("bot");
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
        updateUserBox(button);
        updateCPUBox();
        updatePercentage();
        updateTime();
    }



    /**
    * Update the cellvalues, botLandSize, userLandSize,
    * number of Bots, 
    * and check if Round is complete
    */
    public void updateGameBoard(){

    }

    /**
     * Update the position, velocity, and trailPosition list and territoryPosition list
     * of the user box.
     * @param button the button pressed, passed from the controller
     */
    public void updateUserBox(String button){


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

}