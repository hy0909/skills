# Prototype Generator

피그마 화면이랑 기능명세 md를 주면, 눌러볼 수 있는 웹 프로토타입을 HTML 파일 하나로 만들어주는 Claude 스킬이에요.

**왜 쓰나요?**
개발자한테 "일반 사용자랑 관리자 화면이 어떻게 다른지", "이 모달이 어떤 조건에서 어떻게 흘러가는지"를
문서나 말 대신 클릭으로 보여주려고요.

**뭐가 나오나요?**
파일 하나. 브라우저로 열면 끝이에요. 설치도 빌드도 없어요.

- 권한 전환 토글 — 일반 사용자 ↔ 관리자 화면을 오가며 비교
- 실제로 동작하는 플로우 — 발주서 작성, 승인/거절, 발주 취소, 그룹 수정, 토스트까지
- 같은 데이터를 공유해서, 사용자가 취소하면 관리자 화면도 바로 바뀌어요

**디자인은요?**
피그마 변수(컬러·폰트·radius)를 CSS 토큰으로 그대로 가져와서 적용해요. 폰트는 Pretendard(파일에 내장).

**어떻게 쓰나요?**
Claude Code에서 이렇게 주면 돼요:
> "이 화면 프로토타입으로 만들어줘" + 피그마 디자인 링크 + 스펙 md 링크(GitHub도 OK)

**예제:** [examples/safeqr-qr-order-prototype.html](examples/safeqr-qr-order-prototype.html) — SafeQR QR 발주·그룹 관리
**만드는 기준:** [SKILL.md](SKILL.md) · [references/prototype-standards.md](references/prototype-standards.md)
