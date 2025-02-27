# 雙指針、移動窗口
# sum 是 python 函式名稱，不應該當變數名稱
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        current_sum = 0
        min_length = len(nums)+1
        s = 0

        # 左指針：s , 右指針: e
        for e in range(len(nums)) : 
            current_sum = current_sum + nums[e]
            while current_sum >= target :
                min_length = min(min_length,e-s+1)
                current_sum -= nums[s]
                s += 1
        return min_length if len(nums) >= min_length else 0