from fpdf import FPDF
from PIL import  Image
import fpdf
name = input('Name: ')
class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("shirtificate.png", 10, 8, 33)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", style="B", size=15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "Title", border=1, align="C")
        # Performing a line break:
        self.ln(20)
pdf = FPDF(orientation="portrait", format="A4")
pdf.set_auto_page_break(False)
pdf.add_page()
pdf.set_font("helvetica", style="B", size=50)
pdf.cell(80)
pdf.cell(30, 10, "CS50 Shirtificate", align="C")
pdf.ln(20)
pdf.set_font("Times", size=35)
pdf.set_text_color(255,255,255)
pdf.image('shirtificate.png',w=210,h=247,x="C")
pdf.cell(80)
pdf.cell(30, -327,f"{name} took CS50", align="C")
pdf.output("shirtificate.pdf")
