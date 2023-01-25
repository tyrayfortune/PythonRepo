SELECT * FROM dojos_and_ninjas.dojos;
insert into dojos(name)
values('seattle'), ('las vegas'), ('san jose');

DELETE from dojos;
SELECT * FROM dojos;

SELECT * FROM dojos;
insert into dojos(name)
values('boston'), ('reno'), ('sacramento');

select * from ninjas;
insert into ninjas(first_name, last_name, age, dojo_id)
values('tyray', 'fortune', 24, 1), ('jack', 'jhosnon', 30, 1), ('james', 'fredricksen', 50, 1);

select * from ninjas;
insert into ninjas(first_name, last_name, age, dojo_id)
values('tra', 'foun', 24, 2), ('jac', 'jhno', 30, 2), ('jme', 'fredkse', 50, 2);

select * from ninjas;
insert into ninjas(first_name, last_name, age, dojo_id)
values('trsdasa', 'foudsakn', 24, 3), ('jac', 'jhkkjno', 30, 3), ('jme', 'freddfgdfgkse', 50, 3);

select * from ninjas
where dojo_id = 1;

select * from ninjas
where dojo_id = 2;

select name from dojos
where dojos.id = (select dojo_id from ninjas order by id desc limit 1);




