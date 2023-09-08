#include<vector>
#include<utility>
#include<iostream>
using namespace std;
#define IOS ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

int N;
int dx[] = {-2, -2, -1, -1, 1, 1, 2, 2};
int dy[] = {-1, 1, -2, 2, -2, 2, -1, 1};

pair<int, int> operator+ (const pair<int, int>& a, const pair<int, int>& b) {
    return {a.first + b.first, a.second + b.second};
}
bool operator== (const pair<int, int>& a, const pair<int, int>& b) {
    return a.first == b.first && a.second == b.second;
}
vector<pair<int, int>> path, ans;
// vector<vector<pair<int, int>>> ans;
vector<vector<bool>> check;
void solve();
void out() {
    ans = path;
}
bool found = false;
bool inside(pair<int, int> x) {
    return 0 <= x.first && x.first < N && 0 <= x.second && x.second < N;
}
void backtrack(pair<int, int> pos) {
    if (found) return;
    for(int i =0; i < 8; ++i) {
        pair<int, int> curr = pos+make_pair(dx[i], dy[i]);
        if (inside(curr)) {
            if (!check[curr.first][curr.second]) {
                check[curr.first][curr.second] = 1;
                path.push_back(curr);
                backtrack(curr);
                check[curr.first][curr.second] = 0;
                path.pop_back( );
            }
            else if (curr == make_pair(0, 0) && path.size() == N*N) {
                out();
                found = true;
            }
        }
    }
}
int main()
{
    IOS;
    solve();
}
void solve() {
    cin >> N;    
    check.resize(N, vector<bool>(N, 0));
    check[0][0] = 1;
    path.push_back({0, 0});
    backtrack({0, 0});
    cout << ans.size() <<"\n";
    // print(ans);
    if (!found) {
        cout << "Not found!";
    } else {
        if (ans.size() != 0) {
            vector<vector<int>> grid(N, vector<int>(N));
            int i = 0;
            for(auto &it: ans) {
                grid[it.first][it.second] = i++;
            }
            for(auto &it: grid) {
                for(auto &it2: it) {
                    cout << it2 << " ";
                }
                cout << "\n";
            }
        }
    }

}