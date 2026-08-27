#!/bin/bash
# uxflow-generator 스킬이 수정됐는지 확인하고, 수정분만 자동 커밋/푸시 (hy0909/skills)
# Claude Code 전역 Stop 훅에서 호출됨. 변경 없으면 아무것도 하지 않음.
REPO="$HOME/Downloads/figmaplugin_260531/skills"
LOG="$REPO/.hooks/autopush.log"

cd "$REPO" 2>/dev/null || exit 0

# uxflow-generator(및 훅 자신)의 변경만 스테이징
git add -A uxflow-generator .hooks 2>/dev/null

if ! git diff --cached --quiet 2>/dev/null; then
  git commit -m "uxflow-generator 스킬 업데이트 ($(date '+%Y-%m-%d %H:%M'))" --quiet \
    && echo "[$(date '+%F %T')] 커밋 완료" >> "$LOG"
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
