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
| destructive/red 600 | `--red-600` | `#c90104` | [거절]·[네] 등 위험 버튼, 필수(*) 표시, 한도 초과 안내 |
| pink/600 | `--pink-600` | `#c40d9c` | 반려됨/거절함 텍스트, 병행수입 칩 |

### 파생 색 (토큰 미정의 — 시안에서 추출, 디자이너 확정 필요)

| CSS 변수 | 값 | 용도 |
| --- | --- | --- |
| `--violet-txt` | `#8f8cf0` | '승인 후 생성 ⓘ' 연보라 텍스트 |
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

## Radius · Shadow · Spacing · Icon

- radius: sm `2px`, md `6px` (+ 시안 관례: 인풋·버튼 `8px`, 카드 `12px`, 모달 `16px`, 칩·GNB 우측 버튼 `999px`)
- shadow_m: `1px 2px 8px rgba(0,0,0,.10)` (카드, 페이지네이션 현재 페이지)
- spacing 스케일: 0/2/4/6/8/12/16/20/24/32
- 아이콘: **lucide** (stroke ≈ 1.33px, 시안 커스텀 값) — 프로토타입에는 인라인 SVG로 넣는다
