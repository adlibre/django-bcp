"""
Module: Barcode Printer Views
Project: Adlibre DMS
Copyright: Adlibre Pty Ltd 2012
License: See LICENSE for license information
"""

from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.core.urlresolvers import reverse
from django.shortcuts import render

from django.conf import settings

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


def print_barcode_embed_example(request, code, barcode_type, template='embed_example.html'):
    """
    This is a test page showing how you can embed a request to print a barcode
    """
    bcp_url = reverse('bcp-print', kwargs = {'barcode_type': barcode_type, 'code': code, 'auto_print': True, })
    context = { 'bcp_url': bcp_url, }
    return render(request, template, context)


def print_barcode(request, code, barcode_type, template='print.html'):
    """
    This page causes the browser to request the barcode be printed
    """
    pdf_url = reverse('bcp-generate', kwargs = {'barcode_type': barcode_type, 'code': code, 'auto_print': True, })
    context = { 'pdf_url': pdf_url, }
    return render(request, template, context)


def generate(request, code, barcode_type='Standard39', auto_print=False):
    """
     Returns a PDF Barcode using ReportLab
    """

    from reportlab.graphics.shapes import String
    from reportlab.graphics import renderPDF
    from reportlab.graphics.barcode import createBarcodeDrawing
    from reportlab.pdfbase import pdfdoc
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont

    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'inline; filename=%s.pdf' % (code,)

    # Config
    import settings
    font_size = settings.FONT_SIZE
    bar_height = settings.BAR_HEIGHT
    bar_width = settings.BAR_WIDTH
    font_name = settings.FONT_NAME
    font_path = settings.FONT_PATH
    try:
        # If this is extended to different barcode types, then these options will need to be specified differently, eg not all formats support checksum.
        bc = createBarcodeDrawing(barcode_type, barHeight=bar_height, barWidth=bar_width, value=str(code), isoScale=True, quiet=settings.BAR_QUIET, checksum=settings.BAR_CHECKSUM,)
    except KeyError, e:
        return HttpResponseBadRequest('Barcode Generation Failed: %s' % (e))

    # Register the font
    pdfmetrics.registerFont(TTFont(font_name, font_path))

    # Set JS to Autoprint document
    if auto_print:
        pdfdoc.PDFCatalog.OpenAction = '<</S/JavaScript/JS(this.print\({bUI:true,bSilent:false,bShrinkToFit:true}\);)>>'
        pdfdoc.PDFInfo.title = code # nicety :)

    # Position for our text label
    x = bc.width / 2
    y = - font_size  # or (bar_height + font_size) if placing on top
    # The textual barcode
    text = String(x, y, code, textAnchor='middle', fontName=font_name, fontSize=font_size)
    bc.add(text)
    bc = bc.resized() # resize barcode drawing object to accommodate text added

    buffer = StringIO() # buffer for the output
    renderPDF.drawToFile(bc, buffer, autoSize=1) # write PDF to buffer

    # Get the value of the StringIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response