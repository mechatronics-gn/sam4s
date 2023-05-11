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


class Message:
    def __init__(self):
        self.b = bytearray()
        self.current_lang = TextLanguage.EN

    def add_text_align(self, align: TextAlign):
        self.b.append(0x1B)
        self.b.append(0x61)
        self.b.append(align.value)
        self.b.append(0x00)

    def add_text_line_space(self, line_space: int = 60):
        self.b.append(0x1B)
        self.b.append(0x33)
        self.b.append(line_space)
        self.b.append(0x00)

    def add_text(self, text: str):
        self.b.append(0x00)
        if self.current_lang == TextLanguage.EN:
            self.b += bytes(text, 'utf-8')
        elif self.current_lang == TextLanguage.KO:
            self.b += bytes(text, 'cp949')
        self.b.append(0x00)

    def add_text_lang(self, language: TextLanguage):
        self.b.append(0x1B)
        self.b.append(0x52)
        self.b.append(language.value & 0xFF)
        self.b.append(0x00)
        self.current_lang = language

    def add_text_font(self, font: TextFont):
        self.b.append(0x1B)
        self.b.append(0x4D)
        self.b.append(font.value)
        self.b.append(0x00)

    def add_text_double(self, double_width: bool, double_height: bool):
        self.b.append(0x1B)
        self.b.append(0x21)
        if double_width and double_height:
            self.b.append(0x30)
        elif double_width:
            self.b.append(0x20)
        elif double_height:
            self.b.append(0x10)
        else:
            self.b.append(0x00)
        self.b.append(0x00)

    def add_text_size(self, width: int, height: int):
        self.b.append(0x1D)
        self.b.append(0x21)
        self.b.append((width - 1) * 16 + (height - 1))
        self.b.append(0x00)

    def add_text_position(self, pos: int):
        self.b.append(0x1B)
        self.b.append(0x24)
        self.b.append(pos // 256)
        self.b.append(pos % 256)
        self.b.append(0x00)

    def add_text_modification(self, modification: TextModification, flag: bool):
        self.b.append(modification.value[0])
        self.b.append(modification.value[1])
        self.b.append(flag)
        self.b.append(0x00)

    def add_feed_unit(self, unit: int):
        self.b.append(0x1B)
        self.b.append(0x4A)
        self.b.append(unit)
        self.b.append(0x00)

    def add_feed_line(self, line: int):
        self.b.append(0x1B)
        self.b.append(0x64)
        self.b.append(line)
        self.b.append(0x00)

    def add_cut(self, feed: int):
        if feed:
            self.add_feed_unit(200)
        self.b.append(0x1D)
        self.b.append(0x56)
        self.b.append(0x31)
        self.b.append(0x00)

    def generate_message(self):
        return bytes(self.b)
