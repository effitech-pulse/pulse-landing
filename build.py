"""Независимая сборка самодостаточного лендинга «Пульс скважины»."""
from __future__ import annotations

import base64
import logging
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def render() -> str:
    """Встроить утверждённый знак в HTML без внешних зависимостей."""
    html = (ROOT / "template.html").read_text(encoding="utf-8")
    logo = base64.b64encode((ROOT / "assets/pulse-symbol.svg").read_bytes()).decode("ascii")
    return html.replace("__PULSE_LOGO__", "data:image/svg+xml;base64," + logo)


def main() -> None:
    """Собрать статическую страницу в dist/index.html."""
    out = ROOT / "dist/index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(render(), encoding="utf-8")
    logging.info("Лендинг собран: %s", out)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
