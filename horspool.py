# horspool.py
# By: Shahzeb Jadoon


class make_shift_table():

    def __init__(self, pat):
        self.m = len(pat)
        
        self.table = {i:self.m for i in pat}

        i = 0
        for j in pat[:-1]:
            self.table[j] = self.m - 1 - i
            i += 1

    def get(self, letter):

        if letter in self.table:
            return self.table[letter]

        else:
            return self.m


def horspool(pat, text):
    table = make_shift_table(pat)
    m = len(pat)
    n = len(text)
    i = 0

    while i < n - m + 1:

        if text[i:i + m] == pat:
            return i

        i += table.get(text[i + m - 1])

    return -1


def main():
    pat = "zelle"
    text = "yes,_we_have_no_gazelles_today."
    print("The pattern is '" + pat + "'\n")
    print("The text is\n'" + text + "'\n")
    print("The index where the pattern is located is\n", horspool(pat, text))


if __name__ == "__main__":
    main()
