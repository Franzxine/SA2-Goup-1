def compute_tentative(formative, summative):
    # Compute tentative grade using weights:
    #30 formative + 70% summative
    return (0.3 * formative) + (0.7 * summative)


def compute_quarter_grades(q1, t_q2, t_q3, t_q4):
    # Apply formulas  for quarterly grades
    Q1 = q1
    Q2 = (Q1 + 2 * t_q2) / 3
    Q3 = (Q2 + 2 * t_q3) / 3
    Q4 = (Q3 + 2 * t_q4) / 3 # Final grade
    return Q1, Q2, Q3, Q4


def get_adjective(grade):
    # Determine adjectival rating based on final grade
    if 96 <= grade <= 100:
        return "EXCELLENT"
    elif 90 <= grade:
        return "VERY GOOD"
    elif 84 <= grade:
        return "VERY GOOD"
    elif 78 <= grade:
        return "GOOD"
    elif 72 <= grade:
        return "GOOD"
    elif 66 <= grade:
        return "SATISFACTORY"
    elif 60 <= grade:
        return "SATISFACTORY"
    elif 55 <= grade:
        return "FAIR"
    elif 50 <= grade:
        return "FAIR"
    elif 40 <= grade:
        return "FAILED ON CONDITION"
    else:
        return "FAILED"


# ==== PROGRAM START ====
print("Hello Scholar! Welcome to the PSHS Grade Calculator.\n")

# Input for first quarter (already final)
q1 = float(input("Enter Q1 Grade: "))

# Input and compute tentative grade for Q2
print("\n--- Q2 Scores ---")
f2 = float(input("Formative: "))
s2 = float(input("Summative: "))
t_q2 = compute_tentative(f2, s2)

# Input and compute tentative grade for Q3
print("\n--- Q3 Scores ---")
f3 = float(input("Formative: "))
s3 = float(input("Summative: "))
t_q3 = compute_tentative(f3, s3)

# Input and compute tentative grade for Q4
print("\n--- Q4 Scores ---")
f4 = float(input("Formative: "))
s4 = float(input("Summative: "))
t_q4 = compute_tentative(f4, s4)

# Compute final quarterly grades
Q1, Q2, Q3, Q4 = compute_quarter_grades(q1, t_q2, t_q3, t_q4)

# Get adjectival rating based on final grade
adjective = get_adjective(Q4)

# Display results
print("\n=== RESULTS ===")
print(f"Q1: {Q1:.2f}")
print(f"Q2: {Q2:.2f}")
print(f"Q3: {Q3:.2f}")
print(f"Final Grade (Q4): {Q4:.2f}")
print(f"Adjectival Rating: {adjective}")
