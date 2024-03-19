# Part of case-study #2: Profitability Indicators
# Developer: Malcev A, Kolchik K.
#
import ru_local as ru
import en_local as en

lang = input('Choose language(ru/en): \n')

if lang != 'ru' and lang != 'en':
    print("Wrong language!!!")

if lang == 'ru':
    input_revenue = ru.REVENUE_INPUT
    input_cost = ru.TYPE_COST_INPUT
    input_amount = ru.AMOUNT_INPUT
    output_revenue = ru.REVENUE_OUTPUT
    output_total_cost = ru.TOTAL_COST
    output_profit = ru.PROFIT
    output_profitability = ru.PROFITABILITY
    break_word = ru.WORD_BREAK
    bad_profitability = ru.BAD_PROFITABILITY
    good_profitability = ru.GOOD_PROFITABILITY
    great_profitability = ru.GREAT_PROFITABILITY
if lang == 'en':
    input_revenue = en.REVENUE_INPUT
    input_cost = en.TYPE_COST_INPUT
    input_amount = en.AMOUNT_INPUT
    output_revenue = en.REVENUE_OUTPUT
    output_total_cost = en.TOTAL_COST
    output_profit = en.PROFIT
    output_profitability = en.PROFITABILITY
    break_word = en.WORD_BREAK
    bad_profitability = en.BAD_PROFITABILITY
    good_profitability = en.GOOD_PROFITABILITY
    great_profitability = en.GREAT_PROFITABILITY
    '''
   Main function.
   :return: None
   '''


def work_with_indicators():
    revenue = float(input(f'{input_revenue}: \n'))
    cost = {}
    while True:
        type_cost = input(f'{input_cost}: \n')
        if type_cost == f'{break_word}':
            break
        amount = float(input(f'{input_amount}{type_cost}: \n'))
        cost[type_cost] = amount
    total_cost = sum(cost.values())
    profit = revenue - total_cost
    profitability = (profit / total_cost)

    match profitability:
        case float() as quantity if quantity < 0:
            print(f'{output_profitability} = {profitability*100:.2f}%\n {bad_profitability}!')
        case float() as quantity if quantity < 1:
            print(f'{output_profitability} = {profitability*100:.2f}%\n {good_profitability}')
        case float() as quantity if quantity > 1:
            print(f'{output_profitability} = {profitability * 100:.2f}%\n {great_profitability}')
    print(f'{output_revenue} = {revenue}\n {output_total_cost} = {total_cost}\n {output_profit} = {profit}\n')

work_with_indicators()
