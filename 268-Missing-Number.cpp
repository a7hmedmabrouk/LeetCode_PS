class Solution {
public:
    int missingNumber(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int count =0;
        for(int i=0;i<nums.size();++i){
            if(count == nums[i])
                count ++;
            else
                return count;
        }
        return count;
    }
};