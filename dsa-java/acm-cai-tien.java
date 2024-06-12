import java.util.*;
import java.lang.*;

class ACMCAITIEN
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		int test = sc.nextInt();
		while(test > 0) {
            test -= 1;
            int n = sc.nextInt();
            int[] arr = new int[n];
            for(int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }
            int max = 0;
            max = sc.nextInt();
            int tmp_mx = -1;
            for(int i = 0; i < n-2; ++i) {
                for(int j = i+1; j < n-1; ++j) {
                    for(int z = j+1; z < n; ++z) {
                        if (arr[i] + arr[j] + arr[z] > tmp_mx && arr[i] + arr[j] + arr[z] <= max)
                            tmp_mx = arr[i] + arr[j] + arr[z];
                    }
                }
            }
            System.out.println(tmp_mx);
        }
	}
}