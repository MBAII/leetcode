class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
         unordered_multimap<int,int> m;
         unordered_multimap<int,int>::iterator it;
         vector<int> result;
         for(int i=0; i < nums.size(); i++){
             int another = target - nums[i];
             it = m.find(another);
             if(it == m.end()){
                 m.insert(make_pair(nums[i],i));
             }
             else{
                 result.push_back(it->second);
                 result.push_back(i);
                 break;
             }
         }
         return result;
    }
};