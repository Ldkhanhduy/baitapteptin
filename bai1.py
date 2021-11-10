'''Bài 1: Viết chương trình thực hiện các yêu cầu sau:
- Nhập một chuỗi kí tự từ bàn phím
- Nhập tên tập tin từ bàn phím
- Lưu chuỗi ký tự ở trên vào tập tin.'''
link='D:/file.txt'
ghi=input("nhap du lieu: ")
with open(link, mode='w') as f:
  f.write(ghi)
with open(link) as f:
  print(f.read())