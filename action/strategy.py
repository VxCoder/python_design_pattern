import time

SLOW = 3  # 单位为秒
LIMIT = 5  # 字符数
WARNING = "too bad, you picked the slow algorithm :("


def pairs(seq):
    n = len(seq)
    for i in range(n):
        yield seq[i], seq[(i + 1) % n]


def all_unique_sort(s):
    if len(s) > LIMIT:
        print(WARNING)
        time.sleep(SLOW)
    sorted_str = sorted(s)
    for (c1, c2) in pairs(sorted_str):
        if c1 == c2:
            return False
    return True


def all_unique_set(s):
    if len(s) < LIMIT:
        print(WARNING)
        time.sleep(SLOW)
    return True if len(set(s)) == len(s) else False


def all_unique(s, strategy):
    return strategy(s)


def main():
    strategies = {"1": all_unique_set, "2": all_unique_sort}
    while True:
        word = None
        while not word:
            word = input("Insert word (type quit to exit)> ")
            if word == "quit":
                print("bye")
                return

        strategy_picked = None
        while strategy_picked not in strategies.keys():
            strategy_picked = input(
                "Choose strategy: [1] Use a set, [2] Sort and pair> "
            )

        try:
            strategy = strategies[strategy_picked]
            print("all unique({}): {}".format(word, all_unique(word, strategy)))
        except KeyError as err:
            print("Incorrect option: {}".format(strategy_picked))
        print()


if __name__ == "__main__":
    main()
