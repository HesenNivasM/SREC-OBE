#!C:/Python27/python.exe
print "content-type: text/python\n\n"
import matplotlib.pyplot as plt
import glob
import pandas as pd
import os
import numpy
from _winreg import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait

with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
    Downloads = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]
with open(Downloads + '/maxmin.txt', 'r') as myfile:
    minmax = myfile.read()
    min = minmax[0:3]
    max = minmax[4:]
with open(Downloads + '/file.txt', 'r') as myfile:
    newpath = myfile.read().replace('\n', '')
    print(newpath)

if not os.path.exists(newpath + '/test1'):
    os.makedirs(newpath + '/test1')

def headfoot(filename):
    c = canvas.Canvas(filename + ".pdf", pagesize=portrait(A4))
    seal = ".\\a.png"
    right = ".\\b.png"
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
    c.drawCentredString(495, 55, 'Signature of the HOD with Date')
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.setFont('Helvetica-Bold', 10, leading=None)
    new = 'F.Vishnudurai'
    c.drawCentredString(125, 750, 'Department: ' + new)
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawCentredString(295, 750, 'Year: ')
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawCentredString(435, 750, 'Semester: ')
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawCentredString(120, 725, 'Faculty Name: ' + new)
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawCentredString(295, 725, 'Subject Code: ')
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawCentredString(120, 700, 'Subject Name: ')
    c.showPage()
    c.save()
    os.remove(filename + ".png")


source_dir = Downloads  # Path where your files are at the moment
allFiles = glob.glob(source_dir + "/*test*.csv")
df = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_, index_col=None)
    list_.append(df)
df = pd.concat(list_)
df = df[
    ['NO', 'NAME', 'ROLLNO', 'QN1', 'QN2', 'QN3', 'QN4', 'QN5', 'QN6', 'QN7', 'QN8', 'QN9', 'QN10', 'QN11a',
     'QN11b',
     'QN12a', 'QN12b', 'QN13a', 'QN13b', 'TOTAL', 'PERCENT', 'RESULT']]
df.drop(df.index[2])

# raw_data = dict(QN1=1, QN2=1, QN3=1, QN4=1, QN5=1, QN6=3, QN7=3, QN8=3, QN9=3, QN10=3, QN11a=8, QN11b=7,
#                 QN12a=8, QN12b=7, QN13a=8, QN13b=7)
# df = df.append(raw_data, ignore_index=True)
summa = df
new_header = summa.iloc[0]  # grab the first row for the header
summa = summa[1:]  # take the data less the header row
summa.columns = new_header  # set the header row as the summa header
orgco = summa.iloc[2:]
orgcovalue = orgco.groupby(orgco.columns, axis=1).sum()
orgcovalue = orgcovalue.reset_index()
orgcovalue['index'] = orgcovalue.index + 3
df = df.reset_index()
df['index'] = df.index
new = df.set_index('index').join(orgcovalue.set_index('index'))
summa = df
new_header = summa.iloc[1]
summa = summa[3:]  # getting rows for cl's
summa.columns = new_header
orgcl = summa
orgclvalue = orgcl.groupby(orgcl.columns, axis=1).sum()
orgclvalue = orgclvalue.reset_index()
del orgclvalue[1]
old = df.set_index('index').join(orgclvalue.set_index('index'))
answer = new.merge(old)
col_list = list(answer)
col_list.remove('ROLLNO')
col_list.remove('NAME')
col_list.remove('NO')
col_list.remove('RESULT')
answer.loc['Column_Total'] = answer[col_list].sum(axis=0)

df = answer
header_ = list(df)
cos = df.iloc[0]
cl = df.iloc[1]

# for calculating the total marks of each COS


cos_total = {'CO1': 0, 'CO2': 0, 'CO3': 0, 'CO4': 0, 'CO5': 0, 'CO6': 0, 'CO7': 0}
cl_total = {'CL1': 0, 'CL2': 0, 'CL3': 0, 'CL4': 0, 'CL5': 0, 'CL6': 0}

for i in xrange(header_.index('QN1'), header_.index('QN13b') + 1):
    # print df[header_[i]][2]
    try:
        cos_total[cos[i]] += int(df[header_[i]][2])
    except:
        cos_total[cos[i]] += 0

    try:
        cl_total[cl[i]] += int(df[header_[i]][2])
    except:
        cl_total[cl[i]] += 0

####To store the total of COs and CLs in CSV file

for i in xrange(header_.index(min), header_.index(max) + 1):
    try:
        df.at[2, header_[i]] = cos_total[header_[i]]
    except:
        df.at[2, header_[i]] = cl_total[header_[i]]

