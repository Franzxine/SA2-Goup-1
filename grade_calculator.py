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


# Start here migz
