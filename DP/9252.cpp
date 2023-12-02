#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int lcs(string s1, string s2);
void printLCS(string s1, string s2, int** S, int len1, int len2);

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
    printLCS(s1, s2, s, s1.length(), s2.length());
    cout << endl;
    return dp[s1.length()][s2.length()];
}

void printLCS(string s1, string s2, int** S, int len1, int len2){
    if (len1 == 0 || len2 ==0) return;
    if (S[len1][len2] == 0){
        printLCS(s1, s2, S, len1 - 1, len2 -1);
        cout << s1[len1 - 1];
    } else if (S[len1][len2] == 1){
        printLCS(s1, s2, S, len1 - 1, len2);
    } else{
        printLCS(s1, s2, S, len1, len2 - 1);
    }
}