with open('logfile.txt','r') as file_handle:
    log_file_list = file_handle.readlines()

def get_referrer_from_iis_line(iis_line,index):
    '''finds the referrer in the given iis line'''
    split_line = iis_line.split(' ')
    return split_line[index]

def get_header_index(iis_header_line):
    split_header = iis_header_line.split(' ')
    return split_header.index('cs(Referer)')

referrer_list = []
for line in log_file_list:
    if line.startswith('#Fields:'):
        header_index = get_header_index(line)
        header_index -= 1
    if 'Chrome' in line:
        referrer_list.append(get_referrer_from_iis_line(line,header_index))
print(referrer_list)
