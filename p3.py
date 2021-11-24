#p_3. Write a function that takes an integer minutes and converts it to seconds.

print("Welcome to time convertor calculator")
minutes=int(input('How many minutes do you want to be converted to second? '))

def func1(minutes):
    return minutes*60
func1(minutes)

print(f'Your minutes is equal to {func1(minutes)} seconds')
print('Thank you')