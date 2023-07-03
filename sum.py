class solution:
    def calc(self,nums,target):
        for i in range(len(nums)):
            j=i+1
            for j in range(len(nums)):
                if nums[i]+nums[j]==target:
                    break
            break
        return i,j
        