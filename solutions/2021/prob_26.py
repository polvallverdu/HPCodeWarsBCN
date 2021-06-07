import re


def get_popular(words: list) -> str:
    count = 0
    num = words[0]

    for word in words:
        raw_repeted = words.count(count)
        if raw_repeted > count:
            count = raw_repeted
            num = word

    return num


def solution(line: str, keyword: str):
    matches = re.findall(keyword, line)


line = input()
keyword = input()
solution(line, keyword)
