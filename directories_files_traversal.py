import os


for dir_name, subdir_list, file_list in os.walk('.'):
    print('Directory: {}'.format(dir_name))
    for file_name in file_list:
        print('\t' + file_name)
