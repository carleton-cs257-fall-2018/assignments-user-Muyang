package ColorLand;

import java.util.*;

public class Box{
    private HashMap<String, Integer> headPosition;
    private HashMap<String, Integer> velocity;
    private String type;
    private ArrayList<HashMap<String, Integer>> trailPosition;
    private ArrayList<HashMap<String, Integer>> territoryPosition;


    /**
     * Constructor
     * Initialize the headPosition, trailPosition, and territoryPosition.
     * @param type -- either user or bot
     */
    public Box(String type, int rowCount, int columnCount){
        this.type = type;
        this.trailPosition = new ArrayList<>();
        this.velocity = initializeVelocity();
        this.initializePosition(rowCount, columnCount);
    }

    /**
     * Randomizes position for box creation
     * @return the initialized position coordinates
     */
    private void initializePosition(int rowCount, int columnCount){
        Random rand = new Random();
        headPosition = new HashMap<>();
        headPosition.put("X-coordinate", rand.nextInt(columnCount-2)+1);
        headPosition.put("Y-coordinate", rand.nextInt(rowCount-2)+1);

        initializeTerritory();
    }
    private void initializeTerritory(){
        this.territoryPosition = new ArrayList<>();
        int XCoord =  this.headPosition.get("X-coordinate");
        int YCoord = this.headPosition.get("Y-coordinate");
        HashMap<String, Integer> initialTerr = new HashMap<>();
        initialTerr.put("X-coordinate", XCoord);
        initialTerr.put("Y-coordinate", YCoord);
        this.territoryPosition.add(initialTerr);
    }
    private HashMap<String, Integer> initializeVelocity(){
        velocity = new HashMap<>();
        velocity.put("X-velocity", 0);
        velocity.put("Y-velocity", 0);
        return velocity;
    }


    public void updatePosition() {
        updateTrail();
        updateHead();
    }
    private void updateTrail(){
        HashMap<String, Integer> addedTrail = new HashMap<>();
        addedTrail.put("X-coordinate", this.headPosition.get("X-coordinate"));
        addedTrail.put("Y-coordinate", this.headPosition.get("Y-coordinate"));
        if (!this.trailPosition.contains(addedTrail)){
            this.trailPosition.add(addedTrail);
        }
    }
    private void updateHead(){
        int currentX = headPosition.get("X-coordinate");
        int currentY = headPosition.get("Y-coordinate");
        int nextX = currentX + velocity.get("X-velocity");
        int nextY = currentY + velocity.get("Y-velocity");

        this.headPosition.replace("X-coordinate", nextX);
        this.headPosition.replace("Y-coordinate", nextY);
    }

    public void updateVelocity(String movement) {
        switch (movement) {
            case "UP":
                velocity.replace("X-velocity", 0);
                velocity.replace("Y-velocity", -1);
                break;
            case "LEFT":
                velocity.replace("X-velocity", -1);
                velocity.replace("Y-velocity", 0);
                break;
            case "DOWN":
                velocity.replace("X-velocity", 0);
                velocity.replace("Y-velocity", 1);
                break;
            case "RIGHT":
                velocity.replace("X-velocity", 1);
                velocity.replace("Y-velocity", 0);
                break;
            case "STOP-X":
                velocity.replace("X-velocity", 0);
                break;
            case "STOP-Y":
                velocity.replace("Y-velocity", 0);
                break;
            case "STOP":
                velocity.replace("Y-velocity", 0);
                velocity.replace("X-velocity", 0);
                break;
        }
    }

    public void removeTrailPosition(int row, int col){
        HashMap<String, Integer> deleteTrail = new HashMap<>();
        deleteTrail.put("X-coordinate", col);
        deleteTrail.put("Y-coordinate", row);

        trailPosition.remove(deleteTrail);
        territoryPosition.add(deleteTrail);
    }

    /**
     * The box will stop moving when its at the edge of the board
     */
    public String stopAtWall(String movement, int boardLength, int boardHeight){
        int headX = getHeadX();
        int headY = getHeadY();
        if(! (headX < boardLength-1) || !(headX > 0)){
            movement = "STOP-X";
        }
        if (! (headY < boardHeight-1) || !(headY > 0)){
            if (movement.equals("STOP-X")){
                movement = "STOP";
            }
            else {
                movement = "STOP-Y";
            }
        }
        return movement;
    }


    public String getType(){
        return this.type;
    }
    public int getHeadX(){return this.headPosition.get("X-coordinate");}
    public int getHeadY(){return this.headPosition.get("Y-coordinate");}
    public ArrayList<HashMap<String, Integer>> getTrailPosition() {
        return trailPosition;
    }
    public ArrayList<HashMap<String, Integer>> getTerrPosition(){
        return territoryPosition;
    }
}
