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