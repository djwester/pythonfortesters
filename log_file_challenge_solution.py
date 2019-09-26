with open('logfile.txt','r') as file_handle:
    log_file_list = file_handle.readlines()

def get_fields(iis_fields_line):
    '''get the headers from the fields line of the iis file'''
    fields_list = iis_fields_line.strip().split(' ')
    print (fields_list)
    return fields_list

chrome_list = []
firefox_list = []
for line in log_file_list:
    if line.startswith('#Fields:'):
        fields_list = get_fields(line)
        time_taken_index = fields_list.index('time-taken')
        time_taken_index -= 1
    if 'Chrome' in line:
        chrome_list.append(int(line.split(' ')[time_taken_index]))
    if 'Firefox' in line:
        firefox_list.append(int(line.split(' ')[time_taken_index]))

avg_chrome_time = sum(chrome_list)/len(chrome_list)
avg_firefox_time = sum(firefox_list)/len(firefox_list)

print('On average it the chrome time was %s and the firefox time was %s'%(avg_chrome_time,avg_firefox_time))
