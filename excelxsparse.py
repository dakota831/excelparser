
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
                for i in range(0, len(dayarray)) :
                    curkey = row[0]
                    currow=row[4]
                    if currow.find(dayarray[i]) == -1:
                        timedict[dayarray[i]]={'Open':'N/A','Closed':'N/A'}
                        # rowdict[line_count]=timedict
                        # rowdict[line_count].append({'keyword':curkey})
                        continue
                    dayindex=currow.find(dayarray[i])
                    startoftime=dayindex+len(dayarray[i])+4
                    if currow[startoftime]=='C':
                        timedict[dayarray[i]]={'Open':'Closed','Closed':'Closed'}
                    else:
                        storage=currow[startoftime:]
                        endoftime=storage.find(' ')
                        timeofinterest=currow[startoftime:startoftime+endoftime]
                        timedict[dayarray[i]]=timeofinterest
                        opentime=timeofinterest[0:timeofinterest.find('?')]
                        closetime=timeofinterest[timeofinterest.find('?')+1:]
                        openclosedict={'Open':opentime,'Closed':closetime}
                        timedict[dayarray[i]]=openclosedict
                    # print(timedict)
                rowdict[line_count]=timedict
                rowdict[line_count].update({'keyword':curkey})
                timedict = {}
                line_count += 1
    print(f'Processed {line_count} lines.')


with open('ffloutput.csv', mode='w') as fflout:
     employee_writer = csv.writer(fflout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
     employee_writer.writerow(['keyword', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
     for i in range(1, line_count) :
        employee_writer.writerow([rowdict[i]['keyword'], rowdict[i]['Sunday'], rowdict[i]['Monday'], rowdict[i]['Tuesday'], rowdict[i]['Wednesday'], rowdict[i]['Thursday'], rowdict[i]['Friday'], rowdict[i]['Saturday']])
  


    