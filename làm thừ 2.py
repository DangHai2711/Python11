tu_so = int(input("nhập tu_so: "))
mau_so =int(input("nhập mau_so: "))
def rut_gon_phan_so(tu_so, mau_so):
    def tim_uoc_chung_lon_nhat(a, b):
        while b:
            a, b = b, a % b
        return a
 
    ucln = tim_uoc_chung_lon_nhat(tu_so, mau_so)
    tu_so_rut_gon = tu_so // ucln
    mau_so_rut_gon = mau_so // ucln
    return tu_so_rut_gon, mau_so_rut_gon
 

tu_so_rut_gon, mau_so_rut_gon = rut_gon_phan_so(tu_so, mau_so)
print(f"Phân số sau khi rút gọn: {tu_so_rut_gon}/{mau_so_rut_gon}")