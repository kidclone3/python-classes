import java.util.*;
import java.lang.*;

class SNTGT
{
	public static void main (String[] args) throws java.lang.Exception
	{
        int N = 100000+5;
        int[] gt = new int[N];
        int[] prime = new int[N];
        int tmp_gt = 1;
        gt[1] = 1;
        for(int i = 2; tmp_gt * i < N; ++i) {
            tmp_gt *= i;
            gt[tmp_gt] = 1;
            gt[tmp_gt-1] = 1;
            gt[tmp_gt+1] = 1;
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
            if (gt[n] == 1 && prime[n] == 0) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
	}
}