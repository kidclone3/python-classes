
import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.IOException;

public class CTRICK{
    static class Reader {
        final private int BUFFER_SIZE = 1 << 16;
        private DataInputStream din;
        private byte[] buffer;
        private int bufferPointer, bytesRead;

        public Reader()
        {
            din = new DataInputStream(System.in);
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }

        public Reader(String file_name) throws IOException
        {
            din = new DataInputStream(
                    new FileInputStream(file_name));
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }

        public String readLine() throws IOException
        {
            byte[] buf = new byte[64]; // line length
            int cnt = 0, c;
            while ((c = read()) != -1) {
                if (c == '\n') {
                    if (cnt != 0) {
                        break;
                    }
                    else {
                        continue;
                    }
                }
                buf[cnt++] = (byte)c;
            }
            return new String(buf, 0, cnt);
        }

        public int nextInt() throws IOException
        {
            int ret = 0;
            byte c = read();
            while (c <= ' ') {
                c = read();
            }
            boolean neg = (c == '-');
            if (neg)
                c = read();
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');

            if (neg)
                return -ret;
            return ret;
        }

        public long nextLong() throws IOException
        {
            long ret = 0;
            byte c = read();
            while (c <= ' ')
                c = read();
            boolean neg = (c == '-');
            if (neg)
                c = read();
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
            if (neg)
                return -ret;
            return ret;
        }

        public double nextDouble() throws IOException
        {
            double ret = 0, div = 1;
            byte c = read();
            while (c <= ' ')
                c = read();
            boolean neg = (c == '-');
            if (neg)
                c = read();

            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');

            if (c == '.') {
                while ((c = read()) >= '0' && c <= '9') {
                    ret += (c - '0') / (div *= 10);
                }
            }

            if (neg)
                return -ret;
            return ret;
        }

        private void fillBuffer() throws IOException
        {
            bytesRead = din.read(buffer, bufferPointer = 0,
                    BUFFER_SIZE);
            if (bytesRead == -1)
                buffer[0] = -1;
        }

        private byte read() throws IOException
        {
            if (bufferPointer == bytesRead)
                fillBuffer();
            return buffer[bufferPointer++];
        }

        public void close() throws IOException
        {
            if (din == null)
                return;
            din.close();
        }
    }
    static class FenwickTree {
        int[] tree;
        int n;
        public FenwickTree(int n) {
            this.n = n;
            tree = new int[n + 1];
        }
        public void update(int i, int val) {
            while (i <= n) {
                tree[i] += val;
                i += (i & -i);
            }
        }
        public int get(int i) {
            int sum = 0;
            while (i > 0) {
                sum += tree[i];
                i -= (i & -i);
            }
            return sum;
        }

        public int get(int l, int r) {
            return get(r) - get(l - 1);
        }

        public int find(int low, int high, int k) {
            if (low == high) {
                return low;
            }
            int mid = (low + high) / 2;
            int s;
            if ((s = get(low, mid)) >= k) {
                return find(low, mid, k);
            }
            return find(mid + 1, high, k - s);
        }
    }
    public static void main(String[] args)
            throws IOException
    {
        Reader sc = new Reader();
        int test = sc.nextInt();
        final int N = (int) 2e5+10;
        int[] ans = new int[N];
        StringBuilder sb = new StringBuilder();
        while (test > 0) {
            test -= 1;
            int n = sc.nextInt();
            FenwickTree fw = new FenwickTree(N);
            for(int i = 1; i <= n; i++) {
                fw.update(i, 1);
            }
            int cur_pos = 0;
            for(int i = 2; i <= n+1; i++) {
                int w = i % (n-i+2);
                if (w == 0) {
                    w = n-i+2;
                }
                int has = fw.get(cur_pos+1, n);
                if (has >= w) {
                    cur_pos = fw.find(cur_pos+1, n, w);
                    fw.update(cur_pos, -1);
                } else {
                    cur_pos = fw.find(1, cur_pos, w-has);
                    fw.update(cur_pos, -1);
                }
                ans[cur_pos] = i-1;
            }
            for(int i = 1; i <= n; i++) {
                sb.append(ans[i] + " ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
