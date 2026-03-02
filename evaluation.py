import random
import numpy as np
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

random.seed(42)
y_true=[random.randint(0,1) for _ in range(10)]
y_pred=[random.randint(0,1) for _ in range(10)]
print("Human Labels:",y_true)
print("Model Predictions:",y_pred)

def evaluate_predictions(y_true, y_pred):
    return {
        "accuracy": round(accuracy_score(y_true, y_pred), 2),
        "precision": round(precision_score(y_true, y_pred), 2),
        "recall": round(recall_score(y_true, y_pred), 2),
        "f1": round(f1_score(y_true, y_pred), 2)
    }

metrics = evaluate_predictions(y_true, y_pred)
print("Classification Metrics:", metrics)

scores = [random.random() for _ in range(10)]
ranked = sorted(zip(scores, y_true), reverse=True)
sorted_labels = [label for _, label in ranked]

def precision_at_k(sorted_labels, k):
    return round(sum(sorted_labels[:k]) / k, 2)

p_at_5 = precision_at_k(sorted_labels, 5)

print("Precision@5:", p_at_5)


random.seed(42)

# Simulate 10 candidates
num_candidates = 10

candidates = []

for i in range(num_candidates):
    group = random.choice(["A", "B"])  # A = Tier-1, B = Tier-3
    
    # Simulate final model score between 0 and 1
    score = round(random.uniform(0.4, 0.9), 2)
    
    candidates.append({
        "id": i + 1,
        "group": group,
        "score": score
    })

#  Selection threshold
threshold = 0.65

#  Compute group metrics
group_A_scores = [c["score"] for c in candidates if c["group"] == "A"]
group_B_scores = [c["score"] for c in candidates if c["group"] == "B"]

avg_A = round(np.mean(group_A_scores), 2) if group_A_scores else 0
avg_B = round(np.mean(group_B_scores), 2) if group_B_scores else 0

# Selection rate = % above threshold
sel_A = sum(1 for c in candidates if c["group"] == "A" and c["score"] >= threshold)
sel_B = sum(1 for c in candidates if c["group"] == "B" and c["score"] >= threshold)

total_A = sum(1 for c in candidates if c["group"] == "A")
total_B = sum(1 for c in candidates if c["group"] == "B")

selection_rate_A = round(sel_A / total_A, 2) if total_A else 0
selection_rate_B = round(sel_B / total_B, 2) if total_B else 0

print("Candidates:", candidates)
print("\nAvg Score Group A:", avg_A)
print("Avg Score Group B:", avg_B)
print("Selection Rate Group A:", selection_rate_A)
print("Selection Rate Group B:", selection_rate_B)