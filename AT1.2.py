n = int(input("Enter the number of patient records: "))

patients = []

print("\nEnter Patient IDs:")
for i in range(n):
    patient = input(f"Patient {i + 1}: ")
    patients.append(patient)

print("\nHospital Patient Record System")
print("--------------------------------")
print("Patient Records:")
print(patients)

print("\nDuplicate Records:")
found = False

for i in range(n):
    for j in range(i + 1, n):
        if patients[i] == patients[j]:
            print("Duplicate Record Found:", patients[i])
            found = True

if not found:
    print("No duplicate records found.")

print("\nComplexity Analysis")
print("--------------------")
print("Time Complexity : O(n²)")
print("Space Complexity: O(1)")