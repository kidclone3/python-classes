// https://www.spoj.com/problems/PR003004/
// #include <bits/stdc++.h>
#include <vector>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
#define ll long long

ll dp[20][200][2];
vector<int> num;

ll call(int pos, int sum, bool tight) {
    if (pos == num.size()) return sum;
    if (dp[pos][sum][tight] != -1) return dp[pos][sum][tight];

    int limit = 9;
    if (tight) limit = num[pos];
    ll ans = 0LL;
    for(int i = 0; i <= limit; ++i) {
        ans += call(pos+1, sum + i, tight && (i == num[pos]));
        // cout << pos << " " << i << " " << ans << '\n';
    }
    return dp[pos][sum][tight] = ans;
}

ll digit(ll R) {
    num.clear();
    memset(dp, -1, sizeof dp);
    // cout << R << "\n";
    while (R > 0) {
        num.push_back(R%10);
        R/=10;
    }
    reverse(num.begin(), num.end());
    return call(0, 0, 1);
}

int solve() {
    ll a, b;
    cin >> a >> b;
    // cout << digit(a-1) << '\n';
    // cout << digit(b) << '\n';
    cout << digit(b) - digit(a-1) << '\n';
    return 0;
}

signed main() {
    int t; cin >> t;
    while (t--) {
        solve();
    }
}
