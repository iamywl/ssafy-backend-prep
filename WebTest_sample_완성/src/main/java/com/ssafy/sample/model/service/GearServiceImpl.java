package com.ssafy.sample.model.service;

import java.sql.SQLException;
import java.util.List;

import com.ssafy.sample.model.dao.GearDao;
import com.ssafy.sample.model.dao.GearDaoImpl;
import com.ssafy.sample.model.dto.Gear;
import com.ssafy.sample.model.dto.Member;

public class GearServiceImpl implements GearService {
	private GearServiceImpl() {}
	
	private final GearDao dao = GearDaoImpl.getInstance();
	private static final GearService instance = new GearServiceImpl();
	
	public static GearService getInstance() {
		return instance;
	}

	@Override
	public Member login(String email, String password) {
		try {
			return dao.login(email, password);
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return null;
	}

	@Override
	public List<Gear> selectAll() {
		try {
			return dao.selectAll();
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return null;
	}

	@Override
	public int insert(Gear gear) {
		try {
			return dao.insert(gear);
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return 0;
	}

	@Override
	public Gear selectByCode(String code) {
		try {
			return dao.selectByCode(code);
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return null;
	}

	@Override
	public int deleteByCode(String code) {
		try {
			return dao.deleteByCode(code);
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return 0;
	}

}
