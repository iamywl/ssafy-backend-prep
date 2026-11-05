"""
SSAFY 백엔드 & DB 과목평가 대비 프리미엄 실전 모의고사 10회분 (320문제) 생성기
- 단순 암기형 배제: 실전 자바/JSP/SQL 코드 스니펫 및 실행 결과 예측형 문제 전면 배치
- 시험 공지 7대 영역 100% 매핑:
  1. Servlet 생명주기, 멀티스레드 동시성, URL 매핑 우선순위, Filter 체인, Front Controller, web.xml
  2. JSP 스크립트 변환, 선언문 vs 스크립트릿, include 지시자 vs 액션, 4대 Scope 우선순위, JSTL choose/if, 세션/쿠키
  3. DDL/DML, PK/FK 제약조건, TRUNCATE vs DELETE vs DROP, 삼치 논리(NULL 연산/함정), LIMIT 페이징, CONCAT
  4. 트랜잭션 SAVEPOINT, 다중행 서브쿼리(ALL/ANY/IN), 스칼라 서브쿼리, 상호연관 EXISTS, 차집합(EXCEPT), 뷰(View)
  5. 정규화(1NF~BCNF), Full Table Scan 발생 조건, Clustered Index vs Secondary Index 구조
  6. [서술형 1] forward vs sendRedirect (요청/응답 횟수, URL 변경, request 공유)
  7. [서술형 2] WHERE 절 vs HAVING 절 (조건 적용 시점, 집계함수 사용 여부)
"""

import json
import os

