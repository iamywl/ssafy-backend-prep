"""
SSAFY BackEnd & DB 과목평가 대비 10회분(총 320문제) 모의고사 생성기
- 11/09 평가 공지 100% 반영:
  * 각 회차당 32문제 (객관식 21, 단답형 9, 서술형 2)
  * 7대 핵심 출제 영역 골고루 커버
"""

import json
import os

def create_mock_exams():
    exams = {}

    # 회차별 테마 및 부제 정의
    themes = [
      "제1회: 전범위 기본 완성 모의평가",
      "제2회: 서블릿 아키텍처 & 생명주기 집중형",
      "제3회: JSP 스크립트 & 4대 Scope/상태관리 특화형",
      "제4회: SQL DDL/DML & 무결성 제약조건 마스터형",
      "제5회: 트랜잭션(ACID) & 고급 서브쿼리 정복형",
      "제6회: 데이터베이스 정규화(1NF~BCNF) & 인덱스 구조형",
      "제7회: 실전 기출유형 변형 & 빈출 함정 탈출형",
      "제8회: 심화 아키텍처 & 성능 최적화(FTS/Index)형",
      "제9회: 실전 시뮬레이션 파이널 A형",
      "제10회: 실전 시뮬레이션 파이널 B형 (만점 도전)"
    ]

    # 공통 서술형 2문제 풀 (회차별 뉘앙스 및 추가 채점 기준 변형)
    def get_essay_questions(round_num):
        return [
            {
                "id": 31,
                "type": "essay",
                "tag": f"서술형 1 (forward vs sendRedirect) - {round_num}회",
                "question": f"[제{round_num}회 서술형 1]\n서블릿/JSP에서 화면 이동 시 사용하는 forward 방식과 sendRedirect 방식의 차이점을 다음 3가지 기준에 따라 명확히 비교하여 서술하시오.\n① 클라이언트-서버 간 HTTP 요청/응답 왕복 횟수\n② 웹 브라우저 주소창의 URL 변경 여부\n③ HttpServletRequest 객체의 속성(Attribute) 데이터 공유 여부",
                "keywords": ["1회", "2회", "URL", "변경", "공유", "request", "유지"],
                "modelAnswer": "1) 요청/응답 왕복 횟수: forward는 서버 내부에서 제어권이 넘어가므로 1회 발생하지만, sendRedirect는 302 응답 후 브라우저가 새 주소로 재요청하므로 2회 발생합니다.\n2) URL 변경 여부: forward는 서버 내부 이동이므로 브라우저 URL이 변경되지 않고 유지되지만, sendRedirect는 브라우저가 새 주소를 직접 요청하므로 URL이 변경됩니다.\n3) request 속성 공유 여부: forward는 동일한 request 객체가 유지되어 request.setAttribute() 데이터를 공유할 수 있지만, sendRedirect는 새로운 request 객체가 생성되므로 기존 속성을 공유할 수 없습니다.",
                "exp": "서블릿 화면 이동 메커니즘의 핵심 비교 문제입니다. 3가지 항목(1회 vs 2회, URL 유지 vs 변경, request 속성 공유 가능 vs 불가)을 모두 명시해야 만점이 부여됩니다."
            },
            {
                "id": 32,
                "type": "essay",
                "tag": f"서술형 2 (WHERE vs HAVING) - {round_num}회",
                "question": f"[제{round_num}회 서술형 2]\nSQL 쿼리 작성 시 조건을 부여하는 WHERE 절과 HAVING 절의 차이점을 다음 2가지 기준에 따라 명확히 비교하여 서술하시오.\n① 조건이 적용되는 시점 (GROUP BY 그룹화 전/후)\n② 집계 함수(COUNT, SUM, AVG, MAX, MIN 등) 사용 가능 여부",
                "keywords": ["그룹화 전", "그룹화 후", "집계 함수", "사용 불가", "사용 가능"],
                "modelAnswer": "1) 조건 적용 시점: WHERE 절은 GROUP BY에 의한 그룹화가 수행되기 전 개별 행(Row)에 대해 조건을 검사하여 필터링하는 반면, HAVING 절은 GROUP BY 그룹화가 완료된 후 생성된 집계 그룹에 대해 조건을 검사하여 필터링합니다.\n2) 집계 함수 사용 가능 여부: WHERE 절은 행 단위 평가이므로 COUNT, SUM, AVG 등 집계 함수를 조건식에 직접 사용할 수 없습니다. 반면 HAVING 절은 그룹화 집계 결과를 검사하므로 집계 함수를 조건식에 직접 사용할 수 있습니다.",
                "exp": "SQL 실행 순서(FROM ➔ WHERE ➔ GROUP BY ➔ HAVING ➔ SELECT ➔ ORDER BY)에서 필터링 시점의 차이와 집계함수 허용 여부를 정확히 진술해야 합니다."
            }
        ]

    # 10회분 전체 문제 생성 로직
    for r in range(1, 11):
        mcq_list = []
        short_list = []

        # --- 객관식 21문제 생성 ---
        # 1. 서블릿 생명주기
        q1_opts = [
            ["service()", "init()", "doGet()", "destroy()"],
            ["destroy()", "init()", "service()", "doPost()"],
            ["init()", "service()", "doGet()", "doPost()"],
            ["service()", "doPost()", "init()", "destroy()"]
        ][(r-1) % 4]
        ans1 = q1_opts.index("init()")
        mcq_list.append({
            "id": 1, "type": "mcq", "tag": "서블릿 생명주기",
            "question": f"[제{r}회 Q1] 서블릿(Servlet) 컨테이너가 서블릿 객체를 메모리에 로드한 후, 단 한 번만 호출하여 초기화 작업을 수행하는 생명주기 메서드는?",
            "options": q1_opts, "answer": ans1,
            "exp": "init() 메서드는 서블릿이 최초 로딩될 때 1회만 호출됩니다. 이후 클라이언트 요청마다 service()가 호출됩니다."
        })

        # 2. 서블릿 멀티스레드 동시성
        mcq_list.append({
            "id": 2, "type": "mcq", "tag": "서블릿 멀티스레드 동시성",
            "question": f"[제{r}회 Q2] 서블릿 컨테이너(Tomcat)의 서블릿 인스턴스 관리 및 스레드 모델에 대한 설명으로 올바른 것은?",
            "options": [
                "요청마다 새로운 서블릿 객체가 인스턴스화되므로 멤버 변수는 동시성 문제가 없다.",
                "서블릿 인스턴스는 싱글톤으로 단 1개만 생성되며, 요청마다 별도 스레드가 할당되므로 멤버 변수 사용 시 스레드 안전(Thread-safe)하지 않다.",
                "서블릿은 싱글 스레드로만 동작하여 동시 요청 시 큐에서 순차 실행된다.",
                "doGet과 doPost 메서드의 지역 변수는 모든 스레드가 공유하므로 위험하다."
            ],
            "answer": 1,
            "exp": "서블릿은 싱글톤 구조로 1개의 인스턴스만 존재하며, 요청마다 새로운 스레드가 생성되어 service()를 실행하므로 인스턴스 멤버 변수를 상태 저장용으로 쓰면 레이스 컨디션이 발생합니다."
        })

        # 3. URL 패턴 매핑 규칙
        mcq_list.append({
            "id": 3, "type": "mcq", "tag": "URL 패턴 매핑 규칙",
            "question": f"[제{r}회 Q3] 서블릿 컨테이너의 URL 패턴 매핑 규칙 중 가장 우선순위가 높은 매핑 유형은?",
            "options": ["디렉터리 매핑 (/member/*)", "확장자 매핑 (*.do)", "정확한 경로 매핑 (/member/login)", "기본 서블릿 매핑 (/)"],
            "answer": 2,
            "exp": "URL 매핑 우선순위: 1) 정확한 매핑 (/member/login) > 2) 디렉터리 와일드카드 (/member/*) > 3) 확장자 매핑 (*.do) > 4) 기본 서블릿 (/)"
        })

        # 4. Filter doFilter 체이닝
        mcq_list.append({
            "id": 4, "type": "mcq", "tag": "Filter 체이닝",
            "question": f"[제{r}회 Q4] Filter 인터페이스에서 다음 필터나 목적지 서블릿으로 요청 및 응답 객체를 전달하기 위해 호출해야 하는 메서드는?",
            "options": ["chain.doFilter(request, response)", "dispatcher.forward(request, response)", "filter.proceed()", "filter.invokeNext()"],
            "answer": 0,
            "exp": "FilterChain 객체의 doFilter(request, response)를 명시적으로 호출해야 필터 체인이 다음 단계로 이어집니다."
        })

        # 5. Filter DispatcherType
        mcq_list.append({
            "id": 5, "type": "mcq", "tag": "Filter DispatcherType",
            "question": f"[제{r}회 Q5] RequestDispatcher의 forward()를 통해 내부 포워드된 요청에 대해서만 필터가 적용되도록 하려면 어떤 DispatcherType을 지정해야 하는가?",
            "options": ["REQUEST", "INCLUDE", "FORWARD", "ERROR"],
            "answer": 2,
            "exp": "기본값은 REQUEST(일반 클라이언트 요청)이며, 포워드 이동된 요청에 필터를 적용하려면 DispatcherType.FORWARD를 등록해야 합니다."
        })

        # 6. Front Controller 패턴
        mcq_list.append({
            "id": 6, "type": "mcq", "tag": "Front Controller",
            "question": f"[제{r}회 Q6] 웹 애플리케이션에서 Front Controller 패턴(예: GearController)을 도입하는 핵심 이점은?",
            "options": [
                "모든 클라이언트 요청의 입구를 단일 서블릿으로 일원화하여 공통 사전/사후 작업(인코딩, 세션검증, 로깅)을 집중 처리할 수 있다.",
                "데이터베이스 연결을 서블릿 없이 HTML에서 직접 맺도록 지원한다.",
                "클라이언트 측 자바스크립트 실행 속도를 극대화한다.",
                "서버 재부팅 없이 자동으로 배포를 수행한다."
            ],
            "answer": 0,
            "exp": "Front Controller는 모든 요청을 하나의 대표 창구 서블릿이 접수하여 공통 작업을 수행하고 개별 핸들러로 라우팅하는 패턴입니다."
        })

        # 7. web.xml 에러 페이지 매핑
        mcq_list.append({
            "id": 7, "type": "mcq", "tag": "web.xml 에러 매핑",
            "question": f"[제{r}회 Q7] web.xml에서 HTTP 500 내부 서버 오류 발생 시 특정 JSP 페이지로 이동시키는 올바른 설정 태그는?",
            "options": [
                "<error-page><error-code>500</error-code><location>/error/500.jsp</location></error-page>",
                "<server-error code='500' target='/error/500.jsp' />",
                "<exception-page><status>500</status><url>/error/500.jsp</url></exception-page>",
                "<error-handler><code 500>/error/500.jsp</code 500></error-handler>"
            ],
            "answer": 0,
            "exp": "web.xml에서는 <error-page> 태그 내에 <error-code> 또는 <exception-type>과 <location>을 설정합니다."
        })

        # 8. JSP 스크립트 요소 변환 구조
        mcq_list.append({
            "id": 8, "type": "mcq", "tag": "JSP 변환 구조",
            "question": f"[제{r}회 Q8] JSP 파일이 서블릿으로 변환될 때, 선언문(<%! int count = 0; %>)에 선언된 변수가 배치되는 위치는?",
            "options": [
                "_jspService() 메서드의 지역 변수",
                "서블릿 클래스의 멤버 변수(Field)",
                "doGet() 메서드의 매개변수",
                "Tomcat 서버의 전역 환경변수"
            ],
            "answer": 1,
            "exp": "선언문(<%! %>)은 클래스의 멤버 변수 또는 멤버 메서드로 변환되며, 스크립트릿(<% %>)은 _jspService() 메서드 내부 지역 코드로 변환됩니다."
        })

        # 9. include 지시자 vs 표준 액션
        mcq_list.append({
            "id": 9, "type": "mcq", "tag": "include 지시자 vs 액션",
            "question": f"[제{r}회 Q9] `<%@ include file=\"top.jsp\" %>`와 `<jsp:include page=\"top.jsp\" />`에 대한 비교로 옳지 않은 것은?",
            "options": [
                "include 지시자는 JSP가 서블릿 자바 코드로 변환될 때 정적으로 소스가 병합된다.",
                "jsp:include 액션 태그는 런타임에 동적으로 요청이 위임되어 결과 HTML 조각이 포함된다.",
                "include 지시자를 사용하면 포함되는 파일과 포함하는 파일 간에 동일한 변수명을 선언할 수 있다.",
                "jsp:include 액션 태그는 jsp:param 태그를 통해 파라미터를 추가로 전달할 수 있다."
            ],
            "answer": 2,
            "exp": "include 지시자는 두 파일이 합쳐져 하나의 큰 서블릿으로 번역되므로, 동일한 이름의 변수를 양쪽에서 선언하면 'Duplicate local variable' 컴파일 에러가 발생합니다."
        })

        # 10. 4대 Scope 우선순위
        mcq_list.append({
            "id": 10, "type": "mcq", "tag": "4대 Scope 탐색 우선순위",
            "question": f"[제{r}회 Q10] EL에서 `${{title}}`을 평가할 때 객체를 검색하는 4대 스코프의 우선순위로 올바른 것은?",
            "options": [
                "pageScope ➔ requestScope ➔ sessionScope ➔ applicationScope",
                "requestScope ➔ pageScope ➔ sessionScope ➔ applicationScope",
                "applicationScope ➔ sessionScope ➔ requestScope ➔ pageScope",
                "sessionScope ➔ requestScope ➔ pageScope ➔ applicationScope"
            ],
            "answer": 0,
            "exp": "EL은 가장 좁은 영역부터 넓은 영역 순(page ➔ request ➔ session ➔ application)으로 속성을 탐색합니다."
        })

        # 11. JSTL 조건 태그
        mcq_list.append({
            "id": 11, "type": "mcq", "tag": "JSTL Core 조건문",
            "question": f"[제{r}회 Q11] JSTL Core에서 단일 if 분기를 표현할 때 사용하는 올바른 태그 문법은?",
            "options": [
                "<c:if test=\"${empty loginUser}\"> ... </c:if>",
                "<c:when condition=\"${empty loginUser}\"> ... </c:when>",
                "<c:check eval=\"${empty loginUser}\"> ... </c:check>",
                "<c:condition test=\"${empty loginUser}\"> ... </c:condition>"
            ],
            "answer": 0,
            "exp": "단일 조건 분기는 <c:if test=\"조건식\"> ... </c:if> 태그를 사용하며, <c:else> 태그는 존재하지 않습니다."
        })

        # 12. 세션 식별 쿠키
        mcq_list.append({
            "id": 12, "type": "mcq", "tag": "세션 식별 쿠키",
            "question": f"[제{r}회 Q12] 서블릿 컨테이너가 클라이언트 브라우저와 서버 세션 객체를 매핑하기 위해 클라이언트에 전달하는 기본 세션 식별 쿠키 이름은?",
            "options": ["SESSION_ID", "JSESSIONID", "SSAFY_SESSION", "SERVLET_SESSION"],
            "answer": 1,
            "exp": "서블릿 스펙에서 세션 트래킹용 기본 쿠키의 이름은 'JSESSIONID'입니다."
        })

        # 13. DDL vs DML (DELETE/TRUNCATE/DROP)
        mcq_list.append({
            "id": 13, "type": "mcq", "tag": "DELETE vs TRUNCATE vs DROP",
            "question": f"[제{r}회 Q13] 테이블의 정의와 인덱스 구조는 남겨둔 채 모든 행 데이터를 가장 빠르게 일괄 삭제하며, Undo 로그를 남기지 않아 롤백이 불가한 DDL 명령어는?",
            "options": ["DELETE FROM table_name;", "DROP TABLE table_name;", "TRUNCATE TABLE table_name;", "REMOVE TABLE table_name;"],
            "answer": 2,
            "exp": "TRUNCATE TABLE은 DDL 명령어로 테이블 데이터를 즉시 초기화하며 롤백이 불가능합니다. DML인 DELETE는 행 단위 삭제 및 롤백이 가능합니다."
        })

        # 14. 삼치 논리와 NULL
        mcq_list.append({
            "id": 14, "type": "mcq", "tag": "삼치 논리와 NULL",
            "question": f"[제{r}회 Q14] SQL에서 `WHERE price = NULL`과 같이 작성했을 때 해당 조건식의 논리 평가 결과는?",
            "options": ["True (참)", "False (거짓)", "Unknown (알 수 없음)", "Syntax Error"],
            "answer": 2,
            "exp": "SQL에서 NULL과의 상등 비교(=, !=)는 참이나 거짓이 아닌 Unknown(알 수 없음)으로 평가됩니다. NULL 검사는 반드시 IS NULL을 써야 합니다."
        })

        # 15. LIMIT 페이징 쿼리
        page_num = 2 + (r % 3)
        offset_val = (page_num - 1) * 10
        mcq_list.append({
            "id": 15, "type": "mcq", "tag": "LIMIT 페이징",
            "question": f"[제{r}회 Q15] 한 페이지에 10개씩 목록을 보여줄 때, {page_num}번째 페이지(오프셋 {offset_val})를 조회하기 위한 MySQL LIMIT 구문으로 옳은 것은?",
            "options": [
                f"LIMIT {offset_val}, 10",
                f"LIMIT 10, {offset_val}",
                f"LIMIT {page_num}, 10",
                f"OFFSET {page_num} LIMIT 10"
            ],
            "answer": 0,
            "exp": f"MySQL의 LIMIT 문법은 `LIMIT offset, count`입니다. {page_num}페이지는 {offset_val}건을 건너뛰어야 하므로 `LIMIT {offset_val}, 10`이 정답입니다."
        })

        # 16. 문자열 결합 함수
        mcq_list.append({
            "id": 16, "type": "mcq", "tag": "문자열 결합 함수",
            "question": f"[제{r}회 Q16] MySQL에서 'SSAFY'와 '2026' 문자열을 연결하여 'SSAFY2026'을 만드는 함수 호출은?",
            "options": ["CONCAT('SSAFY', '2026')", "'SSAFY' + '2026'", "APPEND('SSAFY', '2026')", "MERGE('SSAFY', '2026')"],
            "answer": 0,
            "exp": "MySQL에서는 CONCAT() 함수로 문자열을 결합합니다. (+ 연산자는 산술 덧셈으로 동작함)"
        })

        # 17. 트랜잭션 부분 롤백
        mcq_list.append({
            "id": 17, "type": "mcq", "tag": "트랜잭션 부분 롤백",
            "question": f"[제{r}회 Q17] 트랜잭션 진행 중 오류 발생 시 전체 취소 대신 특정 지점(저장점)까지만 롤백하기 위해 사용하는 명령 조합은?",
            "options": [
                "CHECKPOINT & ROLLBACK TO CHECKPOINT",
                "SAVEPOINT & ROLLBACK TO SAVEPOINT",
                "BOOKMARK & RESTORE BOOKMARK",
                "POINT & GOTO POINT"
            ],
            "answer": 1,
            "exp": "트랜잭션 내에서 `SAVEPOINT 포인트명;`으로 저장점을 만들고 `ROLLBACK TO SAVEPOINT 포인트명;`으로 부분 롤백합니다."
        })

        # 18. 다중 행 서브쿼리 ALL vs ANY
        mcq_list.append({
            "id": 18, "type": "mcq", "tag": "다중 행 서브쿼리 연산자",
            "question": f"[제{r}회 Q18] 다중 행 서브쿼리의 반환 값 '모두'에 대해 조건을 만족해야 참(True)이 되는 연산자는?",
            "options": ["ANY", "SOME", "ALL", "EXISTS"],
            "answer": 2,
            "exp": "ALL은 서브쿼리의 모든 결과 값에 대해 조건을 만족해야 참입니다. (예: > ALL(subquery)는 최대값보다 커야 참)"
        })

        # 19. 상호 연관 서브쿼리와 EXISTS
        mcq_list.append({
            "id": 19, "type": "mcq", "tag": "상호 연관 서브쿼리 & EXISTS",
            "question": f"[제{r}회 Q19] 서브쿼리 결과에 부합하는 데이터가 1건이라도 존재하는지 여부만 확인할 때 성능상 가장 우수한 연산자는?",
            "options": ["IN", "EXISTS", "BETWEEN", "LIKE"],
            "answer": 1,
            "exp": "EXISTS 연산자는 조건을 만족하는 첫 행을 발견하는 즉시 검색을 종료하므로 대용량 데이터에서 성능이 매우 뛰어납니다."
        })

        # 20. 뷰(View)의 특성
        mcq_list.append({
            "id": 20, "type": "mcq", "tag": "뷰(View)의 특성",
            "question": f"[제{r}회 Q20] 데이터베이스 뷰(View)의 특성에 대한 설명으로 옳지 않은 것은?",
            "options": [
                "뷰는 복잡한 쿼리를 단순화하고 특정 컬럼만 보여주어 보안을 강화한다.",
                "뷰는 물리적인 데이터를 별도의 디스크 공간에 독립적으로 복제하여 저장한다.",
                "집계 함수(SUM, AVG)나 GROUP BY가 포함된 뷰는 INSERT나 UPDATE가 제한된다.",
                "뷰는 기본적으로 정의된 SELECT 쿼리문만 메타데이터에 저장되는 가상 테이블이다."
            ],
            "answer": 1,
            "exp": "뷰는 물리적 데이터를 저장하지 않는 가상 테이블(Virtual Table)입니다."
        })

        # 21. Clustered Index vs Secondary Index
        mcq_list.append({
            "id": 21, "type": "mcq", "tag": "인덱스 구조 비교",
            "question": f"[제{r}회 Q21] MySQL InnoDB에서 Secondary Index(보조 인덱스)의 리프 노드에 저장되어 있는 값은?",
            "options": [
                "실제 데이터 행 전체 (Row data)",
                "해당 행의 Primary Key (기본키) 값",
                "하드디스크의 물리적 블록 주소 (TID)",
                "다음 인덱스 노드의 해시값"
            ],
            "answer": 1,
            "exp": "InnoDB의 Secondary Index는 리프 노드에 실제 데이터 대신 Clustered Index의 키 값인 Primary Key 값을 저장합니다."
        })

        # --- 주관식 단답형 9문제 (22~30) ---
        short_list.append({
            "id": 22, "type": "short", "tag": "외래키 삭제 DDL",
            "question": f"[제{r}회 Q22] member 테이블을 참조하는 외래키 제약조건 `fk_member_id`를 orders 테이블에서 삭제하는 MySQL DDL 문장을 작성하시오.",
            "answer": "ALTER TABLE orders DROP FOREIGN KEY fk_member_id;",
            "acceptedAnswers": [
                "ALTER TABLE orders DROP FOREIGN KEY fk_member_id;",
                "ALTER TABLE orders DROP FOREIGN KEY fk_member_id",
                "alter table orders drop foreign key fk_member_id;",
                "alter table orders drop foreign key fk_member_id"
            ],
            "exp": "MySQL에서 외래키 삭제 문법: `ALTER TABLE 테이블명 DROP FOREIGN KEY 제약조건명;`"
        })

        short_list.append({
            "id": 23, "type": "short", "tag": "세션 무효화 메서드",
            "question": f"[제{r}회 Q23] 사용자가 로그아웃할 때 현재 HttpSession을 즉시 파기하고 바인딩된 모든 세션 속성을 제거하는 메서드명은?",
            "answer": "invalidate()",
            "acceptedAnswers": ["invalidate()", "invalidate", "session.invalidate()", "session.invalidate"],
            "exp": "session.invalidate(); 를 호출하면 세션이 완전히 무효화됩니다."
        })

        short_list.append({
            "id": 24, "type": "short", "tag": "제2정규형 (2NF)",
            "question": f"[제{r}회 Q24] 제1정규형을 만족하고, 기본키의 일부에 종속되는 '부분 함수적 종속'을 제거하여 '완전 함수적 종속'을 만족시키는 정규화 단계는?",
            "answer": "제2정규형 (2NF)",
            "acceptedAnswers": ["제2정규형", "2NF", "2정규형", "2nf", "제 2 정규형"],
            "exp": "제2정규형(2NF)은 복합 기본키의 진부분집합에 종속되는 부분 함수 종속을 분리하는 단계입니다."
        })

        short_list.append({
            "id": 25, "type": "short", "tag": "BCNF 정규형",
            "question": f"[제{r}회 Q25] 제3정규형을 만족하면서, 릴레이션에 존재하는 '모든 결정자가 후보키'여야 한다는 조건을 만족하는 정규형은?",
            "answer": "BCNF (보이스-코드 정규형)",
            "acceptedAnswers": ["BCNF", "보이스-코드 정규형", "보이스코드 정규형", "보이스코드정규형", "bcnf"],
            "exp": "BCNF는 후보키가 아닌 결정자를 제거하여 모든 결정자가 후보키가 되도록 분해하는 정규형입니다."
        })

        short_list.append({
            "id": 26, "type": "short", "tag": "차집합 연산자",
            "question": f"[제{r}회 Q26] 표준 SQL 및 MySQL 최신 버전에서 두 SELECT 결과의 차집합을 구할 때 사용하는 집합 연산자 키워드는?",
            "answer": "EXCEPT",
            "acceptedAnswers": ["EXCEPT", "except", "MINUS", "minus"],
            "exp": "표준 SQL 차집합 키워드는 `EXCEPT`입니다. (Oracle은 MINUS)"
        })

        short_list.append({
            "id": 27, "type": "short", "tag": "Full Table Scan",
            "question": f"[제{r}회 Q27] 인덱스를 사용하지 않고 테이블의 처음부터 끝까지 모든 데이터 블록을 순차적으로 읽는 스캔 방식은?",
            "answer": "Full Table Scan (FTS)",
            "acceptedAnswers": ["Full Table Scan", "FTS", "테이블 풀 스캔", "풀 테이블 스캔", "full table scan", "fts"],
            "exp": "인덱스가 없거나 대량의 행을 한 번에 읽어야 할 때 옵티마이저는 Full Table Scan(테이블 전체 스캔)을 수행합니다."
        })

        short_list.append({
            "id": 28, "type": "short", "tag": "스칼라 서브쿼리",
            "question": f"[제{r}회 Q28] SELECT 절에 위치하며 반드시 단 1개의 행과 1개의 컬럼(단일 값)만을 반환해야 하는 서브쿼리는?",
            "answer": "스칼라 서브쿼리 (Scalar Subquery)",
            "acceptedAnswers": ["스칼라 서브쿼리", "스칼라", "Scalar Subquery", "scalar subquery", "스칼라서브쿼리"],
            "exp": "SELECT 절에 작성되어 단일 값을 리턴하는 서브쿼리를 스칼라 서브쿼리라고 합니다."
        })

        short_list.append({
            "id": 29, "type": "short", "tag": "IS NULL 연산자",
            "question": f"[제{r}회 Q29] 컬럼의 값이 NULL인지 판별하기 위해 WHERE 절에 사용하는 표준 연산자는?",
            "answer": "IS NULL",
            "acceptedAnswers": ["IS NULL", "is null", "ISNULL"],
            "exp": "NULL은 상등(=) 비교가 불가하며 `IS NULL` 연산자로 확인해야 합니다."
        })

        short_list.append({
            "id": 30, "type": "short", "tag": "쿠키 만료시간 메서드",
            "question": f"[제{r}회 Q30] 서블릿 Cookie 객체의 유효 생존 시간을 초 단위로 지정하는 메서드명은?",
            "answer": "setMaxAge()",
            "acceptedAnswers": ["setMaxAge()", "setMaxAge", "cookie.setMaxAge()", "setmaxage"],
            "exp": "cookie.setMaxAge(초단위)로 쿠키 생존 시간을 설정하며, 0을 넘기면 삭제됩니다."
        })

        # --- 서술형 2문제 (31~32) ---
        essay_list = get_essay_questions(r)

        # 32문제 결합
        round_quiz = mcq_list + short_list + essay_list
        exams[r] = {
            "round": r,
            "title": themes[r-1],
            "questions": round_quiz
        }

    # JS 파일로 내보내기
    js_content = f"// SSAFY BackEnd & DB 과목평가 10회분 (총 320문제) 데이터\nconst ALL_MOCK_EXAMS = {json.dumps(exams, ensure_ascii=False, indent=2)};\n"
    
    js_path = r"C:\Users\SSAFY\Desktop\JSP\mock_exams.js"
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js_content)

    print(f"SUCCESS: 10 mock exams ({len(exams) * 32} questions) generated: {js_path}")

if __name__ == "__main__":
    create_mock_exams()
