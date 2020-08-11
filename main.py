import stonks
import pyttsx3
country = 'UK'
code2 = ['WTB','whitbread']
code3 = ['GSK','gee esk kay']
code4 = ['AZN','astrazeneca']
code5 =  ['FTSE100','footsie']

while True:
    price2 = str(stonks.stonks(code2[0],country,0))
    price2 = (" ".join(price2))
    price2 = price2.replace(' . ', '.')
    print(price2)
    price3 = str(stonks.stonks(code3[0],country,0))
    price3 = (" ".join(price3))
    price3 = price3.replace(' . ', '.')
    print(price3)
    price4 = str(stonks.stonks(code4[0],country,0))
    price4 = (" ".join(price4))
    price4 = price4.replace(' . ', '.')
    print(price4)
