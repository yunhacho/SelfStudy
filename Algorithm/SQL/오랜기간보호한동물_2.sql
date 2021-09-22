-- 코드를 입력하세요
select animal_id, name
from (select ins.animal_id, ins.name, (outs.datetime-ins.datetime) as time_interval
      from ((select animal_id, name, datetime from animal_ins) as ins
            inner join (select animal_id, name, datetime from animal_outs) as outs 
             on ins.animal_id = outs.animal_id)) as result
where time_interval>0
order by time_interval desc
limit 2