def find_max_consecutive_ones(nums):
    max_count = 0  # To keep track of the maximum number of consecutive 1's
    current_count = 0  # To count the current streak of consecutive 1's

    for num in nums:
        if num == 1:
            current_count += 1  # Increment the count for consecutive 1's
        else:
            max_count = max(max_count, current_count)  # Update max_count if current_count is greater
            current_count = 0  # Reset current_count since the streak of 1's was interrupted

    # Final check to update max_count in case the longest streak ends at the end of the array
    max_count = max(max_count, current_count)

    return max_count
find_max_consecutive_ones(input("nums="))