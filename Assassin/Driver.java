package Assassin;
import java.util.*;

public class Driver{
  public static void main(String[] args){
    Scanner s = new Scanner(System.in);
    System.out.println("Welcome to Assassin! First, make sure everyone knows everyone else's name and face");
    
    
    ////make list of players
    System.out.println("Enter your name if you want to play. Enter 'Bye!' when you are done.");
    ArrayList<Player> players = new ArrayList<Player>();
    String input = s.nextLine();
    while (!(input.equals("Bye!"))){
      players.add(new Player(input));
      input = s.nextLine();
    }
    
    ////assign targets
    //randomize order of ArrayList players
    Collections.shuffle(players);
      
    //go through players and .assignTarget for each
    //make the target the name of the person one index up, 
    //except the last person has target of first index
    for (int i = 0; i < players.size()-1; i++){
      players.get(i).setTarget(players.get(i+1).getName());
    }
    players.get(players.size()-1).setTarget(players.get(0).getName());
    
    
    
    ////let people input their names so they can see their targets
    Player currentPlayer;
    int counter;
    Boolean found;
    input = "";
    String endOfGame = "";
    while (!(endOfGame.equals("Bye!"))){
      //give directions
      System.out.println("Type your name to see your prey. Type 'Bye!' if you are the last one");
      
      //input = a name
      input = s.nextLine();
      endOfGame = input;
      
      //find Player with that name
      counter = 0;
      found = false;
      while (counter < players.size() && !found){
        if (players.get(counter).getName().equals(input)){
          found = true;
        }
        counter += 1;
      }
      //this deincrements it, since at the end of the loop the last iteration, 
      //it will be 1 above the index of the current player
 
      counter -= 1;
      if (!found){
        System.out.println("This player is not in the game.");
      }
      
      //print target name
      if (found){
        System.out.println(players.get(counter).getTarget());
      }
      
      System.out.println("Type 'Ok' to clear panel after you record your target.");
      //input = ok
      //prints a bunch of blank lines to clear interactions pane
      input = s.nextLine();
      while (!(input.equals("Ok"))){
        input = s.nextLine();
      }
      for (int i = 0; i < 10; i++){
          System.out.println();
        }
      
      
    }
    
    s.close();
  }
}