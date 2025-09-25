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


def create_students(**kwargs):
    try:
        name, age, gender = kwargs.get('name', 'нет данных'), kwargs.get('age', 0), kwargs.get('gender', 'N') 
        with open('students.txt', 'a', encoding='utf-8') as file:  
            file.write(f"\n{name}, {gender}, {age}")
        print(f'Студент : {name} успешно сохранен')  
    except:
        print(f'Ошибка при сохранении')

def select_student_by_first_letter(fl, student_list):
    #rez = [student for student in student_list if student['name'].lower().startswith(fl.lower())]
    rez = list(filter(lambda x: x['name'].lower().startswith(str(fl).lower()), 
            student_list))
    return(rez)


if __name__ == '__main__':
    rez = read_students(src)
    #count_gend = count_gender(rez)
    student = {'name': 'Фролова Анна Михайловна',
                'age': 22, 
                'gender': 'ж'}
    print(select_student_by_first_letter('м', rez))
