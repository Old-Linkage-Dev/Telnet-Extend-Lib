
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
CHR_CSI_ED0         = CHR_CSI_START + b'0J';
CHR_CSI_ED1         = CHR_CSI_START + b'1J';
CHR_CSI_ED2         = CHR_CSI_START + b'2J';
CHR_CSI_HVP         = CHR_CSI_START + b'f';
CHR_CSI_SGR         = CHR_CSI_START + b'm';
CHR_CSI_SCP         = CHR_CSI_START + b's';
CHR_CSI_RCP         = CHR_CSI_START + b'u';

def CHRf_CSI_CUU(n):
    assert 0 < n < 32768;
    return CHR_CSI_START + bytes(str(n), CHRSET_SYS) + b'A';

def CHRf_CSI_CUD(n):
    assert 0 < n < 32768;
    return CHR_CSI_START + bytes(str(n), CHRSET_SYS) + b'B';

def CHRf_CSI_CUF(n):
    assert 0 < n < 32768;
    return CHR_CSI_START + bytes(str(n), CHRSET_SYS) + b'C';

def CHRf_CSI_CUB(n):
    assert 0 < n < 32768;
    return CHR_CSI_START + bytes(str(n), CHRSET_SYS) + b'D';

def CHRf_CSI_CUMOV(y, x):
    assert abs(y) < 32768;
    assert abs(x) < 32768;
    return (b'' if y == 0 else CHRf_CSI_CUD(y) if y > 0 else CHRf_CSI_CUU(-y)) + (b'' if x == 0 else CHRf_CSI_CUF(x) if x > 0 else CHRf_CSI_CUB(-x));

def CHRf_CSI_CHA(y):
    assert 0 < y < 32768;
    return CHR_CSI_START + bytes(str(y), CHRSET_SYS) + b'G';

def CHRf_CSI_VPA(x):
    assert 0 < x < 32768;
    return CHR_CSI_START + bytes(str(x), CHRSET_SYS) + b'd';

def CHRf_CSI_CUP(y, x):
    assert 0 < y < 32768;
    assert 0 < x < 32768;
    return CHR_CSI_START + bytes(str(y), CHRSET_SYS) + b';' + bytes(str(x), CHRSET_SYS) + b'H';

def CHRf_CSI_HVP(y, x):
    assert 0 < y < 32768;
    assert 0 < x < 32768;
    return CHR_CSI_START + bytes(str(y), CHRSET_SYS) + b';' + bytes(str(x), CHRSET_SYS) + b'f';

def CHRf_CSI_SGR(*args):
    return CHR_CSI_START + b';'.join([bytes(str(arg), CHRSET_SYS) for arg in args]) + b'm';



# 一般控制字符
CHR_RIS             = CHR_ESC + b'c';
CHR_CRLF            = CHR_CR + CHR_LF;
CHR_CRNUL           = CHR_CR + CHR_NUL;
CHR_CLR             = CHR_RIS + CHR_CSI_CUP + CHR_CSI_ED2;
CHRS_ESC_END        = b'@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_';
CHRS_RETURN         = (CHR_CRLF, CHR_CRNUL, CHR_CR, CHR_LF);



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
    return CHR_CSI_START + b';'.join([bytes(str(arg), CHRSET_SYS) for arg in args]) + b'm';

T_BOLD              = 1;
T_UNDLIN            = 4;
T_BLINK             = 5;
T_REVERS            = 7;

T_DEBOLD            = 22;
T_DEUNDLIN          = 24;
T_DEBLINK           = 25;
T_DEREVERS          = 27;

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



# Telnet 控制字符
TEL_NULL            = b'\x00';
TEL_EOF             = b'\xEC';
TEL_SUSP            = b'\xED';
TEL_ABORT           = b'\xEE';
TEL_EOR             = b'\xEF';
TEL_SE              = b'\xF0';
TEL_NOP             = b'\xF1';
TEL_DM              = b'\xF2';
TEL_BRK             = b'\xF3';
TEL_IP              = b'\xF4';
TEL_AO              = b'\xF5';
TEL_AYT             = b'\xF6';
TEL_EC              = b'\xF7';
TEL_EL              = b'\xF8';
TEL_GA              = b'\xF9';
TEL_SB              = b'\xFA';
TEL_WILL            = b'\xFB';
TEL_WONT            = b'\xFC';
TEL_DO              = b'\xFD';
TEL_DONT            = b'\xFE';
TEL_xFF             = b'\xFF';
TEL_IAC             = b'\xFF';

