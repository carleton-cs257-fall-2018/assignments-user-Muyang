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
}
