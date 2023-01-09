import typing
from decimal import Decimal

from borb.pdf.document.document import Document
from borb.pdf.pdf import PDF
from borb.toolkit.text.simple_text_extraction import SimpleTextExtraction

# New import
from borb.toolkit.location.location_filter import LocationFilter
from borb.pdf.canvas.geometry.rectangle import Rectangle


def main():

    d: typing.Optional[Document] = None

    # Define rectangle of interest
    # x, y, width, height
    r: Rectangle = Rectangle(Decimal(311.208556),
                             Decimal(733.112120),
                             Decimal(42.455488),
                             Decimal(44))

    # Set up EventListener(s)
    l0: LocationFilter = LocationFilter(r)
    l1: SimpleTextExtraction = SimpleTextExtraction()
    # l0.add_listener(l1)

    with open("Parser/data/lowes_bill_2.pdf", "rb") as pdf_in_handle:
        d = PDF.loads(pdf_in_handle, [l0])
        # print(d)

    assert d is not None
    print(l1.get_text_from_pdf(d))


if __name__ == "__main__":
    main()