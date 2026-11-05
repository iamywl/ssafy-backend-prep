package com.ssafy.sample.model.service;


import java.util.List;

import com.ssafy.sample.model.dao.GearDao;
import com.ssafy.sample.model.dao.GearDaoImpl;
import com.ssafy.sample.model.dto.Gear;
import com.ssafy.sample.model.dto.Member;

public class GearServiceImpl implements GearService {
	private GearServiceImpl() {
		
	}
	private GearDao dao = GearDaoImpl.getInstance();
	private static GearService instance = new GearServiceImpl();
	public static GearService getInstance() {
		return instance;
	}
	///////////////////////////////////////////////////////
	//------아래 메소드를 확인하고 코드를 완성하세요.---------------//
	///////////////////////////////////////////////////////
	@Override
	public Member login(String email, String password) {
		return null;
	}

	@Override
	public List<Gear> selectAll() {
		return null;
	}

	@Override
	public int insert(Gear gear) {
		return 0;
	}

}
