data=[]
n=int(input("Enter the number of elements you want to store in the list: "))

for i in range(n):
    value=int(input(f"Enter the value {i+1}: "))
    data.append(value)

unique_data=[]

for value in data:
    if value not in unique_data:
        unique_data.append(value)

print("Original list:", data)
print("List with unique elements:", unique_data)