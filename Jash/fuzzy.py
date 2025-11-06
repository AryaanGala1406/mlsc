# Define fuzzy sets (as dictionaries)
A = {'x1': 0.2, 'x2': 0.5, 'x3': 0.7, 'x4': 1.0}
B = {'x1': 0.6, 'x2': 0.3, 'x3': 0.9, 'x4': 0.4}

print("Set A:", A)
print("Set B:", B)

# 1️⃣ Fuzzy Union (A ∪ B) = max(A[x], B[x])
union = {x: max(A[x], B[x]) for x in A}
print("\nUnion (A ∪ B):", union)

# 2️⃣ Fuzzy Intersection (A ∩ B) = min(A[x], B[x])
intersection = {x: min(A[x], B[x]) for x in A}
print("Intersection (A ∩ B):", intersection)

# 3️⃣ Fuzzy Complement (A′) = 1 - A[x]
complement_A = {x: round(1 - A[x], 2) for x in A}
complement_B = {x: round(1 - B[x], 2) for x in B}
print("Complement of A (A′):", complement_A)
print("Complement of B (B′):", complement_B)

# 4️⃣ Fuzzy Difference (A - B) = min(A[x], 1 - B[x])
difference = {x: round(min(A[x], 1 - B[x]), 2) for x in A}
print("Difference (A - B):", difference)

# 5️⃣ Algebraic Sum = A[x] + B[x] - (A[x] * B[x])
algebraic_sum = {x: round(A[x] + B[x] - (A[x] * B[x]), 2) for x in A}
print("Algebraic Sum:", algebraic_sum)

# 6️⃣ Algebraic Product = A[x] * B[x]
algebraic_product = {x: round(A[x] * B[x], 2) for x in A}
print("Algebraic Product:", algebraic_product)

# 7️⃣ Bounded Sum = min(1, A[x] + B[x])
bounded_sum = {x: round(min(1, A[x] + B[x]), 2) for x in A}
print("Bounded Sum:", bounded_sum)

# 8️⃣ Bounded Difference = max(0, A[x] + B[x] - 1)
bounded_diff = {x: round(max(0, A[x] + B[x] - 1), 2) for x in A}
print("Bounded Difference:", bounded_diff)

import matplotlib.pyplot as plt

# Convert dictionary data to lists
elements = list(A.keys())

plt.figure(figsize=(10,6))

plt.plot(elements, list(A.values()), 'bo-', label='A')
plt.plot(elements, list(B.values()), 'ro-', label='B')
plt.plot(elements, list(union.values()), 'g--', label='Union (A ∪ B)')
plt.plot(elements, list(intersection.values()), 'm--', label='Intersection (A ∩ B)')
plt.plot(elements, list(difference.values()), 'c--', label='Difference (A - B)')
plt.plot(elements, list(algebraic_sum.values()), 'y--', label='Algebraic Sum')
plt.plot(elements, list(algebraic_product.values()), 'k--', label='Algebraic Product')
plt.plot(elements, list(bounded_sum.values()), 'b:', label='Bounded Sum')
plt.plot(elements, list(bounded_diff.values()), 'r:', label='Bounded Difference')

plt.title("Fuzzy Set Operations Visualization", fontsize=14)
plt.xlabel("Elements")
plt.ylabel("Membership Value (0 to 1)")
plt.legend()
plt.grid(True)
plt.show()