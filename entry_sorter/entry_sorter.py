import pandas as pd

workbook = pd.read_excel('nevezesek_all.xlsx')

writer = pd.ExcelWriter('output.xlsx')

#print(workbook)
kata_groups = workbook.groupby('KATA KÓD')
for g in kata_groups:
    g[1].to_excel(writer, g[0])

kumite_groups = workbook.groupby('KUMITE KÓD')
for g in kumite_groups:
    g[1].to_excel(writer, g[0])


writer.save()