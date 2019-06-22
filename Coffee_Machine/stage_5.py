"""
Project: Coffee Machine in Python
Stage #5: On a coffee loop

Description
But just one action isn’t interesting.
Let's improve the program so it can do multiple actions, one after another.
The program should repeatedly ask what the user wants to do.
If the user types "buy", "fill" or "take", then just do what the program did in the previous step.
However, if the user wants to switch off the coffee machine, he should type "exit".
Then the program should terminate.
Also, when the user types "remaining", the program should output all the resources that the coffee machine has.

Also, do not forget that you can be out of resources for making coffee.
If the coffee machine doesn’t have enough resources to make coffee,
the program should output a message that says it can't make a cup of coffee.

And the last improvement to the program at this step—if the user types "buy" to buy a cup of coffee and then changes his mind,
he should be able to type "back" to return into the main cycle.

Output example
Your coffee machine should have the the same initial resources as in the example
(400 ml of water, 540 ml of milk, 120 g of coffee beans, 9 disposable cups, $550 in cash.

Write action (buy, fill, take, remaining, exit): remaining

The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
$550 of money

Write action (buy, fill, take, remaining, exit): buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: 2
I have enough resources, making you a coffee!

Write action (buy, fill, take, remaining, exit): remaining

The coffee machine has:
50 of water
465 of milk
100 of coffee beans
8 of disposable cups
$557 of money

Write action (buy, fill, take, remaining, exit): buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: 2
Sorry, not enough water!

Write action (buy, fill, take, remaining, exit): fill

Write how many ml of water do you want to add: 1000
Write how many ml of milk do you want to add: 0
Write how many grams of coffee beans do you want to add: 0
Write how many disposable cups of coffee do you want to add: 0

Write action (buy, fill, take, remaining, exit): remaining

The coffee machine has:
1050 of water
465 of milk
100 of coffee beans
8 of disposable cups
$557 of money

Write action (buy, fill, take, remaining, exit): buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: 2
I have enough resources, making you a coffee!

Write action (buy, fill, take, remaining, exit): remaining

The coffee machine has:
700 of water
390 of milk
80 of coffee beans
7 of disposable cups
$564 of money

Write action (buy, fill, take, remaining, exit): take

I gave you $564

Write action (buy, fill, take, remaining, exit): remaining

The coffee machine has:
700 of water
390 of milk
80 of coffee beans
7 of disposable cups
0 of money

Write action (buy, fill, take, remaining, exit): exit
"""


class CoffeeMachine:

    state_output_template = \
        '\n' \
        'The coffee machine has:\n' \
        '{} of water\n' \
        '{} of milk\n' \
        '{} of coffee beans\n' \
        '{} of disposable cups\n' \
        '${} of money'

    coffee_mapping = {
        1: (250, 0, 16, 1, 4),
        2: (350, 75, 20, 1, 7),
        3: (200, 100, 12, 1, 6),
    }

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550

    def make_coffee(self, coffee_number):
        ingredients = self.coffee_mapping[coffee_number]

        success_flag = True

        if self.water < ingredients[0]:
            success_flag = False
            print('Sorry, not enough water!')

        if self.milk < ingredients[1]:
            success_flag = False
            print('Sorry, not enough milk!')

        if self.coffee_beans < ingredients[2]:
            success_flag = False
            print('Sorry, not enough coffee beans!')

        if self.disposable_cups < ingredients[3]:
            success_flag = False
            print('Sorry, not enough disposable cups!')

        if success_flag:
            self.water -= ingredients[0]
            self.milk -= ingredients[1]
            self.coffee_beans -= ingredients[2]
            self.disposable_cups -= ingredients[3]
            self.money += ingredients[4]

        return success_flag

    def print_state(self):
        print(self.state_output_template.format(
            self.water, self.milk, self.coffee_beans, self.disposable_cups, self.money,
        ))


if __name__ == '__main__':
    coffee_machine = CoffeeMachine()

    while True:
        action = input('Write action (buy, fill, take, remaining, exit):').strip()

        if action == 'remaining':
            coffee_machine.print_state()

        elif action == 'exit':
            break

        elif action == 'take':
            print(f'I gave you ${coffee_machine.money}')
            coffee_machine.money = 0

        elif action == 'fill':
            print()
            coffee_machine.water += int(input('Write how many ml of water do you want to add:'))
            coffee_machine.milk += int(input('Write how many ml of milk do you want to add:'))
            coffee_machine.coffee_beans += int(input('Write how many grams of coffee beans do you want to add:'))
            coffee_machine.disposable_cups += int(input('Write how many disposable cups of coffee do you want to add:'))

        elif action == 'buy':
            coffee_number = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')

            if coffee_number == 'back':
                continue

            if coffee_machine.make_coffee(int(coffee_number)):
                print('I have enough resources, making you a coffee!')

        print()
