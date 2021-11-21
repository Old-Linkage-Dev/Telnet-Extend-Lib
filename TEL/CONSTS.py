
# -*- coding: UTF-8 -*-

# 记录常用常数的接口文件；



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





bCHR_NONE            = b'';
bCHR_NUL             = b'\x00';
bCHR_SOH             = b'\x01';
bCHR_STX             = b'\x02';
bCHR_ETX             = b'\x03';
bCHR_EOT             = b'\x04';
bCHR_ENQ             = b'\x05';
bCHR_ACK             = b'\x06';
bCHR_BEL             = b'\x07';
bCHR_BS              = b'\x08';
bCHR_TAB             = b'\x09';
bCHR_LF              = b'\x0A';
bCHR_VT              = b'\x0B';
bCHR_FF              = b'\x0C';
bCHR_CR              = b'\x0D';
bCHR_SO              = b'\x0E';
bCHR_SI              = b'\x0F';
bCHR_DLE             = b'\x10';
bCHR_DC1             = b'\x11';
bCHR_DC2             = b'\x12';
bCHR_DC3             = b'\x13';
bCHR_DC4             = b'\x14';
bCHR_NAK             = b'\x15';
bCHR_SYN             = b'\x16';
bCHR_ETB             = b'\x17';
bCHR_CAN             = b'\x18';
bCHR_EM              = b'\x19';
bCHR_SUB             = b'\x1A';
bCHR_ESC             = b'\x1B';
bCHR_FS              = b'\x1C';
bCHR_GS              = b'\x1D';
bCHR_RS              = b'\x1E';
bCHR_US              = b'\x1F';
bCHR_DEL             = b'\x7F';

bCHRS_C0 = (
    b'\x00\x01\x02\x03\x04\x05\x06\x07'
    b'\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F'
    b'\x10\x11\x12\x13\x14\x15\x16\x17'
    b'\x18\x19\x1A\x1B\x1C\x1D\x1E\x1F'
);

bCHRS_C1 = (
    b'\x80\x81\x82\x83\x84\x85\x86\x87'
    b'\x88\x89\x8A\x8B\x8C\x8D\x8E\x8F'
    b'\x90\x91\x92\x93\x94\x95\x96\x97'
    b'\x98\x99\x9A\x9B\x9C\x9D\x9E\x9F'
);

bCHRS_NONPRT = bCHRS_C0 + bCHR_DEL + bCHRS_C1;

bCHRS_PRINT = (
    b' !"#$%&\'()*+,-./'
    b'0123456789:;<=>?'
    b'@ABCDEFGHIJKLMNO'
    b'PQRSTUVWXYZ[\\]^_'
    b'`abcdefghijklmno'
    b'pqrstuvwxyz{|}~'
);

bCHRS_EXT = (
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

bCHR_CSI_START       = bCHR_ESC + b'[';
bCHRS_CSI_MID        = b' !"#$%&\'()*+,-./';
bCHRS_CSI_PARAM      = b'0123456789:;<=>?';
bCHRS_CSI_END        = b'@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~';

bCHR_CRLF            = bCHR_CR + bCHR_LF;
bCHR_CRNUL           = bCHR_CR + bCHR_NUL;

bCHRS_ESC_END        = b'@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_';
bCHRS_RETURN         = (bCHR_CRLF, bCHR_CRNUL, bCHR_CR, bCHR_LF);



CHR_KEY_UP          = '\x1b[A';
CHR_KEY_DOWN        = '\x1b[B';
CHR_KEY_LEFT        = '\x1b[D';
CHR_KEY_RIGHT       = '\x1b[C';

CHR_KEY_BS          = '\x08';
CHR_KEY_TAB         = '\x09';
CHR_KEY_SP          = '\x20';
CHR_KEY_DEL         = '\x7f';

CHR_KEY_HOME        = '\x1b[1~';
CHR_KEY_END         = '\x1b[4~';
CHR_KEY_PGUP        = '\x1b[5~';
CHR_KEY_PGDN        = '\x1b[6~';
CHR_KEY_INS         = '\x1b[2~';

CHR_KEY_F1          = '\x1b[11~';
CHR_KEY_F2          = '\x1b[12~';
CHR_KEY_F3          = '\x1b[13~';
CHR_KEY_F4          = '\x1b[14~';
CHR_KEY_F5          = '\x1b[15~';
CHR_KEY_F6          = '\x1b[16~';

CHR_KEY_F7          = '\x1b[18~';
CHR_KEY_F8          = '\x1b[19~';
CHR_KEY_F9          = '\x1b[20~';
CHR_KEY_F10         = '\x1b[21~';
CHR_KEY_F11         = '\x1b[23~';
CHR_KEY_F12         = '\x1b[24~';

CHR_KEY_ESC         = '\x1B';
