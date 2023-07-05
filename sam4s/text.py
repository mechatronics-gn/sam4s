from enum import Enum


class TextAlign(Enum):
    LEFT = 0
    CENTER = 1
    RIGHT = 2


class TextLanguage(Enum):
    EN = 0
    KO = 13


class TextFont(Enum):
    A = 0
    B = 1


class TextModification(Enum):
    Rotate = (0x1B, 0x56)
    Reverse = (0x1D, 0x42)
    Bold = (0x1B, 0x45)
    Underline = (0x1B, 0x2D)
    UpsideDown = (0x1B, 0x7B)
