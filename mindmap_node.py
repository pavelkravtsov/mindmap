from abc import ABCMeta, abstractmethod


class IMindMapNode(metaclass=ABCMeta):
    @abstractmethod
    def display_string(self, limit: int) -> str:
        ...


class MindMapNode(IMindMapNode):
    def __init__(self, name: str):
        self.name = name

    def display_string(self, limit: int) -> str:
        tokens = []
        last_line_length = 0
        for word in self.name.split():
            if not word:
                continue

            if last_line_length + len(word) + 1 > limit and last_line_length > 0:
                last_line_length = len(word)
                tokens.append("\n")
            else:
                last_line_length += len(word) + 1

            tokens.append(word)

        return " ".join(tokens)
