import locale
from sys import exit

def main() -> None:
    locale.setlocale(locale.LC_ALL, '')
    currency_symbol = locale.localeconv()['currency_symbol']
    while True:
        try:
            user_input = input('Enter a cost: ')

            if user_input == 'exit':
                print('Thanks for trying my program!')
                exit()

            cost = float(user_input[1:])

            if cost <= 0:
                print('Invalid cost...')
                continue

            user_input = input('Enter a country or state tax rate: ')

            if user_input[-1] == '%':
                tax_rate = float(user_input[:-1])/100
            else:
                tax_rate = float(user_input)

            if tax_rate < 0:
                print('Invalid tax rate...')
                continue

            tax = round(tax_rate * cost, 2)

            total_cost = round(cost + tax, 2)

            print(
                f'The tax is {currency_symbol}{tax:.2f}, and the total cost with tax is {currency_symbol}{total_cost:.2f}.')
        except ValueError:
            print('Invalid input...')
            continue
        except KeyboardInterrupt:
            print('Exiting...')
            exit()


if __name__ == '__main__':
    main()
