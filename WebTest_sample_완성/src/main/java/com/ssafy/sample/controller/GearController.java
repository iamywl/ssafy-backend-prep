package com.ssafy.sample.controller;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.util.List;

import com.ssafy.sample.model.dto.Gear;
import com.ssafy.sample.model.dto.Member;
import com.ssafy.sample.model.service.GearService;
import com.ssafy.sample.model.service.GearServiceImpl;

@WebServlet({"/gear", "/member"})
public class GearController extends HttpServlet implements ControllerHelper {
	private static final long serialVersionUID = 1L;

	private final GearService service = GearServiceImpl.getInstance();
	
	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		String action = getActionParameter(request, response);
		
		switch (action) {
			case "index" -> redirect(request, response, "/index.jsp");
			case "list" -> list(request, response);
			case "detail" -> detail(request, response);
			case "delete" -> delete(request, response);
			case "regist-form" -> forward(request, response, "/gear/regist.jsp");
			case "login-form" -> forward(request, response, "/login-form.jsp");
			case "logout" -> logout(request, response);
			default -> response.sendError(HttpServletResponse.SC_NOT_FOUND);
		}
	}

	@Override
	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		String action = getActionParameter(request, response);
		
		switch (action) {
			case "regist" -> regist(request, response);
			case "login" -> login(request, response);
			case "delete" -> delete(request, response);
			default -> response.sendError(HttpServletResponse.SC_NOT_FOUND);
		}
	}

	private void list(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		List<Gear> gearList = service.selectAll();
		request.setAttribute("gearList", gearList);
		forward(request, response, "/gear/list.jsp");
	}

	private void detail(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		String code = request.getParameter("code");
		Gear gear = service.selectByCode(code);
		request.setAttribute("gear", gear);
		forward(request, response, "/gear/detail.jsp");
	}

	private void delete(HttpServletRequest request, HttpServletResponse response)
			throws IOException {
		String code = request.getParameter("code");
		service.deleteByCode(code);
		redirect(request, response, "/gear?action=list");
	}

	private void regist(HttpServletRequest request, HttpServletResponse response)
			throws IOException {
		String code = request.getParameter("code");
		String name = request.getParameter("name");
		int price = Integer.parseInt(request.getParameter("price"));
		String brand = request.getParameter("brand");
		String color = request.getParameter("color");

		Gear gear = new Gear(code, name, price, brand, color);
		service.insert(gear);

		redirect(request, response, "/gear?action=list");
	}

	private void login(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		String email = request.getParameter("email");
		String pass = request.getParameter("pass");
		String rememberMe = request.getParameter("remember-me");

		Member member = service.login(email, pass);

		if (member != null) {
			request.getSession().setAttribute("loginUser", member);

			if (rememberMe != null) {
				setupCookie("rememberEmail", email, 60 * 60 * 24 * 7, request.getContextPath(), response);
			} else {
				setupCookie("rememberEmail", "", 0, request.getContextPath(), response);
			}

			redirect(request, response, "/gear?action=index");
		} else {
			request.setAttribute("alertMsg", "로그인 실패! 이메일과 비밀번호를 확인하세요.");
			forward(request, response, "/login-form.jsp");
		}
	}

	private void logout(HttpServletRequest request, HttpServletResponse response)
			throws IOException {
		request.getSession().invalidate();
		redirect(request, response, "/gear?action=index");
	}
}
