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
        this.initializePosition(rowCount, columnCount);
        this.trailPosition = new ArrayList<>();
        //this.territoryPosition = new ArrayList<>();
        this.velocity = initializeVelocity();
    }



    /**
     * Randomizes position for box creation
     * @return the initialized position coordinates
     */
    private void initializePosition(int rowCount, int columnCount){
        this.initializeHeadPosition(rowCount, columnCount);
        this.initializeTerritory(rowCount, columnCount);

    }

    private void initializeHeadPosition(int rowCount, int columnCount){
        Random rand = new Random();
        headPosition = new HashMap<>();
        headPosition.put("X-coordinate", rand.nextInt(columnCount-1));
        headPosition.put("Y-coordinate", rand.nextInt(rowCount-1));
    }

    private void initializeTerritory(int rowCount, int columnCount){
        this.territoryPosition = new ArrayList<>();
        int addedXCoord =  this.headPosition.get("X-coordinate");
        int addedYCoord = this.headPosition.get("Y-coordinate");
        HashMap<String, Integer> initialTerr = new HashMap<>();
        initialTerr.put("X-coordinate", addedXCoord);
        initialTerr.put("Y-coordinate", addedYCoord);
        this.territoryPosition.add(initialTerr);
//        for(int i = -2; i < 2; i++) {
//            for(int j = -2; j < 2; j++) {
//                int addedXCoord =  this.headPosition.get("X-coordinate") + i;
//                int addedYCoord = this.headPosition.get("Y-coordinate") + j;
//                if(addedXCoord > columnCount - 1){ addedXCoord = columnCount - 1;}
//                if(addedYCoord > rowCount - 1){ addedYCoord = rowCount - 1;}
//                HashMap<String, Integer> initialTerr = new HashMap<>();
//                initialTerr.put("X-coordinate", addedXCoord);
//                initialTerr.put("Y-coordinate", addedYCoord);
//                this.territoryPosition.add(initialTerr);
//            }
//        }

    }

    /**
     * Initialize velocity, default is to the right
     * @return the velocity of this box
     */
    public HashMap<String, Integer> initializeVelocity(){
        velocity = new HashMap<>();
        velocity.put("X-velocity", 1);
        velocity.put("Y-velocity", 0);
        return velocity;
    }


    public HashMap<String, Integer> getHeadPosition(){
        return this.headPosition;
    }

    public int getHeadX(){return this.headPosition.get("X-coordinate");}

    public int getHeadY(){return this.headPosition.get("Y-coordinate");}

    public void updatePosition() {
        //HashMap<String, Integer> currentHead = this.headPosition;
        HashMap<String, Integer> addedTrail = new HashMap<>();
        addedTrail.put("X-coordinate", this.headPosition.get("X-coordinate"));
        addedTrail.put("Y-coordinate", this.headPosition.get("Y-coordinate"));
        if (!this.trailPosition.contains(addedTrail)){
            this.trailPosition.add(addedTrail);
        }


        int currentX = this.headPosition.get("X-coordinate");
        int currentY = this.headPosition.get("Y-coordinate");
        int nextX = currentX + this.velocity.get("X-velocity");
        int nextY = currentY + this.velocity.get("Y-velocity");

        this.headPosition.replace("X-coordinate", nextX);
        this.headPosition.replace("Y-coordinate", nextY);


    }

    public void updateVelocity(String button) {
        if (button == null){
            button = "RIGHT";
        }
        if (button.equals("UP")){
            velocity.replace("X-velocity", 0);
            velocity.replace("Y-velocity", -1);
        } else if (button.equals("LEFT")){
            velocity.replace("X-velocity", -1);
            velocity.replace("Y-velocity", 0);
        } else if(button.equals("DOWN")){
            velocity.replace("X-velocity", 0);
            velocity.replace("Y-velocity", 1);
        } else if (button.equals("RIGHT")){
            velocity.replace("X-velocity", 1);
            velocity.replace("Y-velocity", 0);
        } else if(button.equals("STOP-X")){
            velocity.replace("X-velocity", 0);
        } else if(button.equals("STOP-Y")){
            velocity.replace("Y-velocity", 0);
        } else if(button.equals("STOP")){
            velocity.replace("Y-velocity", 0);
            velocity.replace("X-velocity", 0);
        }
    }

    public void removeTrailPosition(int x, int y){
        HashMap<String, Integer> deletedTrail = new HashMap<>();
        deletedTrail.put("X-coordinate", x);
        deletedTrail.put("Y-coordinate", y);

        this.trailPosition.remove(deletedTrail);
        this.territoryPosition.add(deletedTrail);
    }

    public ArrayList<HashMap<String, Integer>> getTrailPosition() {
        return this.trailPosition;
    }
    public ArrayList<HashMap<String, Integer>> getTerrPosition(){
        return territoryPosition;
    }
}
