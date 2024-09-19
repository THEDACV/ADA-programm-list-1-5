def fractional_knapsack(weights, values, capacity):
    items = sorted(zip(values, weights), key=lambda x: x[0] / x[1], reverse=True)
    total_value = 0

    for value, weight in items:
        if capacity >= weight:
            capacity -= weight
            total_value += value
        else:
            total_value += value * (capacity / weight)
            break

    return total_value

# Example usage
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print("Maximum value in knapsack:", fractional_knapsack(weights, values, capacity))