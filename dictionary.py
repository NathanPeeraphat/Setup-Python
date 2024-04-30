book = {
    'name': 'C++',
    'price': 309,
    'page' : 414
}  #ต้องมีคู่ข้อมูลของมัน
book['price'] = 500
print(book['name'])
print(book['price'])

book['place'] = 'Chaiyaphum'    #หากเป็นข้อมูลที่ไม่มีดิกชินารี่จะเพิ่มข้อมูลใหม่ลงไป
print(book)

book.pop('place')   #ลบข้อมูล
print(book)