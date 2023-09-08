#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int inf = 1e9;
vector<vector<pair<int, int>>> G;
vector<int> d;

void dijkstra(){
    int n = G.size();
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, 1});

    while(pq.size()){
        int u = pq.top().second,
            du = pq.top().first;
        pq.pop();
        if (du!=d[u]) continue;

        for(int i = 0; i < G[u].size(); ++i) {
            int v = G[u][i].second,
                uv = G[u][i].first;
            if (d[v] > du+uv) d[v] = du+uv, pq.push({d[v], v});
        }
    }
}

int main(){
    int n, m;
    G = vector<vector<pair<int, int>>>(n+1);
    d = vector<int>(n+1, inf);
    while(m--){
        int u, v, w;
        cin >> u >> v >> w;
        G[u].push_back({w, v});
        G[v].push_back({w, u});
    }
    dijkstra();
}