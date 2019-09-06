with open('logfile.txt','r') as file_handle:
    log_file_list = file_handle.readlines()

def get_referrer_from_iis_line(iis_line,referrer_index):
    '''finds the referrer in the given iis line'''
    split_line = iis_line.split(' ')
    return split_line[referrer_index]

def get_fields(iis_fields_line):
    '''get the headers from the fields line of the iis file'''
    fields_list = iis_fields_line.split(' ')
    return fields_list

referrer_list = []
for line in log_file_list:
    if line.startswith('#Fields:'):
        fields_list = get_fields(line)
        referrer_index = fields_list.index('cs(Referer)')
        referrer_index -= 1
    if 'Chrome' in line:
        referrer_list.append(get_referrer_from_iis_line(line,referrer_index))
print(referrer_list)
