import xlsxwriter

matrix = {
    'bookingType' : ['manual','event'],
    'downloadContentState' : ['partial','complete'],
    'downloadState' : ['notStarted','inProgress','suspended'],
    'embed' : ['eventBooking','seasonBooking','transcodeBooking','transcodeSeasonBooking','reminderBooking'],
    'recordingContentState' : ['partial','complete'],
    'recordingState' : ['notStarted','inProgress'],
    'reminderState' : ['notReminded'],
    'sort' : ['title','date']
    }

matrix_dist = {}
matrix_list = []

for x in matrix.keys():
    matrix_dist[str(x)] = []
    for y in matrix[x]:
        matrix_dist[str(x)].append(str(x)+'='+str(y))
        matrix_list.append(str(x)+'='+str(y))

    tmp_string = str(x)+'='
    y = 0

    while (y < len(matrix[x])):
        if y == 0:
            tmp_string = str(tmp_string)+str(matrix[x][y])
            y += 1
            continue
        else:
            tmp_string = str(tmp_string)+','+str(matrix[x][y])
        
        matrix_dist[str(x)].append(str(tmp_string))
        matrix_list.append(str(tmp_string))
        y += 1

### Create excel report
# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('../FilterMatrix.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})

# Write the column headers.
worksheet.write('A1', 'TypeOne', bold)
worksheet.write('B1', 'TypeTwo', bold)
worksheet.write('C1', 'Filter Query', bold)
# Start from first row after headers.
row = 1
# Create a format for the date or time.
data_format = workbook.add_format({'align': 'left'})
### approach 1
tmp_list = matrix_dist.keys()

first_index = 0

while (first_index < len(tmp_list)):
    for x in matrix_dist[tmp_list[first_index]]:
        second_index = first_index + 1
        while (second_index < len(tmp_list)):
            for y in matrix_dist[tmp_list[second_index]]:
                print str(tmp_list[first_index])+' with '+str(tmp_list[second_index])+' : ' + str(x)+'&'+str(y)
                worksheet.write_string(row, 0, str(tmp_list[first_index]), data_format)
                worksheet.write_string(row, 1, str(tmp_list[second_index]),data_format)
                worksheet.write_string(row, 2, str(x)+'&'+str(y),data_format)
                row += 1
            second_index += 1 
    first_index += 1
workbook.close()
