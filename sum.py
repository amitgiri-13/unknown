class solution:
    def calc(self,nums,target):
        i=0
        for i in range(0,len(nums)-1):
            j=i+1
            for j in range(i+1,len(nums)-i-1):
                if nums[i]+nums[j]==target:
                    break
                
        return i,j
            

            
