 #optimal solution
 
 nums = list(map(int,input().split()))
  nums = sorted(nums)
        temp = 1
        for i in range(0,len(nums)-1,2):
            if(nums[i+1]-nums[i]!=0):
                temp =0 = 0
                return(nums[i])
                break
        if(temp==1):
            return(nums[-1])
