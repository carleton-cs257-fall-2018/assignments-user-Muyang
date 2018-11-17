package ColorLand;

import java.util.*;
import java.lang.*;

public class Model{
    private GameBoard board;
    private Box user;
    private ArrayList<Box> bots;
    private boolean paused;
    private boolean gameOver;
    private int level;

    /**
     * Constructor
     * instantiate a new model, which consists of a GameBoard board, a Box user, and
     * a list of CPU boxes Box[] bots.
     * @param rowCount the number of rows
     * @param columnCount the number of columns
     */
    public Model(int rowCount, int columnCount){
        this.level = 1;
        startNewGame(rowCount, columnCount);
    }

    public boolean isGameOver(){
        return this.gameOver;
    }
    public boolean isLevelComplete(){
        return user.getTerrPosition().size() >= Math.min(this.level * 100, 1000);
    }

    public void startNewGame(int rowCount, int columnCount){
        this.gameOver = false;
        this.paused = false;
        this.board = new GameBoard(rowCount, columnCount);
        this.user = this.initializeUser(rowCount, columnCount);
        this.bots = this.initializeBots(this.level+2, rowCount, columnCount);
    }
    public int getScore(){
        return user.getTerrPosition().size();
    }

    public void startNewLevel(int rowCount, int columnCount){
        this.level += 1;
        startNewGame(rowCount, columnCount);
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
    private ArrayList<Box> initializeBots(int numBots, int rowCount, int columnCount){
        ArrayList<Box> bots = new ArrayList<>();
        for (int i = 0; i < numBots; i++){
            bots.add(new Box("bot", rowCount, columnCount));
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
        checkUserKilled();
        updateGameBoard();
        updateUserBox(button);
        updateCPUBox();
    }
    /**
     * Update the cell values
     * to visualize the model
     */
    public void updateGameBoard(){
//        for (Box bot : this.bots){
//            this.colorTrail(bot);
//            this.colorTerr(bot);
//        }
        this.colorTrail(this.user);
        this.colorTerr(this.user);

        for (Box bot: this.bots){
            this.colorHead(bot);
        }
        checkCapture();
        this.colorHead(this.user);

    }
    /**
     * Loop through the game board
     * Dump USER_TRIAL to USER_TERR
     */
    private void checkCapture(){
        if(this.board.getCellValue(user.getHeadY(), user.getHeadX()) == GameBoard.CellValue.USER_TERR){
            for(int col = 0; col < this.board.getBoardLength(); col++){
                for(int row = 0; row < this.board.getBoardHeight(); row++){
                    if(this.board.getCellValue(row, col) == GameBoard.CellValue.USER_TRAIL){
                        this.user.removeTrailPosition(row,col);
                    }
                }
            }
        }
    }
    private void colorTrail(Box box){
        ArrayList<HashMap<String, Integer>> trailPositions = box.getTrailPosition();
        GameBoard.CellValue cellValue;
        if (box.getType().equals("user")) {
            cellValue = GameBoard.CellValue.USER_TRAIL;
        }
        else{
            cellValue = GameBoard.CellValue.BOT_TRAIL;
        }
        for (HashMap<String, Integer> trailGrid : trailPositions) {
            int trailRow = trailGrid.get("Y-coordinate");
            int trailColumn = trailGrid.get("X-coordinate");
            this.board.updateCellValue(cellValue, trailRow, trailColumn);
        }
    }
    private void colorTerr(Box box){
        ArrayList<HashMap<String, Integer>> terrPositions = box.getTerrPosition();
        GameBoard.CellValue cellValue;
        if (box.getType().equals("user")){
            cellValue = GameBoard.CellValue.USER_TERR;
        }
        else {
            cellValue = GameBoard.CellValue.BOT_TERR;
        }
        for (HashMap<String, Integer> terrGrid : terrPositions){
            int terrRow = terrGrid.get("Y-coordinate");
            int terrColumn = terrGrid.get("X-coordinate");
            this.board.updateCellValue(cellValue, terrRow, terrColumn);

        }
    }
    private void colorHead(Box box){
        GameBoard.CellValue cellValue;
        if (box.getType().equals("user")){
            cellValue = GameBoard.CellValue.USER_HEAD;
        }
        else{
            cellValue = GameBoard.CellValue.BOT_HEAD;
        }
        int columnPosition = box.getHeadX();
        int rowPosition = box.getHeadY();
        this.board.updateCellValue(cellValue, rowPosition, columnPosition);
    }

    /**
     * Update the position, velocity, and trailPosition list and territoryPosition list
     * of the user box.
     * @param button the button pressed, passed from the controller
     */
    private void updateUserBox(String button){
        this.user.updateVelocity(button);
        this.user.updatePosition();
    }

    /**
     * Update the position and velocity of the CPU boxes (bots).
     */
    private void updateCPUBox(){
        for (Box cpu : bots){
            ArrayList<String> button = checkAllowedMoves(cpu);
            Random rand = new Random();
            cpu.updateVelocity(button.get(rand.nextInt(button.size())));
            cpu.updatePosition();
        }

    }
    /**
     * Checked the allowed movement according to the box's position
     * @return ArrayList of the allowed movement
     */
    public ArrayList<String> checkAllowedMoves(Box box){
        int XCoordinate = box.getHeadX();
        int YCoordinate = box.getHeadY();
        ArrayList<String> allowedMoves = new ArrayList<>();
        if(XCoordinate < this.board.getBoardLength() - 1){
            allowedMoves.add("RIGHT");
        }
        if(XCoordinate > 0){
            allowedMoves.add("LEFT");
        }
        if(YCoordinate < this.board.getBoardHeight() - 1){
            allowedMoves.add("DOWN");
        }
        if(YCoordinate > 0){
            allowedMoves.add("UP");
        }
        return allowedMoves;
    }

    /**
     * If the head of any bot runs onto user's trail
     * the user is dead
     */
    public void checkUserKilled(){
        for (Box bot : bots){
            int columnPosition = bot.getHeadX();
            int rowPosition = bot.getHeadY();
            if (this.board.getCellValue(rowPosition,columnPosition) == GameBoard.CellValue.USER_TRAIL){
                gameOver = true;
            }
        }
    }

    public Box getUser(){
        return this.user;
    }
    public GameBoard getBoard(){
        return this.board;
    }
    public boolean isPaused(){
        return this.paused;
    }
    public void setPaused(boolean value){
        this.paused = value;
    }
    public int getLevel(){
        return this.level;
    }
    public int getLevelGoal(){
        return Math.min(this.level * 100,1000);
    }
}




