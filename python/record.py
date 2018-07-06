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

if not os.path.exists(newpath + '/record'):
    os.makedirs(newpath + '/record')


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
allFiles = glob.glob(source_dir + "/record*.csv")
df = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_, index_col=None)
    list_.append(df)
df = pd.concat(list_)
try:
    df = df[
        ['NAME', 'ROLLNO', 'EXP1', 'EXP2', 'EXP3', 'EXP4', 'EXP5', 'EXP6', 'EXP7', 'EXP8', 'EXP9', 'EXP10']]
    y =10
except:
    try:
        df = df[
            ['NAME', 'ROLLNO', 'EXP1', 'EXP2', 'EXP3', 'EXP4', 'EXP5', 'EXP6', 'EXP7', 'EXP8', 'EXP9', 'EXP10', 'EXP11']]
        y = 11
    except:
        try:
            df = df[
                ['NAME', 'ROLLNO', 'EXP1', 'EXP2', 'EXP3', 'EXP4', 'EXP5', 'EXP6', 'EXP7', 'EXP8', 'EXP9', 'EXP10',
                 'EXP11', 'EXP12']]
            y = 12
        except:
            try:
                df = df[
                    ['NAME', 'ROLLNO', 'EXP1', 'EXP2', 'EXP3', 'EXP4', 'EXP5', 'EXP6', 'EXP7', 'EXP8', 'EXP9', 'EXP10',
                     'EXP11', 'EXP12', 'EXP13']]
                y = 13
            except:
                try:
                    df = df[
                        ['NAME', 'ROLLNO', 'EXP1', 'EXP2', 'EXP3', 'EXP4', 'EXP5', 'EXP6', 'EXP7', 'EXP8', 'EXP9',
                         'EXP10',
                         'EXP11', 'EXP12', 'EXP13', 'EXP14']]
                    y = 14
                except:
                    df = df[
                        ['NAME', 'ROLLNO', 'EXP1', 'EXP2', 'EXP3', 'EXP4', 'EXP5', 'EXP6', 'EXP7', 'EXP8', 'EXP9',
                         'EXP10',
                         'EXP11', 'EXP12', 'EXP13', 'EXP14', 'EXP15']]
                    y = 15


df = df.sort_values('ROLLNO')
x = df
df.to_csv(newpath + "\\record\\Record.csv")
x = x.fillna("NAME")
new_header = x.iloc[0] #grab the first row for the header
x = x[1:] #take the data less the header row
x.columns = new_header #set the header row as the df header
x = x.iloc[1:]
# col_list = list(x)
# col_list.remove(0)
# col_list.remove(0)
# x.reset_index(inplace=True)
# x.iloc['Column_Total'] = z.transpose()
x.loc['Column_Total'] = x.sum(axis=0)
x = x.rename(columns= {0: "ROLLNO"})
# x.loc[0]["Column_Total"] = "-"

# x = x.iloc[0:, 1:]
# x.set_index("ROLLNO")
# new_header = x.iloc[0] #grab the first row for the header
# x = x[1:] #take the data less the header row
# x.columns = new_header #set the header row as the df header
# x.set_index(0)
# x = x.iloc[1:, 0:]
# x.loc['Column_Total'] = x.sum(axis=0)
v = x.shape[0]-1
v = v*20

CO_max = []

for i in range(y+2):
    print i
    CO_max.append(v)

x.loc['CO_Max'] = CO_max
#
x = x.groupby(x.columns, axis=1).sum()
coy = x.filter(regex="CO")

z = (coy.iloc[-2]/coy.iloc[-1])*60
z.to_csv(newpath + "\\record\\Record_CO.csv")
z.to_dict()
dbchart = z
plotdf = pd.DataFrame([dbchart])
plotdf = plotdf.transpose()
coplot = plotdf.plot.bar(title='COURSE OUTCOMES (Record)', legend=False)
coplot.set_ylabel('% of COs Achieved')
coplot.set_xlabel('Course Outcomes')
coplot.set_ylim(0, 60)
for p in coplot.patches:
    coplot.annotate(numpy.round(p.get_height(), decimals=3), (p.get_x() + p.get_width() / 2., p.get_height() * 1.05),
                    xytext=(1, 5),
                    textcoords='offset points', ha='center', va='center')
fig = coplot.get_figure()
plt.tight_layout()
plt.savefig(newpath + "\\record\\Record_CO.png")
plt.close()
headfoot(newpath + "\\record\\Record_CO")
