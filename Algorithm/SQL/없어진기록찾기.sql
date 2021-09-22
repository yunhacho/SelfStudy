SELECT outs.animal_id, outs.name
from (select animal_id, name from animal_outs) as outs
left outer join (select animal_id from animal_ins) as ins
on outs.animal_id = ins.animal_id
where ins.animal_id is null;
