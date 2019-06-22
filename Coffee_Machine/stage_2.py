"""
Project: Coffee Machine in Python
Stage #2: Machines have needs

Description
Now let's consider a case where you need a lot of coffee.
Maybe, for example, you’re hosting a party with a lot of guests.
The program should calculate how much water, coffee beans, and milk are necessary to make the specified amount of coffee.
One cup of coffee made on this coffee machine contains 200 ml of water, 50 ml of milk, and 15 g of coffee beans.

The user should input the amount of coffee he needs, in cups, for all the guests.

Of course, all this coffee is not needed right now, so at this stage, the coffee machine doesn’t actually make any coffee.

Output example
The example below shows how your output might look.

Write how many cups of coffee you will need: 25
For 25 cups of coffee you will need:
5000 ml of water
1250 ml of milk
375 g of coffee beans

Write how many cups of coffee you will need: 125
For 125 cups of coffee you will need:
25000 ml of water
6250 ml of milk
1875 g of coffee beans
"""


WATER_PORTION_SIZE = 200
MILK_PORTION_SIZE = 50
COFFEE_BEANS_PORTION_SIZE = 15

OUTPUT = '''\
For {} cups of coffee you will need:
{} ml of water
{} ml of milk
{} g of coffee beans\
'''


def prepare_output(number):
    return OUTPUT.format(
        number,
        WATER_PORTION_SIZE * number,
        MILK_PORTION_SIZE * number,
        COFFEE_BEANS_PORTION_SIZE * number,
    )


if __name__ == '__main__':
    n_cups = int(input('Write how many cups of coffee you will need:'))
    print(prepare_output(n_cups))
