def max_worth_removed(binary_string, worth):
    removed_worth = 0
    last_char = None
    for i in range(len(binary_string)):
        if last_char is None or binary_string[i] != last_char:
            last_char = binary_string[i]
        else:
            removed_worth += worth[i]
    
    return removed_worth
binary_string = input().strip()
worth = list(map(int, input().split()))
print(max_worth_removed(binary_string, worth))