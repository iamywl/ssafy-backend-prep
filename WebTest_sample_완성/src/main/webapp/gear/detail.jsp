<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core"%>
<c:set var="root" value="${pageContext.servletContext.contextPath}" />
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>제품 상세 정보</title>
<style type="text/css">
table, th, td {
	border: 1px solid black;
	border-collapse: collapse;
}
th, td {
	padding: 8px 14px;
}
</style>
</head>
<body>
	<%@ include file="/header.jsp" %>
	<h1>제품 상세 조회</h1>

	<c:if test="${empty gear}">
		<p>해당 제품 정보를 찾을 수 없습니다.</p>
	</c:if>
	<c:if test="${not empty gear}">
		<table>
			<tr>
				<th>제품 코드</th>
				<td>${gear.code}</td>
			</tr>
			<tr>
				<th>제품명</th>
				<td>${gear.name}</td>
			</tr>
			<tr>
				<th>가격</th>
				<td>${gear.price} 원</td>
			</tr>
			<tr>
				<th>브랜드</th>
				<td>${gear.brand}</td>
			</tr>
			<tr>
				<th>색상</th>
				<td>${gear.color}</td>
			</tr>
		</table>

		<p style="margin-top: 15px;">
			<a href="${root}/gear?action=list">목록으로</a> | 
			<a href="${root}/gear?action=delete&code=${gear.code}" onclick="return confirm('정말 삭제하시겠습니까?');">삭제하기</a>
		</p>
	</c:if>
</body>
</html>
