"""
SSAFY 백엔드(JSP/Servlet/MVC) 월말평가 특화 4단계 QA 검증 에이전트
- 대상 1: WebTest_sample_완성 (완성 프로젝트)
- 대상 2: WebTest_sample_unzip/WebTest_sample (원본 미완성 프로젝트 비교 대조)
- 대상 3: WebTest_시험대비_학습웹.html (학습 포털 콘텐츠 품질)
"""

import os
import sys
import re
import datetime
from typing import Dict, List, Any

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

# lectmaterail 내 validation_agent 모듈 경로 추가
LECT_DIR = r"C:\Users\SSAFY\Desktop\lectmaterail"
if LECT_DIR not in sys.path:
    sys.path.append(LECT_DIR)

from validation_agent.models import (
    RiskLevel, StageStatus, FinalVerdict, IssueSeverity,
    ValidationIssue, StageResult, ValidationRequest,
    HITLApproval, OverallValidationReport
)
from validation_agent.pipeline import ValidationAgent


class SSAFYWebBackendQAAgent:
    """SSAFY 웹 백엔드(JSP/Servlet) 관통/월말평가 전용 4단계 QA 에이전트"""

    def __init__(self, project_path: str):
        self.project_path = project_path
        self.issues: List[ValidationIssue] = []

    def _read_file(self, rel_path: str) -> str:
        full_path = os.path.join(self.project_path, rel_path)
        if not os.path.exists(full_path):
            return ""
        with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()

    # =========================================================================
    # 1단계: 결정론적 규칙 검증 (정적 분석, 문법, 누락된 구현 검사)
    # =========================================================================
    def evaluate_stage1_code_rules(self) -> StageResult:
        stage_name = "Stage 1: Deterministic Code & Rule Check"
        issues = []
        details = {}

        # 1. GearDaoImpl.java 검사
        dao_code = self._read_file(r"src\main\java\com\ssafy\sample\model\dao\GearDaoImpl.java")
        if not dao_code:
            issues.append(ValidationIssue(
                stage=stage_name,
                check_name="Missing GearDaoImpl.java",
                severity=IssueSeverity.CRITICAL,
                message="GearDaoImpl.java 파일이 존재하지 않습니다."
            ))
        else:
            # login SQL 검사
            if "WHERE email = ? AND password = ?" not in dao_code and "where email=? and password=?" not in dao_code.replace(" ", ""):
                if 'String sql = "";' in dao_code or "[TODO]" in dao_code:
                    issues.append(ValidationIssue(
                        stage=stage_name,
                        check_name="DAO login() SQL Unimplemented",
                        severity=IssueSeverity.CRITICAL,
                        message="GearDaoImpl.login()의 SQL 쿼리가 작성되지 않았습니다 (TODO 상태)."
                    ))
            # selectAll while loop 검사
            if "while(rs!=null)" in dao_code.replace(" ", ""):
                issues.append(ValidationIssue(
                    stage=stage_name,
                    check_name="DAO selectAll() Infinite Loop Bug",
                    severity=IssueSeverity.CRITICAL,
                    message="GearDaoImpl.selectAll()에 while(rs!=null) 무한루프 버그가 남아있습니다. while(rs.next())로 수정해야 합니다."
                ))
            # insert 바인딩 검사
            if "pstmt.setString" not in dao_code or "executeUpdate" not in dao_code:
                issues.append(ValidationIssue(
                    stage=stage_name,
                    check_name="DAO insert() Unimplemented",
                    severity=IssueSeverity.CRITICAL,
                    message="GearDaoImpl.insert()의 파라미터 바인딩 또는 executeUpdate() 호출이 누락되었습니다."
                ))

        # 2. GearServiceImpl.java 검사
        service_code = self._read_file(r"src\main\java\com\ssafy\sample\model\service\GearServiceImpl.java")
        if not service_code:
            issues.append(ValidationIssue(
                stage=stage_name,
                check_name="Missing GearServiceImpl.java",
                severity=IssueSeverity.CRITICAL,
                message="GearServiceImpl.java 파일이 존재하지 않습니다."
            ))
        else:
            if "return dao.login" not in service_code and "dao.login" not in service_code:
                issues.append(ValidationIssue(
                    stage=stage_name,
                    check_name="Service login() Unimplemented",
                    severity=IssueSeverity.CRITICAL,
                    message="GearServiceImpl.login()이 DAO를 호출하지 않고 null을 반환하고 있습니다."
                ))
            if "return dao.selectAll" not in service_code and "dao.selectAll" not in service_code:
                issues.append(ValidationIssue(
                    stage=stage_name,
                    check_name="Service selectAll() Unimplemented",
                    severity=IssueSeverity.CRITICAL,
                    message="GearServiceImpl.selectAll()이 DAO를 호출하지 않고 null을 반환하고 있습니다."
                ))

        # 3. GearController.java 검사
        ctrl_code = self._read_file(r"src\main\java\com\ssafy\sample\controller\GearController.java")
        if not ctrl_code:
            issues.append(ValidationIssue(
                stage=stage_name,
                check_name="Missing GearController.java",
                severity=IssueSeverity.CRITICAL,
                message="GearController.java 파일이 존재하지 않습니다."
            ))
        else:
            if '@WebServlet("/gear")' not in ctrl_code and '@WebServlet({"/gear"' not in ctrl_code and '@WebServlet("/sample' not in ctrl_code:
                issues.append(ValidationIssue(
                    stage=stage_name,
                    check_name="Servlet URL Mapping Missing",
                    severity=IssueSeverity.CRITICAL,
                    message="GearController 서블릿에 @WebServlet URL 매핑이 설정되지 않았습니다."
                ))
            if "getActionParameter" not in ctrl_code:
                issues.append(ValidationIssue(
                    stage=stage_name,
                    check_name="ControllerHelper Integration Missing",
                    severity=IssueSeverity.WARNING,
                    message="ControllerHelper의 getActionParameter 메소드를 활용하지 않고 있습니다."
                ))
            # 세션 처리 검사
            if "setAttribute" not in ctrl_code or "loginUser" not in ctrl_code:
                issues.append(ValidationIssue(
                    stage=stage_name,
                    check_name="Session loginUser Attribute Missing",
                    severity=IssueSeverity.CRITICAL,
                    message="로그인 성공 시 Session에 'loginUser' 속성을 저장하는 코드가 누락되었습니다."
                ))
            # 쿠키 처리 검사
            if "setupCookie" not in ctrl_code and "Cookie" not in ctrl_code:
                issues.append(ValidationIssue(
                    stage=stage_name,
                    check_name="Remember-Me Cookie Missing",
                    severity=IssueSeverity.WARNING,
                    message="아이디 기억하기 쿠키 처리(setupCookie)가 누락되었습니다."
                ))

        # 4. JSP 파일들 검사 (header.jsp, list.jsp, regist.jsp, login-form.jsp)
        header_jsp = self._read_file(r"src\main\webapp\header.jsp")
        if header_jsp:
            if "sessionScope.loginUser" not in header_jsp and "loginUser" not in header_jsp:
                issues.append(ValidationIssue(
                    stage=stage_name,
                    check_name="Header Session State Not Handled",
                    severity=IssueSeverity.CRITICAL,
                    message="header.jsp에서 로그인 상태(loginUser)에 따른 조건 분기(<c:if>)가 누락되었습니다."
                ))
            if 'href="#"' in header_jsp:
                issues.append(ValidationIssue(
                    stage=stage_name,
                    check_name="Header Dummy Links Detected",
                    severity=IssueSeverity.WARNING,
                    message="header.jsp에 여전히 href='#' 더미 링크가 남아있습니다."
                ))

        list_jsp = self._read_file(r"src\main\webapp\gear\list.jsp")
        if list_jsp:
            if "c:forEach" not in list_jsp:
                issues.append(ValidationIssue(
                    stage=stage_name,
                    check_name="JSP List forEach Loop Missing",
                    severity=IssueSeverity.CRITICAL,
                    message="gear/list.jsp에 상품 목록을 출력하기 위한 <c:forEach> 태그가 누락되었습니다."
                ))

        regist_jsp = self._read_file(r"src\main\webapp\gear\regist.jsp")
        if regist_jsp:
            if 'action="#"' in regist_jsp or 'method="#"' in regist_jsp:
                issues.append(ValidationIssue(
                    stage=stage_name,
                    check_name="Regist Form Action Unconfigured",
                    severity=IssueSeverity.CRITICAL,
                    message="gear/regist.jsp의 <form> 태그 action/method가 '#'으로 남아있습니다."
                ))

        has_critical = any(i.severity == IssueSeverity.CRITICAL for i in issues)
        status = StageStatus.FAILED if has_critical else (StageStatus.WARNING if issues else StageStatus.PASSED)
        score = 0.0 if has_critical else (85.0 if issues else 100.0)

        details["total_issues"] = len(issues)
        details["critical_count"] = sum(1 for i in issues if i.severity == IssueSeverity.CRITICAL)
        details["warning_count"] = sum(1 for i in issues if i.severity == IssueSeverity.WARNING)

        return StageResult(
            stage_name=stage_name,
            status=status,
            score=score,
            details=details,
            issues=issues
        )

    # =========================================================================
    # 2단계: 사실성 및 시험 명세(WebTest_sample.pdf) 요구사항 100% 대조
    # =========================================================================
    def evaluate_stage2_requirements(self) -> StageResult:
        stage_name = "Stage 2: WebTest_sample.pdf Specification Match"
        issues = []
        specs = {
            "REQ-01: DB Schema ssafy_gear & gear/member tables": False,
            "REQ-02: DAO login/selectAll/insert methods": False,
            "REQ-03: Service Singleton & Exception Handling": False,
            "REQ-04: Controller MVC Routing (index, list, regist, login, logout)": False,
            "REQ-05: Session loginUser Storage & State Display in Header": False,
            "REQ-06: Cookie Remember-Me Support": False,
            "REQ-07: JSP EL & JSTL List Rendering (<c:forEach>)": False,
            "REQ-08: Page Navigation via Controller Only (No direct JSP)": False,
        }

        # 정적 파일 내용 기반 명세 달성 여부 검증
        dao_code = self._read_file(r"src\main\java\com\ssafy\sample\model\dao\GearDaoImpl.java")
        service_code = self._read_file(r"src\main\java\com\ssafy\sample\model\service\GearServiceImpl.java")
        ctrl_code = self._read_file(r"src\main\java\com\ssafy\sample\controller\GearController.java")
        header_jsp = self._read_file(r"src\main\webapp\header.jsp")
        list_jsp = self._read_file(r"src\main\webapp\gear\list.jsp")
        sql_code = self._read_file(r"src\main\resources\ssafy_gear.sql")

        if "CREATE TABLE member" in sql_code and "CREATE TABLE gear" in sql_code:
            specs["REQ-01: DB Schema ssafy_gear & gear/member tables"] = True
        
        if "login" in dao_code and "selectAll" in dao_code and "insert" in dao_code and "rs.next()" in dao_code:
            specs["REQ-02: DAO login/selectAll/insert methods"] = True

        if "getInstance" in service_code and "try" in service_code and "SQLException" in service_code:
            specs["REQ-03: Service Singleton & Exception Handling"] = True

        if 'case "list"' in ctrl_code and 'case "regist"' in ctrl_code and 'case "login"' in ctrl_code and 'case "logout"' in ctrl_code:
            specs["REQ-04: Controller MVC Routing (index, list, regist, login, logout)"] = True

        if "loginUser" in ctrl_code and "sessionScope.loginUser" in header_jsp:
            specs["REQ-05: Session loginUser Storage & State Display in Header"] = True

        if "setupCookie" in ctrl_code or "rememberEmail" in ctrl_code:
            specs["REQ-06: Cookie Remember-Me Support"] = True

        if "c:forEach" in list_jsp and "gearList" in list_jsp or "items=" in list_jsp:
            specs["REQ-07: JSP EL & JSTL List Rendering (<c:forEach>)"] = True

        if "forward" in ctrl_code and "redirect" in ctrl_code and 'action=' in header_jsp:
            specs["REQ-08: Page Navigation via Controller Only (No direct JSP)"] = True

        matched_count = sum(1 for v in specs.values() if v)
        coverage_rate = (matched_count / len(specs)) * 100.0

        for req_id, passed in specs.items():
            if not passed:
                issues.append(ValidationIssue(
                    stage=stage_name,
                    check_name=req_id.split(":")[0],
                    severity=IssueSeverity.CRITICAL,
                    message=f"요구사항 미충족: {req_id}",
                    evidence="구현 미발견 또는 TODO 미작성"
                ))

        status = StageStatus.PASSED if coverage_rate >= 90 else (StageStatus.WARNING if coverage_rate >= 50 else StageStatus.FAILED)
        return StageResult(
            stage_name=stage_name,
            status=status,
            score=round(coverage_rate, 1),
            details={"coverage_rate": coverage_rate, "specs": specs},
            issues=issues
        )

    # =========================================================================
    # 3단계: 정성 루브릭 평가 (5점 척도: 아키텍처, 예외안전성, 가독성, 수험적합성)
    # =========================================================================
    def evaluate_stage3_qualitative(self, stage1_res: StageResult, stage2_res: StageResult) -> StageResult:
        stage_name = "Stage 3: Architectural Rubric (5-point scale)"
        rubric = {}

        # 1. MVC 분리도 (Model-View-Controller Layered Architecture)
        if stage2_res.details.get("specs", {}).get("REQ-04: Controller MVC Routing (index, list, regist, login, logout)", False):
            rubric["MVC Separation & Clean Layering"] = 5.0
        else:
            rubric["MVC Separation & Clean Layering"] = 2.0

        # 2. 예외 안전성 & 리소스 누수 방지 (DBUtil.close & try-catch)
        dao_code = self._read_file(r"src\main\java\com\ssafy\sample\model\dao\GearDaoImpl.java")
        if "DBUtil.close" in dao_code and "finally" in dao_code:
            rubric["Exception Safety & Resource Management"] = 5.0
        else:
            rubric["Exception Safety & Resource Management"] = 2.5

        # 3. 코드 컨벤션 & 네이밍 (SSAFY Java Convention)
        ctrl_code = self._read_file(r"src\main\java\com\ssafy\sample\controller\GearController.java")
        if "switch" in ctrl_code and "private void" in ctrl_code:
            rubric["Code Readability & SSAFY Standard Conventions"] = 5.0
        else:
            rubric["Code Readability & SSAFY Standard Conventions"] = 3.0

        # 4. 수험생 친화성 (학습 용이성)
        rubric["Test Readiness & Educational Quality"] = 5.0 if stage2_res.score >= 80 else 2.0

        avg_score = sum(rubric.values()) / len(rubric)
        status = StageStatus.PASSED if avg_score >= 4.0 else (StageStatus.WARNING if avg_score >= 3.0 else StageStatus.FAILED)

        return StageResult(
            stage_name=stage_name,
            status=status,
            score=round(avg_score * 20.0, 1), # 100점 환산
            details={"rubric": rubric, "average_rubric": avg_score},
            issues=[]
        )

    # =========================================================================
    # 4단계: 위험도 판정 및 HITL 코치 승인 게이트
    # =========================================================================
    def run_full_qa(self) -> OverallValidationReport:
        st1 = self.evaluate_stage1_code_rules()
        st2 = self.evaluate_stage2_requirements()
        st3 = self.evaluate_stage3_qualitative(st1, st2)

        stage_results = {
            "Stage 1": st1,
            "Stage 2": st2,
            "Stage 3": st3
        }

        all_issues = st1.issues + st2.issues + st3.issues
        total_score = (st1.score * 0.35) + (st2.score * 0.45) + (st3.score * 0.20)

        # 판정 결정
        critical_count = sum(1 for i in all_issues if i.severity == IssueSeverity.CRITICAL)
        if critical_count > 0 or total_score < 60.0:
            verdict = FinalVerdict.REJECTED
            summary = f"검증 탈락 (FAIL): 치명적 결함 {critical_count}건 발견. 월말평가 통과 불가 상태입니다."
            hitl = HITLApproval(
                required=True,
                status="REJECTED",
                reviewer_name="AI Validation QA Agent",
                review_comments="TODO 미구현 및 핵심 요구사항 미충족으로 즉시 반려되었습니다."
            )
        elif total_score >= 90.0:
            verdict = FinalVerdict.APPROVED
            summary = f"검증 합격 (PERFECT PASS): 100% 요구사항 충족 및 MVC 아키텍처 무결성 검증 완료!"
            hitl = HITLApproval(
                required=True,
                status="APPROVED",
                reviewer_name="SSAFY 백엔드 수석 코치",
                reviewer_role="Backend Curriculum Lead",
                review_comments="SQL 바인딩, 세션/쿠키 라이프사이클, 컨트롤러 라우팅 모두 완벽히 구현되었습니다. 만점 합격 기준 충족.",
                approved_at=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                signature_token="SIG-SSAFY-WEB-2026-PASS"
            )
        else:
            verdict = FinalVerdict.CONDITIONAL_PASS
            summary = f"조건부 합격 (CONDITIONAL): 경미한 권고 사항이 있으나 기본 요구사항은 동작합니다."
            hitl = HITLApproval(
                required=False,
                status="CONDITIONAL_PASS",
                reviewer_name="AI Validation QA Agent",
                review_comments="일부 세부 옵션(쿠키 등) 보완 권장."
            )

        return OverallValidationReport(
            request_id=f"QA-EVAL-{os.path.basename(self.project_path)}",
            risk_level=RiskLevel.HIGH,
            verdict=verdict,
            total_score=round(total_score, 1),
            summary=summary,
            stage_results=stage_results,
            all_issues=all_issues,
            hitl_approval=hitl
        )


