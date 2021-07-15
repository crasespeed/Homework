subj = {}
with open('file_6.txt', 'r') as file_6:
    for line in file_6:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {subj}')


# import codecs
# import re
# subj = {}
# with codecs.open('file_6.txt', 'r', 'utf-8') as file_6:
#     for line in file_6:
#         subject, lecture, practice, lab = line.split()
#         my_list = lecture + practice + lab
#         subj[subject] = sum(map(int, re.findall(r'\d+', my_list)))
#     print(f'Общее количество часов по предмету - \n {subj}')