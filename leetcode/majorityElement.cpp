// 169.  Majority Element: The element that appears more than [n / 2] times.
// assume majority element always exists

#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;


// Brute Force approach :
int majorityElementBruteForce(vector<int> nums) {
    int n = nums.size();

    for (int val: nums) {
        int freq = 0;
        for (int el: nums) {
            if (el == val) {
                freq++;
            }
        }
        if (freq > n/2) {
            return val;
        }
    }
    return -1; // exceptional cause majority element will always exists
}

// more optimized approach for the above is that sort the array use sorting
int majorityElementOptimizedSorting(vector<int> nums) {
    int n = nums.size();

    // sorting using standard template library in c++
    sort(nums.begin(), nums.end());

    // frequency count
    int freq = 1,  ans = nums[0];
    for (int i = 1;  i < n; i++) {
        if (nums[i] == nums[i - 1]) {
            freq++;
        } else {
            freq = 1;
            ans = nums[i];
        }
        if (freq > n/2) {
            return ans;
        }
    }

    // assume ans will not always exists
    int count = 0;
    for (int val: nums) {
        if (val == ans) {
            count++;
        }
    }

    if (count > n/2){
        return ans;
    } else {
        return -1;
    }

    return ans;
}

// Optimized approach: Moore's voting algorithm

int majorityElementMooreAlgo(vector<int> nums) {
    int n = nums.size();
    int freq = 0, ans = 0;

    for (int i = 0; i < n; i++) {
        if (freq == 0) {
            ans = nums[i];
        }
        if (ans == nums[i]) {
            freq++;
        } else {
            freq--;
        }
    }
    return ans;
}



int main() {
    vector<int> nums = {2, 2, 1, 1, 1, 2, 2};
    cout << "Majority Element: " << majorityElementBruteForce(nums) << endl;
    cout << "Majority Element: " << majorityElementOptimizedSorting(nums) << endl;
    cout << "Majority Element: " << majorityElementMooreAlgo(nums) << endl;
    return 0;
}
