package com.ssafy.sample.model.service;

import java.util.List;

import com.ssafy.sample.model.dto.Gear;
import com.ssafy.sample.model.dto.Member;

/////////////////////////////////////
/// --- 수정할 코드가 없습니다.--------///
/////////////////////////////////////
public interface GearService {


    Member login(String email, String password);
    List<Gear> selectAll();
    int insert(Gear gear);
}
