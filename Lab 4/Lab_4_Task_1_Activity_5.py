late_days = [0, 3, 5, 0, 2, 7]

total_fine = 0
late_users = 0

for days in late_days:
    if days > 0:
        total_fine = total_fine + (days * 10)
        late_users = late_users + 1

print("Total Fine: Rs.", total_fine)
print("Users Returned Late:", late_users)