#include <iostream>
#include <cmath>
using namespace std;
// #define MAX 1500010
// int dp[MAX];

int ans(int n, int* t, int* p);

int main(){
    int n;
    cin >> n;
    int* t = new int[n + 1];
    int* p = new int [n + 1];
    // t[0] = p[0] = 0;
    for (int i = 1; i <= n; i++){
        cin >> t[i] >> p[i];
    }
    cout << ans(n, t, p) << endl;
}

int ans(int n, int* t, int* p){
    int* dp = new int[n + 2]();
    int maxNum = 0;
    for (int i = 1; i <= n + 1; i++){ // 퇴사하는 날(n+1)까지도 포함해야함.
        maxNum = max(maxNum, dp[i]); // 0,0  0,0  0,0  0,10  10,30  30,0  30,45 
        if (i + t[i] > n + 1) continue;
        // cout << "i: " << i << " max: " << maxNum << " dp[i]: " << dp[i] << endl;
        // maxNum = max(maxNum, dp[i]); // 0,0  0,0  0,0  0,10  10,30  30,0  
        // a[i + t[i]] = max(a[i + t[i]], max(p[i], maxNum) + p[i + t[i]]); -> 한번에 다음꺼까지 처리하려했기 때문에 오류
        dp[i + t[i]] = max(dp[i + t[i]], p[i] + maxNum);
        // maxNum = max(maxNum, dp[i]); // 0,0  0,0  0,0  0,10  10,20  20,20  
    }
    return maxNum;
}