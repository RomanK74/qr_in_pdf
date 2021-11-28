# def add_image(image_path):
#     dirname = "code_img"
#     images_path = []
#     for fname in os.listdir(dirname):
#         if not fname.endswith(".jpg"):
#             continue
#         path = os.path.join(dirname, fname)
#         if os.path.isdir(path):
#             continue
#         images_path.append(path)
#     for image_path in images_path:
#         pdf = fpdf.FPDF()
#         pdf.add_page()
#         line_no = 1
#         for i in range(200):
#             pdf.image(image_path, x=1, y=1, w=20)
#             pdf.set_font("Arial", size=6)
#             line_no += 1
#     pdf.output("add_image.pdf")

# # create img from file with code
# with open('codes.txt') as qr_string:
#     num = 0
#     for line in qr_string:
#         num += 1
#         print(f'{num} : {line}')
#         create_code(line=line, num=num)
#
# # convert all files ending in .jpg inside a directory
# dirname = "code_img"
# imgs = []
# for fname in os.listdir(dirname):
#     if not fname.endswith(".jpg"):
#         continue
#     path = os.path.join(dirname, fname)
#     if os.path.isdir(path):
#         continue
#     imgs.append(path)
# with open("name.pdf", "wb") as f:
#     f.write(img2pdf.convert(imgs))

