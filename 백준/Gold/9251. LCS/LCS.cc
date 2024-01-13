#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int lcs(string s1, string s2);

int main(){
    string s1, s2;
    cin >> s1 >> s2;
    lcs(s1, s2);
}

int lcs(string s1, string s2){
    int** dp = new int*[s1.length() + 1];
    int** s = new int*[s1.length() + 1];

    for (int i = 0; i <= s1.length(); i++){
        dp[i] = new int [s2.length() + 1];
        s[i] = new int [s2.length() + 1];
    }
    for (int i = 0; i <= s1.length(); i++){
        dp[i][0] = 0;
    }
    for (int i = 0; i <= s2.length(); i++){
        dp[0][i] = 0;
    }
    for(int i = 1; i <= s1.length(); i++){
        for (int j = 1; j <= s2.length(); j++){
            if (s1[i - 1] == s2[j - 1]){
                dp[i][j] = dp[i - 1][j - 1] + 1;
                s[i][j] = 0;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                if (dp[i][j] == dp[i - 1][j]) s[i][j] = 1;
                else s[i][j] = 2;
            }
        }
    }
    cout << dp[s1.length()][s2.length()] << endl;
    return dp[s1.length()][s2.length()];
}
