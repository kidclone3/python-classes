import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class ADAQUEUE {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        Deque<Integer> dq = new ArrayDeque<>();
        boolean reverse = false;
        StringBuilder sb = new StringBuilder();
        int x;
        while (t > 0) {
            t -= 1;
            String s = sc.next();
            if (s.equals("reverse")) {
                reverse = !reverse;
                continue;
            }
            if (!reverse) {
                switch (s) {
                    case "toFront":
                        x = sc.nextInt();
                        dq.addFirst(x);
                        break;
                    case "front" :
                        if (dq.isEmpty()) {
                            sb.append("No job for Ada?\n");
                            continue;
                        }
                        sb.append(dq.getFirst() + "\n");
                        dq.removeFirst();
                        break;

                    case "push_back" :
                        x = sc.nextInt();
                        dq.addLast(x);
                        break;

                    case "back" :
                        if (dq.isEmpty()) {
                            sb.append("No job for Ada?\n");
                            continue;
                        }
                        sb.append(dq.getLast() + "\n");
                        dq.removeLast();
                        break;
                }
            } else {
                switch (s) {
                    case "toFront" :
                        x = sc.nextInt();
                        dq.addLast(x);
                        break;
                    case "front" :
                        if (dq.isEmpty()) {
                            sb.append("No job for Ada?\n");
                            continue;
                        }
                        sb.append(dq.getLast() + "\n");
                        dq.removeLast();
                        break;
                    case "push_back" :
                        x = sc.nextInt();
                        dq.addFirst(x);
                        break;
                    case "back" :
                        if (dq.isEmpty()) {
                            sb.append("No job for Ada?\n");
                            continue;
                        }
                        sb.append(dq.getFirst() + "\n");
                        dq.removeFirst();
                        break;
                }
            }
        }
        System.out.println(sb.toString());
    }
}
