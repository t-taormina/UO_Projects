"""
CIS 211 Lab6
Author: Tyler Taormina
05.05.2021
BINARY NUMBER

"""


class BinaryNumber:

    def __init__(self, b: list):
        self.binary = b

    def __str__(self):
        return str(self.binary)

    def __or__(self, other) -> 'BinaryNumber':
        assert len(self.binary) == len(other.binary), "Binary of different lengths"
        new_b = []
        for i in range(len(self.binary)):
            if self.binary[i] == 1 or  other.binary[i] == 1:
                new_b.append(1)
            else:
                new_b.append(0)
        return BinaryNumber(new_b)

    def __and__(self, other) -> 'BinaryNumber':
        assert len(self.binary) == len(other.binary), "Binary of different lengths"
        new_b = []
        for i in range(len(self.binary)):
            if self.binary[i] == 0 or other.binary[i] == 0:
                new_b.append(0)
            else:
                new_b.append(1)
        return BinaryNumber(new_b)

    def left_shift(self):
        for i in range(len(self.binary) - 1):
            self.binary[i] = self.binary[i + 1]
        self.binary[len(self.binary) - 1] = 0

    def right_shift(self):
        copy_b = self.binary.copy()
        for i in range(len(self.binary) - 1):
            self.binary[i + 1] = copy_b[i]
        self.binary[0] = 0

    def extract(self, start: int, end: int):
        assert 0 <= start < len(self.binary)
        assert start < end < len(self.binary)

        mask = []
        new_start = len(self.binary) - 1 - end
        new_end = len(self.binary) - 1 - start

        for i in range(len(self.binary)):
            if new_start <= i <= new_end:
                mask.append(1)
            else:
                mask.append(0)

        mask_bin_num = BinaryNumber(mask)
        new_bin_num = self & mask_bin_num

        for _ in range(start):
            new_bin_num.right_shift()

        return new_bin_num

def main():
    bn = BinaryNumber([1, 0, 1, 0, 1])
    bn2 = BinaryNumber([1, 1, 1, 0, 0])
    print("1st binary number =", bn)
    print("2nd binary number =", bn2)
    print("AND", bn & bn2)
    print("OR", bn | bn2)
    bn.right_shift()
    print("1st number right shifted =", bn)
    bn.left_shift()
    print("1st number left shifted =", bn)

if __name__ == '__main__':
    main()
