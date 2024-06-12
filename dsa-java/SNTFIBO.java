import java.util.*;
import java.lang.*;

class SNTFIBO
{
	public static void main (String[] args) throws java.lang.Exception
	{
        int N = 100000+5;
        int[] fibo = new int[N];
        int[] prime = new int[N];
        int fibo1, fibo2;
        fibo1 = 0; fibo2 = 1;
        fibo[0] = 1;
        fibo[1] = 1;
        while(fibo2 <= N) {
            fibo[fibo2] = 1;
            int tmp = fibo2;
            fibo2 = fibo1 + fibo2;
            fibo1 = tmp;
        }
        prime[1] = 1;
        prime[2] = 0;
        for(int i = 2; i < N; ++i) {
            if (prime[i] == 0) {
                for(int j = i+i; j < N; j += i) {
                    prime[j] = 1;
                }
            }
        }
		Scanner sc = new Scanner(System.in);
		int test = sc.nextInt();
		while(test > 0) {
            test -= 1;
            int n = sc.nextInt();
            if (fibo[n] == 1 && prime[n] == 0) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
	}
}