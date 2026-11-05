<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>상세 정보 페이지</title>
<style type="text/css">
table, th, td {
	border: 1px solid black;
	border-collapse: collapse;
}
</style>
</head>
<body>
	<%@ include file="/header.jsp"%>
	<h1>상세 정보 페이지</h1>

	<a href="${root }/car?action=car-list">목록으로</a>
	<table>
		<tr>
			<th>제품 코드</th>
			<td>${car.code }</td>
		</tr>
		<tr>
			<th>모델</th>
			<td>${car.model }</td>
		</tr>
		<tr>
			<th>가격</th>
			<td>${car.price }</td>
		</tr>
		<tr>
			<th>브랜드</th>
			<td>${car.vendor }</td>
		</tr>
		<tr>
			<th>차량크기</th>
			<td>${car.size }</td>
		</tr>
	</table>
	<a href="${root}/car?action=delete&code=${car.code}">삭제</a>
</body>
</html>