# RFC 656
TEL_OP_TB           = b'\x00';
# RFC 857
TEL_OP_ECHO         = b'\x01';
# RFC 858
TEL_OP_SPRGA        = b'\x03';
# RFC 859
TEL_OP_STA          = b'\x05';
TEL_OP_STA_IS           = b'\x00';
TEL_OP_STA_SEND         = b'\x01';
# RFC 860
TEL_OP_TM           = b'\x06';
# RFC 884 930 1091
TEL_OP_TTYP         = b'\x18';
TEL_OP_TTYP_IS          = b'\x00';
TEL_OP_TTYP_SEND        = b'\x01';
# RFC 1073
TEL_OP_NAWS         = b'\x1F';
# RFC 884 930 1079
TEL_OP_TSPD         = b'\x20';
TEL_OP_TSPD_IS          = b'\x00';
TEL_OP_TSPD_SEND        = b'\x01';
# RFC 1080 1372
TEL_OP_TOGFC        = b'\x21';
TEL_OP_TOGFC_OFF        = b'\x21';
TEL_OP_TOGFC_ON         = b'\x21';
TEL_OP_TOGFC_RSTANY     = b'\x21';
TEL_OP_TOGFC_RSTXON     = b'\x21';
# RFC 1116 1184
TEL_OP_LNMOD        = b'\x22';
TEL_OP_LNMOD_MODE       = b'\x01';
TEL_OP_LNMOD_EDIT       = b'\x01';
TEL_OP_LNMOD_TRAPSIG        = b'\x02';
TEL_OP_LNMOD_MODEACK        = b'\x04';
TEL_OP_LNMOD_SOFTTAB        = b'\x08';
TEL_OP_LNMOD_LITECHO        = b'\x10';
TEL_OP_LNMOD_FWDMSK     = b'\x02';
TEL_OP_LNMOD_SLC        = b'\x03';
TEL_OP_LNMOD_SLC_SYNCH      = b'\x01';
TEL_OP_LNMOD_SLC_BRK        = b'\x02';
TEL_OP_LNMOD_SLC_IP         = b'\x03';
TEL_OP_LNMOD_SLC_AO         = b'\x04';
TEL_OP_LNMOD_SLC_AYT        = b'\x05';
TEL_OP_LNMOD_SLC_EOR        = b'\x06';
TEL_OP_LNMOD_SLC_ABORT      = b'\x07';
TEL_OP_LNMOD_SLC_EOF        = b'\x08';
TEL_OP_LNMOD_SLC_SUSP       = b'\x09';
TEL_OP_LNMOD_SLC_EC         = b'\x0A';
TEL_OP_LNMOD_SLC_EL         = b'\x0B';
TEL_OP_LNMOD_SLC_EW         = b'\x0C';
TEL_OP_LNMOD_SLC_RP         = b'\x0D';
TEL_OP_LNMOD_SLC_LNEXT      = b'\x0E';
TEL_OP_LNMOD_SLC_XON        = b'\x0F';
TEL_OP_LNMOD_SLC_XOFF       = b'\x10';
TEL_OP_LNMOD_SLC_FORW1      = b'\x11';
TEL_OP_LNMOD_SLC_FORW2      = b'\x12';
TEL_OP_LNMOD_SLC_MCL        = b'\x13';
TEL_OP_LNMOD_SLC_MCR        = b'\x14';
TEL_OP_LNMOD_SLC_MCWL       = b'\x15';
TEL_OP_LNMOD_SLC_MCWR       = b'\x16';
TEL_OP_LNMOD_SLC_MCBOL      = b'\x17';
TEL_OP_LNMOD_SLC_MCEOL      = b'\x18';
TEL_OP_LNMOD_SLC_INSRT      = b'\x19';
TEL_OP_LNMOD_SLC_OVER       = b'\x1A';
TEL_OP_LNMOD_SLC_ECR        = b'\x1B';
TEL_OP_LNMOD_SLC_EWR        = b'\x1C';
TEL_OP_LNMOD_SLC_EBOL       = b'\x1D';
TEL_OP_LNMOD_SLC_EEOL       = b'\x1E';
TEL_OP_LNMOD_SLC_DEFAUL     = b'\x03';
TEL_OP_LNMOD_SLC_VALUE      = b'\x02';
TEL_OP_LNMOD_SLC_CNTCHG     = b'\x01';
TEL_OP_LNMOD_SLC_NOSPRT     = b'\x00';
TEL_OP_LNMOD_SLC_LVLBIT     = b'\x03';
TEL_OP_LNMOD_SLC_ACK        = b'\x80';
TEL_OP_LNMOD_SLC_FLSIN      = b'\x40';
TEL_OP_LNMOD_SLC_FLSOUT     = b'\x20';
TEL_OP_LNMOD_EOF        = b'\xEC';
TEL_OP_LNMOD_SUSP       = b'\xED';
TEL_OP_LNMOD_ABORT      = b'\xEE';
# RFC 1408 1517
TEL_OP_ENVIRON      = b'\x24';
TEL_OP_ENVIRON_IS       = b'\x00';
TEL_OP_ENVIRON_SEND     = b'\x01';
TEL_OP_ENVIRON_INFO     = b'\x02';
TEL_OP_ENVIRON_VAR      = b'\x00';
TEL_OP_ENVIRON_VALU     = b'\x01';
TEL_OP_ENVIRON_ESC      = b'\x02';
TEL_OP_ENVIRON_USEV     = b'\x03';
# RFC 748 you know
TEL_OP_RANDLOS      = b'\x100';
# RFC 1097 you know
TEL_OP_SUBLIMMSG    = b'\x101';

