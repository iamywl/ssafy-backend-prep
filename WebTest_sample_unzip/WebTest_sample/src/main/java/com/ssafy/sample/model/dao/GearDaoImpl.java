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
	///////////////////////////////////////////////////////////////////////////////
	//------아래 메소드를 확인하고 TODO 부분의 내용을 확인하여 코드를 완성하세요.---------------//
	///////////////////////////////////////////////////////////////////////////////
	@Override
	public Member login(String email, String password) throws SQLException {
		Member member = null;
        Connection conn = null;
        PreparedStatement pstmt = null;
        ResultSet rs = null;
        //--[TODO] : sql 쿼리문을 완성하세요.
        String sql = "";

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
		
		String sql = "select * from gear";
		
		try {
			conn = DBUtil.getConnection();
			pstmt = conn.prepareStatement(sql);
			
			rs = pstmt.executeQuery();
			 /* [TODO]: ResultSet의 모든 행을 반복하며 Mobile 객체를 생성하여 list에 추가되도록 while 조건문(rs!=null 부분)을 수정하시오. */
			while(rs!=null) {
				Gear gear = new Gear();
				gear.setCode(rs.getString("code"));
				gear.setName(rs.getString("name"));
				gear.setPrice(Integer.parseInt(rs.getString("price")));
				gear.setBrand(rs.getString("brand"));
				gear.setColor(rs.getString("color"));
				list.add(gear);
			}
			
		}finally {
			DBUtil.close(rs, pstmt, conn);
		}
		return list;
	}

	@Override
	public int insert(Gear gear) throws SQLException {
		Connection conn = null;
		PreparedStatement pstmt = null;
		int cnt = 0;
		
		String sql  = "INSERT INTO gear (code, name, price, brand, color) VALUES (?, ?, ?, ?, ?)";
		
		try {
			conn = DBUtil.getConnection();
			pstmt = conn.prepareStatement(sql);
			
            /* [TODO]: 파라미터 바인딩 및 쿼리를 실행하는 코드를 완성하시오.*/

		}finally {
			DBUtil.close(pstmt, conn);
		}
		return cnt;
	}

}
