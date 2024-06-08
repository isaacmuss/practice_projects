# Problem #1
# Ryerson letter grade

# Define de function
pct = 30

def ryerson_letter_grade(pct):

    if pct <= 49:
        return'F'
    elif pct <= 52:
        return'D-'
    elif pct <= 56:
        return'D'
    elif pct <= 59:
        return'D+'    
    elif pct <= 62:
        return'C-'
    elif pct <= 66:
        return'C'
    elif pct <= 69:
        return'C+'
    elif pct <= 72:
        return'B-'
    elif pct <= 76:
        return'B'
    elif pct <= 79:
        return'B+'
    elif pct <= 84:
        return'A-'
    elif pct <= 89:
        return'A'
    elif pct <= 100:
        return'A+'
