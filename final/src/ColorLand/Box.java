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
        this.headPosition = initializePosition(rowCount, columnCount);
        this.trailPosition = new ArrayList<>();
        this.territoryPosition = new ArrayList<>();
        this.velocity = initializeVelocity();
    }



    /**
     * Randomizes position for box creation
     * @return the initialized position coordinates
     */
    public HashMap<String, Integer> initializePosition(int rowCount, int columnCount){
        Random rand = new Random();
        headPosition = new HashMap<>();
        headPosition.put("X-coordinate", rand.nextInt(columnCount));
        headPosition.put("Y-coordinate", rand.nextInt(rowCount));
        return headPosition;
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

    public void updatePosition() {
        HashMap<String, Integer> currentHead = this.headPosition;
        int currentX = this.headPosition.get("X-coordinate");
        int currentY = this.headPosition.get("Y-coordinate");
        int nextX = currentX + this.velocity.get("X-velocity");
        int nextY = currentY + this.velocity.get("Y-velocity");
        this.trailPosition.add(currentHead);
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
        }
        else if (button.equals("RIGHT")){
            velocity.replace("X-velocity", 1);
            velocity.replace("Y-velocity", 0);
        }else if(button.equals("STOP")){
            velocity.replace("X-velocity", 0);
            velocity.replace("Y-velocity", 0);
        }
    }
}
