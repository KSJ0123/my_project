--테이블 생성을 위한 sql
create table user(userid integer primary key autoincrement,username text not null,password text not null,email text not null,gender text check(gender  in ('male', 'female')),
    create_at timestamp default CURRENT_TIMESTAMP
);

--유저 제이터 삽입을 위한 sql
-- insert into user(username,password,email,gender)
-- values('test','123','test@gmail.com','male')

--테이블 삭제
-- drop table user;