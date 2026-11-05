package com.ssafy.sample.model.dao;

import java.sql.SQLException;
import java.util.List;

import com.ssafy.sample.model.dto.Gear;
import com.ssafy.sample.model.dto.Member;


/////////////////////////////////////
/// --- 수정할 코드가 없습니다.--------///
/////////////////////////////////////
public interface GearDao {
    Member login(String email, String password) throws SQLException;
    List<Gear> selectAll() throws SQLException;
    int insert(Gear gear) throws SQLException;
}
