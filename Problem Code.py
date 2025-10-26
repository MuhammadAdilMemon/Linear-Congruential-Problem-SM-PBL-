# --------------------------------------------
# Linear Congruential Generator (LCG) in Python
# --------------------------------------------
# Formula: X_{i+1} = (a * X_i + c) % m
# Ri = X_i / m
#
# This program demonstrates the LCG method for different seed values (X0)
# using parameters a = 5, c = 3, m = 16.
# It shows the sequence of generated numbers and the cycle length.

a = 5   # Multiplier
c = 3   # Increment
m = 16  # Modulus

# Looping through different seed values
for X0 in range(1, 7):
    X = X0
    seen = []  # Store generated numbers to detect repetition
    print(f"\nSeed X0 = {X0}")
    print("i\tXi\tRi")
    i = 0
    while X not in seen:
        seen.append(X)
        Ri = X / m
        print(f"{i}\t{X}\t{Ri:.4f}")
        X = (a * X + c) % m
        i += 1
    print(f"Cycle repeats after {len(seen)} numbers.")

# --------------------------------------------
# End of Python Program
# --------------------------------------------
