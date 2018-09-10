#!/usr/bin/env python3
import math
import decimal
print('Введіть дохід працівника')

money = decimal.Decimal(input())


physical = decimal.Decimal(money) * decimal.Decimal('18.5') / decimal.Decimal('100')
military =  decimal.Decimal(money) * decimal.Decimal('1.5') / decimal.Decimal('100')

print('Фізичний податок {0}, Військовий податок {1}'.format(physical, military))