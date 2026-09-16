# human-writing

한국어 글을 사람이 쓴 것처럼, AI 티 없이, 개발·디자인을 모르는 사람도 바로 이해하게 쓰는 공통 문체 규칙 스킬입니다.

## 하는 일

| 모드 | 언제 | 무엇을 |
| --- | --- | --- |
| 작성 | 이슈·PR·기획서·정책·답변 등 모든 한국어 글을 쓸 때 | 짧은 문장, 번역투·상투 표현 금지, 비교 항목은 표, 막연한 말은 숫자·사례로 |
| 윤문 | "윤문해줘", "AI 티 없애줘", "번역투 제거"라고 할 때 | AI처럼 보이는 이유 3~5개 진단 → 수정 → 변경량 30% 넘으면 멈추고 보고 |

## 파일

- `SKILL.md` — 규칙 본문. 적용 범위·예외, 문장·쉬운 말·금지 표현·구체성·관점·표 판단·윤문 절차·자기 점검
- `references/ai-patterns-ko.md` — 한국어 AI 글 패턴 10분류와 전/후 예시
- `references/voice-samples.md` — 내 글 샘플을 붙이는 자리. 채우면 그 문체를 따라 씀

## 설치

```bash
git clone https://github.com/hy0909/skills.git
ln -s "$PWD/skills/human-writing" ~/.claude/skills/human-writing   # Claude Code
ln -s "$PWD/skills/human-writing" ~/.codex/skills/human-writing    # Codex
```

스킬을 부르지 않아도 항상 적용하려면 `~/.claude/CLAUDE.md`(Codex는 `~/.codex/AGENTS.md`)에 "모든 한국어 글은 human-writing 스킬 규칙을 따른다"는 한 줄과 핵심 요약을 넣습니다.

## 참고 출처

`SKILL.md` 맨 아래 "참고 출처" 절에 정리했습니다. 한글 AI 티 제거기 [im-not-ai](https://github.com/epoko77-ai/im-not-ai), [woonjangahn의 상투 패턴 gist](https://gist.github.com/woonjangahn/3ad4d8fe1804aed2e7cafc9493ec566f), [blader/humanizer](https://github.com/blader/humanizer), [위키백과 Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), 그리고 폭스씨지·요즘것들·브런치 maven·Promptway·Sid Saladi 글의 프롬프트와 전/후 예시를 참고했습니다.
