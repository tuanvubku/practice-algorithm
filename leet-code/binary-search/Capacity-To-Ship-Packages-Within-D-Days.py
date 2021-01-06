weights = [1,2,3,1,1]
D = 4
current_index = 0
next_index = 1
segment = 0
sum_ = weights[0]
K = 2
included_last_seg = False

while current_index < len(weights) - 1:
    sum_ += weights[next_index]
    if sum_ > K:
        sum_ = weights[next_index]
        segment += 1
        # Last case included
    current_index += 1
    next_index += 1    
print(segment + 1)

def can_ship_in_D_days(k, D):
    current_index = 0
    next_index = 1
    segment = 0
    sum_ = weights[0]
    while current_index < len(weights) - 1:
        sum_ += weights[next_index]
        if sum_ > k:
            sum_ = weights[next_index]
            segment += 1
            # Last case included
        current_index += 1
        next_index += 1 
    return segment + 1 <= D