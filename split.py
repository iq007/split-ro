def split(ro: str) -> (str, str):
    a = [letter for letter in ro if letter.isalpha()]
    b = [digit for digit in ro if digit.isdigit()]
    return "".join(a), "".join(b)


def split2(ro: str) -> (str, str):
    a = filter(str.isalpha, list(ro))
    b = filter(str.isdigit, list(ro))
    return "".join(a), "".join(b)
