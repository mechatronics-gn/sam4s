from sam4s.message import Message
from sam4s.text import TextLanguage, TextModification, TextFont, TextAlign
from sam4s.barcode import BarcodeType, BarcodeHri, BarcodeFont, Barcode
import serial

message = Message()

message.add_text("Hello World!\n")

message.add_text_lang(TextLanguage.KO)
message.add_text("메카트로닉스\n")
message.add_text_lang(TextLanguage.EN)

message.add_text_font(TextFont.B)
message.add_text("This is font B\n")
message.add_text_font(TextFont.A)

message.add_text_align(TextAlign.CENTER)
message.add_text("Center aligned\n")

message.add_text_align(TextAlign.RIGHT)
message.add_text("Right aligned\n")
message.add_text_align(TextAlign.LEFT)

message.add_text_modification(TextModification.Bold, True)
message.add_text("Bolded\n")
message.add_text_modification(TextModification.Bold, False)

message.add_text_modification(TextModification.Reverse, True)
message.add_text("Reversed\n")
message.add_text_modification(TextModification.Reverse, False)

message.add_text_modification(TextModification.Underline, True)
message.add_text("Underlined\n")
message.add_text_modification(TextModification.Underline, False)

message.add_text_modification(TextModification.UpsideDown, True)
message.add_text("UpsideDowned\n")
message.add_text_modification(TextModification.UpsideDown, False)

message.add_text_modification(TextModification.Rotate, True)
message.add_text("Rotated\n")
message.add_text_modification(TextModification.Rotate, False)

message.add_text_position(200)
message.add_text("Text starting at 200\n")
message.add_text_position(0)

message.add_text_double(True, True)
message.add_text("DW DH\n")

message.add_text_double(True, False)
message.add_text("DW Only\n")

message.add_text_double(False, True)
message.add_text("DH Only\n")
message.add_text_double(False, False)

message.add_text_size(8, 8)
message.add_text("sz x8\n")
message.add_text_size(1, 1)

message.add_text_line_space(100)
message.add_text("Line Space 100 " * 5 + "\n")
message.add_text_line_space() # set to default

message.add_text_align(TextAlign.CENTER)
barcode = Barcode("Barcode Test", BarcodeType.CODE93, BarcodeHri.BELOW, BarcodeFont.A, 3, 162) # I recommend sticking to Code93 since it has the least limitations
message.add_barcode(barcode)
message.add_text_align(TextAlign.LEFT)

message.add_text("Finalize with 4 line feeds and a cut with some unit feeds\n")
message.add_feed_line(4)
message.add_cut(True)

output = message.generate_message()

s = serial.Serial(
    port="/dev/ttyACM0",
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    xonxoff=True,
    rtscts=False,
    dsrdtr=False,
)

s.write(output)
s.flush()
