
import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Scanner;
import java.util.StringTokenizer;

public class INVCNT{
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
//        int[] tree;
        HashMap<Integer, Integer> tree;
        int n;
        public FenwickTree(int n) {
            this.n = n;
            tree = new HashMap<>();
        }
        public void update(int i, int val) {
            while(i <= n) {
//                tree[i] += val;
                tree.put(i, tree.getOrDefault(i, 0) + val);
                i += (i & -i);
            }
        }
        public int query(int i) {
            int sum = 0;
            while(i > 0) {
//                sum += tree[i];
                sum += tree.getOrDefault(i, 0);
                i -= (i & -i);
            }
            return sum;
        }
    }

    public static void main(String[] args)
            throws IOException
    {
        Reader sc = new Reader();
        StringBuilder sb = new StringBuilder();
        int t = sc.nextInt();
        while(t > 0) {
            t -= 1;
            int n = sc.nextInt();
            int[] arr = new int[n];
            int ans = 0;
            FenwickTree fw = new FenwickTree(10000000+7);
            for(int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
                ans += i - fw.query(arr[i]-1);
                fw.update(arr[i], 1);
            }
            sb.append(ans).append("\n");
        }
        System.out.println(sb);
    }
}
