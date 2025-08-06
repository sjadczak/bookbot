from collections import Counter


def word_count(contents: str) -> int:
    words = contents.split()
    return len(words)


def char_count(contents: str) -> dict[str, int]:
    cc = Counter(contents.lower())
    return dict(cc)

def sorted_char_count_list(cc: dict[str, int]) -> list[dict[str, int]]:
    rv = []
    for k, v in cc.items():
        rv.append({"char": k, "num": v})

    rv.sort(reverse=True, key=lambda x: x["num"])

    return rv

