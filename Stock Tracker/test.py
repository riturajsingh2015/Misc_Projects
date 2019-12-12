import decimal
import locale

locale.setlocale(locale.LC_ALL, 'de_DE')
mystr = '217,50'
num = locale.atof(mystr, decimal.Decimal)

print('{}'.format(num))
print('{:n}'.format(num))
