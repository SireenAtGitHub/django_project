from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from PyPDF2 import PdfFileWriter, PdfFileReader
import io, os

from django.templatetags.static import static
from reportlab.pdfgen import canvas
from reportlab.platypus import Flowable, Table, TableStyle
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont


def invoice(request):
    print("****************", os.getcwd())
    print(os.getcwd()+static('INVOICE.pdf'))
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment;filename="destination.pdf"'
    packet = io.BytesIO()
    can = canvas.Canvas(packet)
    register_font()
    can.setFont("CenturyGothicBold", 14)
    # can.drawString(495, 685, "10-04-2022")
    name = "Sireen Gothadiya"
    data = [["24-04-2022"], [name], ['+91 97730 55968']]
    t = Table(data, colWidths=160)
    t.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'CenturyGothicBold'),
        ('ALIGN', (0, 0), (0, -1), 'RIGHT'),
        ('FONTSIZE', (0, 0), (0, -1), 15),
        ('BOTTOMPADDING', (0, 0), (0, -1), 14),
    ]))
    t.wrapOn(can, 400, 100)
    t.drawOn(can, 418, 616)
    can.save()

    new_pdf = PdfFileReader(packet)

    existing_pdf = PdfFileReader(open(os.getcwd()+static('INVOICE.pdf'), "rb"))
    output = PdfFileWriter()
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # response = open("destination.pdf", "wb")
    output.write(response)
    # response.close()
    # packet.seek(0)
    # return FileResponse(response, as_attachment=True, filename="destination.pdf")
    return response


def register_font():
    pdfmetrics.registerFont(TTFont('CenturyGothicBold',  os.getcwd()+'\static\CenturyGothicBold.ttf'))
    pdfmetrics.registerFont(TTFont('CenturyGothicRegular', os.getcwd()+'\static\CenturyGothicRegular.ttf'))
    registerFontFamily('CenturyGothic', normal='CGRegular', bold='CGBold')
