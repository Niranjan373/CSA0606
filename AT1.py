import math


def T(n):
    if n == 1:
        return 1
    return T(n - 1) + math.log2(n)

print("========================================")
print(" DIGITAL LIBRARY SEARCH ENGINE")
print("========================================")
print("Recurrence Relation: T(n) = T(n-1) + log2(n)\n")

n = int(input("Enter the number of documents (n): "))

print("\nSubstitution Expansion")
print("----------------------------------------")
print("T(n) = T(n-1) + log2(n)")
print("     = T(n-2) + log2(n-1) + log2(n)")
print("     = T(n-3) + log2(n-2) + log2(n-1) + log2(n)")
print("     = ...")
print("     = T(1) + log2(2) + log2(3) + ... + log2(n)")
print("     = T(1) + log2(n!)")

result = T(n)

print("\nResult")
print("----------------------------------------")
print(f"T({n}) = {result:.4f}")

print("\nPerformance Analysis")
print("----------------------------------------")
print("As n increases, each new document adds")
print("only log2(n) additional processing time.")
print("The accumulated cost becomes log2(n!).")
print("Using Stirling's Approximation:")
print("log(n!) = Θ(n log n)")
print("Therefore,")
print("T(n) = Θ(n log n)")