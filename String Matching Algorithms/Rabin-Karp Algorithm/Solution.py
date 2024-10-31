def rabin_karp_string_match(text, pattern, prime=101):
    def create_hash(s, end):
        hash_value = 0
        for i in range(end):
            hash_value += ord(s[i]) * (prime ** i)
        return hash_value
    
    def recalculate_hash(text, old_index, new_index, old_hash, pattern_len):
        old_hash -= ord(text[old_index])
        old_hash //= prime
        old_hash += ord(text[new_index]) * (prime ** (pattern_len - 1))
        return old_hash
    
    pattern_len = len(pattern)
    text_len = len(text)
    pattern_hash = create_hash(pattern, pattern_len)
    text_hash = create_hash(text, pattern_len)
    matches = []

    for i in range(text_len - pattern_len + 1):
        if pattern_hash == text_hash:
            if text[i: i + pattern_len] == pattern:
                matches.append(i)
        if i < text_len - pattern_len:
            text_hash = recalculate_hash(text, i, i + pattern_len, text_hash, pattern_len)

    return matches

# Example usage
text = "ABABABCA"
pattern = "ABA"
print(f"Matches at positions: {rabin_karp_string_match(text, pattern)}")





# The Rabin-Karp algorithm uses hashing to find matches. It calculates a hash for the pattern and each substring of the text, comparing hash values first before checking for an exact match.

# Steps:
# Calculate the hash for the pattern.
# Calculate the hash for the first part of the text, equal in length to the pattern.
# Slide over the text, updating the hash by removing the left character and adding the next right character.
# If a hash match is found, verify by checking the actual characters.
# Example
# Text: ABABABCA
# Pattern: ABA

# Compute hashes for each substring of length 3 in the text and compare with the hash of ABA. If a hash match occurs, confirm it by comparing the actual substring.