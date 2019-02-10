from typing import Optional, Tuple, NamedTuple, Dict


class MindMapTheme(NamedTuple):
    default_figsize: Optional[Tuple[int, int]] = None

    fontsize: int = 16
    textlimit: int = 15
    bbox: Optional[Dict] = None

    rectangular: bool = False
    edgewidth: int = 3
    edgecolor: str = "blue"


redTheme = MindMapTheme(
    figsize=(40, 40),

    fontsize=20,
    textlimit=15,
    bbox=dict(linewidth=3, edgecolor="black", facecolor="red"),

    rectangular=True,
    edgewidth=5,
    edgecolor="black"
)

blueTheme = MindMapTheme(
    figsize=(40, 40),

    fontsize=20,
    textlimit=15,
    bbox=dict(linewidth=3, edgecolor="blue", facecolor="white", joinstyle="round"),

    rectangular=True,
    edgewidth=10,
    edgecolor="blue"
)

standardTheme = MindMapTheme()
