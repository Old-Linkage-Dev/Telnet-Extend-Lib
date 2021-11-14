
# ASCII 非打印字符
CHR_NONE    = b'';
CHR_NUL     = b'\x00';
CHR_SOH     = b'\x01';
CHR_STX     = b'\x02';
CHR_ETX     = b'\x03';
CHR_EOT     = b'\x04';
CHR_ENQ     = b'\x05';
CHR_ACK     = b'\x06';
CHR_BEL     = b'\x07';
CHR_BS      = b'\x08';
CHR_TAB     = b'\x09';
CHR_LF      = b'\x0A';
CHR_VT      = b'\x0B';
CHR_FF      = b'\x0C';
CHR_CR      = b'\x0D';
CHR_SO      = b'\x0E';
CHR_SI      = b'\x0F';
CHR_DLE     = b'\x10';
CHR_DC1     = b'\x11';
CHR_DC2     = b'\x12';
CHR_DC3     = b'\x13';
CHR_DC4     = b'\x14';
CHR_NAK     = b'\x15';
CHR_SYN     = b'\x16';
CHR_ETB     = b'\x17';
CHR_CAN     = b'\x18';
CHR_EM      = b'\x19';
CHR_SUB     = b'\x1A';
CHR_ESC     = b'\x1B';
CHR_FS      = b'\x1C';
CHR_GS      = b'\x1D';
CHR_RS      = b'\x1E';
CHR_US      = b'\x1F';
CHR_DEL     = b'\x7F';



# CSI 控制字符
CHR_CSI_START = CHR_ESC + b'[';
CHRS_CSI_MID = b' !"#$%&\'()*+,-./';
CHRS_CSI_PARAM = b'0123456789:;<=>?';
CHRS_CSI_FIN = b'@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~';

CHR_CSI_CUU = CHR_CSI_START + b'A';
CHR_CSI_CUD = CHR_CSI_START + b'B';
CHR_CSI_CUF = CHR_CSI_START + b'C';
CHR_CSI_CUB = CHR_CSI_START + b'D';

def CHRf_CSI_CUU(n):
    assert 0 < n < 32768;
    return CHR_CSI_START + bytes(str(n),'ascii') + b'A';

def CHRf_CSI_CUD(n):
    assert 0 < n < 32768;
    return CHR_CSI_START + bytes(str(n),'ascii') + b'B';

def CHRf_CSI_CUF(n):
    assert 0 < n < 32768;
    return CHR_CSI_START + bytes(str(n),'ascii') + b'C';

def CHRf_CSI_CUB(n):
    assert 0 < n < 32768;
    return CHR_CSI_START + bytes(str(n),'ascii') + b'D';

def CHRf_CSI_CHA(y):
    assert 0 < y < 32768;
    return CHR_CSI_START + bytes(str(y),'ascii') + b'G';

def CHRf_CSI_VPA(x):
    assert 0 < x < 32768;
    return CHR_CSI_START + bytes(str(x),'ascii') + b'd';

def CHRf_CSI_CUP(y, x):
    assert 0 < y < 32768;
    assert 0 < x < 32768;
    return CHR_CSI_START + bytes(str(y),'ascii') + b';' + bytes(str(x),'ascii') + b'H';

def CHRf_CSI_HVP(y, x):
    assert 0 < y < 32768;
    assert 0 < x < 32768;
    return CHR_CSI_START + bytes(str(y),'ascii') + b';' + bytes(str(x),'ascii') + b'f';



# RIS 控制字符
CHR_RIS = CHR_ESC + b'c';



# 其他
CHR_CRLF = CHR_CR + CHR_LF;
CHR_CLR = CHR_RIS;
