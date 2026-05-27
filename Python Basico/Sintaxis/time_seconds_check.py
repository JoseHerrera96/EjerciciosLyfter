TIME_LIMIT = 600  # 10 minutes in seconds

user_time = int(input("Enter a time in seconds: "))

if user_time < TIME_LIMIT:
    missing = TIME_LIMIT - user_time
    print(missing)
elif user_time == TIME_LIMIT:
    print("Equal")
else:
    print("Greater")
