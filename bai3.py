'''Bài 3: Viết chương trình thực hiện các yêu cầu sau:
- Nhập tên tập tin từ bàn phím
- Nhập một chuỗi kí tự vào từ bàn phím
- Ghi chuỗi kí tự này vào cuối tập tin ở trên'''
'''Bài 4: Viết chương trình thực hiện các yêu cầu sau:
- Đọc tập tin ở bài 3 và ghi kết quả ra màn hình'''

ten=input("NHap ten tạp tin: ")
f=open(ten, 'r')
nhap=input("Nhap chuoi ky tu: ")
with open(ten, mode='a') as f:
    f.write(nhap)
with open(ten) as f:
    print(f.read())