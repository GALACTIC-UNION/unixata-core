import numpy as np

class Metrics:
    @staticmethod
    def accuracy(y_true, y_pred):
        """Calculate accuracy of predictions."""
        return np.mean(np.array(y_true) == np.array(y_pred)

    @staticmethod
    def precision(y_true, y_pred):
        """Calculate precision of predictions."""
        true_positive = np.sum((y_true == 1) & (y_pred == 1))
        false_positive = np.sum((y_true == 0) & (y_pred == 1))
        return true_positive / (true_positive + false_positive) if (true_positive + false_positive) > 0 else 0.0

    @staticmethod
    def recall(y_true, y_pred):
        """Calculate recall of predictions."""
        true_positive = np.sum((y_true == 1) & (y_pred == 1))
        false_negative = np.sum((y_true == 1) & (y_pred == 0))
        return true_positive / (true_positive + false_negative) if (true_positive + false_negative) > 0 else 0.0

    @staticmethod
    def f1_score(y_true, y_pred):
        """Calculate F1 score of predictions."""
        prec = Metrics.precision(y_true, y_pred)
        rec = Metrics.recall(y_true, y_pred)
        return 2 * (prec * rec) / (prec + rec) if (prec + rec) > 0 else 0.0

# Example usage
if __name__ == "__main__":
    y_true = [1, 0, 1, 1, 0, 1]
    y_pred = [1, 0, 0, 1, 0, 1]
    
    print("Accuracy:", Metrics.accuracy(y_true, y_pred))
    print("Precision:", Metrics.precision(y_true, y_pred))
    print("Recall:", Metrics.recall(y_true, y_pred))
    print("F1 Score:", Metrics.f1_score(y_true, y_pred))
