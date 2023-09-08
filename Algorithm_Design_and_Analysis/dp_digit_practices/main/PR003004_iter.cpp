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

ll digit(ll R) {
    num.clear();
    memset(dp, 0, sizeof dp);
    // cout << R << "\n";
    while (R > 0) {
        num.push_back(R%10);
        R/=10;
    }
    reverse(num.begin(), num.end());
    int n = num.size();

    dp[n][0][0] = 1LL;
    dp[n][0][1] = 1LL;

    for(int i = n-1; i >= 0; --i) {
        for(int tight = 0; tight < 2; ++tight) {
            for(int sum = 0; sum < 200; ++sum) {
                if (tight) {
                    for(int d = 0; d <= num[i]; ++d) {
                        dp[i][sum][1] += (d == num[i]) ? dp[i+1][sum-d][1] : dp[i+1][sum-d][0];
                    }
                } else {
                    for(int d = 0; d <= 9; ++d) {
                        dp[i][sum][0] += dp[i+1][sum-d][0];
                    }
                }
            }
        }
    }
    
    ll ans = 0LL;
    for(int i = 0; i < 200; ++i)  {
        // cout << dp[0][i][1] << " ";
        ans += dp[0][i][1]*i;
    }
    return ans;
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
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t; cin >> t;
    while (t--) {
        solve();
    }
}
