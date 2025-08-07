# Define thresholds
low_threshold = 10
high_threshold = 20

# Number to classify
number = 15

# Classification based on thresholds
if number < low_threshold:
    classification = "Low"
elif low_threshold <= number <= high_threshold:
    classification = "Medium"
else:
    classification = "High"

print(f"The number {number} is classified as {classification}.")
