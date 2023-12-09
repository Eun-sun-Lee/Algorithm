#include <iostream>
using namespace std;

int dp(int n, int* arr);

int main(){
    int t;
    cin >> t;
    int* arr = new int[4];
    for (int i = 0; i < 4; i++){
        arr[i] = i;
    }
    for (int i = 0; i < t; i++){
        int n;
        cin >> n;
        cout << dp(n, arr) << endl;
    }
}

int dp(int n, int* arr){
    int** ans = new int*[4];
    for (int i = 0; i <= 3; i++){
        ans[i] = new int[n + 1];
    }
    for (int i = 0; i<= 3; i++){
        ans[i][0] = 1;
    }
    for (int i = 0; i<= n; i++){
        ans[0][i] = 0;
    }
    int numComb;
    for (int i = 1; i <= 3; i++){
        for (int j = 1; j <= n; j++){
            if (j - arr[i - 1] < 0) numComb = 0;
            else numComb = ans[i][j - arr[i - 1]];
            ans[i][j] = ans[i - 1][j] + numComb;
        }
    }
    return ans[3][n];
}