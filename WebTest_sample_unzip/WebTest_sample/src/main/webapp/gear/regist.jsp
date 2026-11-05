<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>정보 등록 페이지</title>
</head>
<body>
	<h1>등록 페이지</h1>

	<form action="#" method="#">

		<fieldset>
			<label> 제품 코드 <input type="text" name="code" maxlength="15"></label>
			<br> <label> 제품명 <input type="text" name="name"></label>
			<br> <label> 제품 가격 <input type="number" name="price"></label>
			<br> <label> 제품 브랜드 <input type="text" name="brand"></label>
			<br> <label> 제품색 <select name="color">
					<option value="블랙">블랙</option>
					<option value="아이보리">아이보리</option>
					<option value="카키">카키</option>
			</select>
			</label> <br> <input type="submit" value="등록"> <br> <a
				href="#">목록으로</a>
		</fieldset>
	</form>
</body>
</html>