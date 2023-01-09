import typing
from borb.pdf.document.document import Document
from borb.pdf.pdf import PDF
from borb.pdf.canvas.geometry.rectangle import Rectangle

# New imports
from borb.toolkit.text.regular_expression_text_extraction import RegularExpressionTextExtraction, PDFMatch

def main():

    d: typing.Optional[Document] = None
        
    # Set up EventListener
    l: RegularExpressionTextExtraction = RegularExpressionTextExtraction("Your")
    with open("Parser/data/lowes_bill_2.pdf", "rb") as pdf_in_handle:
        d = PDF.loads(pdf_in_handle, [l])

    assert d is not None

    matches: typing.List[PDFMatch] = l.get_matches_for_pdf("Your",d)[0]
    print(matches)
    assert len(matches) == 1
    # print(matches[0])

    r: Rectangle = matches[0].get_bounding_boxes()[0]
    print(r)
    # print("%f %f %f %f" % (r.get_x(), r.get_y(), r.get_width(), r.get_height()))

if __name__ == "__main__":
    main()