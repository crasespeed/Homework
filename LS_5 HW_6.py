subj = {}
with open('file_6.txt', 'r') as file_6:
    for line in file_6:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {subj}')

