import xlrd

### Important variables ###
list_of_schools = []
studentaid_data = []
### End of important variables ###

def add_data(data, year, school_name) :
    for school in list_of_schools:


##Manually doing 1999-2000 due to different structure
workbook = xlrd.open_workbook('../data/99-00/DL_AwardYr_Summary_AY1999_2000_All.xls')
worksheet = workbook.sheet_by_index(0)

start_row = 6
for i in range(start_row, worksheet.nrows):
    #Getting the important data
    year = 9901
    school_name = worksheet.cell(i, 1).value
    school_state = worksheet.cell(i, 2).value
    school_type = worksheet.cell(i, 4).value
    school_sub = [worksheet.cell(i, 5).value, worksheet.cell(i, 6).value, worksheet.cell(i, 7).value,\
                  worksheet.cell(i, 8).value, worksheet.cell(i, 9).value]
    school_unsub = [worksheet.cell(i, 10).value, worksheet.cell(i, 11).value,\
                    worksheet.cell(i, 12).value, worksheet.cell(i, 13).value,\
                    worksheet.cell(i, 14).value]
    school_plus = [worksheet.cell(i, 15).value, worksheet.cell(i, 16).value,\
                   worksheet.cell(i, 17).value, worksheet.cell(i, 18).value,\
                   worksheet.cell(i, 19).value]

    #Adding school name to list
    if school_name not in list_of_schools:
        list_of_schools.append(school_name)
    
    row = [school_state, [year, school_type, school_sub, school_unsub, school_plus]]
    print(row)
