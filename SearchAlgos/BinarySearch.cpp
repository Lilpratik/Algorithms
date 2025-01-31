#include <iostream>
#include <vector>
using namespace std;
// TC = O(log n) SC = O(1)
int binarySearch(vector<int> arr, int tar) {
    int st = 0, end = arr.size() - 1;
    while(st <= end) {
        // int mid = (st + end) / 2; // if the index value is larger it can give overflow
        // here is the optimized formula to calculate the mid in integer and avoid overflow
        int mid = st + (end - st) / 2;
        if(tar > arr[mid]) {
            st = mid + 1;
        } else if(tar < arr[mid]) {
            end = mid - 1;
        } else {
            return mid;
        }
    }
    return -1;
}

// Binary Search using recursion TC / SC = O(log n) 
int recBinarySearch(vector<int> arr, int tar, int st, int end) {
    if(st <= end) {
        int mid = st + (end - st)/2;
        if(tar > arr[mid]) {
            return recBinarySearch(arr, tar, mid+1, end);
        } else if(tar < arr[mid]) {
            return recBinarySearch(arr, tar, st, mid-1);
        } else {
            return mid;
        }
    }
    return -1;
}

int main() {
    vector<int> arr = {-1, 0, 3, 4, 5, 9, 12};
    int tar = 12;

   // cout << binarySearch(arr, tar) << endl;

    vector<int> arr1 = {-1, 0, 3, 5, 9, 12};
    int tar1 = 20;
    int st = 0;
    int end = arr1.size() -1;

    cout << recBinarySearch(arr1, tar1, st, end) << endl;

    return 0;
}
