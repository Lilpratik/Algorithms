def kmp_string_match(text, pattern):
    def build_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    
    lps = build_lps(pattern)
    matches = []
    i = j = 0
    
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            matches.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
                
    return matches

# Example usage
text = "ABABDABABC"
pattern = "ABABC"
print("Matches at positions:", kmp_string_match(text, pattern))


# KMP improves over the naive algorithm by avoiding redundant comparisons. It preprocesses the pattern into a table that allows it to "jump" to the correct next position when a mismatch occurs.

# Steps:
# Build the prefix table (also known as the "longest prefix suffix" or LPS array) for the pattern.
# Start matching the pattern with the text. If there’s a mismatch, use the LPS array to skip comparisons.
# Example
# Pattern: ABABC
# LPS Array for ABABC would be [0, 0, 1, 2, 0].

# Text: ABABDABABC

# Using the LPS array, if a mismatch happens, KMP uses the array to know how many characters to skip, reducing comparisons.
