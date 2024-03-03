import java,util.*;

public class Queue{
  public static void main(String[] args){
    Queue<String> str_queue = new LinkedList<>();
    str_queue.add("one");
    str_queue.add("two");
    str_queue.add("three");
    str_queue.add("four");
    Syystem.out.println("The Queue contains:" + str_queue);
  }
}
