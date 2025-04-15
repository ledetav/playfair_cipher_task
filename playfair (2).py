ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # I and J merged

def clean_text(text):
    return ''.join(c for c in text.upper().replace("J", "I") if c in ALPHABET)

def create_matrix(key):
    key = clean_text(key)
    seen = set()
    matrix = []
    for c in key + ALPHABET:
        if c not in seen:
            seen.add(c)
            matrix.append(c)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def prepare_bigrams(text):
    cleaned = clean_text(text)
    i = 0
    result = []
    while i < len(cleaned):
        a = cleaned[i]
        b = cleaned[i + 1] if i + 1 < len(cleaned) else None
        if b is None:
            result.append((a, 'X'))
            i += 1
        elif a == b:
            result.append((a, 'X'))
            i += 1
        else:
            result.append((a, b))
            i += 2
    return result

def find_pos(matrix, char):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == char:
                return r, c
    return None

def encrypt_bigram(a, b, matrix):
    r1, c1 = find_pos(matrix, a)
    r2, c2 = find_pos(matrix, b)
    if r1 == r2:
        return matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
    elif c1 == c2:
        return matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
    else:
        return matrix[r1][c2] + matrix[r2][c1]

def decrypt_bigram(a, b, matrix):
    r1, c1 = find_pos(matrix, a)
    r2, c2 = find_pos(matrix, b)
    if r1 == r2:
        return matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
    elif c1 == c2:
        return matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
    else:
        return matrix[r1][c2] + matrix[r2][c1]

def encrypt_playfair(text, key):
    matrix = create_matrix(key)
    bigrams = prepare_bigrams(text)
    return ''.join(encrypt_bigram(a, b, matrix) for a, b in bigrams)

def decrypt_playfair(cipher, key):
    matrix = create_matrix(key)
    bigrams = [(cipher[i], cipher[i + 1]) for i in range(0, len(cipher), 2)]
    return ''.join(decrypt_bigram(a, b, matrix) for a, b in bigrams)
