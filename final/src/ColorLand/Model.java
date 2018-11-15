package ColorLand;

import java.util.*;
import java.lang.*;

public class Model{
    public GameBoard board;
    protected Box user;
    private ArrayList<Box> bots;
    private Timer timer;
    private Float percentageUser;
    private Float percentageBot;
    private Boolean pause;
    private boolean gameOver;
    private int score;
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

    protected void startNewGame(int rowCount, int columnCount){
        this.gameOver = false;
        this.board = new GameBoard(rowCount, columnCount);
        this.user = this.initializeUser(rowCount, columnCount);
        this.bots = this.initializeBots(this.level*4, rowCount, columnCount);
        this.score = user.getTerrPosition().size();
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
    public ArrayList<Box> initializeBots(int numBots, int rowCount, int columnCount){
        ArrayList<Box> bots = new ArrayList<>();
        for (int i = 0; i < numBots; i++){
            bots.add(new Box("bot", rowCount, columnCount));
        }
        return bots;
    }


    public boolean isGameOver(){
        return this.gameOver;
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
    protected boolean inRange(Box cpuBox){
        boolean inRange = false;
        if (user.getHeadX() == cpuBox.getHeadX()-1 ||
                user.getHeadX() == cpuBox.getHeadX() ||
                user.getHeadX() == cpuBox.getHeadX()+1){
            if (user.getHeadY() == cpuBox.getHeadY()-1 ||
                    user.getHeadY() == cpuBox.getHeadY() ||
                    user.getHeadY() == cpuBox.getHeadY()+1){
                inRange = true;
            }
        }
        return inRange;
    }


    protected void killed(Box box){
        ArrayList<HashMap<String, Integer>> toBeEmpty = new ArrayList<>();
        toBeEmpty.addAll(box.getTrailPosition());
        toBeEmpty.addAll(box.getTerrPosition());
        for (HashMap<String, Integer> Grid : toBeEmpty) {
            int trailRow = Grid.get("Y-coordinate");
            int trailColumn = Grid.get("X-coordinate");
            this.board.updateCellValue(GameBoard.CellValue.USER_TERR, trailRow, trailColumn);
        }
    }

    public void checkCapture(){
        if(this.board.cells[this.user.getHeadY()][this.user.getHeadX()] == GameBoard.CellValue.USER_TERR){
            for(int x = 0; x < this.board.boardLength; x++){
                for(int y = 0; y < this.board.boardHeight; y++){
                    if(this.board.cells[y][x] == GameBoard.CellValue.USER_TRAIL){
                        this.board.updateCellValue(GameBoard.CellValue.USER_TERR, y,x);
                        this.user.removeTrailPosition(x,y);
                    }
                }
            }
        }
    }


//    public void capture(int x, int y){
//        ArrayList<HashMap<String, Integer>> gainedTerritory = new ArrayList<>();
//        this.board.updateCellValue(GameBoard.CellValue.USER_TERR, y, x);
//        x++;
//        y++;
//        if(x > this.board.getBoardLength()-1){ x = this.board.getBoardLength()-1;}
//        if(y > this.board.getBoardHeight()-1){ y = this.board.getBoardHeight()-1;}
//        while (this.board.cells[y][x] == GameBoard.CellValue.EMPTY){
//            HashMap<String, Integer> newTerr = new HashMap<>();
//            newTerr.put("X-coordinate", x);
//            newTerr.put("Y-coordinate", y);
//            gainedTerritory.add(newTerr);
//            this.board.updateCellValue(GameBoard.CellValue.USER_TERR, y, x);
//            x++;
//            if(x > this.board.getBoardLength()-1){ x = this.board.getBoardLength()-1;}
//        }
//        if(this.board.cells[y][x] == GameBoard.CellValue.USER_TRAIL || this.board.cells[y][x] == GameBoard.CellValue.USER_TERR){
//            absorbTerritory(gainedTerritory);
//            gainedTerritory = new ArrayList<>();
//        }
//        while (this.board.cells[y][x] == GameBoard.CellValue.EMPTY){
//            HashMap<String, Integer> newTerr = new HashMap<>();
//            newTerr.put("X-coordinate", x);
//            newTerr.put("Y-coordinate", y);
//            gainedTerritory.add(newTerr);
//            this.board.updateCellValue(GameBoard.CellValue.USER_TERR, y, x);
//            y++;
//            if(y > this.board.getBoardHeight()-1){ y = this.board.getBoardHeight()-1;}
//        }
//        if(this.board.cells[y][x] == GameBoard.CellValue.USER_TRAIL || this.board.cells[y][x] == GameBoard.CellValue.USER_TERR){
//            absorbTerritory(gainedTerritory);
//            gainedTerritory = new ArrayList<>();
//        }
//    }
//
//    public void absorbTerritory(ArrayList<HashMap<String, Integer>> gainedTerritory){
//        System.out.println(gainedTerritory);
//        for (HashMap<String, Integer> trailGrid : gainedTerritory){
//            int trailRow = trailGrid.get("Y-coordinate");
//            int trailColumn = trailGrid.get("X-coordinate");
//            this.board.updateCellValue(GameBoard.CellValue.USER_TERR, trailRow, trailColumn);
//            this.user.get
//        }
//
//    }

    /**
     * Update the cellvalues, botLandSize, userLandSize,
     * number of Bots,
     * and check if Round is complete
     */
    public void updateGameBoard(){



        for (Box bot : this.bots){
            this.colorTrail(bot);
            this.colorTerr(bot);
        }
        this.colorTrail(this.user);
        this.colorTerr(this.user);

        for (Box bot: this.bots){
            this.colorHead(bot);
        }
        checkCapture();
        this.colorHead(this.user);

    }

    protected void colorTrail(Box box){
        ArrayList<HashMap<String, Integer>> trailPositions = box.getTrailPosition();
        GameBoard.CellValue cellValue;
        if (box.type.equals("user")) {
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
    protected void colorTerr(Box box){
        ArrayList<HashMap<String, Integer>> terrPositions = box.getTerrPosition();
        GameBoard.CellValue cellValue;
        if (box.type.equals("user")){
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
    protected void colorHead(Box box){
        GameBoard.CellValue cellValue;
        if (box.type.equals("user")){
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
    public void updateUserBox(String button){
        this.user.updateVelocity(button);
        this.user.updatePosition();
    }

    /**
     * Update the position, velocity, and trailPosition list and territoryPosition list
     * of the CPU boxes (bots).
     */
    public void updateCPUBox(){
        for (Box cpu : bots){
            ArrayList<String> button = checkAllowedMoves(cpu);
            Random rand = new Random();
            cpu.updateVelocity(button.get(rand.nextInt(button.size())));
            cpu.updatePosition();
        }

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
//    public boolean isRoundComplete(){
//        return bots.length() == 0 || board.getUserLandSize() >= 100;
//    }

//    public Box getUser(){
//        return this.user;
//    }



    /**
     * Checked the allowed movement according to the box's position
     * @return ArrayList of the allowed movement
     */
    public ArrayList<String> checkAllowedMoves(Box box){
        int XCoordinate = box.getHeadX();
        int YCoordinate = box.getHeadY();
        ArrayList<String> allowedMoves = new ArrayList<>();
        if(XCoordinate < this.board.boardLength - 1){
            allowedMoves.add("RIGHT");
        }
        if(XCoordinate > 0){
            allowedMoves.add("LEFT");
        }
        if(YCoordinate < this.board.boardHeight - 1){
            allowedMoves.add("DOWN");
        }
        if(YCoordinate > 0){
            allowedMoves.add("UP");
        }
        return allowedMoves;
    }

    public boolean userKilled(){
        for (Box bot : bots){
            int X = bot.getHeadX();
            int Y = bot.getHeadY();
            if (this.board.getCellValue(Y,X) == GameBoard.CellValue.USER_TRAIL){
                gameOver = true;
            }
        }
        return gameOver;
    }
}




