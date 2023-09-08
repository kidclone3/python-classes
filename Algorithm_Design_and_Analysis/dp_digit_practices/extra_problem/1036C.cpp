// https://codeforces.com/problemset/problem/1036/C

// #include <bits/stdc++.h>
#include <vector>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;

#define ll long long

ll dp[35][2][5];
vector<int> digit;

ll recur(int n, int tight, int remain_zero) {
    if (remain_zero < 0) return 0;
    if (n == 0 && remain_zero >= 0) return 1;
    if (n < 0) return 0;
    if (dp[n][tight][remain_zero] != -1) return dp[n][tight][remain_zero];

    int limit = (tight ? digit[digit.size() - n] : 9);
    ll ans = 0LL;
    for(int i = 0; i <= limit; i++) {
        ans += recur(n-1, tight && (i == limit), remain_zero - (i > 0 ? 1 : 0));
        
    }
    return dp[n][tight][remain_zero] = ans;
}

ll call(ll R) {
    memset(dp, -1, sizeof dp);
    digit.clear();
    while(R > 0) {
        digit.push_back(R % 10);
        R /= 10;
    }
    reverse(digit.begin(), digit.end());
    return recur(digit.size(), 1, 3);
}

ll solve() {
    ll l, r;
    cin >> l >> r;

    ll ans = 0LL;
    ans = call(r) - call(l-1);
    return ans;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t; cin >> t;
    for(int i = 1; i <= t; ++i) {
       cout << solve() << "\n";
    }
}