# df.sort_values('ROLLNO')
# correct one
df.to_csv(newpath + "/test1/Test1.csv")

#########################################################################################
##################   CALCULATING MAXIMUM MARKS FOR EACH COS #############################

df['CO1_max'] = [0] * (df.shape[0])
df['CO2_max'] = [0] * (df.shape[0])
df['CO3_max'] = [0] * (df.shape[0])
df['CO4_max'] = [0] * (df.shape[0])
df['CO5_max'] = [0] * (df.shape[0])
df['CO6_max'] = [0] * (df.shape[0])
df['CO7_max'] = [0] * (df.shape[0])
for j in xrange(3, df.shape[0]):
    cos_max = {'CO1': 0, 'CO2': 0, 'CO3': 0, 'CO4': 0, 'CO5': 0, 'CO6': 0, 'CO7': 0}

    for i in xrange(header_.index('QN1'), header_.index('QN13b') + 1):
        try:
            int(df[header_[i]][j])
            cos_max[cos[i]] += int(df[header_[i]][2])
        except:
            x = 1

    for k in xrange(1, 7):
        df.at[j, "CO" + str(k) + "_max"] = cos_max["CO" + str(k)]
df = df[:-1]
df.to_csv(newpath + "/test1/Test1.csv")
df = df.reset_index()

###########################################################################################


cos_max = {'CO1': 0, 'CO2': 0, 'CO3': 0, 'CO4': 0, 'CO5': 0, 'CO6': 0, 'CO7': 0}
cl_max = {'CL1': 0, 'CL2': 0, 'CL3': 0, 'CL4': 0, 'CL5': 0, 'CL6': 0}
for j in xrange(3, df.shape[0]):
    for i in xrange(header_.index('QN1'), header_.index('QN13b') + 1):
        try:
            int(df[header_[i]][j])
            cos_max[cos[i]] += int(df[header_[i]][2])
            cl_max[cl[i]] += int(df[header_[i]][2])
        except:
            x = 1
# 'x=[]'
# 'for i in xrange(header_.index('CO1'), header_.index('CL6') + 1):'
# 'x.append(df[header_[i]][df.shape[0]-1])'
y = []
co_labels = []

x = [cos_max[i] for i in cos_max]

print sorted(cos_max, key=lambda k: k)

for i in sorted(cos_max, key=lambda k: k):
    if cos_max[i] != 0:
        y.append(df[header_[header_.index(i)]][df.shape[0] - 1] / cos_max[i] * 100)
        print (i)
        co_labels.append(i)

print y, co_labels
dbchart = {}

for i in xrange(len(y)):
    print i, y
    if y[i] != 0:
        dbchart[co_labels[i]] = y[i]
print dbchart
plotdf = pd.DataFrame([dbchart])
plotdf = plotdf.transpose()
coplot = plotdf.plot.bar(title='COURSE OUTCOMES (Internal Test 1)', legend=False)
coplot.set_ylabel('% of COs Achieved')
coplot.set_xlabel('Course Outcomes')
coplot.set_ylim(0, 100)
for p in coplot.patches:
    coplot.annotate(numpy.round(p.get_height(), decimals=3), (p.get_x() + p.get_width() / 2., p.get_height() * 1.05),
                    xytext=(1, 5),
                    textcoords='offset points', ha='center', va='center')
fig = coplot.get_figure()
plt.tight_layout()
plt.savefig(newpath + "/test1/Test1_CO.png")
plt.close()
headfoot(newpath + "/test1/Test1_CO")
# names = list(dbchart.keys())
# names = sorted(names)
# values = list(dbchart.values())
# ax = plt.subplot()
# # tick_label does the some work as plt.xticks()
# new = ax.bar(xrange(len(dbchart)), values, tick_label=names)
# ax.set_ylim(0, 100)
#
#
# def autolabel(rects):
#     # attach some text labels
#     for rect in rects:
#         height = rect.get_height()
#         ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
#                 '%.3f' % float(height),
#                 ha='center', va='bottom')
#
#
# autolabel(new)
# ax.set_xlabel('Course Outcomes')
# ax.set_ylabel('% of COs Achieved')
# ax.set_title('COURSE OUTCOMES (Internal Test 1)')
# # plt.show()
# plt.tight_layout()
# plt.savefig(newpath + "/test1/Test1_CO.pdf")
# plt.close()

