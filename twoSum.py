def twoSum(self, nums: List[int], target: int) -> List[int]:
        # U - param: array of integers - [2,7,11, 15], target - integer
        # one solution, same element only use once.
        # loop through nums, sorted, if element > target, no need to loop for the rest.
        

        hashmap = {}
        # loop through nums list to create a hashmap = {element in nums : index in nums}
        for i in range(len(nums)): # i is index of nums
            # dict[key] == value
            key = nums[i]
            hashmap[key] = i
        # loop through nums list to find if 2nd element exist
        for i in range(len(nums)):
            complement = target - nums[i] # e.g. target 9, nums[0]=2, looking for complement=7
            # if complement exist, and value of hashmap(index in nums) is not index i itself
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        # if no valid pair/complement is found, return an empty list
        return []
    
    # Test case
    # nums = [2,7,11,15], target = 9
    # Expected output: [0,1] or [1,0]
    # nums = [3,2,4], target = 6
    