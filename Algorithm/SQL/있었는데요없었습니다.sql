SELECT ins.animal_id, ins.name
from (select animal_id, name, datetime from animal_ins) as ins
left join (select animal_id, datetime from animal_outs) as outs
on ins.animal_id = outs.animal_id
where ins.datetime > outs.datetime
order by ins.datetime