# print co_df
# df2 = df.filter(regex='CO')
# v = df.shape[0] - 4
# divided = df2.iloc[v+3] / df2.iloc[2]
# divided = (divided[0:] / v) * 100
# coplot = divided.plot.bar()
# fig = coplot.get_figure()
# fig.suptitle('COURSE OUTCOMES(Internal Test)')
# fig.savefig(newpath + "/Test_CO.pdf")
v = df.shape[0] - 4
df3 = df.filter(regex='CL')
dividedcl = df3.iloc[v + 3] / df3.iloc[2]
#  formula:(total/fullmark*no of students)*100
dividedcl = (dividedcl[0:] / v) * 100
clplot = dividedcl.plot.bar()
fig = clplot.get_figure()
fig.suptitle('COGNITIVE LEVEL(Internal Test 1)')
fig.savefig(newpath + "/test1/Test1_CL.pdf")
plt.close()
#  plotting the new dict to get the co label

######################################################


# new = y.plot.bar()
# fig9 = new.get_figure()
# fig9.savefig(newpath+"/test1/Test1_CO.pdf")


# for calculating the number of pass students in each COs and CLs
pass_co = {'CO1': 0, 'CO2': 0, 'CO3': 0, 'CO4': 0, 'CO5': 0, 'CO6': 0, 'CO7': 0}  # number of pass student in each COs
pass_cl = {'CL1': 0, 'CL2': 0, 'CL3': 0, 'CL4': 0, 'CL5': 0, 'CL6': 0}  # number of pass student in each CLs

for i in xrange(header_.index(min), header_.index(max) + 1):
    pass_marks = df[header_[i]][2] // 2
    c = 0
    for j in xrange(3, len(df)):
        if df[header_[i]][j] >= pass_marks:
            c += 1
    if header_[i][1] == 'O':
        pass_co[header_[i]] = c
    else:
        pass_cl[header_[i]] = c

    # df.at[2,header_[i]]=c

co_column = [i for i in pass_co]
cl_column = [i for i in pass_cl]

co_data = [pass_co[i] for i in pass_co]
cl_data = [pass_cl[i] for i in pass_cl]

co_df = pd.DataFrame(index=xrange(3), columns=co_column)
for i in xrange(len(co_data)):
    co_df.at[0, co_column[i]] = co_data[i]

cl_df = pd.DataFrame(index=xrange(3), columns=cl_column)
for i in xrange(len(cl_data)):
    cl_df.at[0, cl_column[i]] = cl_data[i]

co_df.to_csv(newpath + "/test1/co_pass_test1.csv")
cl_df.to_csv(newpath + "/test1/cl_pass_test1.csv")

# '			IMPORTANT THINGS'
# '		>>	TO CHANGE THE VALUE IN DATAFRAME'
# '			df.at[3,'NAME']='rahul''
# '		>> To ADD the new column'
# '		    df['new_column_name'] = None     // with all values No ne'
total = df['PERCENT']
below50 = total < 50
sum(below50)
btw50to60 = (total >= 50) & (total < 60)
sum(btw50to60)
btw60to70 = (total >= 60) & (total < 70)
sum(btw60to70)
btw70to80 = (total >= 70) & (total < 80)
sum(btw70to80)
btw80to90 = (total >= 80) & (total < 90)
sum(btw80to90)
above90 = (total >= 90) & (total <= 100)
sum(above90)

x = [sum(below50)]
y = [sum(btw50to60)]
z = [sum(btw60to70)]
a = [sum(btw70to80)]
b = [sum(btw80to90)]
c = [sum(above90)]

vdf = pd.DataFrame({'Above90': c, 'Below50': x, '50-60': y, '60-70': z, '70-80': a, '80-90': b})
vdf = vdf[['Below50', '50-60', '60-70', '70-80', '80-90', 'Above90']]
vdf = vdf.transpose()
vdf = vdf.plot.bar(title='OVERALL PERFORMANCE (Internal Test 1)', legend=False, figsize=(10, 7))
vdf.set_ylabel("No of Students")
vdf.set_xlabel("Categories")
# vdf.set_ylim(0, 100)
for p in vdf.patches:
    vdf.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()), xytext=(5, 10),
                 textcoords='offset points', ha='center', va='center')
fig = vdf.get_figure()
plt.tight_layout()
# plt.figure(figsize=(8.27,11.69),dpi=100)
# fig.suptitle('OVERALL PERFORMANCE (Internal Test 1)')
# plt.close()
# fig = plt.gcf()
# fig.set_size_inches(8.27, 11.69)
fig.savefig(newpath + "/test1/Overall_Performance_test1.png")
plt.close()
cos_max_csv = pd.DataFrame(cos_max.items())
cos_max_csv.to_csv(newpath + "max_co.csv")

headfoot(newpath + "/test1/Overall_Performance_test1")