TEL_CMD_SE          = TEL_IAC + TEL_SE;
TEL_CMD_NOP         = TEL_IAC + TEL_NOP;
TEL_CMD_DM          = TEL_IAC + TEL_DM;
TEL_CMD_BRK         = TEL_IAC + TEL_BRK;
TEL_CMD_IP          = TEL_IAC + TEL_IP;
TEL_CMD_AO          = TEL_IAC + TEL_AO;
TEL_CMD_AYT         = TEL_IAC + TEL_AYT;
TEL_CMD_EC          = TEL_IAC + TEL_EC;
TEL_CMD_EL          = TEL_IAC + TEL_EL;
TEL_CMD_GA          = TEL_IAC + TEL_GA;
TEL_CMD_SB          = TEL_IAC + TEL_SB;
TEL_CMD_WILL        = TEL_IAC + TEL_WILL;
TEL_CMD_WONT        = TEL_IAC + TEL_WONT;
TEL_CMD_DO          = TEL_IAC + TEL_DO;
TEL_CMD_DONT        = TEL_IAC + TEL_DONT;
TEL_CMD_xFF         = TEL_IAC + TEL_xFF;

def TELf_CMD(cmd):
    assert type(cmd) == bytes;
    return TEL_IAC + cmd;

def TELf_WILL(cmd):
    assert type(cmd) == bytes;
    return TEL_CMD_WILL + cmd;

def TELf_WONT(cmd):
    assert type(cmd) == bytes;
    return TEL_CMD_WONT + cmd;

def TELf_DO(cmd):
    assert type(cmd) == bytes;
    return TEL_CMD_DO + cmd;

def TELf_DONT(cmd):
    assert type(cmd) == bytes;
    return TEL_CMD_DONT + cmd;

def TELf_SB(cmd, *args):
    assert type(cmd) == bytes;
    _ret = TEL_IAC + TEL_SB + cmd;
    for _val in args:
        assert type(_val) == bytes;
        _ret += _val;
    _ret += TEL_IAC + TEL_SE;

TELS_OPFORE         = (TEL_CMD_WILL, TEL_CMD_WONT, TEL_CMD_DO, TEL_CMD_DONT);
TELS_SUBOPLEN       = {
    TEL_IAC + TEL_SB + TEL_OP_NAWS      : 3 + 4 + 2,
    TEL_IAC + TEL_SB + TEL_OP_STA       : -1,
    TEL_IAC + TEL_SB + TEL_OP_TTYP      : -1,
    TEL_IAC + TEL_SB + TEL_OP_TSPD      : -1,
    TEL_IAC + TEL_SB + TEL_OP_TOGFC     : -1,
    TEL_IAC + TEL_SB + TEL_OP_LNMOD     : -1,
    TEL_IAC + TEL_SB + TEL_OP_ENVIRON   : -1,
};







# InputQueue的基类
class InputQueue:
    def __init__(self) -> None:
        self._input = b'';
        return;
    
    def push(self, inp):
        self._input += inp;
        return;
    
    def pop(self):
        _ret = self._input[:1] if len(self._input) >= 1 else b'';
        return b'';
    
    def pops(self):
        _chr = self.pop();
        while _chr:
            yield _chr;
            _chr = self.pop();
        return;



