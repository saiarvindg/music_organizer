import os
import mutagen
from metadata import clear_meta, change_meta

path = 'C:\\Users\\Solomon Kritz\\Desktop\\Wiz Khalifa'

#ONLY WORKS IF M4A
def get_album(path):
   audio = mutagen.File(path)
   return(audio["\xa9ART"][0])

#ONLY WORKS IF M4A
def get_artist(path):
   audio = mutagen.File(path)
   return audio["\xa9alb"][0]

def collapse():
   recreate(path, path)

def goDown(path, oldPath):
   for file in os.listdir(path):
      filePath = os.path.join(path,file)
      if os.path.isdir(filePath):
         goDown(filePath, path)
   for file in os.listdir(path):
      filePath = os.path.join(path,file)
      if(os.path.isdir(filePath)):
         os.rmdir(filePath)
      elif(path != oldPath):
         os.rename(filePath, os.path.join(oldPath, file))
         
def isMusicFile(filePath):
   exts = [".2SF", ".2SFLIB", ".3GA", ".4MP", ".5XB", ".5XE", ".5XS", ".669", ".6CM", ".8CM", ".8MED", ".8SVX", ".A2B", ".A2I", ".A2M", ".A2P", ".A2T", ".A2W", ".A52", ".AA", ".AA3", ".AAC", ".AAX", ".AB", ".ABC", ".ABM", ".AC3", ".ACD", ".ACD-BAK", ".ACD-ZIP", ".ACM", ".ACP", ".ACT", ".ADG", ".ADT", ".ADTS", ".ADV", ".AFC", ".AGM", ".AGR", ".AHX", ".AIF", ".AIFC", ".AIFF", ".AIMPPL", ".AIS", ".AKP", ".AL", ".ALAC", ".ALAW", ".ALC", ".ALL", ".ALS", ".AMF", ".AMR", ".AMS", ".AMS", ".AMXD", ".AMZ", ".ANG", ".AOB", ".APE", ".APF", ".APL", ".ARIA", ".ARIAX", ".ASD", ".ASE", ".AT3", ".ATRAC", ".AU", ".AU", ".AUD", ".AUP", ".AVASTSOUNDS", ".AVR", ".AWB", ".AXA", ".AY", ".B4S", ".BAND", ".BAP", ".BCS", ".BDD", ".BIDULE", ".BMML", ".BNK", ".BONK", ".BOX", ".BRSTM", ".BUN", ".BWF", ".BWG", ".BWW", ".C01", ".CAF", ".CAFF", ".CDA", ".CDDA", ".CDLX", ".CDO", ".CDR", ".CEL", ".CFA", ".CFXR", ".CGRP", ".CIDB", ".CKB", ".CKF", ".CMF", ".CONFORM", ".COPY", ".CPR", ".CPT", ".CSH", ".CTS", ".CWB", ".CWP", ".CWS", ".CWT", ".D00", ".D01", ".DCF", ".DCM", ".DCT", ".DDT", ".DEWF", ".DF2", ".DFC", ".DFF", ".DIG", ".DIG", ".DJR", ".DLS", ".DM", ".DMC", ".DMF", ".DMSA", ".DMSE", ".DRA", ".DRG", ".DS", ".DS2", ".DSF", ".DSM", ".DSP", ".DSS", ".DTM", ".DTS", ".DTSHD", ".DVF", ".DW", ".DWA", ".DWD", ".EAR", ".EFA", ".EFE", ".EFK", ".EFQ", ".EFS", ".EFV", ".EMD", ".EMP", ".EMX", ".EMY", ".EOP", ".ERB", ".ESPS", ".EVR", ".EXPRESSIONMAP", ".F2R", ".F32", ".F3R", ".F4A", ".F64", ".FAR", ".FDA", ".FDP", ".FEV", ".FFF", ".FLAC", ".FLM", ".FLP", ".FLP", ".FLS", ".FPA", ".FRG", ".FSB", ".FSC", ".FSM", ".FTI", ".FTM", ".FTM", ".FTMX", ".FZB", ".FZF", ".FZV", ".G721", ".G723", ".G726", ".GBPROJ", ".GBS", ".GIG", ".GIO", ".GIO", ".GM", ".GMC", ".GP5", ".GPBANK", ".GPK", ".GPX", ".GRO", ".GROOVE", ".GSF", ".GSFLIB", ".GSM", ".GSM", ".GYM", ".H0", ".H3B", ".H3E", ".H4B", ".H4E", ".H5B", ".H5E", ".H5S", ".HBB", ".HBE", ".HBS", ".HDP", ".HMA", ".HMI", ".HPS", ".HSB", ".IAA", ".ICS", ".IFF", ".IGP", ".IGR", ".IMF", ".IMP", ".INS", ".INS", ".INS", ".ISMA", ".IT", ".ITI", ".ITLS", ".ITS", ".JAM", ".JAM", ".JO", ".JO-7Z", ".K25", ".K26", ".KAR", ".KFN", ".KIN", ".KIT", ".KMP", ".KOZ", ".KOZ", ".KPL", ".KRZ", ".KSC", ".KSD", ".KSF", ".KSM", ".KT2", ".KT3", ".KTP", ".L", ".LA", ".LOF", ".LOGIC", ".LOGICX", ".LQT", ".LSO", ".LVP", ".LWV", ".M", ".M1A", ".M2", ".M3U", ".M3U8", ".M4A", ".M4B", ".M4P", ".M4R", ".MA1", ".MBR", ".MDC", ".MDL", ".MDR", ".MED", ".MGV", ".MID", ".MIDI", ".MINI2SF", ".MINIGSF", ".MININCSF", ".MINIPSF", ".MINIPSF2", ".MINIUSF", ".MKA", ".MLP", ".MMF", ".MMLP", ".MMM", ".MMP", ".MMP", ".MMPZ", ".MO3", ".MOD", ".MOGG", ".MP1", ".MP2", ".MP3", ".MP_", ".MPA", ".MPC", ".MPDP", ".MPGA", ".MPU", ".MSCX", ".MSCZ", ".MSV", ".MT2", ".MT9", ".MTE", ".MTF", ".MTI", ".MTM", ".MTP", ".MTS", ".MU3", ".MUI", ".MUS", ".MUS", ".MUS", ".MUSA", ".MUSX", ".MUX", ".MUX", ".MUZ", ".MWAND", ".MWS", ".MX3", ".MX4", ".MX5", ".MX5TEMPLATE", ".MXL", ".MXMF", ".MYR", ".MZP", ".NAP", ".NARRATIVE", ".NBS", ".NCW", ".NKB", ".NKC", ".NKI", ".NKM", ".NKS", ".NKX", ".NML", ".NMSV", ".NOTE", ".NPL", ".NRA", ".NRT", ".NSA", ".NSF", ".NST", ".NTN", ".NVF", ".NWC", ".OBW", ".ODM", ".OFR", ".OGA", ".OGG", ".OKT", ".OMA", ".OMF", ".OMG", ".OMX", ".OPUS", ".ORC", ".OTS", ".OVE", ".OVW", ".OVW", ".PAC", ".PANDORA", ".PAT", ".PBF", ".PCA", ".PCAST", ".PCG", ".PCM", ".PD", ".PEAK", ".PEK", ".PHO", ".PHY", ".PJUNOXL", ".PK", ".PKF", ".PLA", ".PLS", ".PLST", ".PLY", ".PMPL", ".PNA", ".PNO", ".PPC", ".PPCX", ".PRG", ".PRG", ".PSF", ".PSF1", ".PSF2", ".PSM", ".PSY", ".PTCOP", ".PTF", ".PTM", ".PTS", ".PTT", ".PTX", ".PTXT", ".PVC", ".Q1", ".Q2", ".QCP", ".R", ".R1M", ".RA", ".RAD", ".RAM", ".RAW", ".RAX", ".RBS", ".RBS", ".RCY", ".RECORD", ".REX", ".RFL", ".RGRP", ".RIP", ".RMF", ".RMI", ".RMJ", ".RMM", ".RMX", ".RNG", ".RNS", ".ROL", ".RSF", ".RSN", ".RSO", ".RTA", ".RTI", ".RTM", ".RTS", ".RVX", ".RX2", ".S3I", ".S3M", ".S3Z", ".SAF", ".SAM", ".SAP", ".SB", ".SBG", ".SBI", ".SBK", ".SC2", ".SCS11", ".SD", ".SD", ".SD2", ".SD2F", ".SDAT", ".SDII", ".SDS", ".SDT", ".SDX", ".SEG", ".SEQ", ".SES", ".SESX", ".SF", ".SF2", ".SFAP0", ".SFK", ".SFL", ".SFPACK", ".SFS", ".SFZ", ".SGP", ".SHN", ".SIB", ".SID", ".SLP", ".SLX", ".SMA", ".SMF", ".SMP", ".SMP", ".SMPX", ".SND", ".SND", ".SND", ".SNG", ".SNG", ".SNS", ".SNSF", ".SOU", ".SPH", ".SPPACK", ".SPRG", ".SPX", ".SSEQ", ".SSEQ", ".SSM", ".SSND", ".STAP", ".STH", ".STI", ".STM", ".STW", ".STX", ".STY", ".STY", ".SVD", ".SVQ", ".SVX", ".SW", ".SWA", ".SWAV", ".SXT", ".SYH", ".SYN", ".SYN", ".SYW", ".SYX", ".TAK", ".TAK", ".TD0", ".TFMX", ".TG", ".THX", ".TM2", ".TM8", ".TMC", ".TOC", ".TRAK", ".TSP", ".TTA", ".TUN", ".TXW", ".U", ".U8", ".UAX", ".UB", ".ULAW", ".ULT", ".ULW", ".UNI", ".USF", ".USFLIB", ".UST", ".UW", ".UWF", ".V2M", ".VAG", ".VAL", ".VAP", ".VB", ".VC3", ".VCE", ".VDJ", ".VGM", ".VGZ", ".VIP", ".VLC", ".VMD", ".VMF", ".VMF", ".VMO", ".VOC", ".VOI", ".VOX", ".VOXAL", ".VPL", ".VPM", ".VPW", ".VQF", ".VRF", ".VSQ", ".VSQX", ".VTX", ".VYF", ".W01", ".W64", ".WAND", ".WAV", ".WAV", ".WAVE", ".WAX", ".WEM", ".WFB", ".WFD", ".WFM", ".WFP", ".WMA", ".WOW", ".WPK", ".WPP", ".WPROJ", ".WRK", ".WTPL", ".WTPT", ".WUS", ".WUT", ".WV", ".WVC", ".WVE", ".WWU", ".WYZ", ".XA", ".XA", ".XBMML", ".XFS", ".XI", ".XM", ".XMF", ".XMI", ".XMS", ".XMU", ".XMZ", ".XP", ".XPF", ".XRNS", ".XSB", ".XSP", ".XSPF", ".XT", ".XWB", ".YM", ".YOOKOO", ".ZAB", ".ZGR", ".ZPA", ".ZPL", ".ZVD", ".ZVR"]
   name, extension = os.path.splitext(filePath)
   if (extension.upper() in exts):
       return True
   else:
      return False
   
