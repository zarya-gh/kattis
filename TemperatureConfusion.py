# https://open.kattis.com/problems/temperatureconfusion
import math


def solve(f: str):
    # -f_0/f_1
    f_0, f_1 = [int(v) for v in f.split('/')]
    c_a = 5 * (f_0 - 32 * f_1)
    c_b = 9 * f_1
    _gcd = math.gcd(abs(c_a), c_b)
    return f'{c_a//_gcd}/{c_b//_gcd}'


assert (solve('32/1') == '0/1'), solve('32/1')

print(solve(input()))
