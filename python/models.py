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

if not os.path.exists(newpath + '/models'):
    os.makedirs(newpath + '/models')


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
    c.drawCentredString(40, 35, 'Name:' )
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawCentredString(55, 15, 'Designation:')
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawCentredString(495, 55, 'Signature of the HOD with Date')
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawCentredString(125, 750, 'Department: ' + dept)
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawCentredString(295, 750, 'Year: ' +year)
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawCentredString(435, 750, 'Semester: '+sem)
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawCentredString(120, 725, 'Faculty Name: ' + faculty_name)
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawCentredString(295, 725, 'Subject Code: '+ sub_code)
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawCentredString(120, 700, 'Subject Name: '+sub_name)
    c.showPage()
    c.save()
    os.remove(filename + ".png")


source_dir = Downloads  # Path where your files are at the moment
allFiles = glob.glob(source_dir + "/*models*.csv")
df = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_, index_col=None)
    list_.append(df)
df = pd.concat(list_)

df = df[
    ['NAME', 'ROLLNO', 'CO1', 'CO2', 'CO3', 'CO4', 'CO5', 'CO6', 'CO7']]
coonly = df.iloc[1:, 2:]
col_list = list(df)
col_list.remove('ROLLNO')
col_list.remove('NAME')
df.loc['Column_Total'] = coonly[col_list].sum(axis=0)
v = df.shape[0] - 2
df2 = df
divided = df2.iloc[v + 1] / df2.iloc[0, 2:]
divided = divided[0:7] / v * 35.0
divided.to_csv(newpath + "models/Models_co.csv")
coplot = divided.plot.bar(title='COURSE OUTCOMES(MODELS)')
coplot.set_ylabel("% of COs Obtained")
coplot.set_xlabel("Course Outcomes")
coplot.set_ylim(0, 100)
for p in coplot.patches:
    coplot.annotate(numpy.round(p.get_height(), decimals=3), (p.get_x() + p.get_width() / 2., p.get_height()),
                    xytext=(1, 5),
                    textcoords='offset points', ha='center', va='center')
fig = coplot.get_figure()
plt.tight_layout()
# fig = plt.gcf()
# fig.set_size_inches(8.27,11.69)
fig.savefig(newpath + "models/Models_CO.png")
plt.close()
headfoot(newpath + "models/Models_CO")
df.sort_values('ROLLNO')
df.iloc[0, 1] = 1  # 'useful when sorting in combining.py'
df.to_csv(newpath + "/models/Models.csv")
