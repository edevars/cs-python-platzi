objective = int(input('Please select an int number: '))
answer = 0

while answer**2 < objective:
    answer += 1

if answer**2 == objective:
    print(f'The square root of {objective} is {answer}')
else:
    print(f'{objective} not has a square root')
