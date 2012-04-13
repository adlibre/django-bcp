# Barcode Printer for Django

This is a reusable Django application which generates PDF barcodes in various formats with a human readable label.

These barcodes are rendered as a PDF with inline JavaScript which prompts the PDF to be immediately printed.

Currently this is used by <a href="http://www.adlibre.com.au/adlibre-dms/">Adlibre DMS</a> for document barcode generation, but the application is generic and could be reused in any Django app that requires barcode printing.

ReportLab is used for the barcode generation. And the following formats are supported:

 * Code39 (3 of 9),
 * Code128.

However it should be trivial to add support for any format that ReportLab supports.

## Installation

If you use pip to install this then the dependency and any other requirements will be taken care of:

<pre>
    pip install -e git+git://github.com/adlibre/django-bcp.git#egg=django-bcp
</pre>