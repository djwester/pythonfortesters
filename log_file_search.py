with open('logfile.txt','r') as file_handle:
    log_file_list = file_handle.readlines()

def get_referrer_from_iis_line(iis_line):
    '''finds the referrer in the given iis line'''
    return 

referrer_list = []
for line in log_file_list:
    if 'Chrome' in line:
        referrer_list.append(get_referrer_from_iis_line(line))
