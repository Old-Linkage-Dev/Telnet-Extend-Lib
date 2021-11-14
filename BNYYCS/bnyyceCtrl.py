
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
CHR_CSI_CUP = CHR_CSI_START + b'H';
CHR_CSI_HVP = CHR_CSI_START + b'f';
CHR_CSI_SGR = CHR_CSI_START + b'm';

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

def CHRf_CSI_SGR(*args):
    return CHR_CSI_START + b';'.join([bytes(str(arg),'ascii') for arg in args]) + b'm';



# RIS 控制字符
CHR_RIS = CHR_ESC + b'c';



# 其他
CHR_CRLF            = CHR_CR + CHR_LF;
CHR_CLR             = CHR_RIS;

CHR_T_RST           = CHR_CSI_SGR;

CHR_T_BOLD          = CHRf_CSI_SGR(1);
CHR_T_LIGHT         = CHRf_CSI_SGR(2);
CHR_T_ITALIC        = CHRf_CSI_SGR(3);
CHR_T_UNDLIN        = CHRf_CSI_SGR(4);
CHR_T_BLINK         = CHRf_CSI_SGR(5);
CHR_T_BLINKS        = CHRf_CSI_SGR(6);
CHR_T_REVERS        = CHRf_CSI_SGR(7);
CHR_T_HIDDEN        = CHRf_CSI_SGR(8);
CHR_T_DELETE        = CHRf_CSI_SGR(9);

CHR_T_FONT0         = CHRf_CSI_SGR(10);
CHR_T_FONT1         = CHRf_CSI_SGR(11);
CHR_T_FONT2         = CHRf_CSI_SGR(12);
CHR_T_FONT3         = CHRf_CSI_SGR(13);
CHR_T_FONT4         = CHRf_CSI_SGR(14);
CHR_T_FONT5         = CHRf_CSI_SGR(15);
CHR_T_FONT6         = CHRf_CSI_SGR(16);
CHR_T_FONT7         = CHRf_CSI_SGR(17);
CHR_T_FONT8         = CHRf_CSI_SGR(18);
CHR_T_FONT9         = CHRf_CSI_SGR(19);

CHR_T_FRAKT         = CHRf_CSI_SGR(20);
CHR_T_HEAVY         = CHRf_CSI_SGR(21);
CHR_T_NORMW         = CHRf_CSI_SGR(22);
CHR_T_NORMF         = CHRf_CSI_SGR(23);

CHR_T_DEUNDLIN      = CHRf_CSI_SGR(24);
CHR_T_DEBLINK       = CHRf_CSI_SGR(25);
CHR_T_DEREVERS      = CHRf_CSI_SGR(27);
CHR_T_DEHIDDEN      = CHRf_CSI_SGR(28);
CHR_T_DEDELETE      = CHRf_CSI_SGR(29);

CHR_T_FC_BLACK      = CHRf_CSI_SGR(30);
CHR_T_FC_RED        = CHRf_CSI_SGR(31);
CHR_T_FC_GREEN      = CHRf_CSI_SGR(32);
CHR_T_FC_YELLO      = CHRf_CSI_SGR(33);
CHR_T_FC_BLUE       = CHRf_CSI_SGR(34);
CHR_T_FC_MAGEN      = CHRf_CSI_SGR(35);
CHR_T_FC_CYAN       = CHRf_CSI_SGR(36);
CHR_T_FC_WHITE      = CHRf_CSI_SGR(37);
CHR_T_FC_LBLACK     = CHRf_CSI_SGR(90);
CHR_T_FC_LRED       = CHRf_CSI_SGR(91);
CHR_T_FC_LGREEN     = CHRf_CSI_SGR(92);
CHR_T_FC_LYELLO     = CHRf_CSI_SGR(93);
CHR_T_FC_LBLUE      = CHRf_CSI_SGR(94);
CHR_T_FC_LMAGEN     = CHRf_CSI_SGR(95);
CHR_T_FC_LCYAN      = CHRf_CSI_SGR(96);
CHR_T_FC_LWHITE     = CHRf_CSI_SGR(97);
CHR_T_FC_RST        = CHRf_CSI_SGR(39);

CHR_T_BC_BLACK      = CHRf_CSI_SGR(40);
CHR_T_BC_RED        = CHRf_CSI_SGR(41);
CHR_T_BC_GREEN      = CHRf_CSI_SGR(42);
CHR_T_BC_YELLO      = CHRf_CSI_SGR(43);
CHR_T_BC_BLUE       = CHRf_CSI_SGR(44);
CHR_T_BC_MAGEN      = CHRf_CSI_SGR(45);
CHR_T_BC_CYAN       = CHRf_CSI_SGR(46);
CHR_T_BC_WHITE      = CHRf_CSI_SGR(47);
CHR_T_BC_LBLACK     = CHRf_CSI_SGR(100);
CHR_T_BC_LRED       = CHRf_CSI_SGR(101);
CHR_T_BC_LGREEN     = CHRf_CSI_SGR(102);
CHR_T_BC_LYELLO     = CHRf_CSI_SGR(103);
CHR_T_BC_LBLUE      = CHRf_CSI_SGR(104);
CHR_T_BC_LMAGEN     = CHRf_CSI_SGR(105);
CHR_T_BC_LCYAN      = CHRf_CSI_SGR(106);
CHR_T_BC_LWHITE     = CHRf_CSI_SGR(107);
CHR_T_BC_RST        = CHRf_CSI_SGR(49);

CHR_T_FRAMED        = CHRf_CSI_SGR(50);
CHR_T_ENCIRC        = CHRf_CSI_SGR(51);
CHR_T_UPLIN         = CHRf_CSI_SGR(52);
CHR_T_DEFRMENC      = CHRf_CSI_SGR(53);
CHR_T_DEUPLIN       = CHRf_CSI_SGR(54);
