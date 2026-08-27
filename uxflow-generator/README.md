# UX Flow Generator

피그잼(FigJam)에 개발자 친화적인 UX flow를 자동 작성하는 Claude 스킬.
플로우 JSON을 만들어 로컬 플러그인 서버(localhost:3765)로 보내면, 핸드오프문서 자동생성기 플러그인이 피그잼 캔버스에 도형·화살표로 그립니다.

- 페이지/기능 단위 작성, 해피(회색)/에러(빨강)/예외(주황) 케이스 구분
- 권한·상태·FE/BE 담당 뱃지, yes/no 분기 화살표, 참고 피그마 링크 표기
- 스키마: `references/flow-schema.md` · 검증/전송: `scripts/validate_flow.py`
