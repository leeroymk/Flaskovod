def detect_lucky(x: int) -> bool:
    return sum(map(int, str(x)[:3])) == sum(map(int, str(x)[3:]))


print(detect_lucky(985778))
