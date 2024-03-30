
# 練習二維 list

products = []
while True:
    name = input('請輸入商品名稱:')
    if name == 'q' : # quit
        break
    price = input('請輸入商品價格:')
    
    '''
    p = []
    p.append(name)
    p.append(price)
    可以將其改成 
    '''
    p = [name, price]

    products.append(p)

print('有這些商品:', products)
