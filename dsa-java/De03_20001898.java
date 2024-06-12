public class De03_20001898 {
    final static private double INF = 1e18;
    public static double max(double[] a, int n) {
        int low = 0+1, high = n-1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (a[mid-1] < a[mid] && a[mid] > a[mid+1]) return a[mid];
            else if (a[mid-1] < a[mid] && a[mid] < a[mid+1]) {
                low = mid+1;
            } else {
                high = mid-1;
            }
        }
        return -INF; // if not found answer;
    }
    public static void main(String[] args) {
        double[] a = {1, 2, 3, 4, 3.1, 3.2, 1.4};
        System.out.println(max(a, a.length));
    }
}
