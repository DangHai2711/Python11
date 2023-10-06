def TrungBinh(danhsach):
    tong = sum(danhsach)
    soPhanTu = len(danhsach)
    trungBinh = tong / soPhanTu
    return trungBinh
danhsach = (4,5,8,9)
print(danhsach)
print(TrungBinh(danhsach))


