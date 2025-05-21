import math

def dot_product(vec1, vec2):
    return sum(v1 * v2 for v1, v2 in zip(vec1, vec2))

def norm(vec):
    return math.sqrt(sum(v * v for v in vec))

def cosine_distance(vec1, vec2): # 0 si deux vecteurs identique, 1.0 = distance maximale.
    dp = dot_product(vec1, vec2)
    norm1 = norm(vec1)
    norm2 = norm(vec2)
    if norm1 == 0 or norm2 == 0:
        return 1.0  # distance maximale si un vecteur est nul
    cosine_similarity = dp / (norm1 * norm2)
    return 1 - cosine_similarity  # distance cosinus