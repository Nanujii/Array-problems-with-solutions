 def summary_ranges(nums):
    if not nums:
        return []
    
    # Initialize variables to store start and end of the current range
    start = end = nums[0]
    result = []
    
    # Helper function to add range to result list
    def add_range(start, end):
        if start == end:
            result.append(str(start))
        else:
            result.append(f"{start}->{end}")
    
    # Iterate through the sorted array and create summary ranges
    for num in nums[1:]:
        if num == end + 1:
            end = num
        else:
            add_range(start, end)
            start = end = num
    
    # Add the last range to the result
    add_range(start, end)
    
    return result

# Example usage
nums = [0, 1, 2, 4, 5, 7]
result = summary_ranges(nums)
print(result)  # Output: ["0->2", "4->5", "7"]
