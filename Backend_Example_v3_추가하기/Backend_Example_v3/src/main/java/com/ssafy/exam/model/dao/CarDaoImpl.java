package com.ssafy.exam.model.dao;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import com.ssafy.exam.model.dto.Member;
import com.ssafy.exam.util.DBUtil;
import com.ssafy.exam.model.dto.Car;

/*
 * 초기 정보 파일 입출력 관련 처리는 완성된 형태로 제공된다.*/
/* 싱글톤 형태로 완성되어 제공 됨*/
public class CarDaoImpl implements CarDao {
	private static final CarDaoImpl instance = new CarDaoImpl();
	
	private CarDaoImpl() {
	}
	
	public static CarDaoImpl getInstance() {
		return instance;
	}
	
	///////////////////////////////////////////////////////
	//------아래 메소드를 확인하고 코드를 완성하세요.---------------//
	///////////////////////////////////////////////////////
	/// 
	@Override
	public Member login(String email, String password) throws SQLException {
		// TODO Auto-generated method stub
		Member member=null;
		Connection conn=null;
		PreparedStatement pstmt = null;
		ResultSet rs=null;
		
		String sql="SELECT mno, name, email, password, role FROM members WHERE email = ? AND password = ?";
		
		try{
			conn = DBUtil.getConnection();
			pstmt=conn.prepareStatement(sql);
			
			pstmt.setString(1, email);
			pstmt.setString(2, password);
			
			rs=pstmt.executeQuery();
			
			if(rs.next()) {
				member = new Member();
				member.setMno(rs.getInt("mno"));
				member.setName(rs.getString("name"));
                member.setEmail(rs.getString("email"));
                member.setPassword(rs.getString("password"));
                member.setRole(rs.getString("role"));
			}
		}finally {
			DBUtil.close(rs, pstmt, conn);
		}
		return member;
	}

	@Override
	public List<Car> selectAll() throws SQLException {
		// TODO Auto-generated method stub
		Connection conn=null;
		PreparedStatement pstmt = null;
		ResultSet rs=null;
		List<Car> list=new ArrayList<>();
		
		String sql="select * from cars";
		
		try {
			conn = DBUtil.getConnection();
			pstmt=conn.prepareStatement(sql);
			rs=pstmt.executeQuery();
			
			while(rs.next()) {
				Car car=new Car();
				car.setCode(rs.getString("code"));
				car.setModel(rs.getString("model"));
				car.setPrice(rs.getInt("price"));
				car.setVendor(rs.getString("vendor"));
				car.setSize(rs.getString("size"));
				
				list.add(car);
			}
		}finally {
			DBUtil.close(rs, pstmt, conn);
		}
		return list;
	}

	@Override
	public int insert(Car car) throws SQLException {
		// TODO Auto-generated method stub
		int result=0;
		Connection conn=null;
		PreparedStatement pstmt = null;
		
		String sql="insert into cars(code,model,price,vendor,size) values(?,?,?,?,?) ";
		
		try {
			conn = DBUtil.getConnection();
			pstmt=conn.prepareStatement(sql);
			
			pstmt.setString(1, car.getCode());
			pstmt.setString(2, car.getModel());
			pstmt.setInt(3, car.getPrice());
			pstmt.setString(4, car.getVendor());
			pstmt.setString(5, car.getSize());
			
			result=pstmt.executeUpdate();

		}finally {
			DBUtil.close(pstmt, conn);
		}		
		return result;
	}

	@Override
	public Car selectByCode(String code) throws SQLException {
		// TODO Auto-generated method stub
		Connection conn=null;
		PreparedStatement pstmt = null;
		ResultSet rs=null;
		Car car=null; 
		
		String sql="select code,model,price,vendor,size from cars where code=?";
		
		try {
			conn = DBUtil.getConnection();
			pstmt=conn.prepareStatement(sql);
			
			pstmt.setString(1, code);
			rs=pstmt.executeQuery();
			
			if(rs.next()) {
				car=new Car();
				car.setCode(rs.getString("code"));
				car.setModel(rs.getString("model"));
				car.setPrice(rs.getInt("price"));
				car.setVendor(rs.getString("vendor"));
				car.setSize(rs.getString("size"));
				
			}
		}finally {
			DBUtil.close(rs, pstmt, conn);
		}
		return car;
	}

	@Override
	public int deleteByCode(String code) throws SQLException {
		int result = 0;
		Connection conn = null;
		PreparedStatement pstmt = null;
		
		String sql = "delete from cars where code = ?";
		
		try {
			conn = DBUtil.getConnection();
			pstmt = conn.prepareStatement(sql);
			
			pstmt.setString(1, code);
			
			result = pstmt.executeUpdate();
		} finally {
			DBUtil.close(pstmt, conn);
		}
		return result;
	}
}



















