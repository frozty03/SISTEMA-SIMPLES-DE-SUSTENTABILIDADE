/*
Esse arquivo serve apenas para criação da tabela. Os
comandos create precisam ser rodados apenas uma vez
*/

# 1 - Cria a database
#create database pi1;

# 2 - criando as tabelas
use pi1;
# primeira tabela
create table usuario(
u_id int primary key auto_increment,
u_usuario varchar(50) not null,
u_senha varchar(50) not null,
u_nota decimal(10,2)
);

# segunda tabela
create table registro(
r_id int primary key auto_increment,
r_usuarioId int not null,
r_data date not null,
r_energia decimal(10,2) not null,
r_agua decimal(10,2) not null,
r_residuo decimal(10,2) not null,
r_transporte varchar(3) not null,
r_media decimal(10,2) not null
);

#visualização das tabelas, se necessário
select * from usuario;
select * from registro;