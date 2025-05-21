from Tasks_part2.Part2.task_step4 import counter

n = int(input())
reserve_emails = set(input().strip() for _ in range(n))
m = int(input())
new_email = [input().strip() for _ in range(m)]

counters = {}

for name in new_email:
    email = f"{name}@beegeek.bzz"
    if email not in reserve_emails:
        print(email)
        reserve_emails.add(email)
        counters[email] = 1
    else:
        while True:
            email_with_number = f"{name}{counters.get(name, 1)}@beegeek.bzz"
            if email_with_number not in reserve_emails:
                print(email_with_number)
                reserve_emails.add(email_with_number)
                counters[name] = counters.get(name, 1) + 1
                break
            else:
                counters[name] = counters.get(name, 1) + 1
