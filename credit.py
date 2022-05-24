from function import asignar

cards = ['5100010000000015',
         '378282246310005',
         'foo',
         '3782-822-463-10005',
         '378282246310005',
         '6176292929',
         '4970110000000062']


def detected(card):
    return asignar(card)

for element in cards:
    
    print(detected(element))