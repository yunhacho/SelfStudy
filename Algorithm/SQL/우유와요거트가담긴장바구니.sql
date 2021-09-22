select distinct milk.cart_id
from (select cart_id, name from cart_products where name='Milk') as milk
INNER JOIN (select cart_id, name from cart_products where name='Yogurt') as yogurt
on milk.cart_id = yogurt.cart_id
order by milk.cart_id