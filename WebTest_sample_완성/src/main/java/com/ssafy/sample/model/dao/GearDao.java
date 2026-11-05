package com.ssafy.sample.model.dao;

import java.sql.SQLException;
import java.util.List;

import com.ssafy.sample.model.dto.Gear;
import com.ssafy.sample.model.dto.Member;

public interface GearDao {
    Member login(String email, String password) throws SQLException;
    List<Gear> selectAll() throws SQLException;
    int insert(Gear gear) throws SQLException;
    Gear selectByCode(String code) throws SQLException;
    int deleteByCode(String code) throws SQLException;
}
