import java.util.*;
import java.lang.*;

class SLPLN
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		int test = sc.nextInt();
		while(test > 0) {
            test -= 1;
            int n = sc.nextInt();
            int x = (int) Math.cbrt(n);
            System.out.println(x);
        }
	}
}