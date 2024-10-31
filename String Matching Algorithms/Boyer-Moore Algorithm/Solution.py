def boyer_moore(text, pattern):
    m, n = len(pattern), len(text)
    last = {c: -1 for c in set(pattern)}

    for i in range(m):
        last[pattern[i]] = i

    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            print(f"Pattern found at index {s}")
            s += (s + m < n) and (m - last.get(text[s + m], -1)) or 1
        else:
            s += max(last.get(text[s + m], -1) - j, 1)


# The Boyer-Moore algorithm skips sections of the text based on mismatched characters from the end of the pattern. It uses two tables:

# Bad Character Table: Determines how far to skip when a mismatch occurs.
# Good Suffix Table: Helps in cases where a partial match of the pattern is found at the end.
# This algorithm is best for longer patterns and is efficient in large texts.

# Steps:
# Preprocess: Create tables for bad character and good suffix rules.
# Start matching from the end of the pattern.
# If there’s a mismatch, use the tables to decide how far to skip.
# Example (Concept)
# If the text is ABABABCA and the pattern is ABA, the algorithm can skip more characters whenever mismatches occur based on bad character and good suffix rules.