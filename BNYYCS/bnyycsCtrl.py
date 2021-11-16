
# 定义适用字符集
# 系统使用字符集，系统res、user、cmds等使用的字符集
CHRSET_SYS  = 'ascii';
# 系统期望的字符集，即对载入资源等str的解码方式
CHRSET_EXT = 'utf8';

def SET_CHRSET_EXT(val):
    global CHRSET_EXT;
    CHRSET_EXT = val;



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

CHRS_C0 = (
    b'\x00\x01\x02\x03\x04\x05\x06\x07'
    b'\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F'
    b'\x10\x11\x12\x13\x14\x15\x16\x17'
    b'\x18\x19\x1A\x1B\x1C\x1D\x1E\x1F'
);

CHRS_C1 = (
    b'\x80\x81\x82\x83\x84\x85\x86\x87'
    b'\x88\x89\x8A\x8B\x8C\x8D\x8E\x8F'
    b'\x90\x91\x92\x93\x94\x95\x96\x97'
    b'\x98\x99\x9A\x9B\x9C\x9D\x9E\x9F'
);

CHRS_NONPRT = CHRS_C0 + CHR_DEL + CHRS_C1;



# ASCII 打印字符
CHRS_PRINT = (
    b' !"#$%&\'()*+,-./'
    b'0123456789:;<=>?'
    b'@ABCDEFGHIJKLMNO'
    b'PQRSTUVWXYZ[\\]^_'
    b'`abcdefghijklmno'
    b'pqrstuvwxyz{|}~'
);
CHRS_EXT = (
    b'\x80\x81\x82\x83\x84\x85\x86\x87'
    b'\x88\x89\x8A\x8B\x8C\x8D\x8E\x8F'
    b'\x90\x91\x92\x93\x94\x95\x96\x97'
    b'\x98\x99\x9A\x9B\x9C\x9D\x9E\x9F'
    b'\xA0\xA1\xA2\xA3\xA4\xA5\xA6\xA7'
    b'\xA8\xA9\xAA\xAB\xAC\xAD\xAE\xAF'
    b'\xB0\xB1\xB2\xB3\xB4\xB5\xB6\xB7'
    b'\xB8\xB9\xBA\xBB\xBC\xBD\xBE\xBF'
    b'\xC0\xC1\xC2\xC3\xC4\xC5\xC6\xC7'
    b'\xC8\xC9\xCA\xCB\xCC\xCD\xCE\xCF'
    b'\xD0\xD1\xD2\xD3\xD4\xD5\xD6\xD7'
    b'\xD8\xD9\xDA\xDB\xDC\xDD\xDE\xDF'
    b'\xE0\xE1\xE2\xE3\xE4\xE5\xE6\xE7'
    b'\xE8\xE9\xEA\xEB\xEC\xED\xEE\xEF'
    b'\xF0\xF1\xF2\xF3\xF4\xF5\xF6\xF7'
    b'\xF8\xF9\xFA\xFB\xFC\xFD\xFE\xFF'
);



# 一般控制字符
CHR_RIS             = CHR_ESC + b'c';
CHR_CRLF            = CHR_CR + CHR_LF;
CHR_CLR             = CHR_RIS;
CHRS_ESC_END        = b'@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_';
CHRS_RETURN         = (b'\r\n', b'\r', b'\n');



# 输入控制字符
CHR_KEY_UP          = b'\x1b[A';
CHR_KEY_DOWN        = b'\x1b[B';
CHR_KEY_LEFT        = b'\x1b[D';
CHR_KEY_RIGHT       = b'\x1b[C';

CHR_KEY_BS          = b'\x08';
CHR_KEY_TAB         = b'\x09';
CHR_KEY_SP          = b'\x20';
CHR_KEY_DEL         = b'\x7f';

CHR_KEY_HOME        = b'\x1b[1~';
CHR_KEY_END         = b'\x1b[4~';
CHR_KEY_PGUP        = b'\x1b[5~';
CHR_KEY_PGDN        = b'\x1b[6~';
CHR_KEY_INS         = b'\x1b[2~';

CHR_KEY_F1          = b'\x1b[11~';
CHR_KEY_F2          = b'\x1b[12~';
CHR_KEY_F3          = b'\x1b[13~';
CHR_KEY_F4          = b'\x1b[14~';
CHR_KEY_F5          = b'\x1b[15~';
CHR_KEY_F6          = b'\x1b[16~';

CHR_KEY_F7          = b'\x1b[18~';
CHR_KEY_F8          = b'\x1b[19~';
CHR_KEY_F9          = b'\x1b[20~';
CHR_KEY_F10         = b'\x1b[21~';
CHR_KEY_F11         = b'\x1b[23~';
CHR_KEY_F12         = b'\x1b[24~';

