create table if not exists Persona (
	id integer primary key autoincrement,
	nombre varchar(256) not null,
	apellido varchar(256) not null,
	dni integer not null,
	fnac datetime not null);
	
