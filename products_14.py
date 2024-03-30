import os


# 讀取檔案
products = []
if os.path.isfile('products.csv'):
    print('I got it')
    with open('products.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:                  #不想要註解放進list中
                continue                            #是跳成下一迴圈
            name, price = line.strip().split(',')   #strip是砍掉換行跟空白，split是切割，內部放條件
            products.append([name , price])
    print( products )
else:
    print('Can not find file')




# 讓使用者輸入
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

# 印出所有購買紀錄
for p in products:
    print( p[0], '的價格是', p[1])

# 寫入檔案
with open( 'products.csv', 'w', encoding='utf-8') as f: #要增加編碼，因為在開檔或寫檔時 編碼都是很重要
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')