from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import Iterable, Union, Optional, Tuple

from matplotlib.figure import Figure
from networkx import Graph

from .drawing import MindMapDrawing
from .mindmap_node import IMindMapNode, MindMapNode
from .themes import MindMapTheme


class IMindMap(IMindMapNode, metaclass=ABCMeta):
    @abstractmethod
    def to_graph(self) -> Graph:
        ...

    @abstractmethod
    def children(self) -> Tuple[IMindMap]:
        ...

    @abstractmethod
    def draw(self,
             theme: MindMapTheme = MindMapTheme(),
             figsize: Optional[Tuple[int, int]] = None) -> None:
        ...


class MindMap(MindMapNode):
    def __init__(self, root: Union[str, IMindMapNode], name: str,
                 sub_maps: Iterable[Union[str, IMindMapNode, MindMap]] = ()):

        super().__init__(name)

        sub_maps: Tuple[IMindMapNode] = tuple(
            map(lambda m: MindMapNode(m) if isinstance(m, str) else m, sub_maps))

        if isinstance(root, str):
            root = MindMapNode(root)

        self._root = root
        self._sub_maps = sub_maps

    def children(self) -> Tuple[IMindMapNode]:
        return self._sub_maps

    def draw(self,
             theme: MindMapTheme = MindMapTheme(),
             figsize: Optional[Tuple[int, int]] = None) -> None:
        MindMapDrawing(self).draw(theme, figsize)

    def to_graph(self) -> Graph:
        graph = Graph()
        self._write_to_graph(graph)
        return graph

    def _write_to_graph(self, graph: Graph) -> None:
        for sub_map in self._sub_maps:

            if isinstance(sub_map, IMindMapNode):
                graph.add_edge(self._root, sub_map)

            if isinstance(sub_map, MindMap):
                graph.add_edge(self._root, sub_map._root)
                sub_map._write_to_graph(graph)




if __name__ == "__main__":
    MindMap("a", ["b", "c", "d"]).draw()
