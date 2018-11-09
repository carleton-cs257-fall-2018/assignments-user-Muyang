package ColorLand;

import java.util.*;

public class Box{
    private HashMap<String, Integer> headPosition;
    private HashMap<String, Integer> velocity;
    private String type;
    private ArrayList<HashMap<String, Integer>> trailPosition;
    private ArrayList<HashMap<String, Integer>> territoryPosition;



    /*
     * Constructor
     * Initialize the headPosition, trailPosition, and territoryPosition.
     * @param type -- either user or bot
     */
    public Box(String type){
        this.type = type;
        this.headPosition = initializePosition();
        this.trailPosition = new ArrayList<>();
        this.territoryPosition = new ArrayList<>();
        this.velocity = initializeVelocity();
    }

    /*
     * Randomizes position for box creation
     * @return the initialized position coordinates
     */
    public HashMap<String, Integer> initializePosition(){
        headPosition = new HashMap<>();
        headPosition.put("X-coordinate", 0);
        headPosition.put("Y-coordinate", 0);
        return headPosition;
    }
    /*
     * Initialize velocity
     * @return the velocity of this box
     */
    public HashMap<String, Integer> initializeVelocity(){
        velocity = new HashMap<>();
        velocity.put("X-velocity", 1);
        velocity.put("Y-velocity", 0);
        return velocity;
    }
}
