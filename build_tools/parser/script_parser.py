from contents.default import *


class Parse:
    def __init__(self, target: list, edges: list):
        self.target = target
        self.edges = edges
        self.leaves: int = len(self.target)
        # print(f"Build::Parse > Num of leaves={self.leaves}")

        self.parsed_token: list = []
        # Index: [TYPE, {CONTENT}, (INPUT-OUTPUT)]
        # print(self.target)
        for c in range(self.leaves):
            # print(self.target[c]["type"])
            self.parsed_token.append(
                [
                    self.target[c]["type"],
                    self.target[c]["content"],
                    (
                        self.target[c]["inputs"][0]["id"]
                        if target[c]["inputs"] != []
                        else 0,
                        # if self.target[i]["type"] != ENTRY_POINT
                        # else 0,
                        self.target[c]["outputs"][0]["id"],
                    ),
                ]
            )

        self.parsed_connect: list = []
        # Index: [(START, END)]
        for x in range(len(self.edges)):
            self.parsed_connect.append((self.edges[x]["start"], self.edges[x]["end"]))

    def get_token(self):
        return [self.parsed_token, self.parsed_connect]
