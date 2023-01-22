nums=[11,11,9,4,3,3,3,1,-1,-1,3,3,3,5,5,5]
increase = True
decrease = True

for idx in range(1, len(nums)):
    current = nums[idx]
    previous = nums[idx - 1]
    
    if previous > current:
        increase = False
    elif previous < current:
        decrease = False
        
print(increase or decrease)