k, n, w = map(int, input().split())
# Total cost for w bananas is k + 2k + ... + wk
# This is an arithmetic series with the sum formula: (first_term + last_term) * number_of_terms / 2
total_cost = (k + k * w) * w // 2
# Calculate the remaining dollars he needs to borrow
remaining_dollar = max(0, total_cost - n)
print(remaining_dollar)