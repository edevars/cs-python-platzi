# Obtain square root

objective = int(input('Select a number: '))
epsilon = 0.1 # Error margin
step = epsilon**2 # Distance that the algorithm travels
answer = 0.0 # Acumulative variable that increases in each iteration one step

while abs(answer**2 - objective) >= epsilon and answer <=objective:
    print(abs(answer**2 - objective), answer)
    answer += step

if abs(answer**2 - objective) >= epsilon:
    print(f'{objective} not has a square root')
else:
    print(f'The square root of {objective} is {answer}')