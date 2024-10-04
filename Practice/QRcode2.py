import qrcode
from PIL import Image
import qrcode.constants

qr= qrcode.QRCode(version=1, error_correction= qrcode.constants.ERROR_CORRECT_H, box_size = 10)
