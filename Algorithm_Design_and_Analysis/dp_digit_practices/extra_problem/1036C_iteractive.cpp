// #include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <cstring>

using namespace std;
#define int long long

int dp[20][2][5];
vector<int> digit;


int call(int R) {
    memset(dp, 0, sizeof dp);
    digit.clear();
    while (R > 0) {
        digit.push_back(R % 10);
        R /= 10;
    }
    int n = digit.size();
    dp[n][1][0] = dp[n][0][0] = 1;

    for(int i = n-1; i > -1; i--) {
        for(int tight = 0; tight < 2; tight++) {
            for(int notZero = 0; notZero < 4; notZero++) {
                if (tight) {
                    for(int d = 0; d <= digit[i]; d++) {
                        if (d == 0) {
                            dp[i][1][notZero] += (d == digit[i] ? dp[i+1][1][notZero] : dp[i+1][0][notZero]);
                        }
                        else {
                            if (notZero - 1 < 0) break;
                            dp[i][1][notZero] += (d == digit[i] ? dp[i+1][1][notZero - 1] : dp[i+1][0][notZero-1]);
                        }
                    }
                } else {
                    for(int d = 0; d <= 9; d++) {
                        if (d == 0) {
                            dp[i][1][notZero] += dp[i+1][0][notZero];
                        }
                        else {
                            if (notZero - 1 < 0) break;
                            dp[i][1][notZero] += dp[i+1][0][notZero-1];
                        }
                    }
                }
            }
        }
    }
    for(int i = 0; i < n; ++i) {
        cout << "i: " << i << "\n";
        for(int tight = 0; tight < 2; ++tight) {
            for(int nZero = 0; nZero < 4; ++nZero) {
                cout << dp[i][tight][nZero] << ",";
            }
            cout << ' ';
            
        }
        cout << '\n';
    }
    int ans = 0;
    for(int i = 0; i < 4; ++i) {
        ans += dp[0][1][i];
    }
    return ans;
}

int solve() {
    int l, r; cin >> l >> r;

    cout << call(r) - call(l-1) << "\n";
    return 0;
}

signed main() {
    int t; cin >> t;
    while (t--) solve();
}