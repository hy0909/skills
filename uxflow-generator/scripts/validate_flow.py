#!/usr/bin/env python3
"""UX Flow JSON 검증 + 플러그인 서버 전송.

사용법:
  python3 validate_flow.py flow.json           # 검증만
  python3 validate_flow.py flow.json --send    # 검증 후 localhost:3765/ux-flow 로 전송
"""
import json
import sys
import urllib.request
import urllib.error

NODE_TYPES = {"start", "end", "screen", "action", "decision", "api", "note"}
CASES = {"happy", "error", "exception"}
SERVER = "http://localhost:3765"

YES_LABELS = {"yes", "y", "예", "네", "ok", "성공"}


def validate(flow):
    errors, warns = [], []

    for key in ("page", "feature"):
        if not flow.get(key):
            errors.append(f"필수 필드 누락: {key}")

    for link in flow.get("figmaLinks", []) or []:
        if not isinstance(link, dict) or not link.get("url"):
            errors.append(f"figmaLinks 항목에 url이 없습니다: {link}")
    if not flow.get("figmaLinks"):
        warns.append("figmaLinks가 비어 있습니다 — 참고한 피그마 링크를 표기하세요.")

    nodes = flow.get("nodes") or []
    edges = flow.get("edges") or []
    if not nodes:
        errors.append("nodes가 비어 있습니다.")

    ids, cells = {}, {}
    for i, n in enumerate(nodes):
        tag = n.get("id") or f"nodes[{i}]"
        if not n.get("id"):
            errors.append(f"{tag}: id 누락")
        elif n["id"] in ids:
            errors.append(f"{tag}: id 중복")
        else:
            ids[n["id"]] = n

        if n.get("type") not in NODE_TYPES:
            errors.append(f"{tag}: type이 잘못됨 ({n.get('type')!r}) — {sorted(NODE_TYPES)} 중 하나")
        if not n.get("label"):
            errors.append(f"{tag}: label 누락")
        elif len(n["label"]) > 16:
            warns.append(f"{tag}: label이 {len(n['label'])}자 — 16자 이하 권장 ({n['label']!r})")

        if not isinstance(n.get("col"), (int, float)) or not isinstance(n.get("row"), (int, float)):
            errors.append(f"{tag}: col/row는 숫자 필수")
        else:
            cell = (n["col"], n["row"])
            if cell in cells:
                errors.append(f"{tag}: (col={cell[0]}, row={cell[1]}) 위치가 {cells[cell]}와 겹침")
            cells[cell] = tag

        if n.get("case") and n["case"] not in CASES:
            errors.append(f"{tag}: case가 잘못됨 ({n['case']!r}) — {sorted(CASES)} 중 하나")

        details = n.get("details") or []
        is_note = n.get("type") == "note"  # note 스티커는 긴 정책 텍스트 허용
        if not is_note and len(details) > 6:
            warns.append(f"{tag}: details {len(details)}개 — 6개 이하 권장, 긴 내용은 note 노드로")
        for d in details:
            if not is_note and len(str(d)) > 22:
                warns.append(f"{tag}: detail이 {len(str(d))}자 — 22자 이하 권장 ({d!r})")
        if n.get("type") == "api" and details and "/" not in str(details[0]):
            warns.append(f"{tag}: api 노드 details 첫 줄은 'METHOD /path' 권장 ({details[0]!r})")

    outgoing = {}
    for j, e in enumerate(edges):
        for end in ("from", "to"):
            if e.get(end) not in ids:
                errors.append(f"edges[{j}]: {end}={e.get(end)!r} 노드가 없습니다")
        if e.get("from") in ids:
            outgoing.setdefault(e["from"], []).append(e)

    for nid, n in ids.items():
        outs = outgoing.get(nid, [])
        if n.get("type") == "decision":
            if len(outs) < 2:
                errors.append(f"{nid}: decision은 나가는 edge가 2개 이상 필요 (현재 {len(outs)}개)")
            for e in outs:
                if not e.get("label"):
                    errors.append(f"{nid} → {e.get('to')}: decision 분기 edge에 label 필수 (YES/NO/조건)")
            if outs and not any(str(e.get("label", "")).strip().lower() in YES_LABELS for e in outs):
                warns.append(f"{nid}: YES/성공 분기 라벨이 없음 — 해피 패스가 어느 쪽인지 표시 권장")
        elif n.get("type") not in ("end", "note") and not outs:
            warns.append(f"{nid}: 나가는 edge가 없음 — 종착이면 type을 end로")

    # 인접성: FigJam 커넥터는 경유점 제어가 불가 — 2칸 이상 건너뛰는 엣지는 중간 노드를 관통한다
    pos = {n.get("id"): (n.get("col"), n.get("row")) for n in nodes if n.get("id")}
    for e in edges:
        f, t = pos.get(e.get("from")), pos.get(e.get("to"))
        if not f or not t or None in f or None in t:
            continue
        dc, dr = abs(t[0] - f[0]), abs(t[1] - f[1])
        if dc >= 2 or (dc == 0 and dr >= 2):
            errors.append(
                f"비인접 엣지 {e.get('from')}({f[0]},{f[1]})→{e.get('to')}({t[0]},{t[1]}) — "
                "선이 다른 노드를 관통합니다. 중간 노드를 추가하거나 배치를 인접 셀로 조정하세요.")

    # 해피 패스가 row 0에 있는지 대략 확인
    row0 = [n for n in nodes if n.get("row") == 0 and n.get("type") != "note"]
    if nodes and not row0:
        warns.append("row 0에 노드가 없습니다 — 해피 패스는 row 0 왼→오른쪽으로 배치하세요.")

    return errors, warns


def send(flow):
    req = urllib.request.Request(
        SERVER + "/ux-flow",
        data=json.dumps(flow, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=5) as res:
            print("전송 완료:", res.read().decode("utf-8"))
    except urllib.error.URLError as e:
        print("전송 실패:", e)
        print("→ 플러그인 서버가 꺼져 있으면 플러그인 폴더에서 ./start-server.sh 를 먼저 실행하세요.")
        sys.exit(2)


def main():
    args = [a for a in sys.argv[1:] if a != "--send"]
    do_send = "--send" in sys.argv
    if not args:
        print(__doc__)
        sys.exit(1)

    with open(args[0], encoding="utf-8") as f:
        flow = json.load(f)

    errors, warns = validate(flow)
    for w in warns:
        print("WARN :", w)
    for e in errors:
        print("ERROR:", e)
    print(f"— 노드 {len(flow.get('nodes') or [])}개, 엣지 {len(flow.get('edges') or [])}개, "
          f"오류 {len(errors)}건, 경고 {len(warns)}건")

    if errors:
        sys.exit(1)
    if do_send:
        send(flow)


if __name__ == "__main__":
    main()
