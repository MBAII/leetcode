class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
         int i = 0;
         int j = nums.size() - 1;
         vector<int> result;
         while(true){
             if (nums[i] + nums[j] == target){
                 result.push_back(i);
                 result.push_back(j);
                 return result;
             }
             else if(nums[i] + nums[j] > target){
                 j--;
             }
             else if(nums[i] + nums[j] < target){
                 i++;
             }
         }
         
    }
};