iban = 'TR12345678901234567890123456'

test= iban.split('TR')
print(test[1])
print(len(test[1]))
print('oldu',len(iban.split('TR')[1]))
print(type(iban.split('TR')[1]))
if iban.startswith('TR') and len(test[1]) == 26:
    print('true')