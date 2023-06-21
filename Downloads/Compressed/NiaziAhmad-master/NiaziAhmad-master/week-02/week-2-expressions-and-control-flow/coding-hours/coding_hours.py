# An average Green Fox attendee codes 6 hours daily
# The semester is 17 weeks long
#
# Print how many hours is spent with coding in a semester by an attendee,
# if the attendee only codes on workdays.
#
# Print the percentage of the coding hours in the semester if the average
# work hours weekly is 52
daily_coding_hours = 6
week_days = 5
week_hours = daily_coding_hours * week_days
semester_weeks = 17
print(f"Attendee hours equals to: {week_hours * semester_weeks}")
print(f"the percentage of coding hours equals to: {(week_hours / 52) * 100} %")  # 52 is weekly hours used in
# percentage formula
