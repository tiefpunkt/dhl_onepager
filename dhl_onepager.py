import fitz
import sys

input_file = sys.argv[1]

output_file = input_file.replace(".pdf", "_onepager.pdf")

doc = fitz.open()
page=doc.new_page()
r1 = fitz.Rect(0, 0, page.rect.width, page.rect.height/2)
r2 = r1 + (0, page.rect.height/2, 0, page.rect.height/2)

src = fitz.open(input_file)

if src.page_count != 2:
    print("Input does not have two pages. Abort!")
    sys.exit(1)

page.show_pdf_page(r1, src, 0, clip=r1)
page.show_pdf_page(r2, src, 1, clip=r1, rotate=180)

doc.save(output_file)