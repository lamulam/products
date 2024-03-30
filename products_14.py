
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
    p = [name, int(price)]

    products.append(p)

print('有這些商品:', products)

for p in products:
    print( p[0], '的價格是', p[1])

with open( 'products.csv', 'w', encoding='utf-8') as f: #要增加編碼，因為在開檔或寫檔時 編碼都是很重要
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')