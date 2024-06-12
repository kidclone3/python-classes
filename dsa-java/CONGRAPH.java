import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayList;

public class CONGRAPH {
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
    static class Graph {
        int V;
        ArrayList<ArrayList<Integer>> adjList;
        ArrayList<Boolean> visited;
        Graph(int V) {
            this.V = V;
            adjList = new ArrayList<ArrayList<Integer>>();
            visited = new ArrayList<Boolean>(V);
            for (int i = 0; i < V; i++) {
                adjList.add(new ArrayList<Integer>());
                visited.add(false);
            }

        }
        void addEdge(int u, int v) {
            adjList.get(u).add(v);
            adjList.get(v).add(u);
        }

        void DFS(int v) {
            visited.set(v, true);
            for (int i = 0; i < adjList.get(v).size(); i++) {
                if (!visited.get(adjList.get(v).get(i))) {
                    DFS(adjList.get(v).get(i));
                }
            }
        }
        int connectedComponent() {
            int count = 0;
            for (int i = 0; i < V; i++) {
                if (!visited.get(i)) {
                    DFS(i);
                    count++;
                }
            }
            return count;
        }
    }
    public static void main(String[] args) throws IOException {
        Reader sc = new Reader();
        int N, M, u, v;
        N = sc.nextInt();
        M = sc.nextInt();
        Graph g = new Graph(N);
        for (int i = 0; i < M; i++) {
            u = sc.nextInt();
            v = sc.nextInt();
            g.addEdge(u, v);
        }
        System.out.println(g.connectedComponent()-1);
    }
}
