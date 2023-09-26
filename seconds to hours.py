#this progrma show how to use return
def convert_seconds(seconds):
    hours=seconds//3600
    minutes=(seconds-hours*3600)//60
    remaining_sec=(seconds-hours*3600-minutes*60)
    return hours,minutes,remaining_sec
#convert_given_seconds_into_hrs_min_sec=convert_seconds(5000)
#print(convert_given_seconds_into_hrs_min_sec)
hours,minutes,remaining_sec=convert_seconds(5000)
print(hours,minutes,remaining_sec)