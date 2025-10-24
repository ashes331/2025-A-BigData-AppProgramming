import platform

from matplotlib import pyplot as plt
from matplotlib import rc

#현재 파이썬이 실행되는 플랫폼 확인

def is_windows_platform():
    return platform.system() == 'Windows'

def is_mac_platform():
    return platform.system() == 'Darwin'

def is_linux_platform():
    return platform.system() == 'Linux'

def get_font_name():
    if is_mac_platform():
        return 'AppleGothic'
    elif is_linux_platform():
        return 'linuxFont?'
    else:
        return 'Malgun Gothic'

def init_matplotlib():
    # 한글폰트 처리(깨짐처리)
    rc('font', family=get_font_name())
    plt.rcParams['axes.unicode_minus'] = False