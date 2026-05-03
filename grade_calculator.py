def compute_tentative(formative, summative):
    return (0.3 * formative) + (0.7 * summative)


def compute_quarter_grades(q1, t_q2, t_q3, t_q4):
    Q1 = q1
    Q2 = (Q1 + 2 * t_q2) / 3
    Q3 = (Q2 + 2 * t_q3) / 3
    Q4 = (Q3 + 2 * t_q4) / 3
    return Q1, Q2, Q3, Q4


def get_adjective(grade):
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


# ==== START ====
print("Hello Scholar! Welcome to the PSHS Grade Calculator.\n")

q1 = float(input("Enter Q1 Grade: "))

print("\n--- Q2 Scores ---")
f2 = float(input("Formative: "))
s2 = float(input("Summative: "))
t_q2 = compute_tentative(f2, s2)

print("\n--- Q3 Scores ---")
f3 = float(input("Formative: "))
s3 = float(input("Summative: "))
t_q3 = compute_tentative(f3, s3)

print("\n--- Q4 Scores ---")
f4 = float(input("Formative: "))
s4 = float(input("Summative: "))
t_q4 = compute_tentative(f4, s4)

Q1, Q2, Q3, Q4 = compute_quarter_grades(q1, t_q2, t_q3, t_q4)
adjective = get_adjective(Q4)

print("\n=== RESULTS ===")
print(f"Q1: {Q1:.2f}")
print(f"Q2: {Q2:.2f}")
print(f"Q3: {Q3:.2f}")
print(f"Final Grade (Q4): {Q4:.2f}")
print(f"Adjectival Rating: {adjective}")
