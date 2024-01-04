#include <iostream>
#include <climits>
#include <cmath>
using namespace std;

int chainedMatrix(int n, int*d, int** M);

int main(){
    int n;
    cin >> n;
    int *d = new int[n + 1];
    int ** M = new int*[n + 1]; 
    for (int i = 0; i < n; i++){
        int a, b;
        cin >> a >> b;
        if (i == n - 1){
            d[i] = a;
            d[i + 1] = b;
        } else{
            d[i] = a;
        }
    }
    for (int i = 0; i <= n; i++){
        M[i] = new int[n + 1];
    }
    cout << chainedMatrix(n, d, M) << endl;
}

int chainedMatrix(int n, int*d, int** M){
    for (int i = 1; i <= n; i++){
        M[i][i] = 0;
    }
    for (int diagonal = 1; diagonal <= n - 1; diagonal++){ // diagonal : gap
        for (int i = 1; i <= n - diagonal; i++){
            int j = i + diagonal;
            M[i][j] = INT_MAX; 
            for (int k = i; k <= j - 1; k++){
                int temp = M[i][k] + M[k + 1][j] + d[i - 1] * d[k] * d[j];
                if (temp < M[i][j]) {
                    M[i][j] = temp;
                }
            }
        }
    }
    return M[1][n];
}