CHR_KEY_ESC         = b'\x1B';



# CSI 控制字符
CHR_CSI_START       = CHR_ESC + b'[';
CHRS_CSI_MID        = b' !"#$%&\'()*+,-./';
CHRS_CSI_PARAM      = b'0123456789:;<=>?';
CHRS_CSI_END        = b'@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~';

CHR_CSI_CUU         = CHR_CSI_START + b'A';
CHR_CSI_CUD         = CHR_CSI_START + b'B';
CHR_CSI_CUF         = CHR_CSI_START + b'C';
CHR_CSI_CUB         = CHR_CSI_START + b'D';
CHR_CSI_CUP         = CHR_CSI_START + b'H';
CHR_CSI_HVP         = CHR_CSI_START + b'f';
CHR_CSI_SGR         = CHR_CSI_START + b'm';

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

def CHRf_CSI_CUMOV(y, x):
    assert abs(y) < 32768;
    assert abs(x) < 32768;
    return (b'' if y == 0 else CHRf_CSI_CUD(y) if y > 0 else CHRf_CSI_CUU(-y)) + (b'' if x == 0 else CHRf_CSI_CUF(x) if x > 0 else CHRf_CSI_CUB(-x));

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



# 字体
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


# 常用字体
def CHRf_T(*args):
    return CHR_CSI_START + b';'.join([bytes(str(arg),'ascii') for arg in args]) + b'm';

T_BOLD          = 1;
T_UNDLIN        = 4;
T_BLINK         = 5;
T_REVERS        = 7;

T_DEBOLD        = 22;
T_DEUNDLIN      = 24;
T_DEBLINK       = 25;
T_DEREVERS      = 27;

T_BLACK             = 30;
T_RED               = 31;
T_GREEN             = 32;
T_YELLO             = 33;
T_BLUE              = 34;
T_MAGEN             = 35;
T_CYAN              = 36;
T_WHITE             = 37;
T_LBLACK            = 90;
T_LRED              = 91;
T_LGREEN            = 92;
T_LYELLO            = 93;
T_LBLUE             = 94;
T_LMAGEN            = 95;
T_LCYAN             = 96;
T_LWHITE            = 97;
T_RST               = 39;

T_BBLACK            = 40;
T_BRED              = 41;
T_BGREEN            = 42;
T_BYELLO            = 43;
T_BBLUE             = 44;
T_BMAGEN            = 45;
T_BCYAN             = 46;
T_BWHITE            = 47;
T_BLBLACK           = 100;
T_BLRED             = 101;
T_BLGREEN           = 102;
T_BLYELLO           = 103;
T_BLBLUE            = 104;
T_BLMAGEN           = 105;
T_BLCYAN            = 106;
T_BLWHITE           = 107;
T_BRST              = 49;

class InputQueue:
    def __init__(self) -> None:
        self._input = b'';
        return;
    
    def push(self, inp):
        self._input += inp;
        return;
    
    def pop(self):
        if len(self._input) > 0:
            if len(self._input) > 1 and self._input[:1] == CHR_ESC:
                _i = 0;
                if len(self._input) > 1 and self._input[:2] == CHR_RIS:
                    _i = 1;
                elif len(self._input) > 1 and self._input[1:2] in CHRS_ESC_END:
                    _i = 1;
                    if _i < len(self._input) and self._input[:2] == CHR_CSI_START:
                        _i = 2;
                        while _i < len(self._input) and self._input[_i:_i+1] not in CHRS_CSI_END:
                            _i += 1;
                if _i < len(self._input):
                    _chr, self._input = self._input[:_i+1], self._input[_i+1:];
                    return _chr;
                else:
                    return b'';
            elif len(self._input) == 1 and self._input[:1] == CHR_ESC:
                _chr, self._input = self._input[:1], self._input[1:];
                return _chr;
            elif self._input[:1] in CHRS_RETURN:
                if len(self._input) > 1:
                    if self._input[:2] == CHR_CRLF:
                        _chr, self._input = self._input[:2], self._input[2:];
                        return _chr;
                    else:
                        _chr, self._input = self._input[:1], self._input[1:];
                        return _chr;
                else:
                    _chr, self._input = self._input[:1], self._input[1:];
                    return _chr;
            else:
                _chr, self._input = self._input[:1], self._input[1:];
                return _chr;
        else:
            return b'';
    
    def pops(self):
        _chr = self.pop();
        while _chr:
            yield _chr;
            _chr = self.pop();
        return;
