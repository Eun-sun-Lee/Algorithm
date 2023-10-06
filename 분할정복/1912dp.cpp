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

    for(j = 1; j < n; j++){
        arr[j] = max(arr[j], arr[j] + arr[j-1]); 
        maxSum = max(maxSum, arr[j]);  
    }
    return maxSum;
}
