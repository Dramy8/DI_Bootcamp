import datetime

def countdown_to_birthday(birth_month, birth_day):
    now = datetime.datetime.now()
    current_year = now.year

    next_birthday = datetime.datetime(current_year, birth_month, birth_day)

    if next_birthday < now:
        next_birthday = datetime.datetime(current_year + 1, birth_month, birth_day)

    time_left = next_birthday - now

    print(f"My birthday is in {time_left.days} days, and {time_left.seconds // 3600:02}:{(time_left.seconds % 3600) // 60:02}:{time_left.seconds % 60:02}")

countdown_to_birthday(07, 04)