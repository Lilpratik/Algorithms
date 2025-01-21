//  maximum sum of a subarray using Kadane's Algorithm, a popular and efficient approach
#include<iostream>
#include<vector>
#include<climits>
using namespace std;

int maxSubArray(vector<int>& nums) {
    int currSum = 0, maxSum = INT_MIN;
    for (int val : nums) {
        currSum += val;
        maxSum = max(currSum, maxSum);
        if (currSum < 0) {
            currSum = 0;
        }
    }
    return maxSum;
}

int main() {
    vector<int> nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    cout << "Maximum subarray sum is: " << maxSubArray(nums) << endl;
    return 0;
}


// Complexity:
// Time Complexity: 
// 𝑂(𝑛)
// O(n), as the array is traversed once.
// Space Complexity: 
// 𝑂(1)
// O(1), as no extra space is used except for a few variables.
