def trap(height):
    n = len(height)
    trapped_water = 0
    for i in range(1, n - 1):
        left_max = max(height[:i])
        right_max = max(height[i + 1:])
        min_height = min(left_max, right_max)
        
        if min_height > height[i]:
            trapped_water += min_height - height[i]

    return trapped_water

# Example usage
height = [0,1,0,2,1,0,1,3,2,1,2,18]
print(trap(height))




