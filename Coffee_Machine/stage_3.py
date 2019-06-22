"""
Project: Coffee Machine in Python
Stage #3: Enough coffee for everyone

Description
A real coffee machine never has an infinite supply of water, milk, or coffee beans.
And if you input a really big number,
it’s almost certain that a real coffee machine wouldn't have the supplies needed to make all that coffee.

In this stage, you need to improve the previous program.
Now you need to input amounts of water, milk, and coffee beans that your coffee machine has at the moment.

If the coffee machine has enough supplies to make the specified amount of coffee,
the program should print "Yes, I can make that amount of coffee". If the coffee machine can make more than that,
the program should output "Yes, I can make that amount of coffee (and even N more than that)",
where N is the number of additional cups of coffee that the coffee machine can make.
If the amount of resources is not enough to make the specified amount of coffee,
the program should output "No, I can make only N cups of coffee".

Like in the previous stage, the coffee machine needs 200 ml of water, 50 ml of milk,
and 15 g of coffee beans to make one cup of coffee.

Output example
The program should firstly request for a water, then milk, then beans, then amount of cups.

Write how many ml of water the coffee machine has: 300
Write how many ml of milk the coffee machine has: 65
Write how many grams of coffee beans the coffee machine has: 100
Write how many cups of coffee you will need: 1
Yes, I can make that amount of coffee

Write how many ml of water the coffee machine has: 500
Write how many ml of milk the coffee machine has: 250
Write how many grams of coffee beans the coffee machine has: 200
Write how many cups of coffee you will need: 10
No, I can make only 2 cups of coffee

Write how many ml of water the coffee machine has: 1550
Write how many ml of milk the coffee machine has: 299
Write how many grams of coffee beans the coffee machine has: 300
Write how many cups of coffee you will need: 3
Yes, I can make that amount of coffee (and even 2 more than that)

Write how many ml of water the coffee machine has: 0
Write how many ml of milk the coffee machine has: 0
Write how many grams of coffee beans the coffee machine has: 0
Write how many cups of coffee you will need: 1
No, I can make only 0 cups of coffee

Write how many ml of water the coffee machine has: 0
Write how many ml of milk the coffee machine has: 0
Write how many grams of coffee beans the coffee machine has: 0
Write how many cups of coffee you will need: 0
Yes, I can make that amount of coffee

Write how many ml of water the coffee machine has: 200
Write how many ml of milk the coffee machine has: 50
Write how many grams of coffee beans the coffee machine has: 15
Write how many cups of coffee you will need: 0
Yes, I can make that amount of coffee (and even 1 more than that)
"""


WATER_PORTION_SIZE = 200
MILK_PORTION_SIZE = 50
COFFEE_BEANS_PORTION_SIZE = 15


if __name__ == '__main__':
    current_water = int(input('Write how many ml of water the coffee machine has:'))
    current_milk = int(input('Write how many ml of milk the coffee machine has:'))
    current_coffee_beans = int(input('Write how many grams of coffee beans the coffee machine has:'))
    current_n_cups = int(input('Write how many cups of coffee you will need:'))

    possible_n_cups = min((
        current_water // WATER_PORTION_SIZE,
        current_milk // MILK_PORTION_SIZE,
        current_coffee_beans // COFFEE_BEANS_PORTION_SIZE,
    ))

    if current_n_cups == possible_n_cups:
        print('Yes, I can make that amount of coffee')
    elif possible_n_cups > current_n_cups:
        print(f'Yes, I can make that amount of coffee (and even {possible_n_cups - current_n_cups} more than that)')
    else:
        print(f'No, I can make only {possible_n_cups} cups of coffee')
