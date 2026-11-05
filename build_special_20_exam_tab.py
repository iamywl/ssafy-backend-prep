# -*- coding: utf-8 -*-
"""
build_special_20_exam_tab.py
과목평가 핵심 족보 & 실전 적중 20제 탭을 생성하고 SVG 다이어그램 및 완벽 해설을 주입하는 스크립트
"""

import sys

def get_svg_diagram(item_id):
    if item_id == 1:
        # WHERE vs HAVING
        return '''<svg viewBox="0 0 680 150" style="width: 100%; max-width: 680px; height: auto; background: #0f172a; border-radius: 10px; margin: 12px 0; padding: 10px; box-sizing: border-box;">
  <defs>
    <marker id="arr1" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#38bdf8"/></marker>
  </defs>
  <rect x="15" y="45" width="105" height="60" rx="8" fill="#1e293b" stroke="#475569" stroke-width="2"/>
  <text x="67" y="73" fill="#94a3b8" font-size="12" font-weight="bold" text-anchor="middle">1. 원본 데이터</text>
  <text x="67" y="93" fill="#cbd5e1" font-size="13" font-weight="bold" text-anchor="middle">FROM 절</text>
  
  <line x1="120" y1="75" x2="145" y2="75" stroke="#38bdf8" stroke-width="2" marker-end="url(#arr1)"/>
  
  <rect x="145" y="30" width="135" height="90" rx="8" fill="#ef4444" fill-opacity="0.15" stroke="#ef4444" stroke-width="2"/>
  <text x="212" y="55" fill="#f87171" font-size="12" font-weight="bold" text-anchor="middle">2. WHERE 절</text>
  <text x="212" y="77" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">개별 행(Row) 필터</text>
  <text x="212" y="98" fill="#fca5a5" font-size="11" text-anchor="middle">❌ 집계함수 불가</text>
  <text x="212" y="112" fill="#94a3b8" font-size="10" text-anchor="middle">(그룹화 이전 시점)</text>
  
  <line x1="280" y1="75" x2="305" y2="75" stroke="#38bdf8" stroke-width="2" marker-end="url(#arr1)"/>
  
  <rect x="305" y="45" width="105" height="60" rx="8" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
  <text x="357" y="73" fill="#60a5fa" font-size="12" font-weight="bold" text-anchor="middle">3. 그룹 생성</text>
  <text x="357" y="93" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">GROUP BY</text>
  
  <line x1="410" y1="75" x2="435" y2="75" stroke="#38bdf8" stroke-width="2" marker-end="url(#arr1)"/>
  
  <rect x="435" y="30" width="135" height="90" rx="8" fill="#10b981" fill-opacity="0.15" stroke="#10b981" stroke-width="2"/>
  <text x="502" y="55" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">4. HAVING 절</text>
  <text x="502" y="77" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">그룹(Group) 필터</text>
  <text x="502" y="98" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">✅ 집계함수 가능</text>
  <text x="502" y="112" fill="#94a3b8" font-size="10" text-anchor="middle">(SUM, COUNT 등)</text>
  
  <line x1="570" y1="75" x2="595" y2="75" stroke="#38bdf8" stroke-width="2" marker-end="url(#arr1)"/>
  
  <rect x="595" y="45" width="70" height="60" rx="8" fill="#1e293b" stroke="#475569" stroke-width="2"/>
  <text x="630" y="73" fill="#94a3b8" font-size="11" font-weight="bold" text-anchor="middle">5. 최종출력</text>
  <text x="630" y="93" fill="#cbd5e1" font-size="12" font-weight="bold" text-anchor="middle">SELECT</text>
</svg>'''

    elif item_id == 2:
        # forward vs sendRedirect
        return '''<svg viewBox="0 0 680 180" style="width: 100%; max-width: 680px; height: auto; background: #0f172a; border-radius: 10px; margin: 12px 0; padding: 10px; box-sizing: border-box;">
  <defs>
    <marker id="arrF" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#38bdf8"/></marker>
    <marker id="arrR" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#f59e0b"/></marker>
  </defs>
  <!-- forward side -->
  <rect x="15" y="15" width="315" height="150" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="172" y="38" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">🔹 forward (서버 내부 포워딩)</text>
  <rect x="30" y="55" width="70" height="35" rx="6" fill="#334155"/>
  <text x="65" y="77" fill="#f8fafc" font-size="11" text-anchor="middle">브라우저</text>
  <line x1="100" y1="72" x2="160" y2="72" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrF)"/>
  <rect x="160" y="50" width="150" height="45" rx="6" fill="#1e1b4b" stroke="#6366f1"/>
  <text x="235" y="68" fill="#a5b4fc" font-size="11" text-anchor="middle">서버: 서블릿 ➔ JSP</text>
  <text x="235" y="85" fill="#e0e7ff" font-size="10" text-anchor="middle">내부 제어권 위임</text>
  <line x1="160" y1="85" x2="100" y2="85" stroke="#38bdf8" stroke-dasharray="3,3" stroke-width="1.5"/>
  <text x="172" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">① 왕복 1회 | ② URL 불변 | ③ request 유지(O)</text>
  <text x="172" y="135" fill="#94a3b8" font-size="10" text-anchor="middle">request.setAttribute() 데이터 그대로 JSP 전달</text>
  <text x="172" y="150" fill="#cbd5e1" font-size="9" text-anchor="middle">rd.forward(request, response);</text>

  <!-- redirect side -->
  <rect x="350" y="15" width="315" height="150" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="507" y="38" fill="#f59e0b" font-size="14" font-weight="bold" text-anchor="middle">🔸 sendRedirect (브라우저 재요청)</text>
  <rect x="365" y="55" width="65" height="35" rx="6" fill="#334155"/>
  <text x="397" y="77" fill="#f8fafc" font-size="11" text-anchor="middle">브라우저</text>
  <line x1="430" y1="65" x2="520" y2="65" stroke="#f59e0b" stroke-width="2" marker-end="url(#arrR)"/>
  <line x1="520" y1="75" x2="430" y2="75" stroke="#f59e0b" stroke-dasharray="3,3" stroke-width="1.5"/>
  <text x="475" y="60" fill="#fcd34d" font-size="9" text-anchor="middle">1. 요청 / 2. 302 응답</text>
  <rect x="520" y="50" width="130" height="45" rx="6" fill="#451a03" stroke="#d97706"/>
  <text x="585" y="70" fill="#fed7aa" font-size="11" text-anchor="middle">서버: 서블릿</text>
  <text x="585" y="85" fill="#fdba74" font-size="9" text-anchor="middle">302 Move URL 응답</text>
  <text x="507" y="115" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">① 왕복 2회 | ② URL 변경(O) | ③ request 초기화(X)</text>
  <text x="507" y="135" fill="#94a3b8" font-size="10" text-anchor="middle">완전히 새로운 요청이므로 request 데이터 소멸</text>
  <text x="507" y="150" fill="#cbd5e1" font-size="9" text-anchor="middle">response.sendRedirect(url);</text>
</svg>'''

    elif item_id == 3:
        # DB 정규화 1NF, 2NF, 3NF
        return '''<svg viewBox="0 0 680 150" style="width: 100%; max-width: 680px; height: auto; background: #0f172a; border-radius: 10px; margin: 12px 0; padding: 10px; box-sizing: border-box;">
  <defs>
    <marker id="arrN" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#38bdf8"/></marker>
  </defs>
  <!-- 1NF -->
  <rect x="15" y="20" width="200" height="110" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <rect x="25" y="28" width="55" height="22" rx="4" fill="#0284c7"/>
  <text x="52" y="43" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">1NF ★</text>
  <text x="135" y="44" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">제1정규화</text>
  <text x="115" y="70" fill="#f1f5f9" font-size="12" font-weight="bold" text-anchor="middle">원자값(Atomic) 보장</text>
  <text x="115" y="90" fill="#94a3b8" font-size="10" text-anchor="middle">모든 컬럼은 더 이상</text>
  <text x="115" y="105" fill="#94a3b8" font-size="10" text-anchor="middle">쪼갤 수 없는 단일 값만 저장</text>

  <line x1="215" y1="75" x2="245" y2="75" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrN)"/>

  <!-- 2NF -->
  <rect x="245" y="20" width="200" height="110" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
  <rect x="255" y="28" width="55" height="22" rx="4" fill="#7e22ce"/>
  <text x="282" y="43" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">2NF</text>
  <text x="365" y="44" fill="#c084fc" font-size="13" font-weight="bold" text-anchor="middle">제2정규화</text>
  <text x="345" y="70" fill="#f1f5f9" font-size="12" font-weight="bold" text-anchor="middle">부분 함수 종속성 제거</text>
  <text x="345" y="90" fill="#94a3b8" font-size="10" text-anchor="middle">복합 기본키(PK)의 일부에만</text>
  <text x="345" y="105" fill="#94a3b8" font-size="10" text-anchor="middle">종속되는 컬럼을 별도 테이블로 분리</text>

  <line x1="445" y1="75" x2="475" y2="75" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrN)"/>

  <!-- 3NF -->
  <rect x="475" y="20" width="190" height="110" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
  <rect x="485" y="28" width="55" height="22" rx="4" fill="#047857"/>
  <text x="512" y="43" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">3NF</text>
  <text x="590" y="44" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">제3정규화</text>
  <text x="570" y="70" fill="#f1f5f9" font-size="12" font-weight="bold" text-anchor="middle">이행 함수 종속성 제거</text>
  <text x="570" y="90" fill="#94a3b8" font-size="10" text-anchor="middle">일반 컬럼 간 꼬리물기 종속</text>
  <text x="570" y="105" fill="#94a3b8" font-size="10" text-anchor="middle">(A ➔ B ➔ C) 제거</text>
</svg>'''

    elif item_id == 4:
        # Full Table Scan vs Index Scan
        return '''<svg viewBox="0 0 680 150" style="width: 100%; max-width: 680px; height: auto; background: #0f172a; border-radius: 10px; margin: 12px 0; padding: 10px; box-sizing: border-box;">
  <defs>
    <marker id="arrFts" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#ef4444"/></marker>
    <marker id="arrIdx" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#10b981"/></marker>
  </defs>
  <!-- Full Table Scan -->
  <rect x="20" y="15" width="305" height="120" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
  <text x="172" y="38" fill="#f87171" font-size="14" font-weight="bold" text-anchor="middle">🚨 Full Table Scan (FTS) ★</text>
  <text x="172" y="58" fill="#fca5a5" font-size="11" text-anchor="middle">인덱스 없이 테이블 처음부터 끝까지 전체 행 스캔</text>
  <g transform="translate(45, 68)">
    <rect x="0" y="0" width="40" height="25" rx="3" fill="#7f1d1d" stroke="#ef4444"/><text x="20" y="17" fill="#fff" font-size="10" text-anchor="middle">행 1</text>
    <rect x="48" y="0" width="40" height="25" rx="3" fill="#7f1d1d" stroke="#ef4444"/><text x="68" y="17" fill="#fff" font-size="10" text-anchor="middle">행 2</text>
    <rect x="96" y="0" width="40" height="25" rx="3" fill="#7f1d1d" stroke="#ef4444"/><text x="116" y="17" fill="#fff" font-size="10" text-anchor="middle">행 3</text>
    <rect x="144" y="0" width="40" height="25" rx="3" fill="#7f1d1d" stroke="#ef4444"/><text x="164" y="17" fill="#fff" font-size="10" text-anchor="middle">행 4</text>
    <rect x="192" y="0" width="55" height="25" rx="3" fill="#b91c1c" stroke="#ef4444"/><text x="219" y="17" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">...전체</text>
    <line x1="5" y1="32" x2="240" y2="32" stroke="#ef4444" stroke-width="2" marker-end="url(#arrFts)"/>
  </g>
  <text x="172" y="123" fill="#cbd5e1" font-size="10" text-anchor="middle">I/O 디스크 부하 극대화 (인덱스 미존재 or 컬럼 변형 시 발생)</text>

  <!-- Index Scan -->
  <rect x="355" y="15" width="305" height="120" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
  <text x="507" y="38" fill="#34d399" font-size="14" font-weight="bold" text-anchor="middle">⚡ Index Range Scan (인덱스 검색)</text>
  <text x="507" y="58" fill="#6ee7b7" font-size="11" text-anchor="middle">B-Tree 정렬 목차를 타고 원하는 타겟 행만 즉시 접근</text>
  <g transform="translate(390, 68)">
    <rect x="80" y="0" width="60" height="20" rx="3" fill="#065f46" stroke="#10b981"/><text x="110" y="14" fill="#fff" font-size="10" text-anchor="middle">Root Node</text>
    <path d="M 110 20 L 70 35" stroke="#10b981" stroke-width="1.5"/>
    <rect x="40" y="35" width="60" height="20" rx="3" fill="#047857" stroke="#10b981"/><text x="70" y="49" fill="#fff" font-size="10" text-anchor="middle">Leaf [타겟]</text>
  </g>
  <text x="507" y="123" fill="#cbd5e1" font-size="10" text-anchor="middle">최소 I/O 디스크 읽기로 초고속 데이터 조회</text>
</svg>'''

    elif item_id == 5:
        # SAVEPOINT timeline
        return '''<svg viewBox="0 0 680 150" style="width: 100%; max-width: 680px; height: auto; background: #0f172a; border-radius: 10px; margin: 12px 0; padding: 10px; box-sizing: border-box;">
  <defs>
    <marker id="arrSp" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#38bdf8"/></marker>
    <marker id="arrRb" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#f43f5e"/></marker>
  </defs>
  <text x="340" y="25" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">트랜잭션 부분 취소(Rollback) 메커니즘</text>
  
  <line x1="40" y1="75" x2="620" y2="75" stroke="#475569" stroke-width="3"/>
  
  <!-- Step 1 -->
  <circle cx="90" cy="75" r="14" fill="#10b981"/>
  <text x="90" y="80" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">1</text>
  <text x="90" y="105" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">1번 데이터 수정</text>
  <text x="90" y="120" fill="#94a3b8" font-size="10" text-anchor="middle">(성공)</text>
  
  <!-- SAVEPOINT -->
  <rect x="200" y="50" width="130" height="50" rx="8" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
  <text x="265" y="70" fill="#a5b4fc" font-size="11" font-weight="bold" text-anchor="middle">🚩 SAVEPOINT SP1;</text>
  <text x="265" y="88" fill="#e0e7ff" font-size="10" text-anchor="middle">중간 체크포인트 기록</text>
  
  <!-- Step 2 (Error) -->
  <circle cx="430" cy="75" r="14" fill="#ef4444"/>
  <text x="430" y="80" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">2</text>
  <text x="430" y="105" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">2번 작업 오류 발생 💥</text>
  <text x="430" y="120" fill="#fca5a5" font-size="10" text-anchor="middle">SQL 예외 발생</text>
  
  <!-- Rollback arrow -->
  <path d="M 430 55 Q 350 25 270 50" fill="none" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="4,4" marker-end="url(#arrRb)"/>
  <text x="350" y="32" fill="#fb7185" font-size="11" font-weight="bold" text-anchor="middle">ROLLBACK TO SP1; (2번만 취소!)</text>

  <!-- Final Commit -->
  <rect x="540" y="55" width="100" height="40" rx="6" fill="#065f46" stroke="#10b981" stroke-width="2"/>
  <text x="590" y="74" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">COMMIT;</text>
  <text x="590" y="88" fill="#a7f3d0" font-size="9" text-anchor="middle">1번 작업 최종 반영</text>
</svg>'''

    elif item_id == 6:
        # 단일행 내장함수 4대장
        return '''<svg viewBox="0 0 680 140" style="width: 100%; max-width: 680px; height: auto; background: #0f172a; border-radius: 10px; margin: 12px 0; padding: 10px; box-sizing: border-box;">
  <g transform="translate(15, 15)">
    <rect x="0" y="0" width="150" height="110" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="75" y="25" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">CONCAT ★</text>
    <text x="75" y="45" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">문자열 결합 함수</text>
    <rect x="15" y="55" width="120" height="45" rx="4" fill="#0f172a"/>
    <text x="75" y="72" fill="#94a3b8" font-size="9" text-anchor="middle">CONCAT('A', 'B')</text>
    <text x="75" y="90" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">➔ 'AB'</text>
  </g>
  <g transform="translate(180, 15)">
    <rect x="0" y="0" width="150" height="110" rx="8" fill="#1e293b" stroke="#818cf8" stroke-width="1.5"/>
    <text x="75" y="25" fill="#818cf8" font-size="13" font-weight="bold" text-anchor="middle">SUBSTR</text>
    <text x="75" y="45" fill="#f8fafc" font-size="11" text-anchor="middle">부분 문자열 추출</text>
    <rect x="15" y="55" width="120" height="45" rx="4" fill="#0f172a"/>
    <text x="75" y="72" fill="#94a3b8" font-size="9" text-anchor="middle">SUBSTR('SSAFY',1,3)</text>
    <text x="75" y="90" fill="#a5b4fc" font-size="11" font-weight="bold" text-anchor="middle">➔ 'SSA'</text>
  </g>
  <g transform="translate(345, 15)">
    <rect x="0" y="0" width="150" height="110" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="75" y="25" fill="#f59e0b" font-size="13" font-weight="bold" text-anchor="middle">LENGTH</text>
    <text x="75" y="45" fill="#f8fafc" font-size="11" text-anchor="middle">문자열 길이 반환</text>
    <rect x="15" y="55" width="120" height="45" rx="4" fill="#0f172a"/>
    <text x="75" y="72" fill="#94a3b8" font-size="9" text-anchor="middle">LENGTH('Java')</text>
    <text x="75" y="90" fill="#fcd34d" font-size="11" font-weight="bold" text-anchor="middle">➔ 4</text>
  </g>
  <g transform="translate(510, 15)">
    <rect x="0" y="0" width="155" height="110" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="77" y="25" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">ROUND</text>
    <text x="77" y="45" fill="#f8fafc" font-size="11" text-anchor="middle">지정 자리 반올림</text>
    <rect x="15" y="55" width="125" height="45" rx="4" fill="#0f172a"/>
    <text x="77" y="72" fill="#94a3b8" font-size="9" text-anchor="middle">ROUND(12.345, 1)</text>
    <text x="77" y="90" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">➔ 12.3</text>
  </g>
</svg>'''

    elif item_id == 7:
        # JSESSIONID cookie flow
        return '''<svg viewBox="0 0 680 160" style="width: 100%; max-width: 680px; height: auto; background: #0f172a; border-radius: 10px; margin: 12px 0; padding: 10px; box-sizing: border-box;">
  <defs>
    <marker id="arrJ" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#38bdf8"/></marker>
  </defs>
  <!-- Browser -->
  <rect x="25" y="25" width="120" height="110" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
  <text x="85" y="50" fill="#94a3b8" font-size="12" font-weight="bold" text-anchor="middle">클라이언트</text>
  <text x="85" y="72" fill="#f8fafc" font-size="14" font-weight="bold" text-anchor="middle">브라우저</text>
  <rect x="35" y="90" width="100" height="30" rx="4" fill="#334155"/>
  <text x="85" y="108" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">쿠키 저장소</text>

  <!-- Server -->
  <rect x="535" y="25" width="120" height="110" rx="8" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
  <text x="595" y="50" fill="#60a5fa" font-size="12" font-weight="bold" text-anchor="middle">WAS 컨테이너</text>
  <text x="595" y="72" fill="#f8fafc" font-size="14" font-weight="bold" text-anchor="middle">Tomcat 서버</text>
  <rect x="545" y="90" width="100" height="30" rx="4" fill="#1e3a8a"/>
  <text x="595" y="108" fill="#93c5fd" font-size="10" font-weight="bold" text-anchor="middle">HttpSession 풀</text>

  <!-- Arrows -->
  <path d="M 145 50 L 530 50" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrJ)"/>
  <text x="340" y="42" fill="#93c5fd" font-size="10" text-anchor="middle">1. 첫 HTTP 요청 (세션 없음)</text>

  <path d="M 535 78 L 150 78" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,4" marker-end="url(#arrJ)"/>
  <text x="340" y="72" fill="#fcd34d" font-size="11" font-weight="bold" text-anchor="middle">2. Set-Cookie: JSESSIONID=AB39F... 발급 ★</text>

  <path d="M 145 110 L 530 110" stroke="#10b981" stroke-width="2" marker-end="url(#arrJ)"/>
  <text x="340" y="104" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">3. 이후 모든 요청 시 Cookie: JSESSIONID 헤더 전송 ➔ 사용자 식별!</text>
</svg>'''

    elif item_id == 8:
        # Front Controller Pattern
        return '''<svg viewBox="0 0 680 150" style="width: 100%; max-width: 680px; height: auto; background: #0f172a; border-radius: 10px; margin: 12px 0; padding: 10px; box-sizing: border-box;">
  <defs>
    <marker id="arrFc" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#38bdf8"/></marker>
  </defs>
  <!-- Clients -->
  <rect x="15" y="20" width="100" height="110" rx="6" fill="#1e293b" stroke="#475569"/>
  <text x="65" y="45" fill="#94a3b8" font-size="11" font-weight="bold" text-anchor="middle">클라이언트들</text>
  <text x="65" y="70" fill="#f8fafc" font-size="10" text-anchor="middle">/gear?action=list</text>
  <text x="65" y="90" fill="#f8fafc" font-size="10" text-anchor="middle">/gear?action=regist</text>
  <text x="65" y="110" fill="#f8fafc" font-size="10" text-anchor="middle">/gear?action=detail</text>

  <line x1="115" y1="75" x2="160" y2="75" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrFc)"/>

  <!-- Front Controller -->
  <rect x="160" y="15" width="220" height="120" rx="8" fill="#1e1b4b" stroke="#818cf8" stroke-width="2.5"/>
  <rect x="175" y="25" width="190" height="26" rx="4" fill="#4338ca"/>
  <text x="270" y="42" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">★ Front Controller (단일 진입점)</text>
  <text x="270" y="70" fill="#c7d2fe" font-size="11" text-anchor="middle">공통 작업 일괄 처리:</text>
  <text x="270" y="88" fill="#a5b4fc" font-size="10" text-anchor="middle">인코딩 설정, 세션 검증, 로깅, 예외 핸들링</text>
  <text x="270" y="112" fill="#fcd34d" font-size="10" font-weight="bold" text-anchor="middle">요청 action에 따라 세부 로직 위임!</text>

  <line x1="380" y1="75" x2="425" y2="75" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrFc)"/>

  <!-- Sub handlers -->
  <g transform="translate(425, 20)">
    <rect x="0" y="0" width="110" height="28" rx="4" fill="#334155"/><text x="55" y="18" fill="#f8fafc" font-size="10" text-anchor="middle">GearService.list()</text>
    <rect x="0" y="38" width="110" height="28" rx="4" fill="#334155"/><text x="55" y="56" fill="#f8fafc" font-size="10" text-anchor="middle">GearService.insert()</text>
    <rect x="0" y="76" width="110" height="28" rx="4" fill="#334155"/><text x="55" y="94" fill="#f8fafc" font-size="10" text-anchor="middle">GearService.detail()</text>
  </g>

  <line x1="535" y1="75" x2="570" y2="75" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrFc)"/>
  <!-- DAO/DB -->
  <rect x="570" y="35" width="95" height="75" rx="6" fill="#1e293b" stroke="#10b981"/>
  <text x="617" y="65" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">DAO ➔ DB</text>
  <text x="617" y="85" fill="#94a3b8" font-size="10" text-anchor="middle">데이터 영속화</text>
</svg>'''

    elif item_id == 9:
        # service() method routing
        return '''<svg viewBox="0 0 680 140" style="width: 100%; max-width: 680px; height: auto; background: #0f172a; border-radius: 10px; margin: 12px 0; padding: 10px; box-sizing: border-box;">
  <defs>
    <marker id="arrSvc" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#38bdf8"/></marker>
  </defs>
  <rect x="20" y="40" width="120" height="60" rx="8" fill="#1e293b" stroke="#475569" stroke-width="2"/>
  <text x="80" y="65" fill="#94a3b8" font-size="11" font-weight="bold" text-anchor="middle">클라이언트</text>
  <text x="80" y="85" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">HTTP 요청</text>

  <line x1="140" y1="70" x2="190" y2="70" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrSvc)"/>

  <rect x="190" y="25" width="220" height="90" rx="8" fill="#1e1b4b" stroke="#6366f1" stroke-width="2.5"/>
  <text x="300" y="52" fill="#a5b4fc" font-size="14" font-weight="bold" text-anchor="middle">★ service(req, res)</text>
  <text x="300" y="73" fill="#ffffff" font-size="11" text-anchor="middle">서블릿 호출 시 최우선 실행!</text>
  <text x="300" y="93" fill="#cbd5e1" font-size="10" text-anchor="middle">요청 Method(GET/POST) 판별 및 분기</text>

  <path d="M 410 55 L 470 35" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrSvc)"/>
  <rect x="470" y="15" width="180" height="40" rx="6" fill="#065f46" stroke="#10b981" stroke-width="2"/>
  <text x="560" y="38" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">doGet(request, response)</text>

  <path d="M 410 85 L 470 105" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrSvc)"/>
  <rect x="470" y="85" width="180" height="40" rx="6" fill="#78350f" stroke="#f59e0b" stroke-width="2"/>
  <text x="560" y="108" fill="#fcd34d" font-size="12" font-weight="bold" text-anchor="middle">doPost(request, response)</text>
</svg>'''

    elif item_id == 10:
        # web.xml error-page mapping
        return '''<svg viewBox="0 0 680 140" style="width: 100%; max-width: 680px; height: auto; background: #0f172a; border-radius: 10px; margin: 12px 0; padding: 10px; box-sizing: border-box;">
  <rect x="25" y="20" width="630" height="100" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <rect x="40" y="32" width="140" height="30" rx="4" fill="#0284c7"/>
  <text x="110" y="52" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">&lt;error-page&gt; ★</text>
  <text x="195" y="52" fill="#93c5fd" font-size="11">(최상위 태그: web.xml 공통 에러 매핑)</text>

  <g transform="translate(60, 72)">
    <rect x="0" y="0" width="230" height="35" rx="4" fill="#334155" stroke="#64748b"/>
    <text x="115" y="22" fill="#fcd34d" font-size="11" font-weight="bold" text-anchor="middle">&lt;error-code&gt; 404 &lt;/error-code&gt;</text>
    <text x="245" y="22" fill="#94a3b8" font-size="10">(또는 &lt;exception-type&gt;)</text>

    <rect x="360" y="0" width="220" height="35" rx="4" fill="#334155" stroke="#64748b"/>
    <text x="470" y="22" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">&lt;location&gt; /error/404.jsp &lt;/location&gt;</text>
  </g>
</svg>'''

    elif item_id == 11:
        # Primary Key = NOT NULL + UNIQUE
        return '''<svg viewBox="0 0 680 140" style="width: 100%; max-width: 680px; height: auto; background: #0f172a; border-radius: 10px; margin: 12px 0; padding: 10px; box-sizing: border-box;">
  <circle cx="270" cy="70" r="50" fill="#3b82f6" fill-opacity="0.25" stroke="#3b82f6" stroke-width="2.5"/>
  <text x="220" y="75" fill="#93c5fd" font-size="13" font-weight="bold" text-anchor="middle">NOT NULL</text>
  <text x="220" y="93" fill="#cbd5e1" font-size="10" text-anchor="middle">(빈 값 금지)</text>

  <circle cx="410" cy="70" r="50" fill="#10b981" fill-opacity="0.25" stroke="#10b981" stroke-width="2.5"/>
  <text x="460" y="75" fill="#6ee7b7" font-size="13" font-weight="bold" text-anchor="middle">UNIQUE</text>
  <text x="460" y="93" fill="#cbd5e1" font-size="10" text-anchor="middle">(중복 값 금지)</text>

  <!-- Intersection -->
  <rect x="295" y="40" width="90" height="60" rx="8" fill="#f59e0b" fill-opacity="0.4" stroke="#f59e0b" stroke-width="2"/>
  <text x="340" y="66" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">PRIMARY</text>
  <text x="340" y="84" fill="#fef08a" font-size="13" font-weight="bold" text-anchor="middle">KEY ★</text>

  <text x="340" y="125" fill="#e2e8f0" font-size="11" text-anchor="middle">개체 무결성 보장: 테이블의 모든 튜플(Row)을 유일하게 식별</text>
</svg>'''

    elif item_id == 12:
        # SQL 집합 연산자 4종 (EXCEPT, UNION, INTERSECT, CROSS JOIN)
        return '''<svg viewBox="0 0 680 145" style="width: 100%; max-width: 680px; height: auto; background: #0f172a; border-radius: 10px; margin: 12px 0; padding: 10px; box-sizing: border-box;">
  <!-- EXCEPT -->
  <g transform="translate(15, 10)">
    <rect x="0" y="0" width="150" height="120" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <text x="75" y="24" fill="#f87171" font-size="12" font-weight="bold" text-anchor="middle">① EXCEPT ★ (차집합)</text>
    <circle cx="55" cy="58" r="22" fill="#ef4444" fill-opacity="0.7" stroke="#ef4444"/>
    <circle cx="85" cy="58" r="22" fill="#1e293b" stroke="#64748b"/>
    <text x="50" y="62" fill="#fff" font-size="10" font-weight="bold">A</text>
    <text x="90" y="62" fill="#94a3b8" font-size="10">B</text>
    <text x="75" y="100" fill="#fca5a5" font-size="10" font-weight="bold" text-anchor="middle">A 결과에서 B 제외</text>
  </g>
  <!-- UNION -->
  <g transform="translate(180, 10)">
    <rect x="0" y="0" width="150" height="120" rx="8" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="75" y="24" fill="#60a5fa" font-size="12" font-weight="bold" text-anchor="middle">② UNION (합집합)</text>
    <circle cx="55" cy="58" r="22" fill="#3b82f6" fill-opacity="0.5" stroke="#3b82f6"/>
    <circle cx="85" cy="58" r="22" fill="#3b82f6" fill-opacity="0.5" stroke="#3b82f6"/>
    <text x="75" y="100" fill="#93c5fd" font-size="10" text-anchor="middle">A와 B 결과 전체 병합</text>
  </g>
  <!-- INTERSECT -->
  <g transform="translate(345, 10)">
    <rect x="0" y="0" width="150" height="120" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="75" y="24" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">③ INTERSECT (교집합)</text>
    <circle cx="55" cy="58" r="22" fill="#1e293b" stroke="#64748b"/>
    <circle cx="85" cy="58" r="22" fill="#1e293b" stroke="#64748b"/>
    <!-- intersection overlap -->
    <ellipse cx="70" cy="58" rx="8" ry="15" fill="#10b981"/>
    <text x="75" y="100" fill="#6ee7b7" font-size="10" text-anchor="middle">공통된 행만 추출</text>
  </g>
  <!-- CROSS JOIN -->
  <g transform="translate(510, 10)">
    <rect x="0" y="0" width="155" height="120" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <text x="77" y="24" fill="#c084fc" font-size="12" font-weight="bold" text-anchor="middle">④ CROSS JOIN</text>
    <text x="77" y="58" fill="#e9d5ff" font-size="14" font-weight="bold" text-anchor="middle">M × N 조합</text>
    <text x="77" y="80" fill="#cbd5e1" font-size="10" text-anchor="middle">(카티션 곱)</text>
    <text x="77" y="100" fill="#a855f7" font-size="10" text-anchor="middle">모든 가능한 경우의 수</text>
  </g>
</svg>'''

    elif item_id == 13:
        # MySQL LIMIT 페이징 계산
        return '''<svg viewBox="0 0 680 145" style="width: 100%; max-width: 680px; height: auto; background: #0f172a; border-radius: 10px; margin: 12px 0; padding: 10px; box-sizing: border-box;">
  <text x="340" y="25" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">MySQL LIMIT Offset(시작점), Count(개수) 계산 공식</text>
  
  <g transform="translate(25, 45)">
    <rect x="0" y="0" width="135" height="50" rx="6" fill="#334155"/>
    <text x="67" y="22" fill="#94a3b8" font-size="11" text-anchor="middle">1페이지 (15개)</text>
    <text x="67" y="40" fill="#cbd5e1" font-size="11" font-weight="bold" text-anchor="middle">LIMIT 0, 15</text>
  </g>
  <g transform="translate(175, 45)">
    <rect x="0" y="0" width="135" height="50" rx="6" fill="#334155"/>
    <text x="67" y="22" fill="#94a3b8" font-size="11" text-anchor="middle">2페이지 (15개)</text>
    <text x="67" y="40" fill="#cbd5e1" font-size="11" font-weight="bold" text-anchor="middle">LIMIT 15, 15</text>
  </g>
  <g transform="translate(325, 45)">
    <rect x="0" y="0" width="135" height="50" rx="6" fill="#334155"/>
    <text x="67" y="22" fill="#94a3b8" font-size="11" text-anchor="middle">3페이지 (15개)</text>
    <text x="67" y="40" fill="#cbd5e1" font-size="11" font-weight="bold" text-anchor="middle">LIMIT 30, 15</text>
  </g>
  <g transform="translate(475, 40)">
    <rect x="0" y="0" width="170" height="60" rx="8" fill="#1e1b4b" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="85" y="23" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">★ 4페이지 (currentPage=4)</text>
    <text x="85" y="43" fill="#fcd34d" font-size="14" font-weight="bold" text-anchor="middle">LIMIT 45, 15</text>
    <text x="85" y="55" fill="#a5b4fc" font-size="9" text-anchor="middle">Offset: (4-1)*15 = 45</text>
  </g>
  <text x="340" y="125" fill="#93c5fd" font-size="11" text-anchor="middle">공식: LIMIT (currentPage - 1) * pageSize, pageSize</text>
</svg>'''

    elif item_id == 14:
        # 4대 Scope 순서
        return '''<svg viewBox="0 0 680 140" style="width: 100%; max-width: 680px; height: auto; background: #0f172a; border-radius: 10px; margin: 12px 0; padding: 10px; box-sizing: border-box;">
  <defs>
    <marker id="arrSc" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#38bdf8"/></marker>
  </defs>
  <text x="340" y="25" fill="#94a3b8" font-size="12" text-anchor="middle">유효 범위 및 생명주기가 좁고 짧은 순서 ➔ 넓고 긴 순서</text>

  <g transform="translate(30, 45)">
    <rect x="0" y="0" width="120" height="65" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
    <text x="60" y="28" fill="#94a3b8" font-size="11" text-anchor="middle">1단계</text>
    <text x="60" y="48" fill="#f8fafc" font-size="14" font-weight="bold" text-anchor="middle">page</text>
    <text x="60" y="60" fill="#64748b" font-size="9" text-anchor="middle">(현재 JSP 1장)</text>
  </g>
  <line x1="160" y1="78" x2="185" y2="78" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrSc)"/>

  <g transform="translate(185, 45)">
    <rect x="0" y="0" width="120" height="65" rx="8" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
    <text x="60" y="28" fill="#60a5fa" font-size="11" text-anchor="middle">2단계</text>
    <text x="60" y="48" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">request</text>
    <text x="60" y="60" fill="#93c5fd" font-size="9" text-anchor="middle">(1회 요청-응답)</text>
  </g>
  <line x1="315" y1="78" x2="340" y2="78" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrSc)"/>

  <g transform="translate(340, 45)">
    <rect x="0" y="0" width="120" height="65" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="60" y="28" fill="#fcd34d" font-size="11" text-anchor="middle">3단계</text>
    <text x="60" y="48" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">session</text>
    <text x="60" y="60" fill="#fde68a" font-size="9" text-anchor="middle">(브라우저 세션)</text>
  </g>
  <line x1="470" y1="78" x2="495" y2="78" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrSc)"/>

  <g transform="translate(495, 45)">
    <rect x="0" y="0" width="145" height="65" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2.5"/>
    <text x="72" y="28" fill="#34d399" font-size="11" text-anchor="middle">4단계</text>
    <text x="72" y="48" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">application</text>
    <text x="72" y="60" fill="#a7f3d0" font-size="9" text-anchor="middle">(WAS 서버 전체 공유)</text>
  </g>
  <text x="340" y="128" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">암기 공식: page ➔ request ➔ session ➔ application</text>
</svg>'''

    elif item_id == 15:
        # JSP 스크립트 요소
        return '''<svg viewBox="0 0 680 145" style="width: 100%; max-width: 680px; height: auto; background: #0f172a; border-radius: 10px; margin: 12px 0; padding: 10px; box-sizing: border-box;">
  <g transform="translate(15, 10)">
    <rect x="0" y="0" width="150" height="120" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="75" y="24" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">표현식 &lt;%= %&gt; ★</text>
    <rect x="15" y="38" width="120" height="40" rx="4" fill="#0f172a"/>
    <text x="75" y="55" fill="#fcd34d" font-size="10" text-anchor="middle">&lt;%= name %&gt;</text>
    <text x="75" y="70" fill="#34d399" font-size="10" font-weight="bold" text-anchor="middle">out.print(name)</text>
    <text x="75" y="100" fill="#93c5fd" font-size="10" text-anchor="middle">브라우저 바로 출력</text>
  </g>
  <g transform="translate(180, 10)">
    <rect x="0" y="0" width="150" height="120" rx="8" fill="#1e293b" stroke="#818cf8" stroke-width="1.5"/>
    <text x="75" y="24" fill="#818cf8" font-size="12" font-weight="bold" text-anchor="middle">스크립틀릿 &lt;% %&gt;</text>
    <rect x="15" y="38" width="120" height="40" rx="4" fill="#0f172a"/>
    <text x="75" y="55" fill="#e0e7ff" font-size="10" text-anchor="middle">&lt;% int a=10; %&gt;</text>
    <text x="75" y="70" fill="#a5b4fc" font-size="9" text-anchor="middle">_jspService() 내부</text>
    <text x="75" y="100" fill="#cbd5e1" font-size="10" text-anchor="middle">메서드 지역변수</text>
  </g>
  <g transform="translate(345, 10)">
    <rect x="0" y="0" width="150" height="120" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="75" y="24" fill="#f59e0b" font-size="12" font-weight="bold" text-anchor="middle">선언문 &lt;%! %&gt;</text>
    <rect x="15" y="38" width="120" height="40" rx="4" fill="#0f172a"/>
    <text x="75" y="55" fill="#fde68a" font-size="10" text-anchor="middle">&lt;%! int count; %&gt;</text>
    <text x="75" y="70" fill="#f59e0b" font-size="9" text-anchor="middle">클래스 멤버 변수</text>
    <text x="75" y="100" fill="#fed7aa" font-size="10" text-anchor="middle">서블릿 필드/메서드</text>
  </g>
  <g transform="translate(510, 10)">
    <rect x="0" y="0" width="155" height="120" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="77" y="24" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">지시자 &lt;%@ %&gt;</text>
    <rect x="15" y="38" width="125" height="40" rx="4" fill="#0f172a"/>
    <text x="77" y="55" fill="#a7f3d0" font-size="9" text-anchor="middle">&lt;%@ page ... %&gt;</text>
    <text x="77" y="70" fill="#6ee7b7" font-size="9" text-anchor="middle">page, taglib, include</text>
    <text x="77" y="100" fill="#cbd5e1" font-size="10" text-anchor="middle">페이지 속성 설정</text>
  </g>
</svg>'''

    elif item_id == 16:
        # JSTL & EL 조건문 분기 Flowchart
        return '''<svg viewBox="0 0 680 150" style="width: 100%; max-width: 680px; height: auto; background: #0f172a; border-radius: 10px; margin: 12px 0; padding: 10px; box-sizing: border-box;">
  <defs>
    <marker id="arrJstl" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#38bdf8"/></marker>
  </defs>
  <rect x="15" y="50" width="115" height="50" rx="6" fill="#1e293b" stroke="#475569"/>
  <text x="72" y="70" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">userRole='MEMBER'</text>
  <text x="72" y="87" fill="#fcd34d" font-size="11" font-weight="bold" text-anchor="middle">point=150</text>

  <line x1="130" y1="75" x2="160" y2="75" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrJstl)"/>

  <!-- when 1 -->
  <rect x="160" y="20" width="130" height="35" rx="6" fill="#1e293b" stroke="#ef4444"/>
  <text x="225" y="42" fill="#f87171" font-size="10" text-anchor="middle">role eq 'ADMIN' ➔ ❌</text>

  <!-- when 2 -->
  <rect x="160" y="60" width="170" height="35" rx="6" fill="#1e293b" stroke="#ef4444"/>
  <text x="245" y="82" fill="#f87171" font-size="10" text-anchor="middle">MEMBER &amp; point ge 200 ➔ ❌</text>

  <!-- when 3 (MATCH) -->
  <rect x="160" y="100" width="230" height="40" rx="6" fill="#065f46" stroke="#10b981" stroke-width="2"/>
  <text x="275" y="125" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">MEMBER &amp; point lt 200 (150&lt;200) ➔ ✅ 참!</text>

  <line x1="390" y1="120" x2="450" y2="120" stroke="#10b981" stroke-width="2" marker-end="url(#arrJstl)"/>

  <!-- Result box -->
  <rect x="450" y="40" width="200" height="70" rx="8" fill="#1e1b4b" stroke="#38bdf8" stroke-width="2.5"/>
  <text x="550" y="65" fill="#f8fafc" font-size="12" text-anchor="middle">최종 화면 출력 결과</text>
  <text x="550" y="93" fill="#38bdf8" font-size="18" font-weight="bold" text-anchor="middle">③ 일반회원 ★</text>
</svg>'''

    elif item_id == 17:
        # session.invalidate() vs removeAttribute()
        return '''<svg viewBox="0 0 680 140" style="width: 100%; max-width: 680px; height: auto; background: #0f172a; border-radius: 10px; margin: 12px 0; padding: 10px; box-sizing: border-box;">
  <g transform="translate(20, 15)">
    <rect x="0" y="0" width="305" height="110" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <text x="152" y="28" fill="#f87171" font-size="13" font-weight="bold" text-anchor="middle">① session.invalidate() ★ (로그아웃용)</text>
    <rect x="25" y="45" width="255" height="40" rx="6" fill="#7f1d1d" fill-opacity="0.4" stroke="#ef4444" stroke-dasharray="4,4"/>
    <text x="152" y="65" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">💥 세션 객체 자체를 완전히 무효화/파괴</text>
    <text x="152" y="80" fill="#fee2e2" font-size="10" text-anchor="middle">loginUser 등 모든 세션 데이터 일괄 초기화</text>
    <text x="152" y="103" fill="#cbd5e1" font-size="10" text-anchor="middle">로그아웃 처리 시 표준 권장 메서드</text>
  </g>
  <g transform="translate(355, 15)">
    <rect x="0" y="0" width="305" height="110" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="152" y="28" fill="#fcd34d" font-size="13" font-weight="bold" text-anchor="middle">② session.removeAttribute("키이름")</text>
    <rect x="25" y="45" width="255" height="40" rx="6" fill="#334155"/>
    <text x="152" y="65" fill="#fde68a" font-size="11" text-anchor="middle">세션 객체는 그대로 유지</text>
    <text x="152" y="80" fill="#94a3b8" font-size="10" text-anchor="middle">지정한 1개의 속성(Attribute) 데이터만 핀셋 삭제</text>
    <text x="152" y="103" fill="#cbd5e1" font-size="10" text-anchor="middle">세션 자체는 소멸되지 않음</text>
  </g>
</svg>'''

    elif item_id == 18:
        # TRUNCATE vs DROP vs DELETE
        return '''<svg viewBox="0 0 680 145" style="width: 100%; max-width: 680px; height: auto; background: #0f172a; border-radius: 10px; margin: 12px 0; padding: 10px; box-sizing: border-box;">
  <g transform="translate(15, 10)">
    <rect x="0" y="0" width="200" height="125" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="100" y="25" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">TRUNCATE TABLE ★</text>
    <text x="100" y="45" fill="#fcd34d" font-size="11" font-weight="bold" text-anchor="middle">구조 유지 + 데이터만 초기화</text>
    <text x="100" y="68" fill="#cbd5e1" font-size="10" text-anchor="middle">명령어 분류: DDL</text>
    <text x="100" y="85" fill="#cbd5e1" font-size="10" text-anchor="middle">테이블 구조: 그대로 보존</text>
    <text x="100" y="102" fill="#ef4444" font-size="10" text-anchor="middle">Rollback: 불가 (초고속)</text>
    <text x="100" y="117" fill="#6ee7b7" font-size="9" text-anchor="middle">용도: 테이블 재사용 데이터 청소</text>
  </g>
  <g transform="translate(240, 10)">
    <rect x="0" y="0" width="200" height="125" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <text x="100" y="25" fill="#f87171" font-size="13" font-weight="bold" text-anchor="middle">DROP TABLE</text>
    <text x="100" y="45" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">구조 + 데이터 영구 완전 삭제</text>
    <text x="100" y="68" fill="#cbd5e1" font-size="10" text-anchor="middle">명령어 분류: DDL</text>
    <text x="100" y="85" fill="#fca5a5" font-size="10" text-anchor="middle">테이블 구조: 소멸 (삭제됨)</text>
    <text x="100" y="102" fill="#ef4444" font-size="10" text-anchor="middle">Rollback: 불가</text>
    <text x="100" y="117" fill="#cbd5e1" font-size="9" text-anchor="middle">용도: 테이블 자체 영구 폐기</text>
  </g>
  <g transform="translate(465, 10)">
    <rect x="0" y="0" width="200" height="125" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
    <text x="100" y="25" fill="#94a3b8" font-size="13" font-weight="bold" text-anchor="middle">DELETE FROM</text>
    <text x="100" y="45" fill="#cbd5e1" font-size="11" text-anchor="middle">행(Row) 단위 삭제</text>
    <text x="100" y="68" fill="#cbd5e1" font-size="10" text-anchor="middle">명령어 분류: DML</text>
    <text x="100" y="85" fill="#cbd5e1" font-size="10" text-anchor="middle">테이블 구조: 그대로 보존</text>
    <text x="100" y="102" fill="#34d399" font-size="10" font-weight="bold" text-anchor="middle">Rollback: 가능 (로그 기록)</text>
    <text x="100" y="117" fill="#cbd5e1" font-size="9" text-anchor="middle">용도: 특정 조건 행 선별 삭제</text>
  </g>
</svg>'''

    elif item_id == 19:
        # Clustered Index vs Secondary Index
        return '''<svg viewBox="0 0 680 155" style="width: 100%; max-width: 680px; height: auto; background: #0f172a; border-radius: 10px; margin: 12px 0; padding: 10px; box-sizing: border-box;">
  <!-- Clustered -->
  <g transform="translate(15, 10)">
    <rect x="0" y="0" width="310" height="135" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="155" y="24" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">클러스터드 인덱스 (Clustered)</text>
    <rect x="15" y="35" width="280" height="42" rx="4" fill="#0f172a"/>
    <text x="155" y="52" fill="#fcd34d" font-size="11" font-weight="bold" text-anchor="middle">리프 노드 = 실제 데이터 행 자체! ★</text>
    <text x="155" y="68" fill="#93c5fd" font-size="10" text-anchor="middle">데이터가 인덱스 키 순서로 물리적 정렬</text>
    <text x="155" y="93" fill="#cbd5e1" font-size="10" text-anchor="middle">▪ 테이블당 단 1개만 생성 가능 (보통 PK)</text>
    <text x="155" y="110" fill="#34d399" font-size="10" font-weight="bold" text-anchor="middle">▪ 범위 검색(Range Scan) 속도 극대화</text>
    <text x="155" y="125" fill="#f87171" font-size="9" text-anchor="middle">▪ 데이터 삽입/수정 시 페이지 분할 오버헤드</text>
  </g>
  <!-- Secondary -->
  <g transform="translate(350, 10)">
    <rect x="0" y="0" width="315" height="135" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <text x="157" y="24" fill="#c084fc" font-size="13" font-weight="bold" text-anchor="middle">세컨더리 인덱스 (Secondary / 보조)</text>
    <rect x="15" y="35" width="285" height="42" rx="4" fill="#0f172a"/>
    <text x="157" y="52" fill="#e9d5ff" font-size="11" font-weight="bold" text-anchor="middle">리프 노드 = PK(클러스터드 키) 포인터</text>
    <text x="157" y="68" fill="#cbd5e1" font-size="10" text-anchor="middle">인덱스 목차만 따로 관리 (물리 위치 무관)</text>
    <text x="157" y="93" fill="#cbd5e1" font-size="10" text-anchor="middle">▪ 테이블당 여러 개 생성 가능</text>
    <text x="157" y="110" fill="#fcd34d" font-size="10" text-anchor="middle">▪ 데이터 수정 시 오버헤드가 적음</text>
    <text x="157" y="125" fill="#94a3b8" font-size="9" text-anchor="middle">▪ 실제 데이터 찾을 때 2번 탐색(Double Lookup)</text>
  </g>
</svg>'''

    elif item_id == 20:
        # Scalar Subquery 4대 원칙
        return '''<svg viewBox="0 0 680 155" style="width: 100%; max-width: 680px; height: auto; background: #0f172a; border-radius: 10px; margin: 12px 0; padding: 10px; box-sizing: border-box;">
  <rect x="15" y="10" width="650" height="135" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="340" y="30" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">★ 스칼라 서브쿼리 (Scalar Subquery) 4대 원칙 (필수 암기)</text>
  
  <g transform="translate(30, 42)">
    <rect x="0" y="0" width="140" height="75" rx="6" fill="#0f172a" stroke="#38bdf8"/>
    <text x="70" y="25" fill="#67e8f9" font-size="11" font-weight="bold" text-anchor="middle">① 단 1개의 값 ★</text>
    <text x="70" y="45" fill="#ffffff" font-size="10" text-anchor="middle">정확히 1행 1열</text>
    <text x="70" y="60" fill="#cbd5e1" font-size="9" text-anchor="middle">(단일 값/Scalar) 반환</text>
  </g>
  <g transform="translate(185, 42)">
    <rect x="0" y="0" width="140" height="75" rx="6" fill="#0f172a" stroke="#f59e0b"/>
    <text x="70" y="25" fill="#fcd34d" font-size="11" font-weight="bold" text-anchor="middle">② 행마다 반복 실행</text>
    <text x="70" y="45" fill="#ffffff" font-size="10" text-anchor="middle">메인쿼리 건수만큼</text>
    <text x="70" y="60" fill="#fca5a5" font-size="9" text-anchor="middle">반복 실행 ➔ 성능 저하</text>
  </g>
  <g transform="translate(340, 42)">
    <rect x="0" y="0" width="145" height="75" rx="6" fill="#0f172a" stroke="#ef4444"/>
    <text x="72" y="25" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">③ 2건 이상 시 에러</text>
    <text x="72" y="45" fill="#ffffff" font-size="10" text-anchor="middle">2건 이상 결과 시</text>
    <text x="72" y="60" fill="#fca5a5" font-size="9" text-anchor="middle">런타임 오류 발생</text>
  </g>
  <g transform="translate(498, 42)">
    <rect x="0" y="0" width="145" height="75" rx="6" fill="#0f172a" stroke="#10b981"/>
    <text x="72" y="25" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">④ 불일치 시 NULL</text>
    <text x="72" y="45" fill="#ffffff" font-size="10" text-anchor="middle">조건 일치 행 없으면</text>
    <text x="72" y="60" fill="#a7f3d0" font-size="9" text-anchor="middle">오류 대신 NULL 반환</text>
  </g>
  <text x="340" y="133" fill="#cbd5e1" font-size="10" text-anchor="middle">주로 SELECT 절 컬럼 자리에 사용되며, 대량 데이터 조회 시 JOIN으로 대체하는 것이 성능에 유리함</text>
</svg>'''

    return ''

