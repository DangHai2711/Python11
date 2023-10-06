from sinh_vien import SinhVien
from datetime import datetime

class SinhVienChinhQuy(SinhVien):
    def __inti__(self, maSo: int, hoTen: str, ngaySinh: datetime, diemRL: int) ->None:
        super().__inti__(maSo,hoTen,ngaySinh)
        self.diemRL = diemRL

    def __str__(self) -> str:
        return super().__str__() + f"\t{self.diemRL}"
    