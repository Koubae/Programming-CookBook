import fitz
import calendar
import sys
assert len(sys.argv) == 2, '"need start year as the one and only parameter"'


startyear = sys.argv[1]
assert startyear.isdigit(), "year must be positive numeric"
startyear = int(startyear)
assert startyear > 0, "year must be positive numeric"

doc = fitz.open()
cal = calendar.LocaleTextCalendar(locale="en")
w, h = fitz.PaperSize('a4-l')

txt = cal.formatyear(startyear, m=4)
doc.insertPage(-1, txt, fontsize=12, fontname="Courier", width=w, height=h)

txt = cal.formatyear(startyear + 1, m=4)
doc.insertPage(-1, txt, fontsize=12, fontname='Courier-Oblique', width=w, height=h)

txt = cal.formatyear(startyear + 2, m=4)
doc.insertPage(-1,txt, fontsize=12, fontname="Courier-Bold", width=w, height=h)

txt = cal.formatyear(startyear + 3, m=4)
doc.insertPage(-1,txt, fontsize=12, fontname="Courier-BoldOblique", width=w, height=h)

txt = cal.formatyear(startyear + 4, m=4)
doc.insertPage(-1,txt, fontsize=12, fontname="Times-Roman", width=w, height=h)

doc.save('Calendar.pdf', garbage=4, deflate=True)



# Base14_fontnames = (
#     "Courier",
#     "Courier-Oblique",
#     "Courier-Bold",
#     "Courier-BoldOblique",
#     "Helvetica",
#     "Helvetica-Oblique",
#     "Helvetica-Bold",
#     "Helvetica-BoldOblique",
#     "Times-Roman",
#     "Times-Italic",
#     "Times-Bold",
#     "Times-BoldItalic",
#     "Symbol",
#     "ZapfDingbats",
# )

