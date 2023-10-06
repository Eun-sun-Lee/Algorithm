#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

int kadane(int arr[], int n);

int main(){
    int n;
    cin >> n;
    int* arr = new int[n];

    for (int j = 0; j < n; j++){
        cin >> arr[j];
    }
    cout << kadane(arr, n) << endl;
    delete[] arr;
    return 0; 
}

int kadane(int arr[], int n){
    int j;
    int maxSum = arr[0];
    int thisSum = 0;

    for(j = 0; j < n; j++){
        // cout << "i: " << i << endl; // -4 4 -3 3 6
        thisSum += arr[j];
        if (thisSum > maxSum){
            maxSum = thisSum;
        } else if(thisSum < 0){ // 음수라면
            thisSum = 0;
        } 
    }
    return maxSum;
}