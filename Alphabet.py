# https://open.kattis.com/problems/alphabet

def solve(seq: str):
    max_f = 1
    f = [1 for i in range(len(seq))]
    for i in range(len(seq)):
        f[i] = 1
        for j in range(i):
            if seq[j] < seq[i]:
                f[i] = max(f[i], f[j] + 1)
        max_f = max(max_f, f[i])
    return 26 - max_f


assert (solve('xyzabcdefghijklmnopqrstuvw') == 3)

print(solve(input()))
