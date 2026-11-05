@echo off
chcp 65001 > nul
echo ========================================================
echo   SSAFY 11/09 과목/월말평가 대비 시스템 - Git 원격 배포 도구
echo ========================================================
echo.
echo 현재 로컬 Git 저장소(main 브랜치)와 index.html 배포 준비가 완료되어 있습니다.
echo.
set /p REPO_URL="원격 Git 저장소 URL을 입력하세요 (예: https://github.com/iamywl/ssafy-backend-prep.git): "

if "%REPO_URL%"=="" (
    echo [ERROR] 저장소 URL이 입력되지 않았습니다. 종료합니다.
    pause
    exit /b 1
)

echo.
echo [1/3] 원격 저장소(origin) 설정 중...
git remote remove origin 2>nul
git remote add origin %REPO_URL%

echo [2/3] 최신 변경 사항 확인 및 추가...
git add .
git commit -m "update: latest exam simulators and test materials" 2>nul

echo [3/3] 원격 저장소 main 브랜치로 푸시 중...
git push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ========================================================
    echo   [성공] Git 원격 저장소 배포가 완료되었습니다!
    echo ========================================================
    echo GitHub Pages 배포 설정:
    echo 1. GitHub 저장소 페이지 -> Settings -> Pages 이동
    echo 2. Branch: 'main' / Folder: '/ (root)' 선택 후 Save 클릭
    echo 3. 1~2분 후 생성되는 웹 주소로 시험 대비 사이트에 접속하실 수 있습니다.
) else (
    echo.
    echo [경고] Git push 과정에서 오류가 발생했습니다.
    echo GitHub 인증(로그인/토큰) 상태 또는 저장소 주소를 다시 확인해 주세요.
)
echo.
pause
