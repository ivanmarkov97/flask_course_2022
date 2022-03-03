select first_name,
       last_name,
       birth_date,
       code
from decanat
where group_index='$group_index'
order by code;
