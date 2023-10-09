def containsDuplicate(nums) -> bool:

    return False if len(nums) == len(set(nums)) else True


containsDuplicate([3,4,2,1,1])