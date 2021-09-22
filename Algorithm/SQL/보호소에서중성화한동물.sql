SELECT outs.animal_id, outs.animal_type, outs.name
from (select animal_id, name, animal_type, sex_upon_outcome from animal_outs where substr(sex_upon_outcome,1,6)!='Intact') as outs inner join
(select animal_id, sex_upon_intake from animal_ins where substr(sex_upon_intake,1,6)='Intact') as ins
on ins.animal_id = outs.animal_id