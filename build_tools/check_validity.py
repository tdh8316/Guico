from contents.default import *


class CheckValidity:

    def __init__(self, inter_code: list):
        self.inter_code = inter_code

        self.wn_count = 0

        for ii in range(len(self.inter_code)):
            if self.inter_code[ii][0] == WINDOW_NEW:
                if self.wn_count > 1:
                    raise SyntaxError("창 만들기 잎은 한 개 이상 존재할 수 없습니다.")
                self.wn_count += 1
