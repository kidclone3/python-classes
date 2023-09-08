// https://lightoj.com/problem/investigation

// #include <bits/stdc++.h>
#include <vector>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;
#define int uint32_t
int dp[10][2][100][100];
vector<int> digit;
int recur(int n, bool tight, int remDigit, int remNumber, int k) {
    if (n == 0) {
        if (remDigit== 0 && remNumber == 0) return 1;
        else return 0;
    }
    if (dp[n][tight][remDigit][remNumber] != -1) return dp[n][tight][remDigit][remNumber];

    int limit = 0;
    limit = (tight ? digit[digit.size() - n] : 9);
    int ans = 0;
    for(int i = 0; i <= limit; i++) {
        ans += recur(n-1, tight && (i == limit), (remDigit + i) % k, (remNumber * 10 + i)% k, k);
    }
    return dp[n][tight][remDigit][remNumber] = ans;
}

int sumDigit(int R, int k) {
    memset(dp, -1, sizeof dp);
    digit.clear();
    while (R > 0) {
        digit.push_back(R % 10);
        R /= 10;
    } 
    reverse(digit.begin(), digit.end());
    return recur(digit.size(), 1, 0, 0, k);
}

int solve() {
    int l, r, k;
    cin >> l >> r >> k;
    // cout << "\n" << l << " " << r << '\n';
    if (k <= 81) {
        int ans = 0;
        ans = sumDigit(r, k) - sumDigit(l-1, k);
        return ans;
    } else return 0;
}

signed main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t; cin >> t;
    for(int i = 1; i <= t; ++i) {
        cout << "Case " << i << ": " << solve() << "\n";
    }
}