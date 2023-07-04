class solution:
    def calc(self,nums,target):
        i=0
        for i in range(0,len(nums)-1):
            flag=False
            j=i+1
            for j in range(i+1,len(nums)-1):
                if nums[i]+nums[j]==target:
                    flag=True
                    break

            if flag:
                break    
        return i,j
            

nums=[3,2,3]
s=solution()
s.calc(nums,6)