# The dictionary will be something like:
# {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Often, it's a good idea to hold onto a max_count variable.
# Update it when you find a teacher with more classes than
# the current count. Better hold onto the teacher name somewhere
# too!
#
# Your code goes below here.


def most_classes(teacher_dict):
    max_count = 0
    teacher = ''
    for name in teacher_dict:
        class_num = len(teacher_dict[name])
        if class_num > max_count:
            teacher = name
            max_count = class_num
    print(teacher)
    return teacher


def num_teachers(teacher_dict):
    print(len(teacher_dict))
    return len(teacher_dict)


def stats(teacher_dict):
    new_list = []
    for teacher in teacher_dict:
        teacher_list = [teacher, len(teacher_dict[teacher])]
        new_list.append(teacher_list)
    print(new_list)
    return new_list


def courses(teacher_dict):
    courses_list = []
    for teacher in teacher_dict:
        courses_list += teacher_dict[teacher]
    print(courses_list)
    return courses_list


my_dict = {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
           'Kenneth Love': ['Python Basics', 'Python Collections']}


most_classes(my_dict)
num_teachers(my_dict)
stats(my_dict)
courses(my_dict)
