#!C:/Python27/python.exe
print("Content-Type: text/plain\n")
import os
from _winreg import *
import glob
import numpy
import pandas as pd
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait

with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
    Downloads = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]

with open(Downloads + '/file.txt', 'r') as myfile:
    newpath = myfile.read().replace('\n', '')
    print(newpath)
print(newpath)

if not os.path.exists(newpath + '/combined_practicals'):
    os.makedirs(newpath + '/combined_practicals')


def headfoot(filename):
    information = newpath.split("\\")
    print(information)
    faculty_name = information[2]
    print(information[1])
    dept = information[4]
    year = information[6]
    sub_name = information[8]
    sub_code = information[10]
    sem = information[12]

    c = canvas.Canvas(filename + ".pdf", pagesize=portrait(A4))
    seal = "D:\\XAMPP\\htdocs\\SREC-OBE\\python\\a.png"
    right = "D:\\XAMPP\\htdocs\\SREC-OBE\\python\\b.png"
    graph = filename + ".png"
    c.drawImage(seal, 25, 785, width=None, height=None)
    c.drawImage(right, 535, 785, width=None, height=None)
    c.setFont('Helvetica-Bold', 17, leading=None)
    c.drawCentredString(300, 800, 'SRI RAMAKRISHNA ENGINEERING COLLEGE')
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawCentredString(300, 785, 'Vattamalaipalayam - N.G.G.O Colony Post - Coimbatore')

    c.drawImage(graph, 45, 200, width=500, height=500)

    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawCentredString(40, 205, 'Remarks:')
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawCentredString(95, 55, 'Signature of the faculty with Date')
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawCentredString(40, 35, 'Name:')
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawCentredString(55, 15, 'Designation:')
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawCentredString(495, 55, 'Signature of the HOD with Date')
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawCentredString(125, 750, 'Department: ' + dept)
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawCentredString(295, 750, 'Year: ' + year)
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawCentredString(435, 750, 'Semester: ' + sem)
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawCentredString(120, 725, 'Faculty Name: ' + faculty_name)
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawCentredString(295, 725, 'Subject Code: ' + sub_code)
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawCentredString(120, 700, 'Subject Name: ' + sub_name)
    c.showPage()
    c.save()
    os.remove(filename + ".png")


df = pd.read_csv(newpath + "\\record\\Record_CO.csv")
df1 = pd.read_csv(newpath + "\\models\\Models_CO.csv")
p = df.transpose()
q = p.index
q = q.values.tolist()
x = df.values.tolist()
x.insert(0, q)
p = df1.transpose()
q = p.index
q = q.values.tolist()
y = df1.values.tolist()
y.insert(0, q)
x[0][1] = float(x[0][1])
y[0][1] = float(y[0][1])
dbchart = {}
for i in xrange(0, 7):
    dbchart["CO" + str(i + 1)] = x[i][1] + y[i][1]
print(dbchart)
plotdf = pd.DataFrame([dbchart])
plotdf = plotdf.transpose()
coplot = plotdf.plot.bar(title='COURSE OUTCOMES (Overall Practicals)', legend=False)
coplot.set_ylabel('% of COs Achieved')
coplot.set_xlabel('Course Outcomes')
coplot.set_ylim(0, 95)
for p in coplot.patches:
    coplot.annotate(numpy.round(p.get_height(), decimals=3), (p.get_x() + p.get_width() / 2., p.get_height() * 1.05),
                    xytext=(1, 5),
                    textcoords='offset points', ha='center', va='center')
fig = coplot.get_figure()
plt.tight_layout()
plt.savefig(newpath + "\\combined_practicals\\Combined.png")
plt.close()
headfoot(newpath + "\\combined_practicals\\Combined_Practicals")
#
# # i, x[i][1] + y[i][1]
# # a = z
# # i = iter(a)
# # b = dict(zip(i, i))
# # # x = df.transpose()
# # # y = df1.transpose()
# # # x = x.reset_index()
# # # y = y.reset_index()