def removeNonAudio(path):
   #LIST OF EXTS
   if (not isMusicFile(filePath)):
      os.remove(filePath)
   else:
      change_meta(filePath)
def dirEmpty(path):
   i = 0
   for file in os.listdir(path):
      i+=1
   if i == 0:
      return True
   else:
      return False
   
def recreate(path, root):
   for file in os.listdir(path):
      filePath = os.path.join(path,file)
      if os.path.isdir(filePath):
         recreate(filePath, root)
      elif isMusicFile(filePath):
         #change_meta()
         moveToCorrectLocation(filePath, root)
      else:
         os.remove(filePath)
   if dirEmpty(path):
      os.rmdir(path)


def moveToCorrectLocation(filePath, root):
    dest = filePath
    #if artist already exists then we are joining the paths
    if (os.path.exists(os.path.join(root, get_artist(filePath)))):
        dest = os.path.join(root, get_artist(filePath))
    #if the artist does not exist then we are making the 
    #folders and joining the path 
    else:
        dest = os.path.join(root, get_artist(filePath))
        os.mkdir(dest)
    
    #if the album already exists then we are just joining the paths
    if (os.path.exists(os.path.join(dest, get_album(filePath)))):
        dest = os.path.join(dest, get_album(filePath))
    #if the album does not exist then we are creating the 
    #folders and joining the path
    else:
        dest = os.path.join(dest, get_album(filePath))
        os.mkdir(dest)
        
    if (filePath != dest):
        os.rename(filePath, os.path.join(dest,os.path.basename(filePath)))


if __name__ == "__main__":
    collapse()
