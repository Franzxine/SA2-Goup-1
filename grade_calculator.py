  def compute_quarter_grades(q1, t_q2, t_q3, t_q4):
    Q1 = q1
    Q2 = (Q1 + 2 * t_q2) / 3
    Q3 = (Q2 + 2 * t_q3) / 3
    Q4 = (Q3 + 2 * t_q4) / 3
    return Q1, Q2, Q3, Q4


def get_adjective(grade):
    if 96 <= grade <= 100:
 return "EXCELLENT", 1.00
    elif 90 <= grade <= 95.99:
        return "VERY GOOD", 1.25
    elif 84 <= grade <= 89.99:
        return "VERY GOOD", 1.50
    elif 78 <= grade <= 83.99:
        return "GOOD", 1.75
    elif 72 <= grade <= 77.99:
        return "GOOD", 2.00
    elif 66 <= grade <= 71.99:
        return "SATISFACTORY", 2.25
    elif 60 <= grade <= 65.99:
        return "SATISFACTORY", 2.50
    elif 55 <= grade <= 59.99:
        return "FAIR", 2.75
    elif 50 <= grade <= 54.99:
        return "FAIR", 3.00
    elif 40 <= grade <= 49.99:
        return "FAILED ON CONDITION", 4.00
    else:
        return "FAILED", 5.00


# ==== PROGRAM START ====
print("Hello Scholar! Welcome to the PSHS Grade Calculator.\n")

q1 = float(input("Enter Q1 Grade: "))
t_q2 = float(input("Enter Tentative Q2: "))
t_q3 = float(input("Enter Tentative Q3: "))
t_q4 = float(input("Enter Tentative Q4: "))

Q1, Q2, Q3, Q4 = compute_quarter_grades(q1, t_q2, t_q3, t_q4)
adjective, equivalent = get_adjective(Q4)

print("\n=== RESULTS ===")
print(f"Q1: {Q1:.2f}")
print(f"Q2: {Q2:.2f}")
print(f"Q3: {Q3:.2f}")
print(f"Final Grade (Q4): {Q4:.2f}")
print(f"Equivalent: {equivalent}")
print(f"Adjectival Rating: {adjective}")
