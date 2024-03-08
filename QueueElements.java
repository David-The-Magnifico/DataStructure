import java.util.queue;

public class QueueElements{
  public static vod main(String[] args){
    Queue queue = new LinkedList();
    queue.add("Value-0");
    queue.add("Value-1");
    queue.add("Value-2");
    queue.add("Value-3");
    System.out.println("The Queue elements through iterator:");
    Iterator iterator = queue.iterator();
    while(iterator.hasNext()){
      String element = (String) iterator.next();
      System.out.print(element + " ");
    }
     System.out.println("\n\nThe Queue elements using for loop:");
    for(Object object : queue) {
        String element = (String) object;
        System.out.print(element + " ");
    }
    }
}
