# Barcode Printer for Django

This is a reusable Django application which generates PDF barcodes in various formats with a human readable label.

These barcodes are rendered as a PDF with inline JavaScript which prompts the PDF to be immediately printed.

Currently this is used by [Adlibre DMS](http://www.adlibre.com.au/adlibre-dms/) for document barcode generation, but the application is generic and could be reused in any Django app that requires barcode printing.

ReportLab is used for the barcode generation. And the following formats are supported:

 * Code39 (3 of 9),
 * Code128.

However it should be trivial to add support for any format that ReportLab supports.

## Installation

If you use pip to install this then the dependency and any other requirements will be taken care of:

<pre>
    pip install -e git+git://github.com/adlibre/django-bcp.git#egg=django-bcp
</pre>

## NB ReportLab 2.5 Bug

ReportLab 2.5 has a typo. "OpenActions" should be "OpenAction" as per ISO 32000-1:2008.

<pre>
    diff -r tmp/lib/python2.7/site-packages/reportlab/pdfbase/pdfdoc.py lib/python2.7/site-packages/reportlab/pdfbase/pdfdoc.py
    1022c1022
    <         Dests Outlines Pages Threads AcroForm Names OpenAction PageMode URI
    ---
    >         Dests Outlines Pages Threads AcroForm Names OpenActions PageMode URI
</pre>

You will need to manually patch this, otherwise the barcode will not automatically print.