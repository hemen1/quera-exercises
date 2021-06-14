def calculator(n: int, m: int, li: list):
    results = []
    for i in range(n // m + 1):
        results.append(sum(li[i * m:(i + 1) * m]) * ((-1) ** i))
    return sum(results)
