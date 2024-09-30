# A native Australian named Anatjari wishes to cross a desert carrying only a single water bottle. He has a map that marks all the watering holes along the way.
# Assuming he can walk k miles on one bottle of water, design an efficient algorithm for determining where Anatjari should refill his bottle in order to make as
# few stops as possible. Argue why your algorithm is correct

def min_refill(n, k, watering_holes):
    refills = []
    i = 0 # Starting distance
    
    # Start from the initial position (mile 0) and go up to the destination
    while i < n:
        j = i
        
        # Try to move as far as possible within range 'k'
        while i < n and watering_holes[i] - watering_holes[j] <= k:
            i += 1
        
        # If no progress was made, it's impossible to proceed
        if i == j:
            return "No Solution"
        
        # If we haven't reached the destination, record the last watering hole where we refill
        if i < n:
            refills.append(watering_holes[i-1])
    
    return refills