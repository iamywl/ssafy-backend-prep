<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core"%>
<c:set var="root" value="${pageContext.servletContext.contextPath}" />
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8" />
<title>로그인 페이지</title>
</head>
<body>
	<%@ include file="/header.jsp"%>
	<div class="container">
		<h1>로그인 페이지</h1>
		<form action="${root}/gear" method="post">
			<input type="hidden" name="action" value="login">
			<fieldset>
				<div>
					<label for="email">이메일 </label> 
					<input type="email" id="email" name="email" value="${cookie.rememberEmail.value}" placeholder="email을 입력하세요" required>
				</div>
				<div>
					<label for="pass">비밀번호 </label>
					<input type="password" id="pass" name="pass" required/> <br>
				</div>
				<div>
					<label> 
						<input type="checkbox" name="remember-me" ${not empty cookie.rememberEmail ? 'checked' : ''}> 아이디 기억하기
					</label>
				</div>
				<input type="submit" value="로그인"> <br>
			</fieldset>
		</form>
	</div>
</body>
</html>
