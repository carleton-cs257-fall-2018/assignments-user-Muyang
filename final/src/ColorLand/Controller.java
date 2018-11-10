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
    @FXML private ColorLandView view;

    public Controller() {

    }
    public void initialize() {
        this.model = new Model(this.view.getRowCount(),this.view.getColumnCount(), 2);
        //this.update();
        this.startTimer();
    }

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



    /*
    *   Update the model, based on events
    */
    public void update(String keyPressed) {
        this.model.update(keyPressed);
        this.view.refresh(this.model);
    }


    /*
    * Listen to key events
    * changes velocity (direction) if certain key is pressed
    * proceed the model if nothing happens in this time period
    */
    @Override
    public void handle(KeyEvent keyEvent) {
        //boolean keyRecognized = true;
        KeyCode code = keyEvent.getCode();

        String s = code.getChar();
        if (s.length() > 0) {
            char theCharacterWeWant = s.charAt(0);
        }

        if (code == KeyCode.LEFT || code == KeyCode.A) {
            this.keyPressed = "LEFT";
        } else if (code == KeyCode.RIGHT || code == KeyCode.D) {
            this.keyPressed = "RIGHT";
        } else if (code == KeyCode.UP || code == KeyCode.W) {
            this.keyPressed = "UP";
        } else if (code == KeyCode.DOWN || code == KeyCode.S) {
            this.keyPressed = "DOWN";
        // } else if (code == KeyCode.G) {
        //     if (this.model.isGameOver()) {
        //         this.model.startNewGame();
        //     }
        // } else if (code == KeyCode.L) {
        //     if (this.model.isLevelComplete()) {
        //         this.model.startNextLevel();
        //     }
        } else {
            //keyRecognized = false;
            keyPressed = "N/A";
        }        
        
        keyEvent.consume();

    }



/*    
    @FXML private Label scoreLabel;
    @FXML private Label messageLabel;
    @FXML private ColorLandView ColorLandView;
    private ColorLandModel ColorLandModel;
*/
    

//These lines might also be included in View
/*
 *   public double getBoardWidth() {
 *       return ColorLandView.CELL_WIDTH * this.ColorLandView.getColumnCount();
 *   }
 *
 *   public double getBoardHeight() {
 *       return ColorLandView.CELL_WIDTH * this.ColorLandView.getRowCount();
 *   }
*/
}
