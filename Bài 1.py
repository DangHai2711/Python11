from datetime import datetime
class SinhVien:
    truong = "Đại học Đà Lạt"

    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self.__maSo = maSo
        self.__hoTen = hoTen
        self.__nagySinh = ngaySinh
    
    @property
    def maSo(self):
        return self.__maSo
    
    @maSo.setter
    def maSo(self, maso):
        if self.laMaSoHopLe(maso):
            self.__maSo = maso

    @staticmethod 
    def laMaSoHopLe(maso: int):
            return len(str(maso)) == 7

    @classmethod
    def doiTenTruong(self, tenmoi):
        self.truong = tenmoi

    def __str__(self) -> str:
        return f"{self.maSo}\t{self.__hoTen}\t{self.__nagySinh}"

    def xuat(self):
        print(f"{self.maSo}\t{self.__hoTen}\t{self.__nagySinh}")

class DanhSachSv:
    def __init__(self) -> None:
        self.dssv = []
    
    def themSinhVien(self, sv: SinhVien):
        self.dssv.append(sv)
    
    def xuat(self):
        for sv in self.dssv:
            print(sv)

    def timSvTheoMssv(self, mssv: int):
        return [sv for sv in self.dssv if sv.mssv == mssv]
    
    def timVTSvTheoMssv(self, mssv: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].mssv == mssv:
                return i
            return -1

    def xoaSvTheoMssv(self, mssv : int) -> bool:
        vt = self.timVTSvTheoMssv(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else: 
            return False

    def timSvTheoTen(self, ten: str):
        return [sv for sv in self.dssv if sv.hoTen == ten]

    # def timSvTruocNgay(self. ngay: datetime):
    #     pass

    # đọc file txt

    # f = open("demofile.txt", "r")
    # print(f.readline())
    # f.close()

    #sắp xếp tăng/giảm theo tên
    def sortByName(self):
        self.dssv.sort(reverse=False)

    def sortByName(self):
        self.dssv.sort(reverse=True)
