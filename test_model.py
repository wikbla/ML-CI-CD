import numpy as np
from model import train_and_predict, get_accuracy

def test_predictions_not_none():
    """
    Test 1: Sprawdza, czy otrzymujemy jakąkolwiek predykcję.
    """
    preds, _ = train_and_predict()
    assert preds is not None, "Predictions should not be None."

def test_predictions_length():
    """
    Test 2: Sprawdza, czy długość listy predykcji jest większa od 0 i czy odpowiada przewidywanej liczbie próbek testowych.
    """
    preds, y_test = train_and_predict()
    assert len(preds) > 0, "Predictions list should not be empty."
    assert len(preds) == len(y_test), "Length of predictions should match length of test labels."

def test_predictions_value_range():
    """
    Test 3: Sprawdza, czy wartości w predykcjach mieszczą się w spodziewanym zakresie (0, 1, 2).
    """
    preds, _ = train_and_predict()
    valid_classes = {0, 1, 2}
    assert all(p in valid_classes for p in preds), "Predictions contain invalid class labels."

def test_model_accuracy():
    """
    Test 4: Sprawdza, czy model osiąga co najmniej 70% dokładności.
    """
    preds, y_test = train_and_predict()
    acc = get_accuracy(y_test, preds)
    assert acc >= 0.7, f"Model accuracy too low: {acc:.2f}"