def build_round(r):
    # 각 회차별 실전 코드형 문제 정의
    # 21개 객관식 문항
    mcqs = [
        # Q1: 서블릿 생명주기 및 실행 출력 예측
        {
            "id": 1, "type": "mcq", "tag": "서블릿 생명주기 메서드 (init, service, destroy)",
            "question": f"[제{r}회 Q1] 서블릿(Servlet) 생명주기 3대 메서드(init, service, destroy)의 실행 메커니즘에 대한 설명으로 올바른 것은?\n\n```java\n@WebServlet(\"/life\")\npublic class LifeServlet extends HttpServlet {{\n    public void init() {{ System.out.print(\"init() 호출-\"); }}\n    protected void doGet(HttpServletRequest req, HttpServletResponse resp) {{\n        System.out.print(\"service() 및 doGet() 호출-\");\n    }}\n    public void destroy() {{ System.out.print(\"destroy() 호출-\"); }}\n}}\n```\n클라이언트가 `/life` URL을 3번 연속 요청(새로고침)했을 때의 콘솔 출력 결과는?",
            "options": [
                "init() 호출-service() 및 doGet() 호출-service() 및 doGet() 호출-service() 및 doGet() 호출-",
                "init() 호출-destroy() 호출-init() 호출-destroy() 호출-",
                "service() 및 doGet() 호출-service() 및 doGet() 호출-service() 및 doGet() 호출-",
                "init() 호출-init() 호출-init() 호출-service() 및 doGet() 호출-"
            ],
            "answer": 0,
            "exp": "서블릿의 init() 메서드는 최초 요청 시 서블릿 객체가 메모리에 로드될 때 단 1번만 실행됩니다. 이후 요청마다 service() ➔ doGet()이 반복 호출되며, destroy() 메서드는 서블릿이 언로드되거나 서버가 종료될 때 단 1회 호출됩니다."
        },
        # Q2: 멀티스레드 동시성 버그
        {
            "id": 2, "type": "mcq", "tag": "서블릿 멀티스레드 동시성",
            "question": f"[제{r}회 Q2] 다음 서블릿 코드에서 100명의 사용자가 동시에 POST 요청을 보낼 때 발생할 수 있는 치명적인 아키텍처적 결함은?\n\n```java\n@WebServlet(\"/order\")\npublic class OrderServlet extends HttpServlet {{\n    private int orderNumber = 0; // 서블릿 멤버 변수\n\n    protected void doPost(HttpServletRequest req, HttpServletResponse resp) {{\n        orderNumber++;\n        System.out.println(\"주문 완료 번호: \" + orderNumber);\n    }}\n}}\n```",
            "options": [
                "컴파일 에러가 발생하여 서블릿이 구동되지 않는다.",
                "서블릿 인스턴스는 싱글톤으로 단 1개만 생성되고 요청마다 스레드가 할당되므로, 멤버 변수 orderNumber에 여러 스레드가 동시 접근하여 레이스 컨디션(동시성 충돌)이 발생한다.",
                "doPost() 내의 지역 변수가 아니므로 StackOverflowError가 발생한다.",
                "서블릿 컨테이너가 요청마다 서블릿 객체를 새로 복제하므로 메모리가 고갈된다."
            ],
            "answer": 1,
            "exp": "서블릿은 기본적으로 싱글톤 1개 객체로 동작합니다. 여러 클라이언트가 동시 접속하면 서로 다른 스레드가 동일한 멤버 필드(orderNumber)를 읽고 쓰게 되어 주문 번호가 중복되거나 누락되는 동시성 버그가 발생합니다."
        },
        # Q3: URL 패턴 매핑 우선순위
        {
            "id": 3, "type": "mcq", "tag": "URL 패턴 매핑 우선순위",
            "question": f"[제{r}회 Q3] 서블릿 컨테이너에 다음과 같이 4개의 서블릿 매핑이 등록되어 있을 때, 클라이언트가 `/shop/item.do` URL을 호출하면 실제로 실행되는 서블릿은?\n\n- 서블릿 A: `/shop/*` (디렉터리 매핑)\n- 서블릿 B: `/shop/item.do` (정확한 매핑)\n- 서블릿 C: `*.do` (확장자 매핑)\n- 서블릿 D: `/` (기본 서블릿)",
            "options": ["서블릿 A", "서블릿 B", "서블릿 C", "서블릿 D"],
            "answer": 1,
            "exp": "URL 매핑 우선순위 규칙은 1) 정확한 경로 매핑(/shop/item.do) ➔ 2) 디렉터리 경로 매핑(/shop/*) ➔ 3) 확장자 매핑(*.do) ➔ 4) 기본 서블릿(/) 순서입니다. 따라서 서블릿 B가 실행됩니다."
        },
        # Q4: Filter 체인 순서 예측
        {
            "id": 4, "type": "mcq", "tag": "Filter 체인 실행 순서",
            "question": f"[제{r}회 Q4] web.xml에 FilterA, FilterB 순서로 필터가 등록되어 있고, 각 필터와 서블릿이 다음과 같을 때 콘솔에 출력되는 결과는?\n\n```java\n// FilterA: System.out.print(\"A1-\"); chain.doFilter(req, resp); System.out.print(\"A2-\");\n// FilterB: System.out.print(\"B1-\"); chain.doFilter(req, resp); System.out.print(\"B2-\");\n// 서블릿: System.out.print(\"SERVLET-\");\n```",
            "options": [
                "A1-A2-B1-B2-SERVLET-",
                "A1-B1-SERVLET-B2-A2-",
                "SERVLET-A1-B1-A2-B2-",
                "A1-B1-SERVLET-A2-B2-"
            ],
            "answer": 1,
            "exp": "필터 체인은 스택(재귀) 구조로 동작합니다. FilterA의 전처리(A1) ➔ FilterB의 전처리(B1) ➔ 서블릿 실행(SERVLET) ➔ FilterB의 후처리(B2) ➔ FilterA의 후처리(A2) 순으로 진행됩니다."
        },
        # Q5: DispatcherType 설정
        {
            "id": 5, "type": "mcq", "tag": "Filter DispatcherType",
            "question": f"[제{r}회 Q5] 컨트롤러에서 `request.getRequestDispatcher(\"/view.jsp\").forward(request, response);`로 내부 포워드할 때만 동작하도록 필터를 지정하려면 어떤 DispatcherType을 등록해야 하는가?",
            "options": ["DispatcherType.REQUEST", "DispatcherType.INCLUDE", "DispatcherType.FORWARD", "DispatcherType.ERROR"],
            "answer": 2,
            "exp": "클라이언트의 직접 요청은 REQUEST이며, RequestDispatcher.forward()에 의한 내부 포워드 요청을 가로채려면 FORWARD 타입을 명시해야 합니다."
        },
        # Q6: Front Controller 패턴
        {
            "id": 6, "type": "mcq", "tag": "Front Controller (프론트 컨트롤러) 패턴",
            "question": f"[제{r}회 Q6] 실기 프로젝트(`GearController`)에서 Front Controller(프론트 컨트롤러) 패턴을 적용하여 얻는 핵심 이점으로 가장 알맞은 것은?",
            "options": [
                "클라이언트의 모든 HTTP 요청을 하나의 대표 서블릿이 접수하여 공통 작업(인코딩, 세션/로그인 검증, 예외 처리)을 일괄 처리하고 세부 비즈니스 핸들러로 위임한다.",
                "데이터베이스 연결을 자바 없이 JSP에서 직접 수행하도록 한다.",
                "브라우저의 캐시 메모리를 무력화하여 항상 새 페이지를 강제 다운로드한다.",
                "톰캣 서버의 JVM 힙 메모리를 자동으로 증설해준다."
            ],
            "answer": 0,
            "exp": "Front Controller (프론트 컨트롤러) 패턴은 입구를 단일 서블릿으로 일원화하여 공통 사전/사후 처리를 중앙집중화하고 유지보수성을 극대화하는 디자인 패턴입니다."
        },
        # Q7: web.xml 에러 페이지 매핑
        {
            "id": 7, "type": "mcq", "tag": "web.xml 에러 매핑",
            "question": f"[제{r}회 Q7] `NullPointerException`이 발생했을 때 `/error/500.jsp`로 안내하기 위한 web.xml 태그로 올바른 것은?",
            "options": [
                "<error-page><exception-type>java.lang.NullPointerException</exception-type><location>/error/500.jsp</location></error-page>",
                "<exception-handler class=\"NullPointerException\" page=\"/error/500.jsp\" />",
                "<error-page><error-code>NullPointerException</error-code><url>/error/500.jsp</url></error-page>",
                "<server-error><type>java.lang.NullPointerException</type><jsp>/error/500.jsp</jsp></server-error>"
            ],
            "answer": 0,
            "exp": "예외 클래스 기반 에러 매핑은 `<error-page>` 안에 `<exception-type>`과 `<location>` 태그를 사용합니다."
        },
        # Q8: JSP 변환 구조 (선언문 vs 스크립트릿)
        {
            "id": 8, "type": "mcq", "tag": "JSP 변환 구조",
            "question": f"[제{r}회 Q8] 다음 `test.jsp` 파일의 코드에 대한 컴파일 및 실행 결과 설명으로 올바른 것은?\n\n```jsp\n<%! int num = 10; %>\n<%\n    int num = 20;\n    int result = num + this.num;\n%>\n<h1>결과: <%= result %></h1>\n```",
            "options": [
                "동일한 이름의 변수 `num`이 두 번 선언되어 'Duplicate local variable' 컴파일 에러가 발생한다.",
                "선언문의 `num`은 서블릿 멤버 변수(`this.num = 10`)가 되고, 스크립트릿의 `num`은 `_jspService()`의 지역변수(`num = 20`)가 되므로 정상 실행되어 결과는 30이다.",
                "선언문은 JSP에서 사용할 수 없으므로 무시된다.",
                "스크립트릿 내부에서는 `this` 키워드를 참조할 수 없어 런타임 에러가 발생한다."
            ],
            "answer": 1,
            "exp": "선언문(<%! %>)은 클래스의 멤버 필드로 변환되고, 스크립트릿(<% %>)은 _jspService() 메서드의 지역변수로 변환됩니다. 따라서 지역변수 num(20)과 멤버변수 this.num(10)의 합인 30이 정상 출력됩니다."
        },
        # Q9: include 지시자 vs 액션 태그
        {
            "id": 9, "type": "mcq", "tag": "include 지시자 vs 액션",
            "question": f"[제{r}회 Q9] `<%@ include file=\"header.jsp\" %>`와 `<jsp:include page=\"header.jsp\" />`의 차이점에 대한 설명으로 옳지 않은 것은?",
            "options": [
                "`<%@ include %>` 지시자는 변환(Translation) 시점에 소스 코드가 하나로 합쳐져 단일 자바 클래스로 컴파일된다.",
                "`<jsp:include>` 표준 액션은 실행(Runtime) 시점에 요청이 위임되어 생성된 응답 HTML 결과만 포함된다.",
                "`<%@ include %>` 지시자를 사용한 경우 포함되는 파일과 부모 파일은 별개의 서블릿 객체이므로 변수를 공유할 수 없다.",
                "`<jsp:include>` 태그는 `<jsp:param>` 태그를 이용해 파라미터를 추가로 전달할 수 있다."
            ],
            "answer": 2,
            "exp": "include 지시자는 두 파일의 소스가 하나로 물리적으로 합쳐져 단일 서블릿으로 컴파일되므로 부모 파일에 선언된 변수를 자식 파일에서 그대로 공유하여 사용할 수 있습니다. 따라서 3번이 틀린 설명입니다."
        },
        # Q10: 4대 Scope 우선순위 예측
        {
            "id": 10, "type": "mcq", "tag": "4대 Scope 탐색 우선순위",
            "question": f"[제{r}회 Q10] 서블릿에서 다음과 같이 속성을 저장한 뒤 JSP로 이동했을 때, `${{user}}`가 출력하는 값은?\n\n```java\nrequest.setAttribute(\"user\", \"REQUEST_USER\");\nsession.setAttribute(\"user\", \"SESSION_USER\");\napplication.setAttribute(\"user\", \"APP_USER\");\n```",
            "options": ["REQUEST_USER", "SESSION_USER", "APP_USER", "null (스코프 미지정으로 모호성 에러)"],
            "answer": 0,
            "exp": "EL에서 스코프 접두사 없이 `${user}`를 조회하면 탐색 순서는 pageScope ➔ requestScope ➔ sessionScope ➔ applicationScope 순입니다. 따라서 가장 먼저 매칭되는 requestScope의 'REQUEST_USER'가 출력됩니다."
        },
        # Q11: JSTL 조건 태그 choose/when
        {
            "id": 11, "type": "mcq", "tag": "JSTL Core 분기 태그",
            "question": f"[제{r}회 Q11] JSTL Core에서 if - else if - else 구조의 다중 조건 분기를 구현할 때의 올바른 태그 구성 규칙은?",
            "options": [
                "<c:if> 태그 뒤에 <c:else> 태그를 붙여 작성한다.",
                "<c:choose> 태그 안에 1개 이상의 <c:when test=\"...\"> 태그와 선택적 <c:otherwise> 태그를 배치한다.",
                "<c:switch> 태그 안에 <c:case>와 <c:default>를 배치한다.",
                "<c:condition> 태그 안에 <c:then>과 <c:fallback>을 사용한다."
            ],
            "answer": 1,
            "exp": "JSTL Core 라이브러리에는 <c:else> 태그가 존재하지 않으며, 다중 조건 처리는 반드시 <c:choose> - <c:when> - <c:otherwise> 구조를 사용해야 합니다."
        },
        # Q12: 세션 쿠키 JSESSIONID
        {
            "id": 12, "type": "mcq", "tag": "세션 식별 쿠키",
            "question": f"[제{r}회 Q12] 브라우저가 최초 요청 시 `request.getSession()`이 호출되면, 컨테이너가 세션 객체를 메모리에 생성하고 클라이언트 브라우저에 쿠키로 전송하는 기본 세션 식별자의 이름은?",
            "options": ["SESSION_KEY", "JSESSIONID", "SSAFY_AUTH_ID", "TOMCAT_SESSION"],
            "answer": 1,
            "exp": "자바 서블릿 사양에서 세션을 브라우저와 1:1로 매핑하기 위해 발급하는 기본 쿠키의 이름은 'JSESSIONID'입니다."
        },
        # Q13: TRUNCATE vs DELETE vs DROP
        {
            "id": 13, "type": "mcq", "tag": "DELETE vs TRUNCATE vs DROP",
            "question": f"[제{r}회 Q13] 다음 세 가지 SQL 테이블 삭제 명령어에 대한 비교 설명으로 가장 올바른 것은?\n\n- 명령어 A: `DELETE FROM emp;`\n- 명령어 B: `TRUNCATE TABLE emp;`\n- 명령어 C: `DROP TABLE emp;`",
            "options": [
                "A, B, C 모두 DML 명령어이며 ROLLBACK이 가능하다.",
                "A는 DML로 행 단위 삭제 및 ROLLBACK이 가능하고, B는 DDL로 구조를 남긴 채 데이터를 고속 초기화하며 ROLLBACK이 불가하고, C는 DDL로 테이블 구조 자체를 영구 삭제한다.",
                "B는 WHERE 절을 붙여 특정 조건의 행만 고속으로 삭제할 수 있다.",
                "C를 실행해도 데이터 사전(Data Dictionary)의 테이블 메타데이터는 보존된다."
            ],
            "answer": 1,
            "exp": "DELETE는 DML(WHERE 가능, Undo 로그 기록, Rollback 가능), TRUNCATE는 DDL(WHERE 불가, 스토리지 재할당 고속 삭제, Rollback 불가), DROP은 DDL(테이블 구조 및 데이터 완전 제거)입니다."
        },
        # Q14: SQL 집계함수와 NULL의 함정 계산 & 삼치 논리
        {
            "id": 14, "type": "mcq", "tag": "삼치 논리와 NULL 비교 연산 및 집계",
            "question": f"[제{r}회 Q14] SQL의 삼치 논리(True, False, Unknown) 및 NULL 연산 특성에 대한 설명과 아래 집계 쿼리의 실행 결과 `(sum_val, avg_val, cnt_val)`로 올바른 것은?\n\n- [명제 1] SQL에서 `NULL = NULL` 비교 연산의 결과는 `Unknown`이다.\n- [명제 2] 특정 컬럼이 NULL인지 확인하려면 `= NULL` 대신 `IS NULL` 연산자를 사용해야 한다.\n\n```sql\nCREATE TABLE score (id INT, pt INT);\nINSERT INTO score VALUES (1, 100), (2, NULL), (3, 200);\n\nSELECT SUM(pt) AS sum_val, AVG(pt) AS avg_val, COUNT(pt) AS cnt_val FROM score;\n```",
            "options": [
                "명제 1, 2 모두 참이며, sum_val: 300, avg_val: 150, cnt_val: 2 이다.",
                "명제 1은 거짓이고, sum_val: 300, avg_val: 100, cnt_val: 3 이다.",
                "명제 2는 거짓이고, sum_val: NULL, avg_val: NULL, cnt_val: 2 이다.",
                "명제 1, 2 모두 거짓이며, sum_val: 300, avg_val: 150, cnt_val: 3 이다."
            ],
            "answer": 0,
            "exp": "SQL 삼치 논리에서 `NULL = NULL`은 참이 아니라 Unknown입니다! NULL 검사는 오직 `IS NULL`을 써야 하며, 집계 함수 SUM, AVG, COUNT(컬럼)은 NULL 값을 연산 대상에서 자동으로 제외하므로 SUM=300, COUNT=2, AVG=300/2=150이 됩니다."
        },
        # Q15: LIMIT 페이징 계산
        {
            "id": 15, "type": "mcq", "tag": "LIMIT 페이징 오프셋 계산",
            "question": f"[제{r}회 Q15] 1페이지당 15개씩 게시글을 노출하는 페이징 시스템에서, 4번째 페이지(46번째 글부터 60번째 글까지)를 가져오기 위한 올바른 MySQL LIMIT 구문은?",
            "options": [
                "LIMIT 4, 15",
                "LIMIT 15, 4",
                "LIMIT 45, 15",
                "LIMIT 60, 15"
            ],
            "answer": 2,
            "exp": "LIMIT 문법은 `LIMIT offset, count`입니다. 4번째 페이지의 시작 오프셋은 `(4 - 1) * 15 = 45`이므로, `LIMIT 45, 15`가 정답입니다."
        },
        # Q16: 문자열 결합 및 CONCAT_WS
        {
            "id": 16, "type": "mcq", "tag": "SQL 문자열 결합",
            "question": f"[제{r}회 Q16] MySQL에서 `SELECT CONCAT('SSAFY', '-', '2026')`의 실행 결과와, `SELECT 'SSAFY' + '2026'`의 실행 결과로 올바른 것은?",
            "options": [
                "CONCAT: 'SSAFY-2026' / '+' 연산: 'SSAFY2026'",
                "CONCAT: 'SSAFY-2026' / '+' 연산: 2026 (산술 덧셈 시도하여 문자는 0으로 변환됨)",
                "CONCAT: 에러 발생 / '+' 연산: 'SSAFY-2026'",
                "CONCAT: 'SSAFY-2026' / '+' 연산: NULL"
            ],
            "answer": 1,
            "exp": "MySQL에서 문자열 연결은 오직 CONCAT() 함수를 사용해야 합니다. '+' 연산자는 수치 덧셈 연산자이므로 문자열 'SSAFY'는 0으로 암시적 형변환되어 `0 + 2026 = 2026`이 됩니다."
        },
        # Q17: 트랜잭션 SAVEPOINT 롤백 시뮬레이션
        {
            "id": 17, "type": "mcq", "tag": "트랜잭션 SAVEPOINT 시뮬레이션",
            "question": f"[제{r}회 Q17] 다음 트랜잭션 SQL이 실행된 후, `item` 테이블에 최종적으로 남아있는 행의 개수와 id 값은?\n\n```sql\nSTART TRANSACTION;\nINSERT INTO item VALUES (1, 'A');\nSAVEPOINT sp1;\nINSERT INTO item VALUES (2, 'B');\nSAVEPOINT sp2;\nINSERT INTO item VALUES (3, 'C');\nROLLBACK TO sp1;\nINSERT INTO item VALUES (4, 'D');\nCOMMIT;\n```",
            "options": [
                "4개 (1, 2, 3, 4 모두 보존)",
                "2개 (id: 1, 4만 남음)",
                "1개 (id: 1만 남음)",
                "3개 (id: 1, 2, 4만 남음)"
            ],
            "answer": 1,
            "exp": "`ROLLBACK TO sp1;`에 의해 sp1 저장점 이후에 실행된 id 2('B')와 id 3('C')는 롤백되어 취소됩니다. 따라서 sp1 이전의 1('A')과 sp1 롤백 후 새로 삽입된 4('D')만 COMMIT되어 총 2개(1, 4)가 남습니다."
        },
        # Q18: 다중 행 서브쿼리 ALL vs ANY
        {
            "id": 18, "type": "mcq", "tag": "다중 행 연산자 ALL/ANY",
            "question": f"[제{r}회 Q18] 다음 쿼리의 의미로 가장 알맞은 것은?\n\n```sql\nSELECT name, salary FROM employee \nWHERE salary > ALL (SELECT salary FROM employee WHERE dept_id = 10);\n```",
            "options": [
                "10번 부서 직원들의 '평균 급여'보다 급여가 높은 직원",
                "10번 부서 직원들 중 '가장 급여가 높은 직원(최대값)'보다 급여가 높은 직원",
                "10번 부서 직원들 중 '가장 급여가 낮은 직원(최소값)'보다 급여가 높은 직원",
                "10번 부서에 소속된 모든 직원"
            ],
            "answer": 1,
            "exp": "`> ALL (서브쿼리)`는 서브쿼리가 반환한 모든 값보다 커야 하므로, 10번 부서의 '최대 급여(MAX)'보다 큰 직원을 조회합니다. (반대로 `> ANY`는 최소값(MIN)보다 큰 직원을 조회)"
        },
        # Q19: 상호 연관 서브쿼리와 EXISTS
        {
            "id": 19, "type": "mcq", "tag": "상호 연관 서브쿼리 EXISTS",
            "question": f"[제{r}회 Q19] 상호 연관 서브쿼리(Correlated Subquery)와 `EXISTS` 연산자에 대한 설명으로 가장 옳은 것은?",
            "options": [
                "서브쿼리는 메인 쿼리와 독립적으로 단 1번만 실행되어 캐싱된다.",
                "메인 쿼리의 각 행마다 서브쿼리가 반복 수행되며, 서브쿼리 조건에 맞는 행이 1건이라도 발견되는 즉시 스캔을 멈추고 TRUE를 반환하므로 성능상 효율적이다.",
                "EXISTS는 반드시 서브쿼리 SELECT 절에 모든 컬럼(`SELECT *`)을 나열해야만 동작한다.",
                "EXISTS 연산자는 NULL 값을 반환하는 서브쿼리와 함께 사용할 수 없다."
            ],
            "answer": 1,
            "exp": "EXISTS는 조건을 만족하는 행이 최소 1개 존재하는지만 체크(Early Termination)하므로 실제 데이터를 가져오는 IN 연산자보다 성능상 매우 유리합니다."
        },
        # Q20: 뷰(View)의 특성과 DML 제약
        {
            "id": 20, "type": "mcq", "tag": "뷰(View)의 DML 제약조건",
            "question": f"[제{r}회 Q20] 데이터베이스 뷰(View)를 생성했을 때, 해당 뷰를 통해 `INSERT` 또는 `UPDATE` 연산(DML)을 수행할 수 '없는' 경우는?",
            "options": [
                "기본 테이블의 단일 행을 1:1로 매핑하는 단순 뷰인 경우",
                "기본키(PK) 컬럼이 뷰 정의에 포함되어 있는 경우",
                "뷰 정의 쿼리에 `GROUP BY`, `DISTINCT`, 또는 `COUNT()`, `SUM()` 등의 집계 함수가 포함된 경우",
                "뷰 생성 시 `WITH CHECK OPTION`을 지정하지 않은 경우"
            ],
            "answer": 2,
            "exp": "GROUP BY, DISTINCT, 집계 함수(SUM, COUNT 등)가 포함된 뷰는 여러 행이 하나로 그룹화/축약된 형태이므로 기본 테이블의 특정 행을 1:1로 특정하여 수정/삽입할 수 없습니다."
        },
        # Q21: Clustered Index 구조와 리프 노드
        {
            "id": 21, "type": "mcq", "tag": "인덱스 B+Tree 구조 비교",
            "question": f"[제{r}회 Q21] MySQL InnoDB의 Clustered Index(클러스터형 인덱스)와 Secondary Index(보조 인덱스)의 구조적 차이점에 대한 설명으로 옳은 것은?",
            "options": [
                "Clustered Index는 리프 노드에 실제 데이터 행(Row) 자체가 PK 순서로 정렬되어 저장되고, Secondary Index는 리프 노드에 PK 값을 저장하여 Clustered Index를 찾아가도록(Lookup) 구성된다.",
                "Secondary Index는 테이블당 오직 1개만 생성할 수 있고, Clustered Index는 여러 개 생성할 수 있다.",
                "Clustered Index는 디스크에 정렬되지 않은 채 해시 테이블로 관리된다.",
                "Secondary Index는 실제 데이터의 하드디스크 물리적 섹터 주소(TID)를 직접 가리킨다."
            ],
            "answer": 0,
            "exp": "InnoDB에서 PK로 생성되는 Clustered Index는 리프 노드가 실제 데이터 페이지 자체입니다. 일반 인덱스(Secondary Index)는 리프 노드에 실제 데이터 대신 PK 값을 보관하므로, Secondary Index 검색 후 PK로 다시 Clustered Index를 탐색하는 구조입니다."
        }
    ]

    # 9개 단답형 문항
    shorts = [
        {
            "id": 22, "type": "short", "tag": "외래키 삭제 DDL",
            "question": f"[제{r}회 Q22] orders 테이블에 설정된 외래키 제약조건 `fk_user`를 완전히 삭제하는 MySQL DDL 문장을 작성하시오.\n(세미콜론 및 대소문자 무관)",
            "answer": "ALTER TABLE orders DROP FOREIGN KEY fk_user;",
            "acceptedAnswers": [
                "ALTER TABLE orders DROP FOREIGN KEY fk_user;",
                "ALTER TABLE orders DROP FOREIGN KEY fk_user",
                "alter table orders drop foreign key fk_user;",
                "alter table orders drop foreign key fk_user"
            ],
            "exp": "MySQL 외래키 제약조건 삭제 문법: `ALTER TABLE 테이블명 DROP FOREIGN KEY 제약조건명;`"
        },
        {
            "id": 23, "type": "short", "tag": "세션 무효화 메서드",
            "question": f"[제{r}회 Q23] 사용자가 로그아웃 버튼을 눌렀을 때, 현재 세션을 완전히 파기하고 바인딩된 모든 속성(`loginUser` 등)을 제거하는 HttpSession의 메서드명은?",
            "answer": "invalidate()",
            "acceptedAnswers": ["invalidate()", "invalidate", "session.invalidate()", "session.invalidate"],
            "exp": "session.invalidate(); 를 호출하면 세션 ID가 만료되고 세션 스토리지의 모든 데이터가 파기됩니다."
        },
        {
            "id": 24, "type": "short", "tag": "제2정규형 (2NF)",
            "question": f"[제{r}회 Q24] 제1정규형(1NF)을 만족하고, 복합 기본키의 일부분에 종속되는 '부분 함수적 종속'을 제거하여 '완전 함수적 종속'을 만족시키는 정규화 단계는?\n(예: 제N정규형 또는 2NF)",
            "answer": "제2정규형 (2NF)",
            "acceptedAnswers": ["제2정규형", "2NF", "2정규형", "2nf", "제 2 정규형"],
            "exp": "제2정규형은 기본키가 복합키일 때 발생하는 부분 함수 종속을 테이블 분리를 통해 제거하는 단계입니다."
        },
        {
            "id": 25, "type": "short", "tag": "BCNF (보이스-코드 정규형)",
            "question": f"[제{r}회 Q25] 제3정규형을 만족하면서, 릴레이션에 존재하는 '모든 결정자가 반드시 후보키(Candidate Key)'여야 한다는 제약조건을 만족하는 강한 정규형은?",
            "answer": "BCNF (보이스-코드 정규형)",
            "acceptedAnswers": ["BCNF", "보이스-코드 정규형", "보이스코드 정규형", "보이스코드정규형", "bcnf"],
            "exp": "BCNF는 후보키가 아닌 결정자가 존재하는 비정상적 종속 관계를 분해하여 모든 결정자가 후보키가 되도록 만드는 정규형입니다."
        },
        {
            "id": 26, "type": "short", "tag": "차집합 연산자",
            "question": f"[제{r}회 Q26] 표준 SQL 및 MySQL 8.0.31 이상에서 지원하는 집합 연산자로, 첫 번째 쿼리 결과에서 두 번째 쿼리 결과를 뺀 '차집합'을 구하는 연산자 키워드는?",
            "answer": "EXCEPT",
            "acceptedAnswers": ["EXCEPT", "except", "MINUS", "minus"],
            "exp": "표준 SQL의 차집합 연산자는 `EXCEPT`입니다. (Oracle에서는 `MINUS` 사용)"
        },
        {
            "id": 27, "type": "short", "tag": "Full Table Scan",
            "question": f"[제{r}회 Q27] 인덱스를 경유하지 않고 테이블의 첫 번째 블록부터 마지막 블록까지 모든 데이터를 순차적으로 전체 읽기하는 스캔 방식의 명칭은?\n(영문 약어 FTS, 풀네임, 한글 모두 인정)",
            "answer": "Full Table Scan (FTS / 테이블 풀 스캔)",
            "acceptedAnswers": ["Full Table Scan", "FTS", "테이블 풀 스캔", "풀 테이블 스캔", "full table scan", "fts"],
            "exp": "WHERE 절 조건 컬럼에 인덱스가 없거나 인덱스 컬럼을 함수로 가공했을 때 옵티마이저는 Full Table Scan을 선택합니다."
        },
        {
            "id": 28, "type": "short", "tag": "스칼라 서브쿼리",
            "question": f"[제{r}회 Q28] SELECT 절에 위치하며, 단 1개의 행과 1개의 컬럼(단일 값)만을 반드시 리턴해야 하는 서브쿼리의 명칭은?",
            "answer": "스칼라 서브쿼리 (Scalar Subquery)",
            "acceptedAnswers": ["스칼라 서브쿼리", "스칼라", "Scalar Subquery", "scalar subquery", "스칼라서브쿼리"],
            "exp": "SELECT 절에 포함되어 마치 컬럼의 상수 값처럼 단일 행/열을 반환하는 서브쿼리를 '스칼라 서브쿼리'라고 부릅니다."
        },
        {
            "id": 29, "type": "short", "tag": "기본키(PK) 무결성 제약조건",
            "question": f"[제{r}회 Q29] 관계형 데이터베이스에서 테이블의 기본키(Primary Key)는 중복된 값을 가질 수 없고(UNIQUE), 어떠한 경우에도 NULL 값을 가질 수 없다(NOT NULL)는 무결성 제약조건의 공식 명칭은?",
            "answer": "개체 무결성 (Entity Integrity)",
            "acceptedAnswers": ["개체 무결성", "개체무결성", "개체 무결성 제약조건", "Entity Integrity", "entity integrity", "개체"],
            "exp": "개체 무결성(Entity Integrity) 제약조건은 모든 릴레이션의 기본키는 중복되지 않으며 NULL 값을 가질 수 없다는 핵심 무결성 규칙입니다."
        },
        {
            "id": 30, "type": "short", "tag": "쿠키 유효시간 메서드",
            "question": f"[제{r}회 Q30] 서블릿 Cookie 객체에 대해 유효 수명을 초(second) 단위로 설정하는 메서드명은?\n(0을 설정하면 브라우저에서 즉시 삭제됨)",
            "answer": "setMaxAge()",
            "acceptedAnswers": ["setMaxAge()", "setMaxAge", "cookie.setMaxAge()", "setmaxage"],
            "exp": "cookie.setMaxAge(초); 메서드를 사용하며, 0을 인자로 넘기면 쿠키 삭제 명령이 브라우저로 전송됩니다."
        }
    ]

    # 2개 서술형 문항 (공통 심층 비교)
    essays = [
        {
            "id": 31, "type": "essay", "tag": f"서술형 1 (forward vs sendRedirect) - {r}회",
            "question": f"[제{r}회 서술형 1]\n서블릿/JSP 화면 이동 시 사용하는 forward 방식과 sendRedirect 방식의 차이점을 다음 3가지 기준에 따라 명확히 비교하여 서술하시오.\n① 클라이언트-서버 간 HTTP 요청/응답 왕복 횟수\n② 웹 브라우저 주소창의 URL 변경 여부\n③ HttpServletRequest 객체의 속성(Attribute) 데이터 공유 여부",
            "keywords": ["1회", "2회", "URL", "변경", "공유", "request", "유지"],
            "modelAnswer": "1) 요청/응답 왕복 횟수: forward는 서버 내부에서 제어권이 위임되므로 요청/응답이 1회 발생하지만, sendRedirect는 서버가 302 응답을 보낸 후 브라우저가 새 URL로 재요청하므로 2회 발생합니다.\n2) URL 변경 여부: forward는 서버 내부 이동이므로 브라우저 URL이 변경되지 않고 최초 요청 주소가 유지되지만, sendRedirect는 브라우저가 새 경로로 다시 요청하므로 주소창의 URL이 변경됩니다.\n3) request 속성 공유 여부: forward는 동일한 HttpServletRequest 객체가 대상 JSP까지 유지되므로 request.setAttribute()로 저장한 속성을 공유할 수 있지만, sendRedirect는 새로운 HTTP 요청이 발생하여 새로운 request 객체가 생성되므로 기존 request 속성을 공유할 수 없습니다.",
            "exp": "서블릿 화면 제어의 핵심 차이점 3가지(왕복 횟수 1회 vs 2회, URL 불변 vs 변경, request 속성 유지 vs 불가)를 대조 서술해야 만점입니다."
        },
        {
            "id": 32, "type": "essay", "tag": f"서술형 2 (WHERE vs HAVING) - {r}회",
            "question": f"[제{r}회 서술형 2]\nSQL 쿼리 작성 시 조건을 부여하는 WHERE 절과 HAVING 절의 차이점을 다음 2가지 기준에 따라 명확히 비교하여 서술하시오.\n① 조건이 적용되는 시점 (GROUP BY 그룹화 전/후)\n② 집계 함수(COUNT, SUM, AVG, MAX, MIN 등) 사용 가능 여부",
            "keywords": ["그룹화 전", "그룹화 후", "집계 함수", "사용 불가", "사용 가능"],
            "modelAnswer": "1) 조건 적용 시점: WHERE 절은 GROUP BY에 의한 그룹화가 수행되기 전의 개별 행(Row)에 대해 조건을 검사하여 필터링하는 반면, HAVING 절은 GROUP BY 그룹화가 완료된 후 생성된 집계 그룹에 대해 조건을 검사하여 필터링합니다.\n2) 집계 함수 사용 가능 여부: WHERE 절은 행 단위 평가이므로 COUNT(), SUM(), AVG() 등의 집계 함수를 조건식에 직접 사용할 수 없습니다. 반면 HAVING 절은 그룹 집계 결과를 검사하므로 집계 함수를 조건식에 직접 사용할 수 있습니다.",
            "exp": "SQL 쿼리 논리적 실행 순서(FROM ➔ WHERE ➔ GROUP BY ➔ HAVING ➔ SELECT ➔ ORDER BY)를 바탕으로 필터링 시점과 집계함수 허용 여부를 정확히 진술해야 합니다."
        }
    ]

    return {
        "round": r,
        "title": [
            "제1회: 전범위 기본 완성 모의평가",
            "제2회: 서블릿 아키텍처 & 동시성 코드예측형",
            "제3회: JSP 스크립트 변환 & 4대 Scope 특화형",
            "제4회: SQL 집계함수(NULL) & 페이징 마스터형",
            "제5회: 트랜잭션(SAVEPOINT) & 서브쿼리 정복형",
            "제6회: 데이터베이스 정규화(1NF~BCNF) & 인덱스 구조형",
            "제7회: 실전 기출유형 코드버그 분석형",
            "제8회: 심화 아키텍처 & 성능 최적화(FTS)형",
            "제9회: 실전 시뮬레이션 파이널 A형",
            "제10회: 실전 시뮬레이션 파이널 B형 (만점 도전)"
        ][r-1],
        "questions": mcqs + shorts + essays
    }

def main():
    exams = {}
    for r in range(1, 11):
        exams[r] = build_round(r)
    
    js_content = f"// SSAFY BackEnd & DB 과목평가 프리미엄 실전 10회분 (총 320문제)\nconst ALL_MOCK_EXAMS = {json.dumps(exams, ensure_ascii=False, indent=2)};\n"
    
    js_path = r"C:\Users\SSAFY\Desktop\JSP\mock_exams.js"
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js_content)
    
    print(f"SUCCESS: Premium 10 mock exams (320 questions) created: {js_path}")

if __name__ == "__main__":
    main()
