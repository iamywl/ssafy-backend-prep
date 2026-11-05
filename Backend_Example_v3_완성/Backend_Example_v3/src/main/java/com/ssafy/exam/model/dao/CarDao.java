package com.ssafy.exam.model.dao;

import java.sql.SQLException;
import java.util.List;

import com.ssafy.exam.model.dto.Member;
import com.ssafy.exam.model.dto.Car;


/*이 파일에서는 수정 할 부분이 없습니다. 
 * 다만, 제공된 프로젝트에서 추가로 기능을 확장해서 연습하고 싶다면, 수정하여 사용해도 무방합니다.*/

public interface CarDao {
    Member login(String email, String password) throws SQLException;
	List<Car> selectAll() throws SQLException;
	int insert(Car car) throws SQLException;
	Car selectByCode(String code) throws SQLException;   
	int deleteByCode(String code) throws SQLException;
}
