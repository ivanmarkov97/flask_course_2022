select exams.name,
       exams.mark,
       student.first_name,
       student.last_name,
       student.birth_day,
       student.code
from exams
left join (
        select first_name,
               last_name,
               birth_day
               code
        from student
        where code='$code'
    ) student
    on exams.student_code = student.code
