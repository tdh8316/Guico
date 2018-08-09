from leaf_content.default import *


class _Combiner:

    def __init__(self, code, conn):
        self.code: dict = {"STARTS": [],
                           "ENDS": []}
        self.starts: list = []
        self.ends: list = []
        self.res: list = []
        # print(conn)

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
        print(self.res)
        return self.res


# NOTE: UTC+9, 대한민국 표준시 기준, 2018년 7월 19일 오후 7시 01분 성공함!!!!!!

class Combiner:

    def __init__(self, src, connect):
        self.src = src
        self.connect = connect
        self.replacing: list = []
        self.result: list = []

        # 엔트리 포인트 검색
        for _ in self.src:
            print("search entry :", _)
            if _[2][0] == 0:  # 인풋 소켓이 0이라면 (이벤트 잎이라면)
                self.replacing.append(_)
                continue

        # 엔트리 포인트에 연결된 노드 검색
        for connect in self.connect:
            if connect[0] == self.replacing[0][2][1]:
                for code in self.src:
                    if code[2][0] == connect[1]:
                        self.replacing.append(code)

        # 그 다음부터 끝까지..
        for code in self.replacing:
            if code[2][0] == 0:
                print("이벤트 잎 감지됨")
                # TODO
                self.replacing.append()
                continue
            _socket_of_code = code[2]
            for connect in self.connect:
                # connect[0] : 인풋 잎 ID
                if connect[0] == _socket_of_code[1]:
                    for i in self.src:
                        if connect[1] in i[2]:
                            self.replacing.append(i)

        # 결과 작성
        for full_inf in self.replacing:
            self.result.append([full_inf[0], full_inf[1]])

    def combine(self):
        # print(self.result)
        return self.result
