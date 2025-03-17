class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_seen = set()
        duplicates = set()

        for num in nums:
            if num in nums_seen:
                duplicates.add(num)
            else:
                nums_seen.add(num)
        
        if len(duplicates) > 0:
            return True
        else:
            return False