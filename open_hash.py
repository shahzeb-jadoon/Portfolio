# open_hash.py
# By: Shahzeb Jadoon  & Takeaki Doi

class _Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class IntDict:

    def __init__(self, size):
        self.size = size

        self.table = [_Node(i) for i in range(size)]
        self.num_elements = 0

    def __contains__(self, key):
        value = key % self.size
        current = self.table[value].next

        while current:

            if current.data == key:
                return True

            else:
                current = current.next

        return False

    def insert(self, key):
        self.num_elements += 1
        value = key % self.size
        current = self.table[value]

        while current.next:
            current = current.next
        current.next = _Node(key)

    def remove(self, key):

        if self.__contains__(key):
            value = key % self.size
            current = self.table[value]

            while current.next.data != key:
                current = current.next
            current.next = current.next.next

    def traverse(self, key):
        value = key % self.size
        current = self.table[value].next
        count = 0

        while current:

            if current.data == key:
                count += 1
                return True, count

            else:
                count += 1
                current = current.next

        return False, count

    def verify_load_factor(self, key):

        if self.__contains__(key):
            s = 1 + 0.5 * (self.num_elements / self.size)
            print("S = ", s)
            print("compare count = ", self.traverse(key)[1])

        else:
            s = self.num_elements / self.size
            print("S = ", s)
            print("compare count = ", self.traverse(key)[1])


def main():
    values = [1, 9, 6, 10, 11, 12, 14, 27]
    lst = IntDict(13)

    for value in values:
        lst.insert(value)
    print(lst.traverse(14))
    print(lst.traverse(27))
    print(lst.traverse(40))
    lst.verify_load_factor(14)
    lst.verify_load_factor(40)


if __name__ == "__main__":
    main()