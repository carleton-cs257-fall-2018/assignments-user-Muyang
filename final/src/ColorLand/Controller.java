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

import java.util.Timer;
import java.util.TimerTask;

public class Controller implements EventHandler<KeyEvent> {
    final private double FRAMES_PER_SECOND = 40.0;
    private Model model;
    private String keyPressed;
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

        if (code == KeyCode.LEFT || code == KeyCode.A) {
            this.keyPressed = "LEFT";
        } else if (code == KeyCode.RIGHT || code == KeyCode.D) {
            this.keyPressed = "RIGHT";
        } else if (code == KeyCode.UP || code == KeyCode.W) {
            this.keyPressed = "UP";
        } else if (code == KeyCode.DOWN || code == KeyCode.S) {
            this.keyPressed = "DOWN";
        }
        
        keyEvent.consume();

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