# 用于Telnet接到的数据的重整的类
class TelnetInputQueue(InputQueue):
    def __init__(self) -> None:
        self._input = b'';
        return;
    
    def push(self, inp):
        self._input += inp;
        return;
    
    def popchar(self, l = 1):
        if len(self._input) < l:
            return b'';
        else:
            _chr, self._input = self._input[:l], self._input[l:];
            return _chr;

    def poptelcmd(self):
        if self._input[:1] != TEL_IAC:
            return b'';
        if len(self._input) <= 1:
            return b'';
        else:
            if self._input[:2] in TELS_OPFORE and len(self._input) < 3:
                return b'';
            elif self._input[:2] in TELS_OPFORE and len(self._input) >= 3:
                return self.popchar(3);
            elif self._input[:2] == TEL_CMD_SB and len(self._input) < 5:
                return b'';
            elif self._input[:2] == TEL_CMD_SB and len(self._input) >= 5:
                _sublen = TELS_SUBOPLEN[self._input[:3]] if self._input[:3] in TELS_SUBOPLEN else -1;
                if _sublen == -1:
                    _i = 3;
                    while _i + 1 < len(self._input) and self._input[_i : _i + 2] != TEL_CMD_SE:
                        _i += 1;
                    return self.popchar(_i + 2);
                elif len(self._input) < _sublen:
                    return b'';
                elif len(self._input) >= _sublen and self._input[_sublen - 2 : _sublen] == TEL_CMD_SE:
                    return self.popchar(_sublen);
                else:
                    return self.popchar(3);
            else:
                return self.popchar(2);
    
    def popesc(self):
        if self._input[:1] != CHR_ESC:
            return b'';
        if len(self._input) == 0:
            return b'';
        elif len(self._input) == 1:
            return self.popchar();
        else:
            if self._input[:2] == CHR_RIS:
                return self.popchar(2);
            elif self._input[1:2] not in CHRS_ESC_END:
                return self.popchar();
            elif self._input[1:2] in CHRS_ESC_END and self._input[:2] != CHR_CSI_START:
                return self.popchar(2);
            elif self._input[1:2] in CHRS_ESC_END and self._input[:2] == CHR_CSI_START:
                _i = 2;
                while _i < len(self._input) and self._input[_i:_i+1] not in CHRS_CSI_END:
                    _i += 1;
                return self.popchar(_i + 1);
    
    def popreturn(self):
        if self._input[:1] not in CHRS_RETURN:
            return b'';
        if len(self._input) == 0:
            return b'';
        elif len(self._input) == 1:
            return self.popchar();
        else:
            if self._input[:2] == CHR_CRLF:
                return self.popchar(2);
            elif self._input[:2] == CHR_CRNUL:
                # To deal with the CR NUL defined in rfc854 page 11.
                return self.popchar(2);
            else:
                return self.popchar();

    def pop(self):
        if len(self._input) == 0:
            return b'';
        elif self._input[:1] == TEL_IAC:
            return self.poptelcmd();
        elif self._input[:1] == CHR_ESC:
            return self.popesc();
        elif self._input[:1] in CHRS_RETURN:
            return self.popreturn();
        else:
            return self.popchar();



class TelnetReqWaitStack:
    def __init__(self) -> None:
        self.dowaiting = {};
        self.wiwaiting = {};
        return;
    
    def waiting(self, cmd):
        assert type(cmd) == bytes;
        assert len(cmd) == 3;
        assert cmd[:2] in TELS_OPFORE;
        if cmd[:2] in (TEL_CMD_WILL, TEL_CMD_WONT):
            _in = cmd[2:3] in self.dowaiting;
            _ret = _in and self.dowaiting[cmd[2:3]] > 0;
            if _in:
                self.dowaiting[cmd[2:3]] -= 1;
            return _ret;
        elif cmd[:2] in (TEL_CMD_DO, TEL_CMD_DONT):
            _in = cmd[2:3] in self.wiwaiting;
            _ret = _in and self.wiwaiting[cmd[2:3]] > 0;
            if _in:
                self.dowaiting[cmd[2:3]] -= 1;
            return _ret;
    
    def addwait(self, cmd):
        assert type(cmd) == bytes;
        assert len(cmd) == 3;
        assert cmd[:2] in TELS_OPFORE;
        if cmd[:2] in (TEL_CMD_WILL, TEL_CMD_WONT):
            _in = cmd[2:3] in self.wiwaiting;
            if _in:
                self.wiwaiting[cmd[2:3]] += 1;
            else:
                self.wiwaiting[cmd[2:3]] = 1;
        elif cmd[:2] in (TEL_CMD_DO, TEL_CMD_DONT):
            _in = cmd[2:3] in self.dowaiting;
            if _in:
                self.dowaiting[cmd[2:3]] += 1;
            else:
                self.dowaiting[cmd[2:3]] = 1;
        return;
