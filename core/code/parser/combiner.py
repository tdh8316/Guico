class Combiner:

    def __init__(self, code, conn):
        self.code: dict = {"STARTS": [],
                           "ENDS": []}
        self.starts: list = []
        self.ends: list = []
        self.res: list = []

        for x in range(len(code)):
            leaf_io_id = code[x][2]
            leaf = [code[x][0], code[x][1]]
            # print(leaf)
            for y in range(len(conn)):
                # 줄 시작점 == 잎 아웃풋 (시작점)
                if conn[y][0] == leaf_io_id[1]:
                    self.starts.append(leaf)
                    self.code["STARTS"] = self.starts
                # 줄 끝점 == 잎 인풋 (끝점)
                elif conn[y][1] == leaf_io_id[0]:
                    self.ends.append(leaf)
                    self.code["ENDS"] = self.ends

        del self.starts
        del self.ends

        self.code = self.code["STARTS"] + self.code["ENDS"]
        [self.res.append(_) for _ in self.code if _ not in self.res]

    def combine(self):
        return self.res
