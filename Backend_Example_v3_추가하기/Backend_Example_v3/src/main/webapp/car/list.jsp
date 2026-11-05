<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>목록 조회 페이지</title>
<style type="text/css">
table, th, td {
	border: 1px solid black;
	border-collapse: collapse;
}
</style>
</head>
<body>
	<%@ include file="/header.jsp"%>
	<h1>목록 조회 페이지</h1>

	<a href="${root }">메인 화면으로</a>
	<a href="${root }/car?action=regist-form">등록하기</a>
	<table>
		<thead>
			<tr>
				<th>제품 코드</th>
				<th>모델</th>
				<th>가격</th>
			</tr>
		</thead>
		<tbody>
			<c:forEach var="car"  items="${carlist }">
				<tr>
					<td><a href="${root }/car?action=detail&code=${car.code}">${car.code}</a></td>
					<td>${car.model }</td>
					<td>${car.price }만원</td>
				</tr>
			</c:forEach>
		</tbody>
	</table>
</body>
</html>