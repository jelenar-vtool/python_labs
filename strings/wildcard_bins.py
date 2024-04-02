def generate_wildcard_bins(num_bins):
    """
    Generate wildcard bins for the specified number of bins.
    """
    bins = []
    for i in range(1, num_bins + 1):
        wildcard = "?" * (8 - i) + "1" + "?" * (i - 1)
        bins.append(f"wildcard bins {i} = {{8'b{wildcard}}};")
    return bins

# Number of bins
num_bins = 8

# Generate wildcard bins
bins = generate_wildcard_bins(num_bins)

# Print the wildcard bins
for bin in bins:
    print(bin)
