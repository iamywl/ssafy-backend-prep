-- 데이터베이스 생성 및 문자셋 설정
CREATE DATABASE IF NOT EXISTS ssafy_gear DEFAULT CHARACTER SET utf8mb4;
USE ssafy_gear;

-- 1. 기존 테이블 삭제 (외래키 제약조건 고려 순서 배치)
DROP TABLE IF EXISTS gear;
DROP TABLE IF EXISTS member;

-- 2. 사용자 테이블 (member) 생성
-- 로그인/로그아웃 및 세션 사용자 식별용
CREATE TABLE member (
    mno INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL,
    role VARCHAR(20) DEFAULT 'USER'
);

-- 3. 캠핑 용품 정보 테이블 (gear) 생성
CREATE TABLE gear (
    code VARCHAR(30) PRIMARY KEY,     -- 제품 고유 코드 (직접 입력받는 문자열 PK)
    name VARCHAR(50) NOT NULL,        -- 제품명
    price INT NOT NULL,               -- 가격
    brand VARCHAR(30) NOT NULL,       -- 제조사 / 브랜드
    color VARCHAR(30) NOT NULL        -- 색상
);

-- 4. 초기 테스트 데이터 등록

-- [1] 사용자 계정 (관리자 및 일반 사용자)
INSERT INTO member (name, email, password, role) 
VALUES ('관리자', 'admin@ssafy.com', '1234', 'ADMIN');

INSERT INTO member (name, email, password, role) 
VALUES ('김싸피', 'ssafy@ssafy.com', '1234', 'USER');

-- [2] 초기 용품 목록 3건 (화면 목록 조회 테스트용)
INSERT INTO gear (code, name, price, brand, color) 
VALUES ('CP-TN-001', '랜드락 투룸 텐트', 1850000, '스노우피크', '아이보리');

INSERT INTO gear (code, name, price, brand, color) 
VALUES ('CP-CH-102', '릴렉스 체어 블랙', 79000, '콜맨', '블랙');

INSERT INTO gear (code, name, price, brand, color) 
VALUES ('CP-ST-505', '윈드 블록 스토브', 135000, '코베아', '카키');

COMMIT;