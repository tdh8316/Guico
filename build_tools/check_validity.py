from leaf_content.default import *


class CheckValidity:

    def __init__(self, inter_code: list):
        self.inter_code = inter_code

        self.wn_count = 0

        if self.inter_code.count([ENTRY_POINT, {}]) > 1:
            raise SyntaxError("Event 시작했을 때 잎은 한 개 이상 존재할 수 없습니다.")

        for ii in range(len(self.inter_code)):
            if self.inter_code[ii][0] == WINDOW_NEW:
                self.wn_count += 1
        if self.wn_count > 1:
            raise SyntaxError("창 만들기 잎은 한 개 이상 존재할 수 없습니다.")
