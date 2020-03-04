public class Player{
  private String name;
  private String target;
  
  public Player(String name){
    this.name = name;
  }
  
  public String getTarget(){
    return target;
  }
  
  public void setTarget(String target){
    this.target = target;
  }
  
  public String getName(){
    return this.name;
  }
}
