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


    public Model(int rowCount, int columnCount, int numBots){
        this.board = new GameBoard(rowCount, columnCount);
        this.user = new Box("user");
        this.bots = initializeBots(numBots);
    }


    public Box[] initializeBots(int numBots){
        Box[] bots = new Box[numBots];
        for (int i = 0; i < numBots; i++){
            bots[i] = new Box("bot");
        }
        return bots;
    }

    public void update(String button){
        updateGameBoard();
        updateUserBox(button);
        updateCPUBox();
        updatePercentage();
        updateTime();
    }



    /*
    * Update the cellvalues, botLandSize, userLandSize,
    * number of Bots, 
    * and check if Round is complete
    */
    public void updateGameBoard(){

    }

    /*
    * Update the headPosition, velocity(direction of movement)
    * list of trailPosition, list of territoryPosition
    * @param X-velocity: the horizontal speed
    * @param Y-velocity: the vertical speed
    */
    public void updateUserBox(String button){


    }

    public void updateCPUBox(){

    }

    /*
    * update and increment the time
    */
    public void updateTime(){

    }

    /*
    * update the percent area covered by each the user/bot boxes
    */
    public void updatePercentage(){

    }

    public boolean isRoundComplete(){
        return bots.length == 0 || board.getUserLandSize() == 100;
    }

}