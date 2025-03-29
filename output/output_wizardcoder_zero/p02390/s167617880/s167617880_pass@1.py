hours = S // (60*60)  # calculate hours
minutes = S % (60*60) // 60  # calculate minutes remaining after subtracting all hours from total seconds
seconds = S % 60  # calculate remaining seconds not accounted for by hours and minutes
print(f"{hours}:{minutes}:{seconds}")