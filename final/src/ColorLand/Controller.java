package ColorLand;

import javafx.fxml.FXML;
import javafx.event.EventHandler;
import javafx.scene.control.Label;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;

public class Controller implements EventHandler<KeyEvent> {
    @FXML private Label scoreLabel;
    @FXML private Label messageLabel;
    @FXML private ColorLandView ColorLandView;
    private ColorLandModel ColorLandModel;

    public Controller() {
    }

    public void initialize() {
        this.ColorLandModel = new ColorLandModel(this.ColorLandView.getRowCount(), this.ColorLandView.getColumnCount());
        this.update();
    }

    public double getBoardWidth() {
        return ColorLandView.CELL_WIDTH * this.ColorLandView.getColumnCount();
    }

    public double getBoardHeight() {
        return ColorLandView.CELL_WIDTH * this.ColorLandView.getRowCount();
    }

    private void update() {
        this.ColorLandView.update(this.ColorLandModel);
        this.scoreLabel.setText(String.format("Score: %d", this.ColorLandModel.getScore()));
        if (this.ColorLandModel.isGameOver()) {
            this.messageLabel.setText("Game Over. Hit G to start a new game.");
        } else if (this.ColorLandModel.isLevelComplete()) {
            this.messageLabel.setText("Nice job! Hit L to start the next level.");
        } else {
            this.messageLabel.setText("Use the keys surrounding the S to run from the ColorLand.");
        }
    }

    @Override
    public void handle(KeyEvent keyEvent) {
        boolean keyRecognized = true;
        KeyCode code = keyEvent.getCode();

        String s = code.getChar();
        if (s.length() > 0) {
            char theCharacterWeWant = s.charAt(0);
        }

        if (code == KeyCode.LEFT || code == KeyCode.A) {
            this.ColorLandModel.moveRunnerBy(0, -1);
        } else if (code == KeyCode.RIGHT || code == KeyCode.D) {
            this.ColorLandModel.moveRunnerBy(0, 1);
        } else if (code == KeyCode.UP || code == KeyCode.W) {
            this.ColorLandModel.moveRunnerBy(-1, 0);
        } else if (code == KeyCode.DOWN || code == KeyCode.X) {
            this.ColorLandModel.moveRunnerBy(1, 0);
        } else if (code == KeyCode.Q) {
            this.ColorLandModel.moveRunnerBy(-1, -1);
        } else if (code == KeyCode.E) {
            this.ColorLandModel.moveRunnerBy(-1, 1);
        } else if (code == KeyCode.Z) {
            this.ColorLandModel.moveRunnerBy(1, -1);
        } else if (code == KeyCode.C) {
            this.ColorLandModel.moveRunnerBy(1, 1);
        } else if (code == KeyCode.S) {
            this.ColorLandModel.moveRunnerBy(0, 0);
        } else if (code == KeyCode.T) {
            this.ColorLandModel.teleportRunner();
        } else if (code == KeyCode.G) {
            if (this.ColorLandModel.isGameOver()) {
                this.ColorLandModel.startNewGame();
            }
        } else if (code == KeyCode.L) {
            if (this.ColorLandModel.isLevelComplete()) {
                this.ColorLandModel.startNextLevel();
            }
        } else {
            keyRecognized = false;
        }

        if (keyRecognized) {
            this.update();
            keyEvent.consume();
        }
    }
}
