SELECT ins.name, ins.datetime
from (select animal_id, name, datetime from animal_ins) as ins
left outer join (select animal_id from animal_outs) as outs
on ins.animal_id = outs.animal_id
where outs.animal_id is null
order by ins.datetime
limit 3