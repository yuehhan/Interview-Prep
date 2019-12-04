import os

os.chdir('/path/')

#create a script to rearrange downloaded episodes to a TV show

for f in os.listdir():
    # If .DS_Store file is created, ignore it
    if f == '.DS_Store':
        continue

    file_name, file_ext = os.path.splitext(f)

    f_title, f_course, f_number = file_name.split('-')

    f_title = f_title.strip()
    f_course = f_course.strip()
    # f_number = f_number.strip()

    #need to use zfill so that file 10 will be in the right place
    f_number = f_number.strip()[1:].zfill(2)

    print('{}-{}{}'.format(f_number, f_title.strip(), file_ext.strip()))

    #create a new name for these file so they are all organized
    new_name = '{}-{}{}'.format(file_num, file_title, file_ext)

    os.rename(fn, new_name)
