import sys
import traceback as tb
import qcrash.api as qcrash

from PyQt5.QtWidgets import QMessageBox

from core.config import *

GITHUB_OWNER = 'tdh8316'
GITHUB_REPO = 'Guico'
EMAIL = 'tdh8316@naver.com'


def get_system_info():
    return 'OS: %s\nPython: %r' % (sys.platform, sys.version_info)


def report_unhandled_exception(exctype, value, traceback):
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    print(f"현재 {NAME} 내부에 발생한 오류 전문입니다.")

    if (QMessageBox.information(None, f"{NAME} 예외 처리 체계", f"죄송합니다. {NAME} 에 내부 오류가 발생했습니다.\n"
                                                          "\n문제가 계속해서 발상한다면 오류를 제보해 주세요.\n"
                                                          "이 오류를 제보하시겠습니까?",
                                QMessageBox.Yes | QMessageBox.No)) == 16384:
        # configure backends
        qcrash.install_backend(qcrash.backends.GithubBackend(
            GITHUB_OWNER, GITHUB_REPO))
        qcrash.install_backend(qcrash.backends.EmailBackend(EMAIL, f'{NAME} {VERSION}'))

        # setup our own function to collect system info and application log
        qcrash.get_system_information = get_system_info

        # show report dialog manually
        qcrash.show_report_dialog(window_title=f"{NAME} 오류 제보",
                                  issue_title=f"{exctype} in {NAME} {VERSION}",
                                  issue_description=f"class {value}\n"
                                                    f"file {traceback.tb_frame.f_code.co_filename} "
                                                    f"line {traceback.tb_lineno}\n"
                                                    f"오류가 발생하기 전 상황을 입력해 주세요:")
