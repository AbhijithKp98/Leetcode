class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        foundSol=False
        i=0
        while i<len(nums) and not foundSol:
            j = i+1
            while j <len(nums) and not foundSol:
                if nums[i] + nums[j] == target:
                    sol_list = [i,j]
                j+=1
            i+=1
        return sol_list
