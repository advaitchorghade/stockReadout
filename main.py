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
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)
    engine.say(code2[1]+' - '+price2+' . '+code3[1]+' - '+price3+' . '+code4[1]+' - '+price4)
    engine.runAndWait()
# this is very inefficient if we want to do multiple stocks so we will try to improve this
