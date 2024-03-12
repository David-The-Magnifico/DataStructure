import java.util.*;
public class Main {
    public static void main(String[] args) {
        Queue<Integer> q1 = new LinkedList<Integer>();
        q1.add(10);
        q1.add(20);
        q1.add(30);
        q1.add(40);
        q1.add(50);
        System.out.println("Elements in Queue:"+q1);
        System.out.println("Element removed from the queue: "+q1.remove());
        System.out.println("Head of the queue: "+q1.element());
        System.out.println("Poll():Returned Head of the queue: "+q1.poll());
        System.out.println("peek():Head of the queue: "+q1.peek());
        System.out.println("Final Queue:"+q1);
    }
}
