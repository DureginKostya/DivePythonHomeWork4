'''Задание 3:
Возьмите задачу о банкомате из семинара 2. Разбейте её на
отдельные операции — функции. Дополнительно сохраняйте все
операции поступления и снятия средств в список.
'''

BALANCE = 0
COUNTER = 0
RICH_LIMIT = 5_000_000
RICH_TAX = 0.1
THREE_OPERATIONS = 3
BONUS = 0.03
FRIENDERING = 50
COMMISSION_OUT_DRAW = 0.015
MIN_LIMIT = 30
MAX_LIMIT = 600

def get_money(msg: str) -> int:
    '''Ввод с клавиатуры денежной суммы'''
    return int(input(msg))

def checking_multiplicity_fiftee(money: int) -> bool:
    '''Проверка кратности денежной суммы'''
    return money % FRIENDERING == 0

def wealth_tax(action_history: list[str]) -> list[str]:
    '''Расчет налога на богатство'''
    global BALANCE
    if BALANCE > RICH_LIMIT:
        tax = BALANCE * RICH_TAX
        BALANCE -= tax
        action_history.append(f'Списан налог: -{tax:.2f}')
    return action_history

def commission_calculation(money: int) -> float:
    '''Расчет комиссии'''
    commission = money * COMMISSION_OUT_DRAW
    if commission < MIN_LIMIT:
        commission = MIN_LIMIT
    elif commission > MAX_LIMIT:
        commission = MAX_LIMIT
    return commission

def interest_calculation(action_history: list[str]) -> list[str]:
    '''Начисление процентов после каждого 3 действия'''
    global BALANCE
    global COUNTER
    if (COUNTER % THREE_OPERATIONS == 0) & (COUNTER != 0):
        credit_bonus = BALANCE * BONUS
        BALANCE += credit_bonus
        COUNTER = 0
        action_history.append(f'Зачислены проценты: +{credit_bonus:.2f}')
    return action_history

def withdraw_money(money: int, action_history: list[str]) -> list[str]:
    '''Снятие денег со счета'''
    global BALANCE
    global COUNTER
    if checking_multiplicity_fiftee(money):
        commission = commission_calculation(money)
        if money + commission < BALANCE:
            COUNTER += 1
            BALANCE -= withdraw + commission
            action_history.append(f'Снятие: -{money} (комиссия {commission:.2f})')
    return action_history

def deposit_money(money: int, action_history: list[str]) -> list[str]:
    '''Пополнение счета'''
    global BALANCE
    global COUNTER
    if checking_multiplicity_fiftee(money):
        COUNTER += 1
        BALANCE += money
        action_history.append(f'Пополнение: +{money}')
    return action_history


my_action_history = []
while True:
    action = int(input('Введите действие - 1 (пополнить), 2 (снять), 3 (выйти): '))
    my_action_history = wealth_tax(my_action_history)
    my_action_history = interest_calculation(my_action_history)
    if action == 1:
        withdraw = get_money('Введите сумму пополнения счета (кратна 50): ')
        my_action_history = deposit_money(withdraw, my_action_history)
    elif action == 2:
        withdraw = get_money('Введите сумму снятия со счета (кратна 50): ')
        my_action_history = withdraw_money(withdraw, my_action_history)
    else:
        break
    print(f'Сумма на счете: {BALANCE:.2f}')
    print('------------------')
    print('История операций:')
    print(*my_action_history, sep='\n')
