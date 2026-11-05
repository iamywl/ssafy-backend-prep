package com.ssafy.sample.model.service;

import java.util.List;
import com.ssafy.sample.model.dto.Gear;
import com.ssafy.sample.model.dto.Member;

public interface GearService {
    Member login(String email, String password);
    List<Gear> selectAll();
    int insert(Gear gear);
    Gear selectByCode(String code);
    int deleteByCode(String code);
}
