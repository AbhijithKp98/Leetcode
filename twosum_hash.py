class Solution:
    def twoSum_hash(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        foundSol=False
        i=0
        while i<len(nums):
            hashtable[nums[i]]=i
            i+=1
        i=0
        # print(hashtable)
        while i<len(nums) and not foundSol:
            compliment = target - nums[i]
            
            if compliment in hashtable:
                if i!=hashtable[compliment]:
                    sol_list = [i,hashtable[compliment]]
                    foundSol = True
            i+=1
        return sol_list
