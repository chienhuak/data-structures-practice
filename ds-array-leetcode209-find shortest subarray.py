# 暴力解法 ：只紀錄 sum, length，並迴圈進行比較
# Time : O(n*n) --> Time Limit Exceeded
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        ans_length = len(nums)+1

        for i in range(len(nums)) : # 0 > 1 > 2 > 3 > 4
            current_length = 0
            current_sum = 0
            for j in range(i,len(nums)) : # 0~4, 1~4, 2~4, 3~4, 4
                current_sum = current_sum + nums[j]
                current_length += 1
                if current_sum >= target :
                    if current_length < ans_length :
                        ans_length = current_length
        return ans_length if ans_length <= len(nums) else 0