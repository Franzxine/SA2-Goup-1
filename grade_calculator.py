  def compute_quarter_grades(q1, t_q2, t_q3, t_q4):
    Q1 = q1
    Q2 = (Q1 + 2 * t_q2) / 3
    Q3 = (Q2 + 2 * t_q3) / 3
    Q4 = (Q3 + 2 * t_q4) / 3
    return Q1, Q2, Q3, Q4


def get_adjective(grade):
    if 96 <= grade <= 100:
