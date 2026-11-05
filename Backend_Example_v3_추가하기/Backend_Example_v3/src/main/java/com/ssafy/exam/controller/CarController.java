package com.ssafy.exam.controller;

import java.io.IOException;
import java.sql.SQLException;
import java.util.List;

import com.ssafy.exam.model.service.CarServiceImpl;
import com.ssafy.exam.model.dto.Car;
import com.ssafy.exam.model.dto.Member;
import com.ssafy.exam.model.service.CarService;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

 
@WebServlet({"/member", "/car"})   // 기억할것
public class CarController extends HttpServlet implements ControllerHelper {

	private final CarService mService = CarServiceImpl.getService();

	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		
			String action=getActionParameter(request, response);
			//System.out.println("test:" + action);
			
			switch(action) {
				case "index" -> redirect(request, response, "/index.jsp");
				case "login-form" -> forward(request, response, "/login-form.jsp");
				case "regist-form" -> forward(request, response, "/car/regist.jsp");
				case "car-list" -> list(request, response);
				case "detail" -> detail(request, response);
				case "delete" -> delete(request, response);
				case "logout" -> logout(request, response);
				default ->  response.sendError(HttpServletResponse.SC_NOT_FOUND); // 404 처리
			}
		}
	
	@Override
	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		
		String action=getActionParameter(request, response);
		switch(action) {
			case "index" -> redirect(request, response, "/index.jsp");
			case "login" -> login(request, response);
			case "regist" -> regist(request, response);
			case "delete" -> delete(request, response);
			default ->  response.sendError(HttpServletResponse.SC_NOT_FOUND); // 404 처리
		}
	}
	
	private void login(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
		// TODO Auto-generated method stub
		String email = request.getParameter("email");
		String pass = request.getParameter("pass");
		String rememberMe = request.getParameter("remember-me");     // 추가할것_2
		//System.out.println(email +"  " +pass);
		
		Member member;
		member = mService.login(email, pass);
		
		if(member != null) {
			//System.out.println(member.getName());
			
			//세션객체에 추가---------------------------------------------
			request.getSession().setAttribute("loginUser", member);      // 세션이름:  loginUser
			request.getSession().removeAttribute("alertMsg");
			//---------------------------------------------------------
			
			//쿠키에 추가------------------------------------------------ 추가하기_2
			if(rememberMe == null ) {
				setupCookie("rememberMe", "bye", 0, null, response);
			}else {
				setupCookie("rememberMe", email, 60 * 60 * 24 * 365, null, response);
			}
			//---------------------------------------------------------
			
			redirect(request, response, "/");
		}else {
			//System.out.println("fail");
			request.setAttribute("alertMsg", "로그인에 실패했습니다. 아이디와 비밀번호를 확인해주세요.");
			forward(request, response, "/login-form.jsp");
		}
	}

	private void logout(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
		// TODO Auto-generated method stub
		request.getSession().invalidate();
		redirect(request, response, "/");
	}
	
	private void regist(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
		String code=request.getParameter("code");
		String model=request.getParameter("model");
		int price=Integer.parseInt(request.getParameter("price"));
		String vendor=request.getParameter("vendor");
		String size=request.getParameter("size");
		
		Car car=new Car(code,model,price,vendor,size);
		mService.insert(car);
		
		response.sendRedirect(request.getContextPath() + "/car?action=car-list");
	}
	
	private void list(HttpServletRequest request, HttpServletResponse response) 
			throws ServletException, IOException {
		List<Car> carList=mService.selectAll();
		
		request.setAttribute("carlist", carList);    //리케스트객체명: carlist
		request.getRequestDispatcher("car/list.jsp").forward(request, response);
	}	
	
	private void detail(HttpServletRequest request, HttpServletResponse response) 
			throws ServletException, IOException {
		// TODO Auto-generated method stub
		String code=request.getParameter("code");
		
		Car car=mService.selectByCode(code);
		
		request.setAttribute("car", car);    //리케스트객체명: car
		request.getRequestDispatcher("car/detail.jsp").forward(request, response);
	}
	private void delete(HttpServletRequest request, HttpServletResponse response) 
			throws ServletException, IOException {
		// TODO Auto-generated method stub
		String code = request.getParameter("code");
		
		mService.deleteByCode(code);
		
		response.sendRedirect(request.getContextPath() + "/car?action=car-list");
	}
}
