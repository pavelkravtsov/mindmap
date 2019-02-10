from abc import ABCMeta, abstractmethod
from typing import Dict, Optional, Tuple

import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.axes import Axes
from matplotlib.collections import LineCollection
from networkx import Graph

from .mindmap import MindMap, MindMapTheme


class IMindMapDrawing(metaclass=ABCMeta):
    @abstractmethod
    def draw(self,
             theme: MindMapTheme = MindMapTheme(),
             figsize: Optional[Tuple[int, int]] = None) -> None:
        ...


class MindMapDrawing(IMindMapDrawing):
    def __init__(self, mindmap: MindMap):
        self.mindmap = mindmap

    def draw(self,
             theme: MindMapTheme = MindMapTheme(),
             figsize: Optional[Tuple[int, int]] = None) -> None:
        texts = []
        positions = []
        sizes = []

    def calculate_position(self):
        ...

    def draw_simple(self,
             theme: MindMapTheme = MindMapTheme(),
             figsize: Optional[Tuple[int, int]] = None) -> None:

        graph = self.mindmap.to_graph()
        positions = nx.kamada_kawai_layout(graph)

        with plt.subplots(figsize=figsize if figsize else theme.default_figsize) as (fig, ax):
            self._draw_edges(graph, positions, ax, theme)
            self._draw_nodes(graph, positions, ax, theme)

            ax.axis('off')
            ax.axis('equal')

    def _draw_nodes(self,
                    graph: Graph,
                    positions: Dict[float],
                    ax: Axes,
                    theme: MindMapTheme) -> None:
        for node in graph.nodes:
            ax.text(
                *positions[node],
                node.display_string(theme.textlimit),
                size=theme.fontsize,
                bbox=theme.bbox
            )

    def _draw_edges(self,
                    graph: Graph,
                    positions: Dict[float],
                    ax: Axes,
                    theme: MindMapTheme) -> None:
        edge_collection = []
        for a, b in graph.edges:
            a, b = positions[a], positions[b]

            if not theme.rectangular:
                edge_collection.append((a, b))
            else:
                c = (a[0], b[1])
                edge_collection.append((a, c))
                edge_collection.append((c, b))

        ax.add_collection(
            LineCollection(
                edge_collection,
                linewidths=theme.edgewidth,
                colors=(theme.edgecolor,)
            )
        )
