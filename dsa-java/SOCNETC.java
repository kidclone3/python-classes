
import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class SOCNETC{
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
    static class DisjointSet {
        int[] parent;
        int[] size;
        public DisjointSet(int n) {
            parent = new int[n];
            size = new int[n];
            for(int i = 0; i < n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }
        public int find(int x) {
            if (parent[x] == x) {
                return x;
            }
            return parent[x] = find(parent[x]);
        }
        public void union(int x, int y) {
            int xRoot = find(x);
            int yRoot = find(y);
            if (xRoot == yRoot) {
                return;
            }
            if (size[xRoot] < size[yRoot]) {
                parent[xRoot] = yRoot;
                size[yRoot] += size[xRoot];
            }
            else {
                parent[yRoot] = xRoot;
                size[xRoot] += size[yRoot];
            }
        }

    }
    public static void main(String[] args)
            throws IOException
    {
        Reader sc = new Reader();
        StringBuilder sb = new StringBuilder();
        int n, m;
        n = sc.nextInt();
        m = sc.nextInt();
        DisjointSet ds = new DisjointSet(n);
        int query = sc.nextInt();
        StringTokenizer st;
        for(int q = 0; q < query; q++) {
            st = new StringTokenizer(sc.readLine());
            char type = st.nextToken().charAt(0);
            int a, b;
            if (type == 'E') {
                a = Integer.parseInt(st.nextToken());
                b = Integer.parseInt(st.nextToken());
                sb.append(ds.find(a - 1) == ds.find(b - 1) ? "Yes" : "No").append("\n");
            }
            else if (type == 'S') {
                // size of community
                a = Integer.parseInt(st.nextToken());
                sb.append(ds.size[ds.find(a - 1)]).append("\n");
            } else if (type == 'A') {
                // add to community
                a = Integer.parseInt(st.nextToken());
                b = Integer.parseInt(st.nextToken());
                if (ds.find(a - 1) != ds.find(b - 1)) {
                    if (ds.size[ds.find(a-1)] + ds.size[ds.find(b-1)] <= m) {
                        ds.union(a - 1, b - 1);
                    }
                }
            }
        }
        System.out.println(sb);
    }
}
