<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core"%>
<c:set var="root" value="${pageContext.servletContext.contextPath}" />
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
th, td {
	padding: 5px 10px;
}
</style>
</head>
<body>
	<%@ include file="/header.jsp" %>
	<h1>목록 조회 페이지</h1>

	<p>
		<a href="${root}/gear?action=index">메인 화면으로</a> | 
		<a href="${root}/gear?action=regist-form">등록하기</a>
	</p>
	<table>
		<thead>
			<tr>
				<th>코드 (클릭 시 상세조회)</th>
				<th>제품명</th>
				<th>제품 가격</th>
				<th>제품 색</th>
				<th>관리</th>
			</tr>
		</thead>
		<tbody>
			<c:forEach var="gear" items="${gearList}">
				<tr>
					<td><a href="${root}/gear?action=detail&code=${gear.code}">${gear.code}</a></td>
					<td>${gear.name}</td>
					<td>${gear.price}</td>
					<td>${gear.color}</td>
					<td><a href="${root}/gear?action=delete&code=${gear.code}" onclick="return confirm('삭제하시겠습니까?');">삭제</a></td>
				</tr>
			</c:forEach>
		</tbody>
	</table>
</body>
</html>
