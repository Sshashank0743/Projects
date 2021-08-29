import pyqrcode
from pyqrcode import QRCode

s = "https://www.youtube.com/channel/UC2hW4llAGURDNnjx_cq8C6A"

qr = pyqrcode.create(s)

qr.svg("myyoutube.svg",scale = 7)
