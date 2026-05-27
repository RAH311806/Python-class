# Functions in AI and ML

# ML Pipeline as Functions

def load_data(file_path):
    """Load dataset from file."""

    data = []

    with open(file_path, 'r') as file:
        for line in file:
            data.append(line.strip().split(','))

    return data


def normalize(values):
    """Min-max normalization - standard ML step."""

    min_val = min(values)
    max_val = max(values)

    return [(x - min_val) / (max_val - min_val) for x in values]


def accuracy(predictions, labels):
    """Calculate accuracy of a model's predictions."""

    correct = sum(p == l for p, l in zip(predictions, labels))

    return correct / len(labels)


def train_epoch(model, data, labels):
    """Simulate training for one epoch."""

    total_loss = 0

    for x, y in zip(data, labels):

        pred = model(x)              # forward pass
        loss = (pred - y) ** 2       # simple MSE loss

        total_loss += loss

        # backpropagation and weight update would go here

    return total_loss / len(data)


# =========================
# Compose the pipeline
# =========================

raw = [23, 4, 5, 6, 7, 8, 9, 10]

# Data cleaning
clean = [v for v in raw if v > 5]

# Normalization
normalized = normalize(clean)

# Dummy predictions
predictions = [0, 1, 1]

# Actual labels
labels = [0, 1, 1]

print("Normalized:",
      [round(n, 2) for n in normalized])

print("Accuracy:",
      accuracy(predictions, labels))