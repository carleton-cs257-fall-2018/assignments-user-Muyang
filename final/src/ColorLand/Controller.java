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
    final private double FRAMES_PER_SECOND = 15.0;
    private Model model;
    @FXML protected View view;
    private String keyPressed = "initial";
    private Timer timer;
    private int round;

    public Controller() {
    }


    /**
     * Creates a model linked to the controller and starts the timer
     */
    public void initialize() {
        this.model = new Model(view.rowCount,view.columnCount, 5);
        startTimer();
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
    public void update(String movement) {
        model.update(keyPressed);
        String checkedMovement = model.user.hitWall(movement, view.columnCount, view.rowCount);
        keyPressed = checkedMovement;
        view.refresh(model);
    }


    /**
     * Listen to key events
     * changes velocity (direction) if certain key is allowed and pressed
     * proceed the model if nothing happens in this time period
     * @param keyEvent: a pressed keyboard key
     */
    @Override
    public void handle(KeyEvent keyEvent) {
        KeyCode code = keyEvent.getCode();
        ArrayList<String> allowedMoves = this.model.checkAllowedMoves(this.model.user);

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
     * Used in the Main
     * Returns the board's width, in pixels
     * @return View.CELL_WIDTH * this.view.getColumnCount(): size of board width, in px
     */
    public double getBoardWidth() {
        return View.CELL_WIDTH * this.view.columnCount;
    }

    /**
     * Used in the Main
     * Returns the board's height, in pixels
     * @return View.CELL_WIDTH * this.view.getRowCount(): size of board height, in px
     */
    public double getBoardHeight() {
        return View.CELL_WIDTH * this.view.rowCount;
    }
}
