'''Bài 5: Viết chương trình thực các yêu cầu sau:
- Sinh ngẫu nhiên 1 danh sách gồm 1000 số nguyên trong khoảng từ [-1000, 1000]
- Nhập tên tập tin từ bàn phím
- Ghi danh sách trên vào tập tin theo quy tắc:
o 10 số trên một hàng
o Các số phân tách nhau bởi dấu phẩy (,)
- Đọc nội dung tập tin ở trên và in ra màn hình theo quy tắc:
o 10 số trên một hàng
o Các số phan tách nhau bởi dấu tab.'''

import random
danhsach=[]
i=random.choices(range(-1000, 1001), k=1000)
for u in i:
    danhsach.append(u)
for i in range(len(danhsach)):
    danhsach[i]=str(danhsach[i])
ten=input("nhap ten tap tin: ")
f=open(ten, 'w')
tam=[]
for i in range(0,10):
    tam.append(i)
for i in range(0,100):
    for j in range(0,10):
        tam[j]=str(danhsach[i*10+j])
    f.write(",".join(tam)+"\n")
f.close()
with open(ten, mode='r') as f:
    print(f.read())