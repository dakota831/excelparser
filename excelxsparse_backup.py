
import csv

#CSV READING
#https://realpython.com/python-csv/


with open('hours.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    timedict = {}
    rowdict = {}
    dayarray = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    for row in csv_reader:
            if line_count == 0:
                print('we are in the header so do nothing')
                line_count = line_count + 1
            else:
                currow=row[4]
                for i in range(0, len(dayarray)-1) :
                    dayindex=currow.find(dayarray[i])
                    startoftime=dayindex+len(dayarray[i])+4
                    print(currow[startoftime])
                    if currow[startoftime]=='C':
                        timedict[dayarray[i]]='Closed'
                    else:
                        storage=currow[startoftime:]
                        endoftime=storage.find(' ')
                        timedict[dayarray[i]]=currow[startoftime:startoftime+endoftime]
                    print(timedict)
                rowdict[line_count]=timedict
                timedict = {}
                line_count += 1
    print(f'Processed {line_count} lines.')


# with open('employee_file.csv', mode='w') as employee_file:
#     employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

#     employee_writer.writerow(['John Smith', 'Accounting', 'November'])
#     employee_writer.writerow(['Erica Meyers', 'IT', 'March'])


    