'''Bài 2: Viết chương trình thực hiện các yêu cầu sau:
- Nhập tên tập tin từ bàn phím
- Đọc nội dung tập tin và in ra màn hình'''
ten=input("NHap ten tạp tin: ")
f=open(ten, 'r')
with open(ten, mode='r') as f:
    print(f.read())
