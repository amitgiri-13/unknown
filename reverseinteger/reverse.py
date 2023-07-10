class solution:
    def reverse(self,x:int)->int:
        x=str(x)
        new=''
        flag=False
        if x[0]=='-':
           flag=True
           x= x.replace('-','')
        r=reversed(x)
        if flag:
            new='-'
        else:
            new=''
        for i in r:
            new+=i
        
        if int(new) in range(-2147483648,2147483647):
            return int(new)
        else:
            return 0
