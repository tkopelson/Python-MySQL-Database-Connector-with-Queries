create database Empresa;

use Empresa;


create table Departamentos (
id_d INTEGER, 
nombre_d char(40),
primary key (id_d)
);

create table Empleados ( 
id_e INTEGER, 
nombre_e char(40), 
id_d INTEGER, 
primary key (id_e),
constraint fke_d foreign key (id_d) references Departamentos(id_d)
);

create table Notas (
id_n INTEGER, 
tipo_n INTEGER, 
id_e INTEGER,
id_d INTEGER,
fecha char(50),
contenido char(100),
primary key (id_n),
constraint fkn_d foreign key (id_d) references Departamentos(id_d),
constraint fkn_e foreign key (id_e) references Empleados(id_e)
);

create table Comentarios (
id_n INTEGER, 
id_e INTEGER,
contenido char(100),
constraint fkc_n foreign key (id_n) references Notas(id_n),
constraint fkc_e foreign key (id_e) references Empleados(id_e)
);

create table Likes (
id_e INTEGER, 
id_n INTEGER,
id_l INTEGER,
constraint fkl_n foreign key (id_n) references Notas(id_n),
constraint fkl_e foreign key (id_e) references Empleados(id_e),
primary key (id_l)
);

insert into departamentos 
values (1,'Globant');

insert into empleados
values (1,'Matias',1);

insert into empleados 
values  (2,'Tomas K',1);

insert into empleados 
values  (3,'Tomas G',1);

insert into empleados 
values (4,'Claudio G',1);

insert into empleados 
values  (5,'Jean Claude',1);

insert into notas 
values (1,1,1,1,'19/04/2020','Puertas con picaporte');

insert into notas 
values(2,1,2,1,'11/03/2019','Mas papel higenico');

insert into likes 
values (1,1,1);

insert into likes 
values (2,1,2);

insert into likes 
values (3,1,3);

insert into likes 
values (4,1,4);

insert into likes 
values (5,1,5);


insert into empleados  
values (6,'Santiago Pedro',1);

insert into likes 
values (5,2,6);

insert into likes 
values (6,2,7);

insert into notas 
values (3,1,2,1,'19/04/2021','Ehhh Messi' );



select n.contenido ,count(l.id_n)
from likes l ,empleados e ,notas n 
where l.id_e =e.id_e and n.id_n = l.id_n
group by l.id_n 
order by count(l.id_n) desc limit 3;

/*Notas Comentadas*/

/*  
select n.contenido,count(c.id_n)
from comentarios c,empleados e,notas n
where c.id_e =e.id_e and n.id_n = c.id_n
group by c.id_n 
order count(c.id_n) desc limit 10;
*/

/*Empleados con mas notas*/

/*
select n.id_e,e.nombre_e ,count(n.id_n) 
from notas n ,empleados e 
where n.id_e =e.id_e 
group by n.id_e 
order by count(n.id_n) desc
*/

/*
select count(d.id_d)
from departamentos d 
where d.id_d=4
*/