print('SVG generator module ready')

items_data = [
    {
        "id": 1,
        "type": "주관식 서술형 (배점 10.25점)",
        "badge": "★★★★★ 서술형 출제 1순위 (공지 적시)",
        "category": "SQL 기본 및 DML",
        "title": "WHERE 절 vs HAVING 절의 차이점 2대 관점 비교 서술",
        "question": "SQL에서 WHERE 절과 HAVING 절의 차이점을 다음 두 가지 관점에서 비교하여 서술하시오.\n① 조건 적용 시점(그룹화 전/후)\n② 집계 함수 사용 가능 여부",
        "answer": """<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1rem; margin: 0.8rem 0;">
  <strong style="color: #ef4444; font-size: 1.05rem;">&lt;WHERE 절&gt;</strong><br>
  ① <strong>조건 적용 시점</strong>: 데이터를 그룹화(GROUP BY)하기 <strong>전에 개별 행(Row)</strong>을 필터링한다.<br>
  ② <strong>집계 함수</strong>: 사용할 수 없다 (예: <code>WHERE SUM(price) &gt; 1000</code> 사용 불가).<br><br>
  <strong style="color: #10b981; font-size: 1.05rem;">&lt;HAVING 절&gt;</strong><br>
  ① <strong>조건 적용 시점</strong>: 데이터를 그룹화(GROUP BY)한 <strong>후 만들어진 그룹</strong>을 필터링한다.<br>
  ② <strong>집계 함수</strong>: 사용할 수 있다 (예: <code>HAVING COUNT(*) &gt;= 5</code>, <code>HAVING AVG(score) &gt;= 80</code> 등).
</div>""",
        "explanation": """<ul>
  <li><strong>SQL 쿼리 실제 실행 순서</strong>: <code>FROM ➔ ON ➔ JOIN ➔ WHERE ➔ GROUP BY ➔ HAVING ➔ SELECT ➔ DISTINCT ➔ ORDER BY ➔ LIMIT</code></li>
  <li><strong>왜 WHERE에서 집계함수가 불가능한가?</strong>: WHERE 절은 행 단위 데이터를 읽어오는 초기 단계이므로, 아직 그룹이 형성되지 않아 집계 연산(SUM, AVG 등) 자체가 계산되지 않은 상태이기 때문입니다.</li>
  <li><strong>시험장 암기 공식</strong>: <strong>「행 먼저 WHERE, 묶고 나서 HAVING, 집계는 HAVING만!」</strong></li>
</ul>"""
    },
    {
        "id": 2,
        "type": "주관식 서술형 (배점 10.25점)",
        "badge": "★★★★★ 서술형 출제 1순위 (공지 적시)",
        "category": "Servlet & JSP 아키텍처",
        "title": "forward vs sendRedirect 비교 서술",
        "question": "서블릿/JSP 화면 이동 메커니즘인 forward와 sendRedirect의 차이점을 다음 3가지 관점에서 비교하여 서술하시오.\n① 요청/응답 왕복 횟수\n② 브라우저 URL 변경 여부\n③ request 속성(Attribute) 공유 여부",
        "answer": """<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1rem; margin: 0.8rem 0;">
  <strong style="color: #0284c7; font-size: 1.05rem;">&lt;forward&gt;</strong><br>
  1. <strong>요청/응답 왕복 횟수</strong>: <strong>1회</strong> (클라이언트 모르게 서버 내부에서 제어권 이동)<br>
  2. <strong>브라우저 URL 변경 여부</strong>: <strong>X</strong> (처음 클라이언트가 요청한 URL 그대로 유지)<br>
  3. <strong>request 속성 공유 여부</strong>: <strong>O</strong> (<code>request.setAttribute()</code> 데이터가 목적지 JSP까지 그대로 유지)<br><br>
  <strong style="color: #d97706; font-size: 1.05rem;">&lt;sendRedirect&gt;</strong><br>
  1. <strong>요청/응답 왕복 횟수</strong>: <strong>2회</strong> (서버가 302 응답 ➔ 브라우저가 새 주소로 재요청)<br>
  2. <strong>브라우저 URL 변경 여부</strong>: <strong>O</strong> (이동한 최종 새 주소로 브라우저 주소창이 변경됨)<br>
  3. <strong>request 속성 공유 여부</strong>: <strong>X</strong> (완전히 새로운 HTTP 요청이 발생하므로 기존 request 속성은 초기화/소멸)
</div>""",
        "explanation": """<ul>
  <li><strong>조회(Read) vs 변경(CUD) 패턴</strong>: 목록 조회/상세 조회는 request에 데이터를 담아 JSP로 넘겨야 하므로 <code>forward</code>를 쓰고, 등록/수정/삭제 후에는 중복 요청(새로고침 버그)을 막기 위해 <code>sendRedirect</code>(PRG 패턴)를 사용합니다.</li>
  <li><strong>구현 문법</strong>:
    <pre><code>// forward:
request.getRequestDispatcher("/gear/list.jsp").forward(request, response);

// sendRedirect:
response.sendRedirect(request.getContextPath() + "/gear?action=list");</code></pre>
  </li>
</ul>"""
    },
    {
        "id": 3,
        "type": "핵심 개념 & 객관식/단답형",
        "badge": "★★★★★ 100% 빈출 (1NF~3NF)",
        "category": "데이터베이스 설계 및 인덱스",
        "title": "관계형 데이터베이스 정규화 (1NF, 2NF, 3NF)",
        "question": "관계형 데이터베이스의 제1정규화(1NF), 제2정규화(2NF), 제3정규화(3NF)의 핵심 정의와 제거하는 이상 현상을 서술하시오.",
        "answer": """<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1rem; margin: 0.8rem 0;">
  <p><strong>제1정규화 (1NF) ★ [중요]</strong>: 테이블의 모든 컬럼은 여러 값이 아닌 더 이상 쪼갤 수 없는 <strong>단일 값(원자값, Atomic Value)</strong>만을 갖는다.</p>
  <p><strong>제2정규화 (2NF)</strong>: 1NF를 만족하면서, 복합 기본키의 일부 컬럼에만 종속되는 것을 분리하여 <strong>부분 함수 종속성(Partial Functional Dependency)</strong>을 제거한다. (기본키 전체에 완전 함수 종속)</p>
  <p><strong>제3정규화 (3NF)</strong>: 2NF를 만족하면서, 기본키가 아닌 일반 컬럼들끼리 꼬리를 물고 종속되는 <strong>이행적 함수 종속성(Transitive Functional Dependency, A➔B, B➔C)</strong>을 제거한다.</p>
</div>""",
        "explanation": """<ul>
  <li><strong>원자값 위반 예시</strong>: 한 학생의 [수강과목] 컬럼에 'Java, DB, Spring'처럼 쉼표로 여러 값을 넣으면 1NF 위반! ➔ 행을 분리하여 원자값으로 만들어야 합니다.</li>
  <li><strong>암기 키워드</strong>: <strong>「1원(원자값) ➔ 2부(부분종속제거) ➔ 3이(이행종속제거) ➔ 보결(BCNF 결정자 후보키)」</strong></li>
</ul>"""
    },
    {
        "id": 4,
        "type": "핵심 개념 & 객관식/단답형",
        "badge": "★★★★★ 시험 공지 핵심 키워드",
        "category": "데이터베이스 설계 및 인덱스",
        "title": "Full Table Scan (FTS, 전체 테이블 스캔)",
        "question": "Full Table Scan (전체 테이블 스캔)의 정확한 정의와 발생하는 주된 원인을 설명하시오.",
        "answer": """<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1rem; margin: 0.8rem 0;">
  <strong>정의 ★ [초특급 중요]</strong><br>
  데이터베이스에서 <strong>인덱스(Index)를 거치지 않고 테이블의 처음부터 끝까지 모든 행(Row)과 데이터 블록을 샅샅이 순차적으로 읽어</strong> 원하는 데이터를 찾는 방식.
</div>""",
        "explanation": """<ul>
  <li><strong>FTS가 발생하는 대표적인 경우</strong>:
    <ol>
      <li>WHERE 절 조건에 인덱스가 걸려있지 않은 컬럼을 사용했을 때</li>
      <li>인덱스 컬럼을 가공/변형했을 때 (예: <code>WHERE SUBSTR(code, 1, 3) = 'CAR'</code> 또는 <code>WHERE price * 1.1 &gt; 1000</code>)</li>
      <li>부정형 조건이나 앞쪽 와일드카드 사용 시 (예: <code>WHERE code != 'A'</code>, <code>WHERE name LIKE '%테스트'</code>)</li>
      <li>옵티마이저 판단 상 조회할 데이터가 전체의 20~25% 이상이라 인덱스를 타는 것보다 한 번에 다 읽는 게 더 빠르다고 판단했을 때</li>
    </ol>
  </li>
</ul>"""
    },
    {
        "id": 5,
        "type": "고급 SQL & 실전 쿼리 예측",
        "badge": "★★★★★ 100% 빈출 (부분 롤백)",
        "category": "트랜잭션 및 고급 SQL",
        "title": "트랜잭션 SAVEPOINT (저장점) 및 부분 롤백",
        "question": "트랜잭션에서 SAVEPOINT의 기능과 ROLLBACK TO 문법의 동작 원리를 설명하시오.",
        "answer": """<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1rem; margin: 0.8rem 0;">
  <strong>정의 ★ [중요]</strong><br>
  데이터베이스 트랜잭션 작업 중 <strong>특정 지점을 기록(저장)해두어</strong>, 문제가 발생했을 때 전체 작업 취소(Rollback)가 아닌 <strong>해당 지점까지만 '부분 취소'</strong>를 할 수 있게 해주는 기능이다.<br><br>
  <strong>동작 예시</strong>:<br>
  1번 데이터 수정 성공 ➔ <code>SAVEPOINT SP1;</code> (중간 저장)<br>
  2번 데이터 수정 시도 중 오류 발생! ➔ <code>ROLLBACK TO SP1;</code> 실행<br>
  👉 <strong>결과: 1번 데이터 수정은 정상 유지되고, 오류가 난 2번 작업만 깔끔하게 취소됨!</strong>
</div>""",
        "explanation": """<ul>
  <li><strong>주의 문법</strong>: <code>ROLLBACK;</code>만 쓰면 트랜잭션 전체가 취소되지만, <code>ROLLBACK TO 세이브포인트명;</code>을 쓰면 해당 저장점 이후의 작업만 부분 취소됩니다.</li>
  <li><strong>시험 함정</strong>: <code>ROLLBACK TO SP1</code> 실행 후에도 트랜잭션은 종료된 것이 아니므로, 최종 반영을 위해서는 반드시 <code>COMMIT;</code>을 호출해야 합니다.</li>
</ul>"""
    },
    {
        "id": 6,
        "type": "핵심 개념 & 객관식",
        "badge": "★★★★★ 단골 출제 (문자열 결합)",
        "category": "SQL 기본 및 함수",
        "title": "SQL 단일행 내장함수 4대장 (CONCAT, SUBSTR, LENGTH, ROUND)",
        "question": "SQL 주요 단일행 내장함수 중 두 개 이상의 문자열을 합치는 함수와 대표 함수 4종의 역할을 서술하시오.",
        "answer": """<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1rem; margin: 0.8rem 0;">
  1. <strong>CONCAT ★ [가장 중요]</strong>: 두 개 이상의 문자열을 하나로 길게 합쳐서(연결해서) 반환 (예: <code>CONCAT('SSAFY', '-', '11기') ➔ 'SSAFY-11기'</code>)<br>
  2. <strong>SUBSTR (또는 SUBSTRING)</strong>: 문자열에서 원하는 부분만 잘라내어 반환 (예: <code>SUBSTR('HELLO', 1, 3) ➔ 'HEL'</code>)<br>
  3. <strong>LENGTH (또는 LEN)</strong>: 문자열의 총 길이나 글자 수를 반환 (예: <code>LENGTH('KOREA') ➔ 5</code>)<br>
  4. <strong>ROUND</strong>: 지정한 소수점 자리에서 숫자를 반올림 (예: <code>ROUND(12.345, 1) ➔ 12.3</code>)
</div>""",
        "explanation": """<ul>
  <li><strong>MySQL 주의사항</strong>: Java나 Oracle에서는 <code>+</code>나 <code>||</code>로 문자열을 결합할 수 있지만, MySQL에서는 문자열에 <code>+</code>를 쓰면 숫자로 형변환하려 하므로 <strong>반드시 <code>CONCAT()</code> 함수</strong>를 써야 합니다.</li>
</ul>"""
    },
    {
        "id": 7,
        "type": "핵심 개념 & 단답형",
        "badge": "★★★★★ 100% 빈출 (세션 식별 쿠키)",
        "category": "JSP 및 상태 관리",
        "title": "JSESSIONID 쿠키와 세션 유지 메커니즘",
        "question": "웹 브라우저와 톰캣 WAS 서버 간에 동일 사용자를 식별하기 위해 사용하는 표준 쿠키인 JSESSIONID의 개념과 동작 원리를 서술하시오.",
        "answer": """<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1rem; margin: 0.8rem 0;">
  <strong>JSESSIONID ★ [초특급 중요]</strong><br>
  HTTP 통신은 기본적으로 이전 상태를 기억하지 못하는 무상태(Stateless) 프로토콜이다.<br>
  서버는 최초 접속한 클라이언트에게 <strong>고유한 세션 ID(JSESSIONID) 값을 부여하여 브라우저 쿠키(Set-Cookie)에 저장</strong>시키고, 이후 브라우저가 매 요청마다 이 쿠키를 전송하면 서버는 이 값을 확인해 동일한 사용자임을 식별한다.<br>
  즉, <strong>클라이언트 브라우저와 서버 세션을 상호 식별하기 위해 웹 컨테이너가 자동으로 발행하여 브라우저에 저장하는 표준 세션 쿠키</strong>이다.
</div>""",
        "explanation": """<ul>
  <li><strong>쿠키 삭제 시</strong>: 사용자가 브라우저를 닫거나 세션 쿠키를 지우면 JSESSIONID가 사라져 서버에 세션 데이터가 남아있더라도 동일인으로 인정받지 못하고 새 세션이 발급됩니다.</li>
  <li><strong>브라우저 단위</strong>: 동일한 브라우저의 새 탭들은 JSESSIONID를 공유하므로 로그인 상태가 유지됩니다.</li>
</ul>"""
    },
    {
        "id": 8,
        "type": "아키텍처 패턴 & 단답형",
        "badge": "★★★★★ MVC 핵심 아키텍처",
        "category": "Servlet 기본 및 아키텍처",
        "title": "프론트 컨트롤러 (Front Controller) 패턴",
        "question": "MVC 모델 2 웹 애플리케이션에서 클라이언트의 모든 요청을 한곳에서 일괄 접수하는 프론트 컨트롤러 패턴의 개념을 정의하시오.",
        "answer": """<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1rem; margin: 0.8rem 0;">
  <strong>프론트 컨트롤러(Front Controller) ★ [초특급 중요]</strong><br>
  웹 애플리케이션으로 들어오는 클라이언트의 모든 요청을 <strong>단일 진입점(Single Entry Point)</strong>에서 일괄적으로 받아 인증, 권한, 인코딩, 로깅 등의 <strong>공통 선행 작업을 수행한 뒤</strong>, 요청 URL이나 파라미터(action)에 맞는 <strong>세부 컨트롤러나 서비스로 위임(Dispatch)</strong>하는 웹 아키텍처 디자인 패턴이다.
</div>""",
        "explanation": """<ul>
  <li><strong>실습 코드 매핑</strong>: 우리 실습의 <code>GearController.java</code>가 <code>/gear</code>로 들어오는 모든 요청을 단일 진입점에서 받아 한글 인코딩 처리 후 <code>action</code>에 따라 <code>list</code>, <code>regist</code>, <code>detail</code> 등으로 분기하는 것이 바로 Front Controller의 전형입니다.</li>
  <li><strong>장점</strong>: 중복 코드 제거, 공통 보안 및 예외 처리의 중앙 집중화.</li>
</ul>"""
    },
    {
        "id": 9,
        "type": "핵심 개념 & 단답형",
        "badge": "★★★★★ 서블릿 생명주기 핵심",
        "category": "Servlet 기본 및 아키텍처",
        "title": "서블릿 service() 메서드의 역할과 분기 원리",
        "question": "서블릿 컨테이너가 클라이언트 요청을 수신했을 때 실행되는 service() 메서드의 구체적인 역할을 설명하시오.",
        "answer": """<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1rem; margin: 0.8rem 0;">
  <strong>service() 메서드</strong><br>
  클라이언트의 HTTP 요청이 들어왔을 때 서블릿 컨테이너에 의해 <strong>가장 먼저 호출되는 메서드</strong>이다.<br>
  요청의 HTTP Method를 분석하여 <strong>GET 요청이면 doGet()을, POST 요청이면 doPost()를 자동으로 호출</strong>하여 적절한 메서드가 실행되도록 길을 안내(라우팅)해 주는 역할을 한다.
</div>""",
        "explanation": """<ul>
  <li><strong>서블릿 생명주기 순서</strong>: <code>생성자 호출 ➔ init() (최초 1회만) ➔ service() (요청마다 매번) ➔ doGet()/doPost() ➔ destroy() (서버 종료 시 1회)</code></li>
  <li><strong>주의</strong>: 개발자가 <code>service()</code>를 오버라이딩하여 직접 구현할 수도 있지만, 보통은 <code>doGet()</code>과 <code>doPost()</code>를 구현하여 사용합니다.</li>
</ul>"""
    },
    {
        "id": 10,
        "type": "설정 문법 & 단답형",
        "badge": "★★★★★ 태그명 정확히 기억",
        "category": "Servlet 기본 및 아키텍처",
        "title": "web.xml 에러 페이지 매핑 3대 태그",
        "question": "web.xml에서 HTTP 오류 코드나 예외 클래스별로 사용자 정의 에러 페이지를 매핑할 때 사용하는 최상위 태그와 하위 태그들을 쓰시오.",
        "answer": """<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1rem; margin: 0.8rem 0;">
  최상위 태그는 <strong>&lt;error-page&gt;</strong> 이다.<br>
  하위 태그로 오류 번호를 지정하는 <strong>&lt;error-code&gt;</strong> (예: 404, 500) 또는 예외 클래스를 지정하는 <strong>&lt;exception-type&gt;</strong> 과, 이동할 화면 경로인 <strong>&lt;location&gt;</strong> 을 포함한다.<br><br>
  <strong style="color: #ef4444;">★ 암기: &lt;error-page&gt; / &lt;error-code&gt; / &lt;location&gt;</strong>
</div>""",
        "explanation": """<pre><code>&lt;!-- web.xml 실제 작성 예시 --&gt;
&lt;error-page&gt;
    &lt;error-code&gt;404&lt;/error-code&gt;
    &lt;location&gt;/error/404.jsp&lt;/location&gt;
&lt;/error-page&gt;
&lt;error-page&gt;
    &lt;error-code&gt;500&lt;/error-code&gt;
    &lt;location&gt;/error/500.jsp&lt;/location&gt;
&lt;/error-page&gt;</code></pre>"""
    },
    {
        "id": 11,
        "type": "핵심 개념 & 단답형",
        "badge": "★★★★★ 무결성 1초 컷 공식",
        "category": "SQL 기본 및 제약조건",
        "title": "기본키(Primary Key)의 2대 제약조건 공식",
        "question": "관계형 데이터베이스에서 기본키(Primary Key)가 만족해야 하는 2가지 필수 제약조건을 수식 형태로 쓰시오.",
        "answer": """<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1rem; margin: 0.8rem 0;">
  <strong style="font-size: 1.2rem; color: #0284c7;">기본키(Primary Key) = NOT NULL + UNIQUE</strong><br><br>
  1. <strong>NOT NULL</strong>: 절대 빈 값(Null)을 허용하지 않는다.<br>
  2. <strong>UNIQUE</strong>: 테이블 내에서 중복된 값을 절대 허용하지 않는다.<br>
  👉 이를 통해 테이블의 모든 행(튜플)을 유일하게 식별하는 <strong>개체 무결성(Entity Integrity)</strong>을 보장한다.
</div>""",
        "explanation": """<ul>
  <li><strong>UNIQUE 제약조건과의 차이</strong>: UNIQUE 제약조건은 중복을 허용하지 않지만 NULL 값은 여러 개 저장할 수 있습니다. 반면 기본키는 NULL조차 절대 허용하지 않습니다!</li>
</ul>"""
    },
    {
        "id": 12,
        "type": "핵심 개념 & 객관식/단답형",
        "badge": "★★★★★ 차집합 EXCEPT 적중",
        "category": "트랜잭션 및 고급 SQL",
        "title": "SQL 표준 집합 연산자 4종 (EXCEPT, UNION, INTERSECT, CROSS JOIN)",
        "question": "첫 번째 SELECT 쿼리의 결과 집합에서 두 번째 SELECT 쿼리의 결과 집합을 뺀 차집합을 구하는 표준 연산자와 4대 집합 연산자를 구분하시오.",
        "answer": """<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1rem; margin: 0.8rem 0;">
  ① <strong>EXCEPT ★ [가장 중요]</strong>: 첫 번째 SELECT 쿼리의 결과 집합에서 두 번째 SELECT 쿼리의 결과 집합을 뺀 나머지 행(<strong>차집합</strong>)만을 추출할 때 사용하는 표준 집합 연산자 (※ Oracle에서는 <code>MINUS</code>)<br>
  ② <strong>UNION</strong>: 두 쿼리의 결과를 하나로 합치는 연산자 (<strong>합집합</strong>, 중복 행 자동 제거)<br>
  ③ <strong>INTERSECT</strong>: 두 쿼리 결과에 모두 존재하는 공통된 행만 추출하는 연산자 (<strong>교집합</strong>)<br>
  ④ <strong>CROSS JOIN</strong>: 두 테이블 간의 모든 가능한 데이터 조합을 반환하는 조인 방식 (<strong>카티션 곱</strong>, 행수 = M × N)
</div>""",
        "explanation": """<ul>
  <li><strong>UNION vs UNION ALL</strong>: UNION은 정렬 과정을 거쳐 중복을 제거하지만, UNION ALL은 중복 제거 없이 빠르게 전부 결합합니다.</li>
</ul>"""
    },
    {
        "id": 13,
        "type": "실전 계산형 객관식",
        "badge": "★★★★★ 100% 실전 기출",
        "category": "SQL 기본 및 DML",
        "title": "MySQL LIMIT 페이징 쿼리 Offset 계산 문제",
        "question": "한 페이지당 15개씩 상품을 보여주는 쇼핑몰 웹사이트에서, 4번째 페이지(currentPage = 4)에 해당하는 데이터를 조회하기 위한 MySQL LIMIT 절의 작성법으로 옳은 것을 고르시오.\n\nSELECT * FROM products \nORDER BY product_id DESC \n/* LIMIT 절 작성 */\n\n① LIMIT 15, 45\n② LIMIT 60, 15\n③ LIMIT 45, 15\n④ LIMIT 4, 15",
        "answer": """<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1rem; margin: 0.8rem 0;">
  <strong style="color: #10b981; font-size: 1.2rem;">정답: ③ LIMIT 45, 15</strong>
</div>""",
        "explanation": """<div style="line-height: 1.8;">
  <strong>[퍼펙트 해설]</strong><br>
  MySQL의 LIMIT 절 문법은 <code>LIMIT 시작위치(Offset), 가져올개수(Count)</code> 형식입니다. (※ Offset은 0부터 시작)<br>
  <ul>
    <li><strong>시작 위치(Offset) 구하는 공식</strong>: <code>(현재 페이지 번호 - 1) * 페이지당 개수</code></li>
    <li><strong>대입 계산</strong>: <code>(4 - 1) * 15 = 45</code> 이므로 45번 인덱스부터 시작합니다.</li>
    <li><strong>가져올 개수</strong>: <code>15</code>개</li>
  </ul>
  따라서 45번째부터 15개를 가져오는 <strong>LIMIT 45, 15</strong>가 정답입니다.<br>
  <span style="color: #ef4444; font-weight: bold;">⚠️ 함정 주의</span>: ①번 <code>LIMIT 15, 45</code>는 15번부터 45개를 가져오므로 정반대이며, ②번 <code>LIMIT 60, 15</code>는 5번째 페이지입니다!
</div>"""
    },
    {
        "id": 14,
        "type": "핵심 개념 & 순서 나열형",
        "badge": "★★★★★ 100% 빈출 순서",
        "category": "JSP 및 상태 관리",
        "title": "JSP/Servlet 4대 Scope 유효범위 순서 나열",
        "question": "JSP 및 서블릿에서 데이터를 저장하고 공유하기 위해 사용하는 4가지 영역(Scope)을 유효 범위가 가장 좁고 생명주기가 짧은 것부터 가장 넓고 긴 것 순서대로 나열하시오.",
        "answer": """<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1rem; margin: 0.8rem 0;">
  <strong style="font-size: 1.2rem; color: #0284c7;">page ➔ request ➔ session ➔ application</strong>
</div>""",
        "explanation": """<ul>
  <li><strong>1. page (pageContext)</strong>: 현재 실행 중인 단 1개의 JSP 페이지 내부에서만 유효</li>
  <li><strong>2. request</strong>: 한 번의 HTTP 요청부터 응답이 끝날 때까지 유효 (forward 시 유지됨)</li>
  <li><strong>3. session</strong>: 동일한 웹 브라우저(사용자)가 켜져있는 동안 지속 유지</li>
  <li><strong>4. application</strong>: 웹 애플리케이션(WAS 서버)이 구동되고 종료될 때까지 모든 사용자가 공유</li>
  <li><strong>EL 탐색 우선순위도 동일</strong>: <code>${user}</code>를 호출하면 <code>pageScope ➔ requestScope ➔ sessionScope ➔ applicationScope</code> 순으로 찾습니다!</li>
</ul>"""
    },
    {
        "id": 15,
        "type": "변환 구조 & 객관식/단답형",
        "badge": "★★★★★ 표현식 변환 단골",
        "category": "JSP 및 상태 관리",
        "title": "JSP 스크립트 요소 4종의 서블릿 변환 구조",
        "question": "JSP가 서블릿(.java)으로 변환될 때 각 스크립트 태그가 변환되는 위치와 역할 4가지를 설명하시오.",
        "answer": """<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1rem; margin: 0.8rem 0;">
  1. <strong>지시자 (&lt;%@ page ... %&gt;)</strong>: JSP 컨테이너에게 페이지의 인코딩, import 라이브러리 등 전반적인 환경 속성을 설정하도록 지시<br>
  2. <strong>표현식 (&lt;%= ... %&gt;) ★ [중요]</strong>: <code>_jspService()</code> 메서드 내에서 <code>out.print(...)</code> 형태로 변환되어 브라우저 화면에 바로 출력<br>
  3. <strong>스크립틀릿 (&lt;% ... %&gt;)</strong>: <code>_jspService()</code> 메서드 내부의 <strong>지역 변수 및 실행 로직</strong>으로 변환<br>
  4. <strong>선언문 (&lt;%! ... %&gt;)</strong>: 변환된 서블릿 클래스의 <strong>멤버 변수(필드)나 멤버 메서드</strong> 선언 위치로 변환
</div>""",
        "explanation": """<ul>
  <li><strong>멀티스레드 동시성 버그 주의</strong>: 선언문(<code>&lt;%! %&gt;</code>)에 변수를 선언하면 서블릿 인스턴스의 멤버 변수가 되므로, 모든 접속자가 이 변수를 공유하여 심각한 레이스 컨디션(동시성 오류)이 발생합니다. 반면 스크립틀릿(<code>&lt;% %&gt;</code>) 변수는 요청 스레드별 스택에 생성되는 지역 변수이므로 스레드에 안전합니다.</li>
</ul>"""
    },
    {
        "id": 16,
        "type": "코드 실행 결과 예측형 객관식",
        "badge": "★★★★★ 실전 기출 코드 해석",
        "category": "JSP 및 상태 관리",
        "title": "JSTL & EL 조건문(&lt;c:choose&gt;) 실행 결과 예측",
        "question": "다음 JSTL 및 EL 코드의 실행 결과로 화면에 출력되는 문자열을 고르시오.\n\n&lt;c:set var=\"userRole\" value=\"MEMBER\" /&gt;\n&lt;c:set var=\"point\" value=\"150\" /&gt;\n\n&lt;c:choose&gt;\n    &lt;c:when test=\"${userRole eq 'ADMIN'}\"&gt;\n        관리자\n    &lt;/c:when&gt;\n    &lt;c:when test=\"${userRole eq 'MEMBER' and point ge 200}\"&gt;\n        VIP회원\n    &lt;/c:when&gt;\n    &lt;c:when test=\"${userRole eq 'MEMBER' and point lt 200}\"&gt;\n        일반회원\n    &lt;/c:when&gt;\n    &lt;c:otherwise&gt;\n        비회원\n    &lt;/c:otherwise&gt;\n&lt;/c:choose&gt;\n\n① 관리자\n② VIP회원\n③ 일반회원\n④ 비회원",
        "answer": """<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1rem; margin: 0.8rem 0;">
  <strong style="color: #10b981; font-size: 1.2rem;">정답: ③ 일반회원</strong>
</div>""",
        "explanation": """<div style="line-height: 1.8;">
  <strong>[단계별 조건 판별 과정]</strong><br>
  1. 변수 값: <code>userRole = 'MEMBER'</code>, <code>point = 150</code><br>
  2. 첫 번째 <code>&lt;c:when&gt;</code>: <code>userRole eq 'ADMIN'</code> ➔ 'MEMBER' == 'ADMIN' 이므로 <strong>거짓(False)</strong><br>
  3. 두 번째 <code>&lt;c:when&gt;</code>: <code>userRole eq 'MEMBER' and point ge 200</code><br>
     - <code>userRole eq 'MEMBER'</code> ➔ 참(True)<br>
     - <code>point ge 200</code> (150 &gt;= 200) ➔ <strong>거짓(False)</strong><br>
     - True AND False ➔ <strong>거짓(False)</strong><br>
  4. 세 번째 <code>&lt;c:when&gt;</code>: <code>userRole eq 'MEMBER' and point lt 200</code><br>
     - <code>userRole eq 'MEMBER'</code> ➔ 참(True)<br>
     - <code>point lt 200</code> (150 &lt; 200) ➔ <strong>참(True)</strong><br>
     - True AND True ➔ <strong>참(True)!</strong><br>
  따라서 세 번째 블록의 <strong>일반회원</strong>이 화면에 최종 출력됩니다.
</div>"""
    },
    {
        "id": 17,
        "type": "실무 코드 & 단답형",
        "badge": "★★★★★ 로그아웃 구현 표준",
        "category": "JSP 및 상태 관리",
        "title": "로그아웃 서블릿 세션 처리: invalidate() vs removeAttribute()",
        "question": "서블릿에서 로그아웃을 처리할 때 사용하는 session.invalidate()와 session.removeAttribute()의 결정적 차이점을 서술하시오.",
        "answer": """<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1rem; margin: 0.8rem 0;">
  ① <strong>session.invalidate() ★ [로그아웃 시 필수 사용]</strong><br>
  현재 사용자의 <strong>세션 객체 자체를 완전히 파괴/무효화</strong>하여, 로그인 상태(<code>loginUser</code>)를 비롯한 해당 세션에 담긴 <strong>모든 데이터를 한 번에 초기화</strong>한다.<br><br>
  ② <strong>session.removeAttribute(\"키이름\")</strong><br>
  세션 객체는 그대로 유지한 채, 세션 안에 저장된 <strong>특정 속성(데이터) 1개만 골라서 삭제</strong>한다.
</div>""",
        "explanation": """<ul>
  <li><strong>실무/실기 시험 팁</strong>: 로그아웃 컨트롤러(<code>action=logout</code>)에서는 <code>session.removeAttribute("loginUser")</code>보다 세션 고유 ID까지 완전히 파기하고 새로 발급받을 수 있도록 <strong><code>session.invalidate();</code></strong>를 호출하는 것이 보안상 표준입니다.</li>
</ul>"""
    },
    {
        "id": 18,
        "type": "핵심 개념 & 2자 비교 서술형",
        "badge": "★★★★★ DDL vs DML 3자 비교",
        "category": "SQL 기본 및 DDL",
        "title": "TRUNCATE TABLE과 DROP TABLE의 차이점",
        "question": "테이블 데이터를 삭제하는 TRUNCATE TABLE과 DROP TABLE의 동작 차이점을 명확히 비교 서술하시오.",
        "answer": """<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1rem; margin: 0.8rem 0;">
  ① <strong>TRUNCATE TABLE ★ [중요]</strong>: <strong>테이블 구조(컬럼, 스키마, 인덱스)는 남겨둔 채</strong> 테이블 안의 모든 데이터만 일괄 고속 초기화한다. (테이블 재사용 목적)<br><br>
  ② <strong>DROP TABLE</strong>: 테이블 자체가 더 이상 필요 없을 때 <strong>테이블의 구조와 데이터를 모두 영구적으로 완전히 삭제</strong>한다. (테이블 소멸)
</div>""",
        "explanation": """<ul>
  <li><strong>DELETE와의 3자 비교 총정리</strong>:
    <table style="width: 100%; border-collapse: collapse; margin-top: 0.5rem; font-size: 0.9rem;">
      <tr style="background: #e2e8f0; font-weight: bold;">
        <th style="padding: 6px; border: 1px solid #cbd5e1;">구분</th>
        <th style="padding: 6px; border: 1px solid #cbd5e1;">DELETE</th>
        <th style="padding: 6px; border: 1px solid #cbd5e1;">TRUNCATE</th>
        <th style="padding: 6px; border: 1px solid #cbd5e1;">DROP</th>
      </tr>
      <tr>
        <td style="padding: 6px; border: 1px solid #cbd5e1; font-weight: bold;">분류</td>
        <td style="padding: 6px; border: 1px solid #cbd5e1;">DML</td>
        <td style="padding: 6px; border: 1px solid #cbd5e1; color: #ef4444; font-weight: bold;">DDL</td>
        <td style="padding: 6px; border: 1px solid #cbd5e1; color: #ef4444; font-weight: bold;">DDL</td>
      </tr>
      <tr>
        <td style="padding: 6px; border: 1px solid #cbd5e1; font-weight: bold;">테이블 구조</td>
        <td style="padding: 6px; border: 1px solid #cbd5e1;">유지</td>
        <td style="padding: 6px; border: 1px solid #cbd5e1; color: #0284c7; font-weight: bold;">유지</td>
        <td style="padding: 6px; border: 1px solid #cbd5e1; color: #ef4444; font-weight: bold;">완전 삭제</td>
      </tr>
      <tr>
        <td style="padding: 6px; border: 1px solid #cbd5e1; font-weight: bold;">Rollback</td>
        <td style="padding: 6px; border: 1px solid #cbd5e1; color: #10b981; font-weight: bold;">가능</td>
        <td style="padding: 6px; border: 1px solid #cbd5e1; color: #ef4444; font-weight: bold;">불가 (Auto Commit)</td>
        <td style="padding: 6px; border: 1px solid #cbd5e1; color: #ef4444; font-weight: bold;">불가 (Auto Commit)</td>
      </tr>
    </table>
  </li>
</ul>"""
    },
    {
        "id": 19,
        "type": "핵심 개념 & 객관식/서술형",
        "badge": "★★★★★ 인덱스 물리 구조 핵심",
        "category": "데이터베이스 설계 및 인덱스",
        "title": "클러스터드 인덱스 vs 세컨더리 인덱스 구조 비교",
        "question": "클러스터드 인덱스(Clustered Index)와 세컨더리 인덱스(Secondary Index)의 물리적 구조 및 성능 특징을 비교하시오.",
        "answer": """<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1rem; margin: 0.8rem 0;">
  ① <strong>클러스터드 인덱스 (Clustered Index)</strong>:<br>
  인덱스의 기준값 순서와 <strong>실제 데이터 행이 동일한 순서로 물리적 정렬</strong>되어 저장된다. (리프 노드 = 실제 데이터 페이지).<br>
  따라서 범위 검색(Range Scan) 속도가 매우 빠르지만, <strong>테이블당 오직 단 1개만 생성</strong>할 수 있고 데이터 삽입/수정 시 물리적 재배치 오버헤드가 크다.<br><br>
  ② <strong>세컨더리 인덱스 (Secondary Index, 보조 인덱스)</strong>:<br>
  실제 데이터의 물리적 위치와 무관하게 <strong>인덱스 목차만 따로 관리</strong>하며(리프 노드 = PK 값 또는 포인터), <strong>테이블당 여러 개 생성이 가능</strong>하고 데이터 수정 시 오버헤드가 적다.<br>
  단, 실제 행 데이터를 찾기 위해 포인터를 통해 한 번 더 클러스터드 인덱스로 이동(Double Lookup)해야 하므로 검색 속도가 상대적으로 느리다.
</div>""",
        "explanation": """<ul>
  <li><strong>비유</strong>: 클러스터드 인덱스는 사전처럼 본문 자체가 단어 순서대로 정렬된 책이고, 세컨더리 인덱스는 책 맨 뒤의 찾아보기(색인) 목록과 같습니다!</li>
</ul>"""
    },
    {
        "id": 20,
        "type": "심화 SQL & 객관식 단골 보기",
        "badge": "★★★★★ 4개 보기 전부 암기",
        "category": "트랜잭션 및 고급 SQL",
        "title": "스칼라 서브쿼리 (Scalar Subquery) 4대 원칙",
        "question": "SELECT 절에 주로 사용되는 스칼라 서브쿼리(Scalar Subquery)의 4대 핵심 특징을 서술하시오. (시험 보기 전수 출제)",
        "answer": """<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1rem; margin: 0.8rem 0;">
  <strong style="color: #ef4444;">★ 스칼라 서브쿼리 4대 원칙 (모두 외울 것!)</strong><br>
  1. <strong>단 하나의 행(Row)과 단 하나의 열(Column), 즉 정확히 1개의 단일 값(Scalar)만 반환</strong>한다.<br>
  2. <strong>메인 쿼리의 결과 건수(행 수)만큼 반복 실행</strong>되므로, 대량의 데이터 조회 시 조인(Join)이나 인라인 뷰보다 처리 성능이 저하될 수 있다.<br>
  3. 서브쿼리의 결과가 <strong>2건 이상 반환되면 런타임 오류가 발생</strong>한다.<br>
  4. 조건에 일치하는 행이 서브쿼리에 전혀 없는 경우 오류가 아니라 <strong>NULL이 반환</strong>된다.
</div>""",
        "explanation": """<pre><code>-- 스칼라 서브쿼리 실제 예시:
SELECT emp_id, name,
       (SELECT dept_name FROM department d WHERE d.dept_id = e.dept_id) AS dept_name
FROM employee e;
-- 메인쿼리의 직원 수(1,000명)만큼 부서명 조회 서브쿼리가 1,000번 반복 실행됨!</code></pre>"""
    }
]

