from sys import exit
from unicodedata import category


def main() -> None:
    exit_message: str = 'Exiting program...'
    while True:
        try:
            user_input: str = input('Enter a cost: ')

            if user_input == 'exit':
                print(exit_message)
                exit()

            cost: float = float(user_input[1:])

            currency_symbols: list[str] = [
                ch for ch in user_input if category(ch) == 'Sc']

            if user_input[0] in currency_symbols and len(currency_symbols) == 1:
                currency_symbol: str = currency_symbols[0]
            else:
                print('Please enter a valid cost...')
                continue

            if cost <= 0:
                print('Please enter a valid cost...')
                continue

            user_input = input('Enter a country or state tax rate: ')

            if user_input[-1] == '%':
                tax_rate: float = float(user_input[:-1])/100
            else:
                tax_rate: float = float(user_input)

            if tax_rate < 0:
                print('Invalid tax rate...')
                continue

            tax: float = round(tax_rate * cost, 2)

            total_cost: float = round(cost + tax, 2)

            print(
                f'The tax is {currency_symbol}{tax:.2f}, and the total cost with tax is {currency_symbol}{total_cost:.2f}.')

        except ValueError:
            print('Please enter valid input...')
            continue

        except KeyboardInterrupt:
            print(exit_message)
            exit()


if __name__ == '__main__':
    main()
