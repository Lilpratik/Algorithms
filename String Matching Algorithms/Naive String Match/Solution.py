def naive_string_match(text, patttern):
    matches=[]
    for i in range(len(text) - len(patttern) + 1):
        if text[i: i + len(patttern)] == patttern:
            matches.append(i)
    return matches
# Example usage
text = "ABABABCA"
pattern = "ABA"
print(f"Matches at positions: {naive_string_match(text, pattern)}")

# The naive algorithm checks for the pattern at every possible position in the text.

# Steps:
# Start at the beginning of the text.
# Compare each character of the pattern with the current part of the text.
# If all characters match, record the position as a match.
# Move one position forward in the text and repeat until you reach the end.
# Example
# Text: ABABABCA
# Pattern: ABA

# Compare pattern ABA with ABA in the text at position 0 (Match).
# Move one position and check ABA with BAB (No match).
# Move again and check ABA with ABA at position 2 (Match).
# Repeat until you reach the end.