# parse through the logfile.txt data and compare the 
# average time taken for users with Firefox to users with Chrome
with open('logfile.txt','r') as file_handle:
    log_file_list = file_handle.readlines()

def get_fields(iis_fields_line):
    '''get the headers from the fields line of the iis file'''
    fields_list = iis_fields_line.strip().split(' ')
    return fields_list

chrome_time_list = []
firefox_time_list = []
for line in log_file_list:
    if line.startswith('#Fields:'):
        fields_list = get_fields(line)
        time_taken_index = fields_list.index('time-taken')
        time_taken_index -= 1
    if 'Chrome' in line:
        chrome_time_list.append(int(line.split(' ')[time_taken_index]))
    if 'Firefox' in line:
        firefox_time_list.append(int(line.split(' ')[time_taken_index]))
chrome_time_avg = sum(chrome_time_list)/len(chrome_time_list)
firefox_time_avg = sum(firefox_time_list)/len(firefox_time_list)

print ("On average it took chrome %s and firefox %s"%(chrome_time_avg,firefox_time_avg))
