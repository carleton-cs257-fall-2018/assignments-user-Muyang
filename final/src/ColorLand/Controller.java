package ColorLand;

import javafx.fxml.FXML;
import javafx.event.EventHandler;
import javafx.scene.control.*;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.application.Platform;
import javafx.scene.control.Label;
import java.util.*;


public class Controller implements EventHandler<KeyEvent> {
    final private double FRAMES_PER_SECOND = 15.0;

    private Model model;
    @FXML private View view;
    @FXML private Label startLabel;
    @FXML protected Label scoreLabel;
    @FXML private Label levelStatus;
    private String keyPressed = "NONE";
    private Timer timer;

    public Controller() {
    }


    /**
     * Creates a model linked to the controller and starts the timer
     * Pause the model at the beginning of each round
     */
    public void initialize() {
        this.model = new Model(view.rowCount,view.columnCount);
        update("NONE");
        startTimer();
        this.model.setPaused(true);
    }

    /**
     * Run the model based on time and keyEvent
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
     * Update the model by keyEvents
    */
    public void update(String movement) {
        updateScore();
        if(this.model.isGameOver()){
            setGameOverText();
        }else if(this.model.isPaused()){
            setGamePausedText();
        }else{
            setGamePlayText();
            updateModel(movement);
        }
        updateLevelStatus();
    }
    private void updateModel(String movement){
        model.update(keyPressed);
        keyPressed = model.getUser().stopAtWall(movement, view.columnCount, view.rowCount);
        view.refresh(model);
    }
    private void updateScore(){
        this.scoreLabel.setText("Territory size: " + model.getScore());
    }
    private void setGameOverText(){
        this.scoreLabel.setText("Your trail gets caught by a bot! You Lose!");
        this.startLabel.setText("Game Over. Hit G to start a new game.");
    }
    private void setGamePausedText(){
        this.startLabel.setText("Press P to Start/Pause");
    }
    private void setGamePlayText(){
        this.startLabel.setText("Press P to Start/Pause");
    }
    private void updateLevelStatus(){
        if (!model.isLevelComplete()){
            this.levelStatus.setText("Level " + model.getLevel() + " : Capture " + model.getLevelGoal() + " Grids");
        } else {
            this.levelStatus.setText("Level " + model.getLevel() + " Completed! Press L to start the next Level");
        }
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
        ArrayList<String> allowedMoves = model.checkAllowedMoves(model.getUser());

        if ((code == KeyCode.UP) && allowedMoves.contains("UP")) {
            this.keyPressed = "UP";
        } else if ((code == KeyCode.RIGHT) && allowedMoves.contains("RIGHT")) {
            this.keyPressed = "RIGHT";
        } else if ((code == KeyCode.LEFT) && allowedMoves.contains("LEFT")) {
            this.keyPressed = "LEFT";
        } else if ((code == KeyCode.DOWN) && allowedMoves.contains("DOWN")) {
            this.keyPressed = "DOWN";
        } else if (code == KeyCode.P){
            model.setPaused(!model.isPaused());
        } else if (code == KeyCode.G && model.isGameOver()){
            startNewGame();
        } else if (code == KeyCode.L && model.isLevelComplete()){
            startNewLevel();
        } else if (code == KeyCode.H){
            showHelpMessage();
        }
        keyEvent.consume();
    }
    private void startNewGame(){
        this.timer.cancel();
        this.model.startNewGame(view.rowCount, view.columnCount);
        this.timer = new Timer();
        startTimer();
        this.keyPressed = "STOP";
    }
    private void startNewLevel(){
        this.timer.cancel();
        this.model.startNewLevel(view.rowCount, view.columnCount);
        this.timer = new Timer();
        startTimer();
        this.keyPressed = "STOP";
    }
    private void showHelpMessage(){
        this.timer.cancel();
        Alert helpAlert = new Alert(Alert.AlertType.INFORMATION);
        helpAlert.setTitle("Color Land");
        helpAlert.setHeaderText("Instructions");
        helpAlert.setContentText("Turn your trail (orange) into territory (red) by returning to red." +
                " Avoid blue crocodiles which live in the blue lakes and eat your trail" +
                " The crocodiles also expand their lake." +
                " Capture the goal amount of the territory (shown" +
                " on the lower right corner).");
        helpAlert.showAndWait();
        this.timer = new Timer();
        startTimer();
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
