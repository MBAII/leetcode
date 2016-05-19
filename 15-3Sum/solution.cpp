class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        int length = nums.size();
        for(int i = 0; i < length; i++){
            if ((i > 0) && (nums[i] == nums[i - 1])){
                continue;
            }
            int l = i + 1;
            int r = length - 1;
            while (l < r){
                vector<int> sub_result;
                if (nums[i] + nums[l] + nums[r] == 0){
                    printf("here");
                    sub_result.push_back(nums[i]);
                    sub_result.push_back(nums[l]);
                    sub_result.push_back(nums[r]);
                    result.push_back(sub_result);
                    while(l < r && nums[l] == nums[l+1]){
                    l++;
                    }
                    while(l < r && nums[r] == nums[r-1]){
                        r--;
                    }
                    l++;
                    r--;
                    
                }
                else if(nums[i] + nums[l] + nums[r] < 0){
                    l++;
                }
                else{
                    r--;
                }
                
                
            }
        }
        return result;
        
    }
};