grid = [[1,2,4],[3,3,1]]
for i in range(len(grid)):
    grid[i].sort(reverse=True)
    print(grid[i])
            
sum = 0
        
        # traverse through each column
for i in range(len(grid[0])):
    maxVal = 0
    
    # traverse through each row
    for j in range(len(grid)):
        
        # get max from each row
        maxVal = max(grid[j][i], maxVal)
        
    sum += maxVal
print(sum)