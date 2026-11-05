package com.ssafy.sample.model.dto;

/////////////////////////////////////
/// --- 수정할 코드가 없습니다.--------///
/////////////////////////////////////
public class Member{

    private int mno;
    private String name;
    private String email;
    private String password;
    private String role;

    // 기본 생성자
    public Member() {}

    // 로그인 검증 및 등록용 생성자 (mno 제외)
    public Member(String name, String email, String password) {
        this.name = name;
        this.email = email;
        this.password = password;
    }

    // 전체 필드 생성자
    public Member(int mno, String name, String email, String password, String role) {
        this.mno = mno;
        this.name = name;
        this.email = email;
        this.password = password;
        this.role = role;
    }

    // Getter / Setter
    public int getMno() {
        return mno;
    }

    public void setMno(int mno) {
        this.mno = mno;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }

    @Override
    public String toString() {
        return "Member [mno=" + mno + ", name=" + name + ", email=" + email + ", role=" + role + "]";
    }
}