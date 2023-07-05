from enum import Enum


class BarcodeType(Enum):
    UPC_A = 0
    UPC_E = 1
    EAN13 = 2
    JAN13 = 3
    EAN8 = 4
    JAN8 = 5
    CODE39 = 6
    ITF = 7
    CODABAR = 8
    CODE93 = 9
    CODE128 = 10

    def to_byte(self) -> int:
        match self.value:
            case 0:
                return 0x41
            case 1:
                return 0x42
            case 2 | 3:
                return 0x43
            case 4 | 5:
                return 0x44
            case 6:
                return 0x45
            case 7:
                return 0x46
            case 8:
                return 0x47
            case 9:
                return 0x48
            case 10:
                return 0x49
        return 0x49


class BarcodeHri(Enum):
    NONE = 0
    ABOVE = 1
    BELOW = 2
    BOTH = 3


class BarcodeFont(Enum):
    A = 0
    B = 1


class Barcode:
    def __init__(self, data: str, btype: BarcodeType, hri: BarcodeHri, font: BarcodeFont, width: int, height: int):
        self.data = data
        self.btype = btype
        self.hri = hri
        self.font = font
        self.width = width
        self.height = height
