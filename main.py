import os
import shutil

import qrcode
import fpdf


QR = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)


def barcode(filename: str, dirname: str):
    os.mkdir(dirname)

    def create_barcode(line, num):
        # create a jpg
        QR.add_data(line)
        QR.make(fit=True)
        img = QR.make_image(fill_color="black", back_color="white")
        img.save(f'{dirname}/{num}_code.jpg', 'JPEG')
        QR.clear()

    # create jpg from file from code
    with open(filename) as qr_string:
        num = 0
        for line in qr_string:
            num += 1
            create_barcode(line=line, num=num)


def add_image(dirname: str):
    # creates a pdf file with qr

    def images_paths():
        # convert all files ending in .jpg inside a directory in list of path
        imgs = []
        for fname in os.listdir(dirname):
            if not fname.endswith(".jpg"):
                continue
            path = os.path.join(dirname, fname)
            if os.path.isdir(path):
                continue
            imgs.append(path)
        return imgs

    pdf = fpdf.FPDF()
    pdf.add_page()
    x = 5  # x коардината на странице
    y = 8  # y коардината на странице
    img_in_line = 0
    line_in = 0
    for image_path in images_paths():
        if line_in == 12 and img_in_line == 8:
            pdf.add_page()
            x = 5
            y = 8
            line_in = 0
        if img_in_line <= 8:
            img_in_line += 1
            pdf.image(image_path, x=x, y=y, w=20)
            x += 22
        else:
            line_in += 1
            x = 5
            y += 22
            img_in_line = 1
            img_in_line += 1
            pdf.image(image_path, x=x, y=y, w=20)
            x += 22
    pdf.output("qr_code_images.pdf")
    shutil.rmtree('code_img', ignore_errors=True)


if __name__ == '__main__':
    barcode('codes.txt', 'code_img')
    add_image("code_img")
