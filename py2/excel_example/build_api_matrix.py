import xlsxwriter
import os

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

workbook = xlsxwriter.Workbook('/FilterMatrix.xlsx')
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

### Try for py file creation
fd = open('test_planner_extended_filters.py','w')
fd.write('''from audioop import reverse
from time import sleep
import pytest
import requests
from utils import *
from conftest import file_dir as test_home
from conftest import ref_version
import json
import datetime''')
fd.write('\n\n')

### approach 1
tmp_list = matrix_dist.keys()

# print '\n'.join(tmp_list)
first_index = 0

while (first_index < (len(tmp_list) - 1)):
    fd.write('\n')
    fd.write("class Test"+tmp_list[first_index]+'Major:')
    fd.write('\n')
    counter = 1
    
    for x in matrix_dist[tmp_list[first_index]]:
        second_index = first_index + 1

        while (second_index < len(tmp_list)):
            for y in matrix_dist[tmp_list[second_index]]:
#                 print str(tmp_list[first_index])+' with '+str(tmp_list[second_index])+' : ' + str(x)+'&'+str(y)
                worksheet.write_string(row, 0, str(tmp_list[first_index]), data_format)
                worksheet.write_string(row, 1, str(tmp_list[second_index]),data_format)
                worksheet.write_string(row, 2, str(x)+'&'+str(y),data_format)
                row += 1
                ## add to py file
                test_case_name = 'test_'+str(tmp_list[first_index]) +'_with_' +str(tmp_list[second_index])
                test_case_name = str(test_case_name)+'_'+str(counter)
                fd.write('\tdef '+str(test_case_name)+'(self):\n')
                fd.write('\t\tfilter_response = call_ref_url("get", make_booking_filter_url("'+str(str(x)+'&'+str(y))+'"))\n')
                fd.write('\t\tassert filter_response.status_code == 200\n\n')
                counter += 1
                
            second_index += 1 
    first_index += 1
    
workbook.close()
fd.close()

print "Congratulations ... !!!"
print "You have created filter matrix xlsx at: " + str(os.path.dirname(os.path.abspath(__file__))) + '/FilterMatrix.xlsx'
print "Also You have created PyTest script: " + str(os.path.dirname(os.path.abspath(__file__))) + '/test_planner_extended_filters.py'
