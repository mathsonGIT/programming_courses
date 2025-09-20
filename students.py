def parsing_string(str):
    parts = str.split(',')
    #print(parts)
    
    student_info = {
        "name": parts[0].strip(),
        "gender": parts[1].strip(),
        "age": int(parts[2].strip())
    }
    
    return(student_info)

src = 'students.txt'
def read_students(file):
    rezults = []
    with open(file, 'r', encoding='utf-8') as st_file:
        for line in st_file:
            rezults.append(parsing_string(line))
    return(rezults)

def count_gender(stud_list):
    grouped_students = {'м': 0, 'ж': 0}

    for student in stud_list:
        grouped_students[student['gender']] += 1   
    return(grouped_students)    


rez = read_students(src)
count_gend = count_gender(rez)
print(count_gend)