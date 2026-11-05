package com.ssafy.exam.model.service;


import java.sql.SQLException;
import java.util.List;

import com.ssafy.exam.model.dao.CarDaoImpl;
import com.ssafy.exam.model.dao.CarDao;
import com.ssafy.exam.model.dto.Member;
import com.ssafy.exam.model.dto.Car;


public class CarServiceImpl implements CarService {
	/*싱글톤 형태로 완성되어 제공 됨*/
    private static CarServiceImpl service = new CarServiceImpl();

    private CarServiceImpl() {
    }

    public static CarServiceImpl getService() {
        return service;
    }
	///////////////////////////////////////////////////////
	//------아래 메소드를 확인하고 코드를 완성하세요.---------------//
	///////////////////////////////////////////////////////

    private CarDao carDao = CarDaoImpl.getInstance();    //Service를 Dao랑 연결
    
	@Override
	public Member login(String email, String password){
		// TODO Auto-generated method stub
		try {
			return carDao.login(email, password);
		}catch(SQLException e) {
			e.printStackTrace();
		}
		return null;
	}

	@Override
	public List<Car> selectAll(){
		// TODO Auto-generated method stub
		try {
			return carDao.selectAll();
		}catch(SQLException e){
			e.printStackTrace();
		}
		return null;
	}

	@Override
	public int insert(Car car){
		// TODO Auto-generated method stub
		try {
			return carDao.insert(car);
		}catch(SQLException e){
			e.printStackTrace();
		}
		return 0;
	}

	@Override
	public Car selectByCode(String code) {
		// TODO Auto-generated method stub
		try {
			return carDao.selectByCode(code);
		}catch(SQLException e){
			e.printStackTrace();
		}
		return null;
	}

	@Override
	public int deleteByCode(String code) {
		// TODO Auto-generated method stub
		try {
			return carDao.deleteByCode(code);
		}catch(SQLException e){
			e.printStackTrace();
		}
		return 0;
	}


    



}
