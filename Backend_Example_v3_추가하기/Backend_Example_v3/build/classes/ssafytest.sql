create database if not exists `ssafytest`;
use `ssafytest`;

-- 1. Car 테이블 생성 및 더미 데이터 삽입
drop table if exists `cars`;

create table `cars` (
  `code` varchar(20) primary key not null,
  `model` varchar(20) not null,
  `price` int not null,
  `vendor` varchar(20) not null,
  `size` varchar(10) default '소형'
);

insert into `cars` (`code`, `model`, `price`, `vendor`, `size`) values
('ABC-1234', 'A6', 70000000, '아우디', '대형'),
('XYZ-5678', '코롤라', 36000000, '토요타', '소형'),
('DEF-9012', '머스탱', 60000000, '포드', '소형'),
('GHI-3456', '쏘나타', 31000000, '현대', '중형'),
('JKL-7890', '쏘렌토', 35000000, '기아', '대형');


-- 2. Member 테이블 생성 및 더미 데이터 삽입
drop table if exists `members`;

create table `members` (
  `mno` int auto_increment primary key,
  `name` varchar(30) not null,
  `email` varchar(50) not null,
  `password` varchar(20) not null,
  `role` varchar(20) default 'USER'
);

insert into `members` (`name`, `email`, `password`, `role`) values
('관리자', 'admin@ssafy.com', '1234', 'ADMIN'),
('싸피', 'ssafy@ssafy.com', '1234', 'USER');

commit;