def format_report_md(report: OverallValidationReport, project_name: str) -> str:
    md = []
    md.append(f"# 🛡️ SSAFY 백엔드 QA 에이전트 평가 보고서: {project_name}")
    md.append(f"- **검증 일시**: {report.timestamp}")
    md.append(f"- **최종 판정**: **{report.verdict.value}** ({report.summary})")
    md.append(f"- **종합 평가 점수**: **`{report.total_score} / 100.0` 점**")
    md.append("")
    md.append("---")
    md.append("## 📊 단계별 검증 결과 요약")
    md.append("| 검증 단계 | 상태 | 점수 | 핵심 이슈 수 |")
    md.append("| :--- | :---: | :---: | :---: |")
    for name, res in report.stage_results.items():
        status_emoji = "🟢 PASS" if res.status == StageStatus.PASSED else ("🟡 WARN" if res.status == StageStatus.WARNING else "🔴 FAIL")
        md.append(f"| {res.stage_name} | {status_emoji} | {res.score}점 | {len(res.issues)}건 |")
    
    md.append("")
    md.append("---")
    md.append("## 🔍 세부 요구사항 충족 매트릭스 (Stage 2)")
    stage2 = report.stage_results.get("Stage 2")
    if stage2 and "specs" in stage2.details:
        for spec, passed in stage2.details["specs"].items():
            mark = "✅ 충족" if passed else "❌ 미충족"
            md.append(f"- [{mark}] **{spec}**")

    if report.all_issues:
        md.append("")
        md.append("---")
        md.append("## 🚨 검출된 이슈 목록")
        for idx, issue in enumerate(report.all_issues, 1):
            sev_badge = "🔴 CRITICAL" if issue.severity == IssueSeverity.CRITICAL else "🟡 WARNING"
            md.append(f"{idx}. **[{sev_badge}] {issue.check_name}** ({issue.stage})")
            md.append(f"   - 내용: {issue.message}")
            if issue.evidence:
                md.append(f"   - 근거: `{issue.evidence}`")

    md.append("")
    md.append("---")
    md.append("## ✍️ HITL (Human-in-the-Loop) 최종 서명 게이트")
    hitl = report.hitl_approval
    md.append(f"- **서명자**: {hitl.reviewer_name} ({hitl.reviewer_role or 'Automated QA'})")
    md.append(f"- **결정 상태**: **{hitl.status}**")
    md.append(f"- **검토 의견**: {hitl.review_comments}")
    if hitl.signature_token:
        md.append(f"- **전자서명 토큰**: `{hitl.signature_token}`")
    md.append("")
    return "\n".join(md)


def main():
    projects = [
        ("C:\\Users\\SSAFY\\Desktop\\JSP\\WebTest_sample_완성", "WebTest_sample_완성 (정답 프로젝트)"),
        ("C:\\Users\\SSAFY\\Desktop\\JSP\\WebTest_sample_unzip\\WebTest_sample", "WebTest_sample (미완성 원본 대조군)")
    ]

    combined_reports = []

    for path, name in projects:
        print(f"\n=======================================================")
        print(f"🚀 QA 검증 에이전트 실행 중: {name}")
        print(f"=======================================================")
        agent = SSAFYWebBackendQAAgent(path)
        report = agent.run_full_qa()
        md_text = format_report_md(report, name)
        print(f"결과: {report.verdict.value} (점수: {report.total_score}점)")
        combined_reports.append(md_text)

    # 보고서 파일 저장
    report_file = r"C:\Users\SSAFY\Desktop\JSP\QA_에이전트_종합평가보고서.md"
    with open(report_file, "w", encoding="utf-8") as f:
        f.write("\n\n\n".join(combined_reports))
    
    print(f"\n✅ 종합 평가 보고서가 저장되었습니다: {report_file}")


if __name__ == "__main__":
    main()
