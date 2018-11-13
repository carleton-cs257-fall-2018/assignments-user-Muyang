package ColorLand;

import javafx.fxml.FXML;
import javafx.event.EventHandler;
import javafx.scene.control.Label;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;

import javafx.application.Platform;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.AnchorPane;
import javafx.scene.shape.Rectangle;
import java.util.*;

import java.util.Timer;
import java.util.TimerTask;

public class Controller implements EventHandler<KeyEvent> {
    final private double FRAMES_PER_SECOND = 10.0;

    private Model model;
    private String keyPressed = "initial";
    private Timer timer;
    @FXML private View view;

    public Controller() {
    }


    /**
     * Creates a model linked to the controller and starts the timer
     */
    public void initialize() {
        this.model = new Model(this.view.getRowCount(),this.view.getColumnCount(), 2);
        this.startTimer();
    }


    /**
     * Runs methods that are timer-based(kind of a black box)
     */
    private void startTimer() {
        this.timer = new java.util.Timer();
        TimerTask timerTask = new TimerTask() {
            public void run() {
                Platform.runLater(new Runnable() {
                    public void run() {
                        update(keyPressed);
                    }
                });
            }
        };

        long frameTimeInMilliseconds = (long)(1000.0 / FRAMES_PER_SECOND);
        this.timer.schedule(timerTask, 0, frameTimeInMilliseconds);
    }


    /**
     * Runs methods that are key-event-based
    */
    public void update(String keyPressed) {
        this.model.update(keyPressed);
        this.hitWall();
        this.view.refresh(this.model);
    }


    /**
     * Listen to key events
     * changes velocity (direction) if certain key is pressed
     * proceed the model if nothing happens in this time period
     * @param keyEvent: a pressed keyboard key
     */
    @Override
    public void handle(KeyEvent keyEvent) {
        KeyCode code = keyEvent.getCode();
        ArrayList<String> allowedMoves = this.checkAllowedMoves();

        if ((code == KeyCode.UP) && allowedMoves.contains("UP"))  {
            this.keyPressed = "UP";
        } else if ((code == KeyCode.RIGHT) && allowedMoves.contains("RIGHT")) {
            this.keyPressed = "RIGHT";
        } else if ((code == KeyCode.LEFT) && allowedMoves.contains("LEFT")) {
            this.keyPressed = "LEFT";
        } else if ((code == KeyCode.DOWN) && allowedMoves.contains("DOWN")) {
            this.keyPressed = "DOWN";
        }
        keyEvent.consume();

    }

    /**
     * Checked the allowed movement according to the box's position
     * @return ArrayList of the allowed movement
     */
    private ArrayList<String> checkAllowedMoves(){
        int XCoordinate = this.getCoordinate()[0];
        int YCoordinate = this.getCoordinate()[1];
        ArrayList<String> allowedMoves = new ArrayList<>();
        if(XCoordinate < this.view.getColumnCount()-1){
            allowedMoves.add("RIGHT");
        }
        if(XCoordinate > 0){
            allowedMoves.add("LEFT");
        }
        if(YCoordinate < this.view.getRowCount() - 1){
            allowedMoves.add("DOWN");
        }
        if(YCoordinate > 0){
            allowedMoves.add("UP");
        }
        return allowedMoves;
    }

    /**
     * Stop the box's movement when its at the edge of the game board
     */
    private void hitWall(){
        int XCoordinate = this.getCoordinate()[0];
        int YCoordinate = this.getCoordinate()[1];
        if(! (XCoordinate < this.view.getColumnCount()-1) || !(XCoordinate > 0)){
            this.keyPressed = "STOP-X";
        }
        if (! (YCoordinate < this.view.getRowCount()-1) || !(YCoordinate > 0)){
            if (this.keyPressed.equals("STOP-X")){
                this.keyPressed = "STOP";
            }
            else {
                this.keyPressed = "STOP-Y";
            }
        }
    }

    /**
     * get the X and Y coordinate of the userBox
     * @return int[] int array of user's position. int[1]=X-coordinate, int[2]=Y-coordinate
     */
    private int[] getCoordinate(){
        int[] XY = new int[2];
        XY[0] = this.model.getUser().getHeadPosition().get("X-coordinate");
        XY[1] = this.model.getUser().getHeadPosition().get("Y-coordinate");
        return XY;
    }

    /**
     * Returns the board's width, in pixels
     * @return View.CELL_WIDTH * this.view.getColumnCount(): size of board width, in px
     */
    public double getBoardWidth() {
        return View.CELL_WIDTH * this.view.getColumnCount();
    }

    /**
     * Returns the board's height, in pixels
     * @return View.CELL_WIDTH * this.view.getRowCount(): size of board height, in px
     */
    public double getBoardHeight() {
        return View.CELL_WIDTH * this.view.getRowCount();
    }
}
