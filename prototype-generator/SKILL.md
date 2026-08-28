---
name: prototype-generator
description: Figma 디자인 + 기능명세 md를 받아 개발자 커뮤니케이션용 인터랙티브 웹 프로토타입(단일 HTML)을 만든다. Use when the user asks for a 프로토타입, 인터랙티브 목업, 클릭해볼 수 있는 화면, "피그마 화면 웹으로 구현", 권한(role)별 화면 비교(일반 사용자/관리자), or wants to hand developers a clickable version of Figma screens with working modal/approval/edit flows. 피그마 변수(컬러·타이포·radius)를 CSS 토큰으로 1:1 매핑해 디자인 시스템 그대로 적용한다.
---

# Prototype Generator

피그마 시안과 스펙 md를 "눌러볼 수 있는" 단일 HTML 프로토타입으로 바꾼다. 독자는 개발자 —
"권한별로 뭐가 다른가, 이 모달은 어떤 조건에서 어떻게 흘러가나"를 문서가 아니라 클릭으로 이해시키는 것이 목적이다.
프로덕션 코드가 아니다: 빌드 없음, 프레임워크 없음, API 없음.

## Pipeline

1. **입력 수집.**
   - **스펙 md** — 붙여넣기·로컬 파일·GitHub 링크 모두 허용. GitHub이면
     `gh api "repos/{owner}/{repo}/contents/{path}?ref={branch}" --jq .content | base64 -d`
     (프라이빗 레포도 gh 인증으로 동작). **동작·정책·용어의 최우선 기준은 md다.**
   - **Figma 디자인 파일 링크** — 시각(레이아웃·간격·컬러·컴포넌트 형태)의 기준.
   - **Figma Make 링크는 MCP로 못 읽는다**(`/make/` 미지원). Make 화면은 대부분 디자인 파일에서 파생되므로
     디자인 파일 + md로 구현하고, Make 쪽과 대조가 필요하면 사용자에게 ① Make 우상단 코드 다운로드(zip) 또는
     ② 화면 스크린샷을 요청한다. 요청만 하고 멈추지 말 것 — 디자인 파일 기준으로 먼저 완성한다.
2. **토큰 추출.** `get_variable_defs`를 컴포넌트 섹션(또는 대표 화면) 노드에 호출 → 피그마 변수를 CSS 변수로 1:1 매핑.
   토큰에 없는 색(칩·뱃지 등)은 스크린샷에서 추출하되 **CSS 주석으로 "파생(토큰 미정의)" 표시**를 남긴다.
   현재 프로젝트(SafeQR) 토큰 캐시: `references/design-tokens.md`.
3. **화면 캡처 + 컴포넌트 실측.** 스펙 md의 Figma 링크마다 `get_screenshot`(목록/모달/입력 전·후/처리 후 전부).
   **폰트 크기·웨이트·컬러·패딩은 스크린샷 눈대중 금지** — 반드시 GNB·타이틀·테이블 헤더/셀·칩·버튼·모달 등
   핵심 컴포넌트 노드마다 `get_design_context`를 호출해 실측값(text-[16px], Bold, gray/500 …)을 받아 적용한다
   (스크린샷은 축소 렌더라 13px와 16px 구분이 안 돼 시각 비교만으로는 반드시 틀린다).
   큰 프레임(수만 px)은 `get_design_context`가 XML 구조만 반환하므로, 그 XML에서 내부 노드 ID를 찾아
   작은 컴포넌트 단위로 다시 조회한다. 실측값은 `references/design-tokens.md`의 "컴포넌트별 실측값" 표에 기록해 캐시한다.
   `get_metadata`는 섹션이 크면 수백만 자가 나오므로 노드 구조가 꼭 필요할 때만.
4. **md ↔ 시안 충돌 처리.** 용어·문구는 md 우선(특히 md가 "시안은 구표기, 갱신 예정"이라 명시한 것).
   md에 없는데 시안에만 있는 표기는 시안을 따른다. 어느 쪽이든 **충돌 목록을 최종 보고에 정리**해 사용자가 확정하게 한다.
5. **단일 HTML 작성.** 구현 기준은 `references/prototype-standards.md` — 파일 구조, 상태 모델, 권한 토글,
   모달/토스트 패턴, 폰트 임베드까지 전부 그 문서를 따른다.
6. **브라우저 검증.** 로컬 정적 서버(`python3 -m http.server`)로 띄워 **모든 플로우를 직접 클릭**한다:
   모달 열기 → 검증 규칙(한도·비활성) → 실행 → 토스트 → 목록 반영 → **권한 전환 후 반대편 반영**까지.
   스크린샷을 피그마 원본과 나란히 비교해 어긋난 부분을 고친다.
7. **전달.** ① HTML 파일(브라우저로 열면 끝) ② Claude Artifact로 배포(팀 공유 링크).
   기존 프로토타입 갱신이면 같은 Artifact URL로 재배포한다.

## Hard rules

- **단일 HTML + vanilla JS.** CDN·빌드·외부 요청 없음(폰트 포함 전부 인라인). 파일 하나가 곧 산출물.
- **색·radius·그림자·폰트는 토큰 CSS 변수로만** 쓴다. 하드코딩 금지(파생 색은 변수로 승격 후 사용).
- **폰트는 Pretendard** — Variable woff2를 base64 data URI로 임베드(`font-weight:45 920`). CDN 링크 금지
  (Artifact CSP가 Google Fonts 외 전부 차단하므로 임베드가 유일하게 어디서나 동작).
- **권한별 뷰는 화면 복제가 아니라 같은 상태(데이터)를 공유**한다. 사용자가 취소하면 관리자 목록이 즉시 바뀌는 것
  자체가 이 프로토타입의 존재 이유다.
- **프로토타입 컨트롤은 실제 UI와 시각적으로 분리**(플로팅 카드, "프로토타입 컨트롤" 라벨). 권한 토글 + 데모 가이드.
- **스펙이 TBD인 화면**은 임의로 그리되 화면 안에 `미확정 — 프로토타입 임의 구성 (REQ-XX)` 각주를 남긴다.
- **범위 외 메뉴**는 지우지 말고 빈 상태 페이지("프로토타입 범위 외")로 남긴다 — GNB(IA)는 실제와 동일해야 한다.
- 수량·한도 같은 **입력 검증 규칙은 스펙 숫자 그대로** 구현한다(예: 1만 단위, 최소 10,000, 총합 600,000 컷).
  "비슷하게"는 금지 — 개발자가 이 화면을 보고 검증 로직을 구현한다.

## 파일 위치·이름

- 산출물: `prototype-generator/examples/<서비스>-<도메인>-prototype.html` (이 레포에 커밋해 재사용 예제로 남긴다)
- 참조: `references/design-tokens.md`(프로젝트 토큰 캐시 — 다른 프로젝트면 갱신), `references/prototype-standards.md`
- 예제: `examples/safeqr-qr-order-prototype.html` — SafeQR QR 발주·그룹 관리 v4.0 (사용자/관리자, 발주·승인·거절·취소·그룹 수정 플로우)
