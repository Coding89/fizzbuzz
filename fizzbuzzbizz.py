#The classic fizzbuzz game with a twist
def fizz_buzz_bizz(x):
    for i in range(1, x+1):
        if i % 3 == 0 and i % 5 == 0 and i % 6 == 0:
            print("Fizzbuzzbizz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 6 == 0:
            print("Bizz")
        else: 
            print(i)
fizz_buzz_bizz(100) 