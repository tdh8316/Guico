import os
import sys
import json

from core.config import *


class Lexer:

    def __init__(self, target:str):
        self.res = []
        self._edges = []
        # print(f"{NAME} Build::Lexer > target={target}")
        if target is None or not os.path.isfile(target):
            print(f"{NAME} Build::Lexer > FATAL:Unable to read file.")
            raise IOError(f"다음 파일을 읽을 수 없습니다. {target}")

        with open(os.path.join(target), "r") as _s:
            self.token = json.loads(_s.read().split("Below are the variables.")[0], encoding='utf-8')

        for node_data in self.token['nodes']:
            self.res.append(node_data)
        for edge_data in self.token['edges']:
            self._edges.append(edge_data)

    def lexer(self):
        return self.res

    def edges(self):
        return self._edges
