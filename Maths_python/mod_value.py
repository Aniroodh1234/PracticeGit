def mod_inverse(a, mod):
    a = a % mod
    for i in range(1, mod):
        if (a * i) % mod == 1:
            return i
    return None

def solve_congruence(a, b, mod):
    inv = mod_inverse(a, mod)
    if inv is None:
        return None
    return (inv * b) % mod

a = int(input("Enter the A in Ax ≡ b (mod y): "))
b = int(input("Enter the b in Ax ≡ b (mod y): "))
mod = int(input("Enter the mod in Ax ≡ b (mod y): "))

ans = solve_congruence(a, b, mod)

if ans is not None:
    print(f"The solution for {a}x ≡ {b} (mod {mod}) is x = {ans}")
else:
    print(f"No modular inverse exists for {a} (mod {mod}), so no solution.")