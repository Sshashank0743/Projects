import fitz
fname = "ebharati-pdf-1685602613Balidaanam-SanskritNovel-NCKelakar1940.pdf"
do='one/';
dpi = 200  # choose desired dpi here
zoom = dpi / 72  # zoom factor, standard: 72 dpi
magnify = fitz.Matrix(zoom, zoom)  # magnifies in x, resp. y direction
doc = fitz.open(fname)  # open document
for page in doc:
    pix = page.get_pixmap(matrix=magnify)  # render page to an image
    pix.save(do+f"{page.number}.png")