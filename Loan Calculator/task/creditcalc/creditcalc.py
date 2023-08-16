import argparse
from math import ceil
from math import log
from math import floor


def calc_annuity(interest, principal=0, payment=0, periods=0):
    rate = interest / (12 * 100)
    if not periods:
        periods_finite = ceil(log(payment / (payment - rate * principal), 1 + rate))
        print('You need',
              f'{periods_finite} months' if periods_finite < 12
              else (f'{int(periods_finite // 12)} years' if not periods_finite % 12
                    else f'{int(periods_finite // 12)} years and {ceil(periods_finite % 12)} months'),
              'to repay this loan!')
        print(f'Overpayment = {int(periods_finite * payment - principal)}')
    if not payment:
        payment_finite = principal * rate * pow(1 + rate, periods) / (pow(1 + rate, periods) - 1)
        print(f'Your annuity payment = {ceil(payment_finite)}!')
        print(f'Overpayment = {ceil(ceil(payment_finite)* periods - principal)}')

    if not principal:
        principal_finite = payment / (rate * pow(1 + rate, periods) / (pow(1 + rate, periods) - 1))
        print(f'Your loan principal = {floor(principal_finite)}!')
        print(f'Overpayment = {int(payment * periods - floor(principal_finite))}')


def calc_diff(interest, principal=0, periods=0):
    # Your calculation logic using the 'payment' argument
    rate = interest / (12 * 100)
    total_of_differentiated_payments = 0
    for m in range(1, periods + 1):
        differentiated_payment_of_month_m = ceil(principal/periods + rate * (principal - principal*(m-1)/periods))
        total_of_differentiated_payments += differentiated_payment_of_month_m
        print(f'Month {m}: payment is {differentiated_payment_of_month_m}')
    print(f'\nOverpayment = {int(total_of_differentiated_payments - principal)}')


def main():
    parser = argparse.ArgumentParser(description="This program is a loan calculator")
    parser.add_argument("--type", help="Type of loan ('annuity' or 'diff')")
    parser.add_argument("--payment", type=float, help="Monthly payment amount")
    parser.add_argument("--principal", type=float, help="Used for calculations of both types of payment")
    parser.add_argument("--periods", type=int, help="denotes the number of months needed to repay the loan. "
                                                    "It's calculated based on the interest, annuity payment, "
                                                    "and principal.")
    parser.add_argument("--interest", type=float,  help="Specified without the percent sign.")

    args = parser.parse_args()
    
    # All incorrect parameters conditions 
    num_optional_args = sum(arg is not None for arg in [args.type, args.payment, args.interest, args.principal,
                                                        args.periods])
    if num_optional_args < 4:
        print("Incorrect parameters")
        return
    
    if args.type not in ['annuity', 'diff']:
        print("Incorrect parameters")
        return
    if args.type == 'diff' and args.payment is not None:
        print("Incorrect parameters")
        return
    if args.payment is not None and args.payment < 0:
        print("Incorrect parameters")
    if args.interest is None or (args.interest is not None and args.interest < 0):
        print("Incorrect parameters")
        return
    if args.principal is not None and args.principal < 0:
        print("Incorrect parameters")
        return
    
    if args.type == 'annuity':
        calc_annuity(args.interest, args.principal, args.payment, args.periods)

    if args.type == 'diff':
        calc_diff(args.interest, args.principal, args.periods)


if __name__ == "__main__":
    main()
