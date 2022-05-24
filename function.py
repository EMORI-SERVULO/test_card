# caracteristicas validas tipo de tarjeta, longitud,
#numero de inicio en la serie
# AMEX 15  [34, 37]
# MASTERCARD 16 [51, 52, 53, 54, 55]
# VISA 13-16 [4]
# INVALID 
list_card = ['VISA', 'AMEX', 'MASTERCARD', 'INVALID']

def luhn_checksum(card_number):
  
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return True if (checksum % 10 ) ==0 else False

def asignar(card):
    card = card.replace(' ','')
    card = card.replace('-','')
    card = card.replace('/','')
    if card not in [True, False, 0, []] and card.isnumeric() == True:
        valid_card = luhn_checksum(card)
        
        if valid_card:
            tam = len(card)
            if 13 <= tam or tam <= 16:
                    if card[0] == '4':
                        return list_card[0]
                    if card[0]+card[1] in ['34', '37']:
                        return list_card[1]
                    if card[0]+card[1] in ['51', '52', '53', '54', '55']:
                        return list_card[2]
                        
        else:
            return list_card[3]
    else:
        return list_card[3]

    