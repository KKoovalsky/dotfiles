from typing import Any, Dict

from kitty.boss import Boss, Color
from kitty.window import Window, DynamicColor


def on_focus_change(boss: Boss, window: Window, data: Dict[str, Any]) -> None:
    bg = boss.startup_colors["background"]
    if data["focused"]:
        window.change_colors({DynamicColor.default_bg: bg.as_sharp})
    else:
        dimm_rate = 0.3
        dimmed_bg = Color(
            int(bg.red * dimm_rate),
            int(bg.g * dimm_rate),
            int(bg.b * dimm_rate),
        )
        window.change_colors({DynamicColor.default_bg: dimmed_bg.as_sharp})
