package com.ssafy.sample.model.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import com.ssafy.sample.model.dto.Gear;
import com.ssafy.sample.model.dto.Member;
import com.ssafy.sample.util.DBUtil;

public class GearDaoImpl implements GearDao {
	
	private GearDaoImpl() {};
	private static GearDao instance = new GearDaoImpl();
	public static GearDao getInstance() {
		return instance;
	}

	@Override
	public Member login(String email, String password) throws SQLException {
		Member member = null;
        Connection conn = null;
        PreparedStatement pstmt = null;
        ResultSet rs = null;
        
        String sql = "SELECT name, email, password, role FROM member WHERE email = ? AND password = ?";

        try {
            conn = DBUtil.getConnection();
            pstmt = conn.prepareStatement(sql);
            
            pstmt.setString(1, email);
            pstmt.setString(2, password);

            rs = pstmt.executeQuery();

            if (rs.next()) {
                member = new Member();
                member.setName(rs.getString("name"));
                member.setEmail(rs.getString("email"));
                member.setPassword(rs.getString("password"));
                member.setRole(rs.getString("role"));
            }
        } finally {
            DBUtil.close(rs, pstmt, conn);
        }
        return member;
	}

	@Override
	public List<Gear> selectAll() throws SQLException {
		List<Gear> list = new ArrayList<>();
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		
		String sql = "SELECT code, name, price, brand, color FROM gear";
		
		try {
			conn = DBUtil.getConnection();
			pstmt = conn.prepareStatement(sql);
			
			rs = pstmt.executeQuery();
			while (rs.next()) {
				Gear gear = new Gear();
				gear.setCode(rs.getString("code"));
				gear.setName(rs.getString("name"));
				gear.setPrice(Integer.parseInt(rs.getString("price")));
				gear.setBrand(rs.getString("brand"));
				gear.setColor(rs.getString("color"));
				list.add(gear);
			}
			
		} finally {
			DBUtil.close(rs, pstmt, conn);
		}
		return list;
	}

	@Override
	public int insert(Gear gear) throws SQLException {
		Connection conn = null;
		PreparedStatement pstmt = null;
		int cnt = 0;
		
		String sql = "INSERT INTO gear (code, name, price, brand, color) VALUES (?, ?, ?, ?, ?)";
		
		try {
			conn = DBUtil.getConnection();
			pstmt = conn.prepareStatement(sql);
			
			pstmt.setString(1, gear.getCode());
			pstmt.setString(2, gear.getName());
			pstmt.setInt(3, gear.getPrice());
			pstmt.setString(4, gear.getBrand());
			pstmt.setString(5, gear.getColor());
			
			cnt = pstmt.executeUpdate();
		} finally {
			DBUtil.close(pstmt, conn);
		}
		return cnt;
	}

	@Override
	public Gear selectByCode(String code) throws SQLException {
		Gear gear = null;
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		
		String sql = "SELECT code, name, price, brand, color FROM gear WHERE code = ?";
		
		try {
			conn = DBUtil.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, code);
			rs = pstmt.executeQuery();
			
			if (rs.next()) {
				gear = new Gear();
				gear.setCode(rs.getString("code"));
				gear.setName(rs.getString("name"));
				gear.setPrice(Integer.parseInt(rs.getString("price")));
				gear.setBrand(rs.getString("brand"));
				gear.setColor(rs.getString("color"));
			}
		} finally {
			DBUtil.close(rs, pstmt, conn);
		}
		return gear;
	}

	@Override
	public int deleteByCode(String code) throws SQLException {
		Connection conn = null;
		PreparedStatement pstmt = null;
		int cnt = 0;
		
		String sql = "DELETE FROM gear WHERE code = ?";
		
		try {
			conn = DBUtil.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, code);
			cnt = pstmt.executeUpdate();
		} finally {
			DBUtil.close(pstmt, conn);
		}
		return cnt;
	}

}
