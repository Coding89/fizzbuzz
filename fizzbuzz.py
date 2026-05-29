def fizz_buzz(x):
    for i in range(1, x+1):
        if i % 5 == 0 and i % 10 == 0:
            print("Fizzbuzz")
        elif i % 5 == 0:
            print("Fizz")
        elif i % 10 == 0:
            print("Buzz")
        else: 
            print(i)
fizz_buzz(100) 