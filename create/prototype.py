import copy
from collections import OrderedDict


class Book:
    def __init__(self, name, authors, price, **rest):
        """rest的例子有: 出版商、长度、 标签、出版日期"""
        self.name = name
        self.authors = authors
        self.price = price  # 单位为美元
        self.__dict__.update(rest)

    def __str__(self):
        my_list = []

        ordered = OrderedDict(sorted(self.__dict__.items()))
        for key, value in ordered.items():
            my_list.append(f"{key}: {value}")
            if key == "price":
                my_list.append("$")
        my_list.append("\n")
        return "".join(my_list)


class Prototype:
    def __init__(self):
        self.objects = {}

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        self.objects.pop(identifier, None)

    def clone(self, identifier, **attr):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError("Incorrect object identifier: {}".format(identifier))
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj


def main():
    b1 = Book(
        "The C Programming Language",
        ("Brian W. Kernighan", "Dennis M.Ritchie"),
        price=118,
        publisher="Prentice Hall",
        length=228,
        publication_date="1978-02-22",
        tags=("C", "programming", "algorithms", "data structures"),
    )
    prototype = Prototype()
    cid = "k&r-first"
    prototype.register(cid, b1)
    b2 = prototype.clone(
        cid,
        name="The C Programming Language(ANSI)",
        price=48.99,
        length=274,
        publication_date="1988-04-01",
        edition=2,
    )
    for i in (b1, b2):
        print(i)
    print("ID b1 : {} != ID b2 : {}".format(id(b1), id(b2)))


if __name__ == "__main__":
    main()
