"""Parse Nuxt 3 __NUXT_DATA__ (devalue flatten format) back into normal objects.

Nuxt serializes SSR payload as a flat array. Objects/arrays store *indices*
pointing into that array instead of real values. A few negative indices encode
special values (undefined / NaN / Infinity / -0). Arrays whose first element is
a string are type wrappers (e.g. ["ShallowReactive", 1]); we unwrap them.

This module is shared by the catalog refresh pipeline.
"""
from __future__ import annotations

import json
import math
from typing import Any

_UNSET = object()

_SPECIALS = {
    -1: None,          # undefined -> None
    -2: math.nan,
    -3: math.inf,
    -4: -math.inf,
    -5: -0.0,
}


def unflatten(values: list[Any]) -> Any:
    """Restore the object graph rooted at index 0 of a devalue payload."""
    hydrated: list[Any] = [_UNSET] * len(values)

    def hyd(ref: Any) -> Any:
        if isinstance(ref, bool) or not isinstance(ref, int):
            return ref
        if ref < 0:
            return _SPECIALS.get(ref)
        if ref >= len(values):
            return None
        if hydrated[ref] is not _UNSET:
            return hydrated[ref]

        raw = values[ref]
        if raw is None or isinstance(raw, (int, float, str, bool)):
            hydrated[ref] = raw
        elif isinstance(raw, list):
            # Nuxt type wrapper, e.g. ["ShallowReactive", 1] / ["Reactive", 7]
            if (len(raw) == 2 and isinstance(raw[0], str)
                    and isinstance(raw[1], int) and not isinstance(raw[1], bool)
                    and raw[1] >= 0):
                hydrated[ref] = hyd(raw[1])
            else:
                arr: list[Any] = []
                hydrated[ref] = arr
                for item in raw:
                    arr.append(hyd(item))
        elif isinstance(raw, dict):
            obj: dict[str, Any] = {}
            hydrated[ref] = obj
            for key, index in raw.items():
                obj[key] = hyd(index)
        else:
            hydrated[ref] = raw
        return hydrated[ref]

    return hyd(0)


def load(path: str) -> Any:
    with open(path, encoding="utf-8") as fh:
        return unflatten(json.load(fh))


def walk(obj: Any):
    """Yield every dict found in the object graph (breadth-first-ish)."""
    seen = set()
    stack = [obj]
    while stack:
        cur = stack.pop()
        if id(cur) in seen:
            continue
        seen.add(id(cur))
        if isinstance(cur, dict):
            yield cur
            stack.extend(cur.values())
        elif isinstance(cur, list):
            stack.extend(cur)


if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "raw/market-nuxt.json"
    data = load(target)
    print("root type:", type(data).__name__)
    if isinstance(data, dict):
        print("root keys:", list(data.keys()))
    out = target.replace(".json", "-hydrated.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2, default=str)
    print("wrote:", out)
