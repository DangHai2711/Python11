from sinh_vien import SinhVien
from datetime import datetime

class SinhVienPhiCQ(SinhVien):
    def __inti__(self,maSo: int, hoTen: str, ngaySinh: datetime, trinhdo: str, tgdt: int ) ->None:
        super().__inti__(maSo,hoTen,ngaySinh)
        self.thoiGianDaoTao = tgdt
        self.trinhDo = trinhdo

    def __str__(self) -> str:
        return super().__str__() + f"\t{self.trinhDo}\t{self.thoiGianDaoTao}"
    