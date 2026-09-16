#!/bin/bash
# hy0909/skills 저장소의 스킬이 수정됐는지 확인하고, 변경분을 자동 커밋/푸시한다.
# Claude Code 전역 Stop 훅에서 호출됨. 변경 없으면 아무것도 하지 않음.
# 2026-09-16: uxflow-generator만 → 저장소 전체 스킬로 확장 (human-writing 공통 문체 규칙 반영)
REPO="$HOME/Downloads/figmaplugin_260531/skills"
LOG="$REPO/.hooks/autopush.log"

cd "$REPO" 2>/dev/null || exit 0

# 저장소 전체 변경 스테이징 (.gitignore가 캐시·로그·DS_Store 제외)
git add -A . 2>/dev/null

if ! git diff --cached --quiet 2>/dev/null; then
  CHANGED=$(git diff --cached --name-only | cut -d/ -f1 | sort -u | grep -v '^\.' | tr '\n' ' ' | sed 's/ $//')
  # GitHub 이메일 보호(GH007) 회피 — noreply 주소로 커밋
  git -c user.name="hy0909" -c user.email="hy0909@users.noreply.github.com" \
    commit -m "스킬 업데이트: ${CHANGED:-기타} ($(date '+%Y-%m-%d %H:%M'))" --quiet \
    && echo "[$(date '+%F %T')] 커밋 완료: ${CHANGED}" >> "$LOG"
fi

# 원격보다 앞서 있으면(방금 커밋 포함) 푸시
if [ -n "$(git log origin/main..HEAD --oneline 2>/dev/null)" ]; then
  if git push origin main --quiet 2>>"$LOG"; then
    echo "[$(date '+%F %T')] 푸시 완료" >> "$LOG"
  else
    echo "[$(date '+%F %T')] 푸시 실패 — 네트워크/인증 확인 필요" >> "$LOG"
  fi
fi

exit 0
