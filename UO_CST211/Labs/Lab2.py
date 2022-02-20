"""
CIS 211
Lab 2 April 7th 2021
Going over classes and objects
Author: Tyler Taormina

"""


class Fraction:

    def __init__(self, num: int, den: int ):
        """Numerator and denominator must > 0."""
        self.num = num
        self.den = den
        assert num >= 0 and den > 0, f"Denominator cannot be 0 and Numerator cannot be negative"
        self.simplify()

    def __str__(self) -> str:
        """Reformats the integers into strings with the numerator and denominator seperated by a '/'"""
        return f"{self.num}/{self.den}"

    def __repr__(self):
        return f"Fraction({self.num}/{self.den})"

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return f"{new_num}/{new_den}"

    def __add__(self, other):
        new_den = self.den * other.den
        new_num = self.num * other.den + self.den * other.num
        return f"{new_num}/{new_den}"

    def simplify(self):
        GCD = gcd(self.num, self.den)
        self.num = self.num / GCD
        self.den = self.den / GCD



def gcd(a, b) -> int:
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def main():
    f1 = Fraction(3, 4)
    print(f1, 'F1')
    f2 = Fraction(2, 5)
    print(f1 + f2, 'add')
    print(f1 * f2, 'mul')


if __name__ == '__main__':
    main()


























