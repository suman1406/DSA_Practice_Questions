def assign_spears(soldier_heights, spear_heights):
    # Step 1: Sort both the soldiers' and spears' heights
    soldier_heights.sort()
    spear_heights.sort()

    # Step 2: Calculate the total minimum difference
    total_difference = 0
    for i in range(len(soldier_heights)):
        total_difference += abs(soldier_heights[i] - spear_heights[i])

    return total_difference

# Example usage
soldier_heights = [170, 160, 180]
spear_heights = [175, 165, 155]

# Call the function
result = assign_spears(soldier_heights, spear_heights)
print("Minimum total difference:", result)