print(f"Loaded {len(items_data)} items.")

def generate_tab_html():
    cards_html = []
    for item in items_data:
        svg_code = get_svg_diagram(item["id"])
        
        # Category class for filtering
        cat_class = "cat-sql"
        if "Servlet" in item["category"] or "JSP" in item["category"]:
            cat_class = "cat-web"
        elif "서술형" in item["type"]:
            cat_class = "cat-essay"

        card = f'''
      <!-- Item {item["id"]} -->
      <div class="card special-card {cat_class}" style="border: 2px solid #e2e8f0; border-radius: 14px; margin-bottom: 2rem; background: white; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); overflow: hidden;">
        <div style="background: linear-gradient(135deg, #1e293b, #0f172a); color: white; padding: 1.1rem 1.4rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.6rem;">
          <div style="display: flex; align-items: center; gap: 0.6rem;">
            <span style="background: #38bdf8; color: #0f172a; font-weight: 900; font-size: 0.95rem; padding: 0.25rem 0.65rem; border-radius: 6px;">Q{item["id"]:02d}</span>
            <span style="font-weight: 800; font-size: 1.1rem; color: #f8fafc;">{item["title"]}</span>
          </div>
          <div style="display: flex; gap: 0.4rem; align-items: center;">
            <span style="background: rgba(239, 68, 68, 0.2); border: 1px solid #ef4444; color: #fca5a5; font-size: 0.8rem; font-weight: 800; padding: 0.2rem 0.6rem; border-radius: 12px;">{item["badge"]}</span>
            <span style="background: rgba(255, 255, 255, 0.1); color: #cbd5e1; font-size: 0.8rem; padding: 0.2rem 0.6rem; border-radius: 12px;">{item["category"]}</span>
          </div>
        </div>

        <div style="padding: 1.5rem;">
          <div style="margin-bottom: 1.2rem;">
            <span style="display: inline-block; background: #e0f2fe; color: #0369a1; font-size: 0.82rem; font-weight: 800; padding: 0.2rem 0.5rem; border-radius: 4px; margin-bottom: 0.5rem;">[출제 유형: {item["type"]}]</span>
            <div style="font-size: 1.05rem; font-weight: 700; color: #1e293b; line-height: 1.7; white-space: pre-line;">{item["question"]}</div>
          </div>

          <!-- SVG Visual Diagram -->
          <div style="background: #0b1120; border-radius: 10px; padding: 0.8rem; text-align: center; margin: 1.2rem 0; box-shadow: inset 0 2px 4px rgba(0,0,0,0.5);">
            <div style="font-size: 0.82rem; color: #94a3b8; font-weight: bold; margin-bottom: 0.4rem; display: flex; align-items: center; justify-content: center; gap: 0.4rem;">
              <span>📊</span> 실전 이해를 돕는 시각화 SVG 다이어그램
            </div>
            {svg_code}
          </div>

          <!-- Toggle Button -->
          <button id="special-btn-{item["id"]}" onclick="toggleSpecialAns({item["id"]})" style="width: 100%; background: #f1f5f9; hover: background: #e2e8f0; color: #0f172a; border: 1px solid #cbd5e1; border-radius: 8px; padding: 0.75rem; font-size: 0.95rem; font-weight: 800; cursor: pointer; transition: all 0.2s; display: flex; justify-content: center; align-items: center; gap: 0.5rem;">
            <span>💡</span> 정답 및 퍼펙트 상세 해설 확인하기 ▾
          </button>

          <!-- Answer & Explanation Body -->
          <div id="special-ans-{item["id"]}" style="display: block; margin-top: 1.2rem; animation: fadeIn 0.3s ease;">
            <div style="margin-bottom: 1rem;">
              <strong style="color: #0284c7; font-size: 1.05rem; display: flex; align-items: center; gap: 0.4rem;">
                <span>🎯</span> 모범 정답 (Model Answer)
              </strong>
              {item["answer"]}
            </div>
            <div style="background: #fffbeb; border-left: 4px solid #f59e0b; padding: 1rem 1.2rem; border-radius: 0 8px 8px 0; font-size: 0.92rem; color: #78350f; line-height: 1.7;">
              <strong style="color: #b45309; font-size: 0.98rem; display: block; margin-bottom: 0.4rem;">
                💡 퍼펙트 상세 해설 및 시험장 함정 탈출 팁
              </strong>
              {item["explanation"]}
            </div>
          </div>
        </div>
      </div>
'''
        cards_html.append(card)

    all_cards = "\n".join(cards_html)

    tab_wrapper = f'''
    <!-- ================================================================= -->
    <!-- TAB 0: 🌟 과목평가 핵심 족보 & 실전 적중 20제 (초특급 가중치 완벽 해설 + SVG) -->
    <!-- ================================================================= -->
    <div id="tab-special-20" class="tab-content active">
      <!-- Hero Banner -->
      <div style="background: linear-gradient(135deg, #1e1b4b, #312e81, #1e3a8a); color: white; border-radius: 14px; padding: 1.8rem; margin-bottom: 1.5rem; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.2); position: relative; overflow: hidden;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 1rem;">
          <div>
            <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
              <span style="background: #ef4444; color: white; font-size: 0.8rem; font-weight: 900; padding: 0.2rem 0.6rem; border-radius: 20px;">MUST PASS</span>
              <span style="background: rgba(255,255,255,0.2); color: #fde047; font-size: 0.85rem; font-weight: 800; padding: 0.2rem 0.6rem; border-radius: 20px;">★ 출제 가중치 1위 집중 분석</span>
            </div>
            <h2 style="font-size: 1.6rem; font-weight: 900; margin-bottom: 0.4rem; color: #ffffff;">
              🏆 11/09 과목평가 핵심 족보 & 실전 적중 20제 완벽 마스터
            </h2>
            <p style="font-size: 0.95rem; color: #c7d2fe; line-height: 1.6; max-width: 820px;">
              사용자 지정 <strong>20대 최빈출 핵심 개념 및 서술/객관/단답형 문제</strong>를 완벽한 정답 해설과 <strong>고화질 인라인 SVG 다이어그램</strong>으로 총정리했습니다. 서술형 2문제(WHERE vs HAVING, forward vs redirect)부터 스칼라 서브쿼리, JSESSIONID, 정규화, SAVEPOINT까지 이 20개만 완벽히 마스터하면 과목평가 100점 만점이 보장됩니다!
            </p>
          </div>
          <div style="display: flex; flex-direction: column; gap: 0.5rem;">
            <button onclick="expandAllSpecial()" style="background: #38bdf8; color: #0f172a; border: none; font-weight: 800; padding: 0.65rem 1.2rem; border-radius: 8px; font-size: 0.88rem; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
              📖 전체 해설 펼치기 (학습 모드)
            </button>
            <button onclick="collapseAllSpecial()" style="background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); color: white; font-weight: 800; padding: 0.65rem 1.2rem; border-radius: 8px; font-size: 0.88rem; cursor: pointer; transition: all 0.2s;">
              🙈 전체 정답 가리기 (테스트 모드)
            </button>
          </div>
        </div>
      </div>

      <!-- Category Filter Pills -->
      <div style="display: flex; gap: 0.6rem; margin-bottom: 1.5rem; overflow-x: auto; padding-bottom: 0.3rem;">
        <span class="filter-pill active" onclick="filterSpecialCat('all', this)">🔥 전체 20문항</span>
        <span class="filter-pill" onclick="filterSpecialCat('cat-essay', this)">✍️ 서술형 1순위 (WHERE/HAVING &amp; forward/redirect)</span>
        <span class="filter-pill" onclick="filterSpecialCat('cat-sql', this)">💾 SQL &amp; 트랜잭션 &amp; DB설계 (11문항)</span>
        <span class="filter-pill" onclick="filterSpecialCat('cat-web', this)">🌐 Servlet &amp; JSP &amp; 세션상태관리 (7문항)</span>
      </div>

      <!-- 20 Question Cards Container -->
      <div id="special-20-container">
{all_cards}
      </div>
    </div>
'''
    return tab_wrapper

