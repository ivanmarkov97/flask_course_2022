select first_name,
       last_name,
       birthday,
       code
from decanat.students
where first_name='$first_name' and
      last_name='$last_name' and
      code='$code'
