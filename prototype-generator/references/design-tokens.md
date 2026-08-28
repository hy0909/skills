# SafeQR 디자인 토큰 (피그마 → CSS 변수)

출처: 피그마 [스크럽대디 파일](https://www.figma.com/design/SBGmrsYE4ooIBMwXvdtJ7S/) `component` 섹션(1860:20228)의
변수 정의(`get_variable_defs`). **이 캐시는 SafeQR 전용** — 다른 프로젝트면 그 프로젝트 피그마에서 새로 뽑는다.

## Color

| Figma 변수 | CSS 변수 | 값 | 주 용도 |
| --- | --- | --- | --- |
| gray/0 | `--gray-0` | `#ffffff` | 카드·모달 배경 |
| gray/50 | `--gray-50` | `#f3f5f7` | 페이지 배경, 테이블 헤더, 제품 카드 배경 |
| gray/100 | `--gray-100` | `#eef1f4` | 구분선, 비활성 필드 배경, 안내 박스, 검색 인풋 |
| gray/200 | `--gray-200` | `#e1e4eb` | 기본 보더 |
| gray/300 | `--gray-300` | `#d0d4db` | 비활성 버튼 배경 |
| gray/400 | `--gray-400` | `#9ba2ae` | placeholder, 테이블 헤더 텍스트, **종결 행(거절·취소) dim** |
| gray/500 | `--gray-500` | `#6c727e` | 보조 텍스트 |
| gray/600 | `--gray-600` | `#4b5666` | 아이콘 |
| gray/700 | `--gray-700` | `#364050` | 본문 보조, GNB 활성 칩 배경 |
| gray/900 | `--gray-900` | `#121826` | 본문, GNB 배경, 다크 버튼, 토스트 |
| primary | `--primary` | `#3232e2` | 승인 대기 칩, [승인] 버튼, 활성 상태 |
| purple/100 | `--purple-100` | `#f7f5ff` | [+ 제품 등록] 버튼 배경 |
| purple/200 | `--purple-200` | `#dcdcff` | [+ 제품 등록] 버튼 보더 |
| destructive/red 600 | `--red-600` | `#c90104` | [거절]·[네] 등 위험 버튼, 한도 초과 안내 |
| pink/50 | `--pink-50` | `#ffedfa` | 반려됨/거절함 칩 배경 |
| pink/600 | `--pink-600` | `#c40d9c` | 반려됨/거절함 칩 텍스트, 병행수입 칩 |

### 파생 색 (토큰 미정의 — 시안에서 추출, 디자이너 확정 필요)

| CSS 변수 | 값 | 용도 |
| --- | --- | --- |
| `--chip-pink-bg` | `#fdeef8` | 병행수입 칩 배경 |
| `--chip-blue-bg` / `--chip-blue-txt` | `#eef1fd` / `#3b4ee4` | 불법 복제 칩 |
| `--chip-orange-bg` / `--chip-orange-txt` | `#fff3e8` / `#e8590c` | 오류 칩 |
| `--green-600` | `#0ca678` | 이상 인증횟수 강조 |

## Typography

폰트 패밀리: **Pretendard** (`'Pretendard Variable', Pretendard, 'Noto Sans KR', system-ui, sans-serif`).
Variable woff2(`pretendard@1.3.9` npm, `dist/web/variable/woff2/PretendardVariable.woff2`, 약 2MB)를
base64로 HTML에 임베드한다 — Artifact CSP에서도, 오프라인에서도 항상 Pretendard로 뜬다.

| Figma 스타일 | size/weight | line-height |
| --- | --- | --- |
| H/H3 | 24 / 700 | 1.4 |
| subtitle/subtitle1 | 20 / 700 | 1.3 |
| subtitle/subtitle2 | 18 / 700 | 1.36 |
| body/body1 | 16 / 400·700 | 1.36 |
| body/body2 | 15 / 400·700 | 1.36 |
| body/body3 | 14 / 400·700 | 1.3 |
| caption/caption1 | 13 / 500 | 1.36 |
| caption/caption2 | 12 / 500 | 1.3 |

## 컴포넌트별 실측값 (get_design_context로 노드 단위 확인 — 눈대중 금지)

| 요소 | 실측값 |
| --- | --- |
| 페이지 배경 | **gray50 풀블리드** (흰 표면: **테이블 행 내부**·카드·모달 헤더/푸터·페이지네이션 현재 페이지) |
| GNB (h44, px24) | 로고 18 Bold white · 메뉴 16 Regular gray300, px20 py4 r4, 간격 12 · 활성 16 **Bold** gray100 + bg gray700 · 설정 14 gray100, border gray500 r999 · [QR 발주서 작성] 15 Regular gray900, white bg r6 px12 py4, 아이콘 16 |
| 타이틀바 (h56, px24) | 제목 20 Bold · 검색 h32 w300 bg gray100 r6, 텍스트 14, 아이콘 18 |
| [수정 완료] | h40 w172 r6, 15 Regular white, 활성 bg primary / 비활성 bg **gray400** |
| 테이블 | 헤더 13 Medium gray500, bg **gray100**, py6 px12, 상하 보더 gray200 · 본문 **16 Regular** gray900, p12, 하단 보더 gray100, **행 배경 white**(페이지 gray50 위) · 수량도 **16 Regular**(Bold 아님), 우측 정렬 |
| 상태 칩 | 13 Medium, r4, px6 py1(2) · 대기: bg primary white + x12 · 승인: white bg + border gray200, gray500 · 취소함: bg gray100 **gray600** · 반려됨/거절함: **칩** — bg **pink50 #ffedfa** + pink600 텍스트 |
| 승인 후 생성 | 13 Medium **gray500** + **시계 아이콘** 16 (ⓘ 아님) |
| 테이블 제품 카드 | bg gray50 r10 p8 · 썸네일 40×40 r6 border gray300 · 제품명 **14 Bold gray500** · 코드 12 Medium gray400 |
| [+ 제품 등록] | bg purple100 + border purple200, r10, **h56**, 14 Regular gray700, plus 16 |
| 다운로드 버튼 | h30 px8 r6, white bg + border gray200, 아이콘 16 · 비활성: bg gray200 |
| 페이지네이션 | 아이템 h40 w32 r6, 14 Regular gray900 · 현재 페이지: **bg white**(그림자 없음) · 화살표 16 |
| 발주 모달 (w560, r12) | 헤더 white px32 py24, 타이틀 **20 Bold**, X 32 · **바디 bg gray50**, p32, 섹션 간격 32 · 푸터 white px32 py28, 버튼 3등분(첫 칸 빈 스페이서) p8 r6 15 Regular — 발주 bg gray900 / 취소 border gray300 / 비활성 bg gray300 |
| 모달 입력 | 라벨 15 Regular gray900 + `*`는 **primary**(red 아님) + (선택) 12 Medium gray400 · 셀렉트 r8 **border gray300** py10 px12, 값 16 Regular gray900, 국가명 13 Medium gray400, 화살표 16 |
| 수량 스테퍼 | 행 라벨 'QR 그룹' 16 Regular · 삭제 16 원형 bg gray400 + 흰 x · +/- 버튼 28×28 r8 border gray300(비활성 bg gray50) · 인풋 w112 h32 r8 16 gray700 중앙 · 총 16 gray600(숫자만 Bold) · [QR 그룹 추가] h26 r99 white+border gray200, 13 Medium gray500(비활성 bg gray100) |
| 발주 단계 안내 | 타이틀 14 Bold gray500 + ⓘ18 · 박스 **bg gray200** r8 px24 py12 — 1행 13 Medium gray400, 2행 14 Regular gray700 · 불릿 13 Medium gray500 |
| 제품 셀렉트(모달·상세) | r8 border gray300 p12 · 썸네일 64×64 r6(빈 상태 bg gray100 border gray300 + 이미지 아이콘 24) · placeholder 16 gray400 · 제품명 16 Bold gray700 · 코드 14 Regular gray500 |
| 필터바 | '전체' 15 Regular + 카운트 15 **Bold**, **둘 다 gray500**(확대 스크린샷으로 확정) · 셀렉트 h36 r6 border gray200, 14 Regular **gray600**, 화살표 16 · 고정 폭: 최신순 104 / QR 전체 142 / 기간 240(날짜 13px) |
| QR 그룹 카드 | **그림자 없음** — white bg + **border gray200**, r12, p20 · '그룹 ID' 라벨 12 Medium gray400 · ID **18 Bold** gray900 · 필드 라벨 14 Regular gray400(폭 64) · 값 15 Regular **gray700**(수량 숫자만 15 Bold) · 행 간격 6, ID↔필드 20, 필드↔제품 24 · 마케팅 칩 bg **gray50 r999** 13 Medium gray500 |
| 컨펌 모달 | w448 r12, **border gray900** + shadow 2px 2px 16px rgba(0,0,0,.2) · 헤더 px32 py28 타이틀 **22 Bold** · 본문 px32 py8 **18 Regular gray900** · 푸터 px32 py28 우측 정렬, 버튼 **120×40 r6** 15 Regular, gap12 (ghost border gray300 / 확정 gray900 / 위험 red600) |
| 그룹 상세 카드 | **그림자 없음** — white bg + border gray200, r12, p32 · 카드 타이틀 **18 Bold** · 섹션 간격 48 + 구분선 gray200 · 2단 gap 40 · 비활성 필드: bg gray100 + **border gray300**, 라벨 15 **gray500**, `*` gray400, 값 16 gray500 |
| QR 정보 박스(상세 좌측) | white bg + border gray200, **r16**, px24 py20, 2열 · 라벨 16 Regular gray500 · 값 **22 Bold gray700** |
| QR 이미지 박스(상세 좌측) | white bg + border gray200, r16, h440 · **QR 이미지 160×160 중앙** |
| 관리자 처리 상태 | **칩 아님 — 우측 정렬 14 Regular 텍스트**: 승인함 gray700 · 거절함 gray400 · 사용자가 취소 gray400 (반려됨 핑크 칩은 **사용자 목록 전용**) |

## Radius · Shadow · Spacing · Icon

- radius: sm `2px`, md `6px` (+ 시안 관례: 인풋·버튼 `8px`, 카드 `12px`, 상세 정보 박스 `16px`, 칩·GNB 우측 버튼 `999px`)
- shadow: **카드·테이블·페이지네이션은 그림자 없음(보더로 구분)** · shadow_m 토큰 `1px 2px 8px rgba(0,0,0,.10)` = 드롭다운·토스트 · 모달 실측 `2px 2px 16px rgba(0,0,0,.2)`
- spacing 스케일: 0/2/4/6/8/12/16/20/24/32
- 아이콘: **lucide** (stroke ≈ 1.33px, 시안 커스텀 값) — 프로토타입에는 인라인 SVG로 넣는다