print("Tab generator function ready.")

def update_files():
    with open('WebTest_시험대비_학습웹.html', 'r', encoding='utf-8') as f:
        content = f.read()

    tab_html = generate_tab_html()

    js_code = '''
    // ==========================================
    // 🌟 과목평가 핵심 20제 인터랙션 스크립트
    // ==========================================
    function toggleSpecialAns(id) {
      const ans = document.getElementById('special-ans-' + id);
      const btn = document.getElementById('special-btn-' + id);
      if (!ans || !btn) return;
      if (ans.style.display === 'none') {
        ans.style.display = 'block';
        btn.innerHTML = '<span>💡</span> 정답 및 상세 해설 접기 ▴';
      } else {
        ans.style.display = 'none';
        btn.innerHTML = '<span>💡</span> 정답 및 퍼펙트 상세 해설 확인하기 ▾';
      }
    }

    function expandAllSpecial() {
      for (let i = 1; i <= 20; i++) {
        const ans = document.getElementById('special-ans-' + i);
        const btn = document.getElementById('special-btn-' + i);
        if (ans) ans.style.display = 'block';
        if (btn) btn.innerHTML = '<span>💡</span> 정답 및 상세 해설 접기 ▴';
      }
    }

    function collapseAllSpecial() {
      for (let i = 1; i <= 20; i++) {
        const ans = document.getElementById('special-ans-' + i);
        const btn = document.getElementById('special-btn-' + i);
        if (ans) ans.style.display = 'none';
        if (btn) btn.innerHTML = '<span>💡</span> 정답 및 퍼펙트 상세 해설 확인하기 ▾';
      }
    }

    function filterSpecialCat(cat, el) {
      document.querySelectorAll('#tab-special-20 .filter-pill').forEach(p => p.classList.remove('active'));
      if (el) el.classList.add('active');
      const cards = document.querySelectorAll('.special-card');
      cards.forEach(card => {
        if (cat === 'all' || card.classList.contains(cat)) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    }
'''

    # Update switchTab function for safe button selection
    old_switch = '''function switchTab(tabId) {
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
      event.target.classList.add('active');
      document.getElementById('tab-' + tabId).classList.add('active');
    }'''

    new_switch = '''function switchTab(tabId) {
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
      const btn = (event && (event.currentTarget || event.target.closest('.tab-btn')));
      if (btn) btn.classList.add('active');
      const targetContent = document.getElementById('tab-' + tabId);
      if (targetContent) targetContent.classList.add('active');
    }''' + js_code

    if old_switch in content:
        content = content.replace(old_switch, new_switch)
    else:
        # If already replaced or slightly different, append JS before </script>
        content = content.replace('</script>', js_code + '\n</script>')

    # Update nav bar
    old_nav = '''    <div class="tabs-nav">
      <button class="tab-btn active" onclick="switchTab('exam-sim')">📝 1. 과목평가 실전 모의고사 (총 32문제)</button>
      <button class="tab-btn" onclick="switchTab('notes')">📚 2. 7대 출제영역 핵심 요약집</button>
      <button class="tab-btn" onclick="switchTab('practical')">🛠️ 3. WebTest_sample 실습형 대비 (6단계)</button>
      <button class="tab-btn" onclick="switchTab('codes')">💻 4. 완성본 전체 소스코드 뷰어</button>
    </div>'''

    new_nav = '''    <div class="tabs-nav">
      <button class="tab-btn active" onclick="switchTab('special-20')" style="background: rgba(239, 68, 68, 0.08); border-bottom: 3px solid #ef4444; color: #ef4444;">
        <span style="background: #ef4444; color: white; padding: 2px 7px; border-radius: 12px; font-size: 0.72rem; font-weight: 900;">MUST PASS</span>
        ⭐ 1. 과목평가 핵심 20제 족보 (SVG 완비)
      </button>
      <button class="tab-btn" onclick="switchTab('exam-sim')">📝 2. 실전 모의고사 10회분 (총 320제)</button>
      <button class="tab-btn" onclick="switchTab('notes')">📚 3. 7대 출제영역 핵심 요약집</button>
      <button class="tab-btn" onclick="switchTab('practical')">🛠️ 4. WebTest_sample 실습형 대비 (6단계)</button>
      <button class="tab-btn" onclick="switchTab('codes')">💻 5. 완성본 전체 소스코드 뷰어</button>
    </div>'''

    content = content.replace(old_nav, new_nav)

    # Change old tab-exam-sim active
    content = content.replace('<div id="tab-exam-sim" class="tab-content active">', '<div id="tab-exam-sim" class="tab-content">')

    # Insert new tab before tab-exam-sim
    target_marker = '    <!-- ================================================================= -->\n    <!-- TAB 1: 실전 모의고사 32문제 시뮬레이터 -->'
    if target_marker in content:
        content = content.replace(target_marker, tab_html + "\n" + target_marker)
    else:
        print("Marker not found, looking for <div id=\"tab-exam-sim\"")
        content = content.replace('<div id="tab-exam-sim"', tab_html + '\n    <div id="tab-exam-sim"')

    # Save to WebTest_시험대비_학습웹.html
    with open('WebTest_시험대비_학습웹.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated WebTest_시험대비_학습웹.html successfully.")

    # Save to index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated index.html successfully.")

if __name__ == '__main__':
    update_files()
