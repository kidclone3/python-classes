import java.util.ArrayList;
import java.util.Scanner;
import java.util.Stack;

public class STPAR {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(true) {
            int n = sc.nextInt();
            if (n == 0) break;
            int x;

            Stack<Integer> st = new Stack<>();
            Stack<Integer> order = new Stack<>();
            for (int i = 0; i < n; ++i) {
                x = sc.nextInt();
                st.push(x);
            }
//        sc.nextInt();
            while (!st.empty()) {
                order.push(st.pop());
            }
            int lowest = 1;
            boolean ans = true;
            while ((!order.empty() || !st.empty()) && ans) {
                if (!order.empty() && order.peek() == lowest) {
                    order.pop();
                    lowest += 1;
                } else if (!st.empty() && st.peek() == lowest) {
                    st.pop();
                    lowest += 1;
                } else {
                    if (!order.empty()) {
                        st.push(order.pop());
                    } else {
                        ans = false;
                    }
                }
            }
            System.out.println(ans ? "yes" : "no");
        }
    }
}
