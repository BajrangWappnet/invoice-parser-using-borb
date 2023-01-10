from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import json

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    with open(path, 'rb') as fp:
        for page in PDFPage.get_pages(fp, set()):
            interpreter.process_page(page)
            text = retstr.getvalue()

    return text

# convert_pdf_to_txt("work/data/lowes_bill_2.pdf")

def convert_txt_to_json(text):
    invoice_data = {}
    # parsing the text and extracting the data
    invoice_data["order"] = text[text.index("Invoice Number: ")+15:text.index("Invoice Date: ")-1]
    invoice_data["invoice_date"] = text[text.index("Invoice Date: ")+13:text.index("Customer Name: ")-1]
    invoice_data["customer_name"] = text[text.index("Customer Name: ")+15:text.index("Items:")-1]
    invoice_data["total_amount"] = text[text.rindex("Total: ")+7:]
    return json.dumps(invoice_data)

pdf_invoice = "work/data/lowes_bill_2.pdf"
text = convert_pdf_to_txt(pdf_invoice)
json_invoice = convert_txt_to_json(text)

print(json_invoice)
