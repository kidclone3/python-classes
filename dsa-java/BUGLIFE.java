
import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BUGLIFE{
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
    // 2 coloring graph class
    static class Graph {
        private int V;
        private LinkedList<Integer> adj[];

        Graph(int v)
        {
            V = v;
            adj = new LinkedList[v];
            for (int i = 0; i < v; ++i)
                adj[i] = new LinkedList();
        }

        void addEdge(int v, int w)
        {
            adj[v].add(w);
            adj[w].add(v);
        }

        // colouring graph
        boolean isBipartite(int src, int colorArr[])
        {
            colorArr[src] = 1;
            LinkedList<Integer> q = new LinkedList<Integer>();
            q.add(src);
            while (q.size() != 0) {
                int u = q.poll();
                if (adj[u].size() != 0) {
                    Iterator<Integer> it = adj[u].iterator();
                    while (it.hasNext()) {
                        int v = it.next();
                        if (colorArr[v] == -1) {
                            colorArr[v] = 1 - colorArr[u];
                            q.add(v);
                        }
                        else if (colorArr[v] == colorArr[u])
                            return false;
                    }
                }
            }
            return true;
        }
        boolean isBipartite()
        {
            int colorArr[] = new int[V];
            for (int i = 0; i < V; ++i)
                colorArr[i] = -1;
            for (int i = 0; i < V; i++)
                if (colorArr[i] == -1)
                    if (!isBipartite(i, colorArr))
                        return false;
            return true;
        }
    }

    public static void main(String[] args)
            throws IOException
    {
        Reader sc = new Reader();
        StringBuilder sb = new StringBuilder();
        int test = sc.nextInt();
        for (int t = 1; t <= test; t++) {
            int n, m;
            n = sc.nextInt();
            m = sc.nextInt();
            Graph g = new Graph(n);
            for(int i = 0; i < m; i++) {
                int u, v;
                u = sc.nextInt();
                v = sc.nextInt();
                g.addEdge(u-1, v-1);
            }
            sb.append("Scenario #").append(t).append(":").append("\n");
            sb.append(!g.isBipartite() ? "Suspicious bugs found!" : "No suspicious bugs found!").append("\n");
        }
        System.out.println(sb);
    }
}
