import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.*;

public class STOPCITY {
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
        ArrayList<Integer> parent;
        ArrayList<Integer> distance;
        Graph(int V) {
            this.V = V;
            adjList = new ArrayList<ArrayList<Integer>>();
            visited = new ArrayList<Boolean>();
            parent = new ArrayList<Integer>();
            distance = new ArrayList<Integer>();
            for (int i = 0; i < V; i++) {
                adjList.add(new ArrayList<Integer>());
                visited.add(false);
                parent.add(-1);
                distance.add(Integer.MAX_VALUE);
            }
        }
        void addEdge(int u, int v) {
            adjList.get(u).add(v);
            adjList.get(v).add(u);
        }
        boolean BFS(int s, int d) {
            // BFS can be used to find the shortest path from s to d
            Queue<Integer> q = new LinkedList<Integer>();
            q.add(s);
            visited.set(s, true);

            while (!q.isEmpty()) {
                int u = q.poll();
                for(int i = 0; i < adjList.get(u).size(); i++) {
                    if (visited.get(adjList.get(u).get(i)) == false) {
                        q.add(adjList.get(u).get(i));
                        visited.set(adjList.get(u).get(i), true);
                        distance.set(adjList.get(u).get(i), distance.get(u) + 1);
                        parent.set(adjList.get(u).get(i), u);

                        if (adjList.get(u).get(i) == d) {
                            return true;
                        }
                    }
                }
            }
            return false;
        }
        void printPath(int s, int d) {
            if (!BFS(s, d)) {
                return;
            }
            ArrayList<Integer> path = new ArrayList<Integer>();
            int crawl = d;
            path.add(crawl);
            while (parent.get(crawl) != -1) {
                path.add(parent.get(crawl));
                crawl = parent.get(crawl);
            }
            Collections.sort(path);
            for (int i = 0; i < path.size(); i++) {
                System.out.print(path.get(i) + " ");
            }
        }
    }
    public static void main(String[] args) throws IOException {
        Reader sc = new Reader();
        int N = sc.nextInt();
        Graph g = new Graph(N);
        int u, v;
        u = sc.nextInt();
        v = sc.nextInt();
        while (u != -1 && v != -1) {
            g.addEdge(u, v);
            u = sc.nextInt();
            v = sc.nextInt();
        }
        u = sc.nextInt();
        v = sc.nextInt();
        g.printPath(u, v);
        sc.close();
    }
}
