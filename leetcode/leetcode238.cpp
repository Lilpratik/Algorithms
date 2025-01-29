//238. Product of Array Except Self
//Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

//The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

//You must write an algorithm that runs in O(n) time and without using the division operation.
// O(1) space comlexity 
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n, 1);
        // prefix => ans
        for(int i = 1; i < n; i++) {
            ans[i] = ans[i-1] * nums[i-1];
        }
        int suffix = 1;
        // suffix
        for(int i = n - 2; i >= 0; i--){
            suffix *= nums[i+1]; // ith suffix
            ans[i] *= suffix;
        }
        return ans;
    }
};
