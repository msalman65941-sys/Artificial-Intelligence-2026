def find_duplicates(files):
    seen = set()
    duplicates = set()

    for file in files:
        if file in seen:
            duplicates.add(file)
        else:
            seen.add(file)

    return duplicates


files = ["abc.py", "data.txt", "abc.py", "report.pdf", "data.txt"]

duplicates = find_duplicates(files)

print("Duplicate Files:")
for file in duplicates:
    print(file)