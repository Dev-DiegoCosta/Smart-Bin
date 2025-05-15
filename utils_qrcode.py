
import qrcode
from PIL import Image, ImageTk

def gerar_qr_code(cpf):
    url = f"https://www.instagram.com/diegocosta081/user/{cpf}"
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white").convert("RGB")
    img_with_margin = Image.new("RGB", (img.size[0] + 20, img.size[1] + 20), "white")
    img_with_margin.paste(img, (10, 10))
    return ImageTk.PhotoImage(img_with_margin)
