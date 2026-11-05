package com.ssafy.exam.model.service;


import java.util.List;

import com.ssafy.exam.model.dto.Car;
import com.ssafy.exam.model.dto.Member;

/*이 파일에서는 수정 할 부분이 없습니다. 
 * 다만, 제공된 프로젝트에서 추가로 기능을 확장해서 연습하고 싶다면, 수정하여 사용해도 무방합니다.*/

public interface CarService {
    Member login(String email, String password);
	List<Car> selectAll();
	int insert(Car car);
	Car selectByCode(String code);    
	int deleteByCode(String code);
}
