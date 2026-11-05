<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>정보 등록 페이지</title>
</head>
<body>
	<%@ include file="/header.jsp"%>
	<nav>
		<h1>등록 페이지</h1>

	</nav>
	<form action="${root}/car" method="post">
		<fieldset>
			<input type="hidden" name="action" value="regist"> <br>
			<label> 제품 코드 <input type="text" name="code" maxlength="15"></label>
			<br> <label> 모델 <input type="text" name="model"></label>
			<br> <label> 가격 <input type="number" name="price">만원
			</label> <br> <label> 브랜드 <input type="text" name="vendor"></label>
			<br> <label> 차량 크기 <select name="size">
					<option value="소형">소형</option>
					<option value="중형">중형</option>
					<option value="대형">대형</option>
			</select>
			</label> <br> <input type="submit" value="등록"> <br> <a
				href="${root }/car?action=car-list">목록으로</a>
		</fieldset>
	</form>
</body>
</html>
















