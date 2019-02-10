from typing import Optional, Tuple

from .mindmap import IMindMap, MindMapTheme, MindMap


def draw_mindmap(mindmap: IMindMap,
                 theme: MindMapTheme = MindMapTheme(),
                 figsize: Optional[Tuple[int, int]] = None):
    return mindmap.draw(theme, figsize)


mmap = MindMap
