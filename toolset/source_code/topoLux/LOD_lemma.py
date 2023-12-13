import re

LOD_lemma_load = [] # commune;localité;section;lieu-dit;page
# CommuneSection;Ur-Plang;aal lieudit;nei lieudit;Haaptwuert;nummer;Doubles toponymes;Remarques;Ur-Plang;;
with open('LOD_lemma/LOD_lemma_2019_10.csv', encoding='utf-8') as cabernet:
    pinot = cabernet.readlines()
    # print(pinot)
for item in pinot:
    LOD_lemma_load.append(item.rstrip('\n'))
#     elbling = item.rstrip('\n')
#     rivaner = elbling.split(';')
#     # LOD_lemma_load.append(dict({'lemma': rivaner[0],
#     #                             #'cat': rivaner[1]
#     #                             }))
#     LOD_lemma_load.append(rivaner[0])
cabernet.close()


characters = [' ', '#', "'", '-', '.', '?', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'à', 'â', 'ä', 'ç', 'è', 'é', 'ê', 'ë', 'î', 'ï', 'ô', 'ö', 'û', 'ü']

def vowel_clusters(input_string): # code from phonsearch project
    #  returnsstring with any vowel replaced by '0'. aeiouéëèäüöíìïàáòóùú
    v = re.compile('[oeüiuaöéàëäyíèôêìåûïâú]+[h]*', re.I)
    return v.findall(input_string)

def consonant_clusters(input_string): # code from phonsearch project
    #  returnsstring with any vowel replaced by '0'. aeiouéëèäüöíìïàáòóùú
    v = re.compile('[bcdfghjklmnpqrstvwxz]+', re.I)
    return v.findall(input_string)

v_s = ['a', 'aa', 'ae', 'aee', 'ah', 'ai', 'aie', 'ao', 'au', 'auaa', 'aue', 'auh', 'auu', 'ay', 'aya', 'aye', 'ayo', 'ayou', 'aïe', 'e', 'ea', 'eaa', 'eau', 'ee', 'eea', 'eeau', 'eeee', 'eeeeë', 'eeh', 'eeu', 'eeë', 'eh', 'ei', 'eia', 'eie', 'eih', 'eii', 'eiu', 'eo', 'eoi', 'eoo', 'eu', 'eue', 'eui', 'ey', 'eye', 'eä', 'eéie', 'eë', 'i', 'ia', 'iai', 'iaue', 'ie', 'iea', 'iee', 'ieo', 'ieu', 'ih', 'ii', 'io', 'ioa', 'iou', 'ioue', 'iu', 'iä', 'iè', 'ié', 'iée', 'iéi', 'iéie', 'ië', 'iö', 'o', 'oa', 'oau', 'oe', 'oei', 'oh', 'oi', 'oia', 'oie', 'oo', 'ooi', 'ou', 'oua', 'oue', 'ouh', 'oui', 'ouue', 'ouéie', 'oy', 'oya', 'oyau', 'oye', 'oyeu', 'oyé', 'oyée', 'oäi', 'oû', 'u', 'ua', 'uaa', 'uai', 'uay', 'uaye', 'ue', 'uee', 'uei', 'uh', 'ui', 'uie', 'uii', 'uiè', 'uo', 'uoi', 'uu', 'uya', 'uyau', 'uyè', 'uä', 'ué', 'uéie', 'uê', 'uë', 'y', 'ya', 'ye', 'yo', 'à', 'â', 'ä', 'äe', 'äh', 'äi', 'äia', 'äie', 'äih', 'äu', 'ää', 'è', 'é', 'ée', 'éi', 'éia', 'éie', 'éiei', 'éih', 'éii', 'éiu', 'éiue', 'éu', 'éë', 'ê', 'ë', 'ô', 'ö', 'öe', 'öh', 'öö', 'û', 'ü', 'üh', 'üü']
c_s = ['b', 'bb', 'bbk', 'bbr', 'bch', 'bd', 'bh', 'bj', 'bl', 'bn', 'br', 'bs', 'bsb', 'bsch', 'bschn', 'bscht', 'bsf', 'bsk', 'bskr', 'bsl', 'bst', 'bstb', 'bstcr', 'bstdr', 'bstr', 'bstz', 'bsz', 'bt', 'btr', 'bv', 'bw', 'bz', 'c', 'cc', 'cch', 'cd', 'cf', 'ch', 'chb', 'chbl', 'chbr', 'chcl', 'chd', 'chdr', 'chf', 'chfl', 'chfr', 'chg', 'chgl', 'chh', 'chj', 'chk', 'chkr', 'chl', 'chm', 'chn', 'chp', 'chpl', 'chpr', 'chr', 'chs', 'chsb', 'chsch', 'chschl', 'chschm', 'chschn', 'chschw', 'chsd', 'chsf', 'chsg', 'chsj', 'chsk', 'chsm', 'chsp', 'chspr', 'chst', 'chstch', 'chsth', 'chstp', 'chstr', 'chstw', 'chstz', 'chsv', 'chsw', 'chsz', 'cht', 'chtb', 'chtbl', 'chtch', 'chtd', 'chtdr', 'chtf', 'chtg', 'chtgl', 'chth', 'chtj', 'chtk', 'chtkr', 'chtl', 'chtm', 'chtn', 'chts', 'chtsb', 'chtsch', 'chtsd', 'chtsf', 'chtsg', 'chtsgr', 'chtsh', 'chtsk', 'chtskl', 'chtskr', 'chtsl', 'chtsm', 'chtsp', 'chtspl', 'chtspr', 'chtsr', 'chtsrh', 'chtss', 'chtsschr', 'chtsst', 'chtst', 'chtsv', 'chtsz', 'chtt', 'chtv', 'chtw', 'chtz', 'chv', 'chw', 'chz', 'ck', 'ckb', 'ckbl', 'ckbr', 'ckc', 'ckch', 'ckd', 'ckdr', 'ckf', 'ckfl', 'ckfr', 'ckg', 'ckgr', 'ckh', 'ckj', 'ckk', 'ckkr', 'ckl', 'ckm', 'ckn', 'ckp', 'ckr', 'cks', 'cksb', 'cksch', 'ckschl', 'ckschr', 'cksd', 'cksf', 'cksg', 'cksh', 'cksk', 'cksm', 'cksp', 'ckspr', 'ckssch', 'ckst', 'ckstr', 'cksv', 'cksw', 'cksz', 'ckt', 'cktf', 'cktg', 'ckth', 'cktkr', 'cktl', 'cktm', 'cktr', 'cktsch', 'cktschl', 'ckv', 'ckw', 'ckz', 'cl', 'cq', 'cr', 'cs', 'ct', 'ctr', 'cv', 'd', 'db', 'dbr', 'dch', 'dd', 'ddch', 'ddh', 'ddl', 'ddr', 'ddw', 'df', 'dg', 'dh', 'dhs', 'dj', 'dk', 'dkr', 'dl', 'dm', 'dn', 'dpl', 'dr', 'ds', 'dsb', 'dsc', 'dsch', 'dschl', 'dscht', 'dschw', 'dsfl', 'dsfr', 'dskr', 'dsm', 'dsr', 'dst', 'dsth', 'dt', 'dv', 'dvd', 'dz', 'f', 'fb', 'fbl', 'fbr', 'fch', 'fd', 'fdr', 'ff', 'ffb', 'ffch', 'ffd', 'ffg', 'ffk', 'ffl', 'ffn', 'ffp', 'ffr', 'ffs', 'ffsch', 'ffschm', 'ffsl', 'ffsp', 'ffsr', 'ffss', 'ffstr', 'ffsv', 'fft', 'ffw', 'ffz', 'fg', 'fgh', 'fgl', 'fgr', 'fh', 'fk', 'fkl', 'fkn', 'fkr', 'fl', 'fm', 'fn', 'fp', 'fpl', 'fpr', 'fr', 'fs', 'fsb', 'fsbr', 'fsch', 'fschl', 'fschm', 'fschn', 'fschr', 'fschw', 'fsh', 'fsk', 'fsl', 'fsm', 'fsp', 'fspr', 'fsschn', 'fsst', 'fsstr', 'fst', 'fstr', 'fsv', 'fsw', 'fsz', 'ft', 'ftb', 'ftbl', 'ftch', 'ftdr', 'ftfl', 'ftg', 'ftgr', 'fth', 'ftl', 'ftm', 'ftp', 'ftpfl', 'ftr', 'ftsb', 'ftsd', 'ftsfr', 'ftsh', 'ftsk', 'ftskr', 'ftsl', 'ftsm', 'ftsp', 'ftsr', 'ftssp', 'ftsstr', 'ftst', 'ftsv', 'ftsz', 'fttr', 'ftw', 'ftz', 'ftzw', 'fv', 'fw', 'fz', 'g', 'gb', 'gbr', 'gd', 'gdg', 'gdh', 'gdp', 'gds', 'gdsch', 'gdschl', 'gdz', 'gf', 'gfl', 'gg', 'ggl', 'ggr', 'gh', 'gj', 'gk', 'gkr', 'gl', 'gm', 'gn', 'gpl', 'gps', 'gr', 'gs', 'gschm', 'gsf', 'gsk', 'gsm', 'gsp', 'gspr', 'gst', 'gt', 'gtst', 'gw', 'gz', 'h', 'hb', 'hl', 'hlb', 'hlc', 'hld', 'hlg', 'hlm', 'hls', 'hm', 'hmk', 'hmm', 'hn', 'hnp', 'hns', 'hnst', 'hr', 'hrl', 'hrsch', 'hrst', 'hrz', 'hs', 'hspr', 'hss', 'hst', 'hw', 'j', 'k', 'kbr', 'kd', 'kg', 'kk', 'kkr', 'kl', 'km', 'kn', 'kp', 'kr', 'ks', 'ksc', 'ksd', 'ksf', 'ksfr', 'ksg', 'ksgr', 'ksh', 'ksk', 'ksl', 'ksm', 'kspr', 'kss', 'kssch', 'kssp', 'ksst', 'kst', 'ksw', 'ksz', 'kt', 'ktg', 'kth', 'ktl', 'ktp', 'ktr', 'ktsp', 'ktv', 'ktw', 'kz', 'l', 'lb', 'lbl', 'lbm', 'lbr', 'lbst', 'lbstb', 'lbstm', 'lbstst', 'lbstv', 'lbz', 'lc', 'lch', 'ld', 'ldb', 'ldbr', 'ldch', 'lddr', 'ldf', 'ldg', 'ldh', 'ldj', 'ldkr', 'ldl', 'ldm', 'ldn', 'ldp', 'ldr', 'lds', 'ldsch', 'ldschm', 'ldsp', 'ldstr', 'ldt', 'ldtr', 'ldw', 'lf', 'lfl', 'lfr', 'lfs', 'lfsp', 'lg', 'lgl', 'lgr', 'lh', 'lj', 'lk', 'lkl', 'lkr', 'lksh', 'll', 'llb', 'llbl', 'llbr', 'llch', 'llcl', 'lld', 'llf', 'llfr', 'llg', 'llgl', 'llh', 'llj', 'llk', 'llkl', 'lll', 'llm', 'lln', 'llp', 'llpl', 'llr', 'lls', 'llsch', 'llschl', 'llschm', 'llschn', 'llschr', 'llschw', 'llscl', 'llscr', 'llsd', 'llsf', 'llsg', 'llsgl', 'llsm', 'llsp', 'llspl', 'llss', 'llssp', 'llsst', 'llst', 'llstr', 'llsv', 'llsw', 'llsz', 'llt', 'lltr', 'llv', 'llw', 'llz', 'lm', 'lmf', 'lmpr', 'lmr', 'lmst', 'ln', 'lp', 'lpfl', 'lph', 'lpl', 'lpr', 'lpt', 'lptr', 'lq', 'lr', 'ls', 'lsb', 'lsbr', 'lsch', 'lschdr', 'lschh', 'lschl', 'lschn', 'lschr', 'lscht', 'lschw', 'lsd', 'lsdr', 'lsf', 'lsfr', 'lsg', 'lsh', 'lsj', 'lsk', 'lskl', 'lskr', 'lsm', 'lsp', 'lspr', 'lsr', 'lss', 'lsschl', 'lsst', 'lst', 'lstr', 'lsw', 'lsz', 'lt', 'ltb', 'ltf', 'ltfr', 'ltg', 'lth', 'ltj', 'ltk', 'ltkl', 'ltkr', 'ltl', 'ltm', 'ltn', 'ltpr', 'ltr', 'lts', 'ltsch', 'ltsp', 'ltst', 'ltt', 'ltv', 'ltw', 'ltz', 'ltzb', 'lv', 'lw', 'lwr', 'lz', 'lzb', 'lzh', 'lzl', 'lzm', 'lzr', 'lzs', 'lzsp', 'lzst', 'lzstr', 'lzt', 'lzv', 'lzw', 'm', 'mb', 'mbl', 'mbr', 'mc', 'mch', 'md', 'mdr', 'mf', 'mfl', 'mfr', 'mg', 'mgr', 'mh', 'mj', 'mk', 'mkl', 'mkn', 'mkr', 'ml', 'mm', 'mmb', 'mmbr', 'mmch', 'mmd', 'mmf', 'mmh', 'mmk', 'mml', 'mmm', 'mmpl', 'mmr', 'mms', 'mmschn', 'mmst', 'mmsz', 'mmt', 'mmth', 'mmz', 'mn', 'mp', 'mpch', 'mpf', 'mpfl', 'mpfp', 'mpfsp', 'mpfst', 'mph', 'mphdr', 'mpj', 'mpl', 'mpm', 'mpr', 'mps', 'mpt', 'mpv', 'mpw', 'mq', 'mr', 'ms', 'msb', 'msch', 'mschd', 'mschl', 'mschm', 'mschr', 'mschw', 'msd', 'msl', 'msp', 'msph', 'mspl', 'mspr', 'mss', 'mssch', 'mssp', 'mst', 'mstr', 'msw', 'msz', 'mt', 'mth', 'mtk', 'mtl', 'mtm', 'mtr', 'mts', 'mtsspr', 'mtsz', 'mtz', 'mv', 'mw', 'mz', 'n', 'nb', 'nc', 'nch', 'nchm', 'nchr', 'ncht', 'ncks', 'ncl', 'nct', 'nd', 'ndb', 'ndbr', 'ndch', 'ndd', 'ndf', 'ndfl', 'ndg', 'ndgr', 'ndh', 'ndk', 'ndkr', 'ndl', 'ndm', 'ndn', 'ndp', 'ndpr', 'ndr', 'nds', 'ndsch', 'ndschl', 'ndschm', 'ndschn', 'ndschr', 'ndsdr', 'ndsf', 'ndsfr', 'ndsg', 'ndsh', 'ndsj', 'ndsk', 'ndsl', 'ndsm', 'ndspr', 'ndsr', 'ndssch', 'ndsst', 'ndst', 'ndstr', 'ndsw', 'ndv', 'ndw', 'ndzw', 'nf', 'nfbr', 'nfk', 'nfl', 'nfr', 'nft', 'nftsl', 'nftsp', 'ng', 'ngb', 'ngbr', 'ngc', 'ngch', 'ngf', 'ngfr', 'ngg', 'nggl', 'ngh', 'ngj', 'ngk', 'ngkr', 'ngl', 'ngm', 'ngn', 'ngp', 'ngpr', 'ngr', 'ngs', 'ngsb', 'ngsbl', 'ngsbr', 'ngsc', 'ngsch', 'ngschl', 'ngschr', 'ngscht', 'ngschtj', 'ngschtl', 'ngschtr', 'ngschtschw', 'ngschtv', 'ngschtw', 'ngsd', 'ngsdr', 'ngsf', 'ngsfr', 'ngsg', 'ngsgl', 'ngsh', 'ngsk', 'ngskl', 'ngsl', 'ngsm', 'ngsn', 'ngsp', 'ngspl', 'ngspr', 'ngsr', 'ngss', 'ngsschr', 'ngsschw', 'ngssp', 'ngsspr', 'ngsst', 'ngsstr', 'ngst', 'ngstr', 'ngsv', 'ngsw', 'ngsz', 'ngt', 'ngtch', 'ngth', 'ngv', 'ngw', 'ngz', 'nh', 'nj', 'nk', 'nkb', 'nkbl', 'nkch', 'nkd', 'nkf', 'nkg', 'nkh', 'nkk', 'nkkn', 'nkl', 'nkm', 'nkn', 'nkp', 'nkr', 'nks', 'nkschr', 'nksf', 'nksh', 'nksk', 'nksp', 'nksr', 'nksschw', 'nksst', 'nkst', 'nksv', 'nksz', 'nkt', 'nktch', 'nktl', 'nkw', 'nkz', 'nl', 'nm', 'nn', 'nnb', 'nnbl', 'nnch', 'nnd', 'nnfl', 'nng', 'nnh', 'nnkr', 'nnl', 'nnm', 'nnn', 'nnp', 'nnr', 'nns', 'nnsbr', 'nnsch', 'nnsg', 'nnsl', 'nnsp', 'nnspr', 'nnsschw', 'nnsst', 'nnsstr', 'nnst', 'nnstr', 'nnsv', 'nnsw', 'nnt', 'nnth', 'nntl', 'nntm', 'nntn', 'nntsch', 'nnv', 'nnw', 'nnz', 'np', 'npr', 'nq', 'nr', 'ns', 'nsb', 'nsbr', 'nsc', 'nsch', 'nschd', 'nschh', 'nschl', 'nschn', 'nschr', 'nscht', 'nschtbr', 'nschtd', 'nschtf', 'nschtfl', 'nschtg', 'nschth', 'nschtk', 'nschtl', 'nschtm', 'nschtr', 'nschts', 'nschtsch', 'nschtst', 'nschtstr', 'nschttr', 'nschtw', 'nschw', 'nschz', 'nscr', 'nsd', 'nsdr', 'nsf', 'nsfl', 'nsfr', 'nsg', 'nsgr', 'nsh', 'nsj', 'nsk', 'nskr', 'nsl', 'nsm', 'nsn', 'nsp', 'nspl', 'nspr', 'nsq', 'nsr', 'nss', 'nssch', 'nssk', 'nsst', 'nsstr', 'nst', 'nstl', 'nstr', 'nsv', 'nsw', 'nsz', 'nt', 'ntb', 'ntch', 'ntd', 'ntf', 'ntfl', 'ntg', 'ntgl', 'nth', 'ntj', 'ntk', 'ntl', 'ntm', 'ntn', 'ntr', 'nts', 'ntsc', 'ntsch', 'ntschl', 'ntsd', 'ntsfl', 'ntsh', 'ntsk', 'ntskr', 'ntsl', 'ntsm', 'ntsp', 'ntspr', 'ntss', 'ntst', 'ntsw', 'ntt', 'ntv', 'ntw', 'ntz', 'nv', 'nw', 'nz', 'nzb', 'nzc', 'nzch', 'nzf', 'nzg', 'nzgl', 'nzk', 'nzkr', 'nzl', 'nzm', 'nzp', 'nzpl', 'nzr', 'nzs', 'nzsch', 'nzspr', 'nzt', 'nzv', 'nzw', 'nzz', 'p', 'pb', 'pbl', 'pbr', 'pc', 'pch', 'pd', 'pdr', 'pf', 'pfh', 'pfl', 'pfr', 'pg', 'pgl', 'pgr', 'ph', 'phl', 'phr', 'pht', 'phth', 'pj', 'pk', 'pkl', 'pkn', 'pkr', 'pl', 'pm', 'pn', 'pp', 'ppch', 'ppd', 'ppf', 'ppgr', 'pph', 'ppj', 'ppk', 'ppkr', 'ppl', 'ppm', 'ppn', 'ppr', 'pps', 'ppsch', 'ppspr', 'ppst', 'ppt', 'ppv', 'ppw', 'ppz', 'pr', 'ps', 'psch', 'pschl', 'pschn', 'pschr', 'pscht', 'pschw', 'psfl', 'psh', 'psp', 'pspl', 'pspr', 'psr', 'pst', 'pstl', 'pstr', 'pt', 'ptb', 'ptf', 'ptfl', 'ptg', 'ptgr', 'ptm', 'ptp', 'ptpfl', 'ptpl', 'ptpr', 'ptr', 'pts', 'ptsch', 'ptst', 'ptstr', 'ptth', 'ptw', 'ptz', 'pv', 'pw', 'pz', 'pzr', 'pzw', 'q', 'r', 'rb', 'rbf', 'rbl', 'rbr', 'rbsg', 'rbst', 'rc', 'rch', 'rchb', 'rchbl', 'rchbr', 'rchch', 'rchd', 'rchdr', 'rchf', 'rchg', 'rchgr', 'rchh', 'rchk', 'rchl', 'rchm', 'rchp', 'rchr', 'rchs', 'rchsch', 'rchschl', 'rchschn', 'rchstr', 'rcht', 'rchtb', 'rchw', 'rchz', 'rcl', 'rcr', 'rd', 'rdb', 'rdch', 'rdd', 'rdf', 'rdfl', 'rdg', 'rdk', 'rdl', 'rdn', 'rdp', 'rdr', 'rds', 'rdsb', 'rdsd', 'rdsfl', 'rdsh', 'rdsm', 'rdsr', 'rdsschw', 'rdsst', 'rdsz', 'rdw', 'rf', 'rfb', 'rfc', 'rfch', 'rfd', 'rff', 'rfgr', 'rfh', 'rfk', 'rfl', 'rfm', 'rfn', 'rfr', 'rfsch', 'rfst', 'rfv', 'rg', 'rgbr', 'rgc', 'rgd', 'rgfl', 'rgg', 'rgh', 'rgk', 'rgl', 'rgm', 'rgpl', 'rgr', 'rgs', 'rgsch', 'rgschn', 'rgschw', 'rgst', 'rgt', 'rh', 'rj', 'rk', 'rkh', 'rkl', 'rkm', 'rkn', 'rkpl', 'rkr', 'rks', 'rksb', 'rksch', 'rksg', 'rksh', 'rksl', 'rkst', 'rkt', 'rkz', 'rl', 'rlth', 'rm', 'rmb', 'rmch', 'rmf', 'rmfl', 'rmgr', 'rmh', 'rmkr', 'rml', 'rmm', 'rms', 'rmsdr', 'rmsp', 'rmspr', 'rmst', 'rmt', 'rmv', 'rn', 'rnd', 'rndr', 'rnh', 'rnl', 'rnpr', 'rns', 'rnsch', 'rnschl', 'rnst', 'rnsw', 'rnt', 'rnv', 'rnz', 'rp', 'rpfl', 'rph', 'rpl', 'rpn', 'rpr', 'rq', 'rr', 'rrg', 'rrh', 'rrkr', 'rrl', 'rrm', 'rrsch', 'rrw', 'rs', 'rsb', 'rsch', 'rschb', 'rschd', 'rschdr', 'rschk', 'rschkr', 'rschl', 'rschm', 'rschn', 'rschr', 'rscht', 'rschtch', 'rschtf', 'rschtk', 'rschtm', 'rschtst', 'rschw', 'rscr', 'rsd', 'rsf', 'rsfl', 'rsg', 'rsgl', 'rsgr', 'rsh', 'rsj', 'rsk', 'rskl', 'rsl', 'rsm', 'rsn', 'rsp', 'rspl', 'rspr', 'rsr', 'rss', 'rssch', 'rssp', 'rsst', 'rst', 'rstr', 'rsv', 'rsz', 'rt', 'rtb', 'rtc', 'rtch', 'rtd', 'rtdr', 'rtf', 'rtfl', 'rtfr', 'rtg', 'rth', 'rthr', 'rtj', 'rtk', 'rtkn', 'rtl', 'rtm', 'rtn', 'rtp', 'rtpl', 'rtr', 'rts', 'rtsb', 'rtsch', 'rtschl', 'rtschr', 'rtschw', 'rtscl', 'rtsd', 'rtsfr', 'rtsh', 'rtsj', 'rtsl', 'rtsm', 'rtsn', 'rtsp', 'rtspl', 'rtss', 'rtssch', 'rtsst', 'rtst', 'rtsw', 'rtv', 'rtw', 'rtz', 'rtzh', 'rv', 'rvl', 'rw', 'rx', 'rxm', 'rz', 'rzb', 'rzbr', 'rzch', 'rzd', 'rzdr', 'rzf', 'rzfr', 'rzg', 'rzh', 'rzk', 'rzkl', 'rzkr', 'rzl', 'rzm', 'rzrh', 'rzs', 'rzschl', 'rzschn', 'rzschr', 'rzst', 'rzt', 'rztr', 'rzw', 's', 'sb', 'sbl', 'sbr', 'sc', 'sch', 'schb', 'schbl', 'schbr', 'schc', 'schd', 'schdr', 'schf', 'schfl', 'schfr', 'schg', 'schh', 'schj', 'schk', 'schkr', 'schl', 'schm', 'schn', 'schp', 'schpl', 'schpr', 'schr', 'schschn', 'schsp', 'schst', 'schstr', 'scht', 'schtb', 'schtc', 'schtch', 'schtd', 'schtdr', 'schtf', 'schtfr', 'schtg', 'schtgr', 'schth', 'schtj', 'schtk', 'schtkl', 'schtkr', 'schtl', 'schtm', 'schtn', 'schtpr', 'schtq', 'schtr', 'schts', 'schtsch', 'schtst', 'schtv', 'schtw', 'schtz', 'schv', 'schw', 'schz', 'scl', 'scr', 'sd', 'sdr', 'sf', 'sfl', 'sfr', 'sg', 'sgl', 'sgr', 'sh', 'sj', 'sk', 'skl', 'skn', 'skr', 'skt', 'sl', 'sm', 'sms', 'sn', 'sp', 'sph', 'spl', 'spn', 'spr', 'sq', 'sr', 'ss', 'ssb', 'ssbl', 'ssbr', 'ssc', 'ssch', 'sschl', 'sschm', 'sschn', 'sschr', 'sschw', 'ssd', 'ssdr', 'ssf', 'ssfl', 'ssg', 'ssgl', 'ssh', 'ssj', 'ssk', 'sskl', 'sskn', 'sskr', 'ssl', 'ssm', 'ssn', 'ssp', 'sspr', 'ssr', 'sss', 'ssschr', 'ssschw', 'sssp', 'ssspr', 'ssst', 'sst', 'sstr', 'ssts', 'ssv', 'ssw', 'ssz', 'st', 'stb', 'stbr', 'stch', 'std', 'stf', 'stfr', 'stg', 'stgr', 'sth', 'sthm', 'stk', 'stkl', 'stl', 'stm', 'stn', 'stpl', 'str', 'sts', 'stsch', 'stst', 'sttr', 'sv', 'sw', 'sz', 't', 'tb', 'tbl', 'tbr', 'tc', 'tch', 'td', 'tdr', 'tf', 'tfl', 'tg', 'tgr', 'th', 'thl', 'thm', 'thr', 'tj', 'tk', 'tkl', 'tkr', 'tl', 'tm', 'tn', 'tp', 'tpl', 'tpr', 'tr', 'ts', 'tsb', 'tsc', 'tsch', 'tschb', 'tschbl', 'tschfl', 'tschg', 'tschl', 'tschm', 'tschn', 'tschr', 'tschs', 'tscht', 'tschw', 'tsd', 'tsf', 'tsfl', 'tsfr', 'tsg', 'tsgr', 'tsh', 'tsk', 'tskl', 'tskr', 'tsl', 'tsm', 'tsn', 'tsp', 'tsph', 'tspl', 'tspr', 'tsr', 'tss', 'tssch', 'tssp', 'tsst', 'tsstr', 'tst', 'tsth', 'tstr', 'tsv', 'tsw', 'tsz', 'tt', 'ttb', 'ttbr', 'ttch', 'ttd', 'ttdr', 'ttf', 'ttfl', 'ttfr', 'ttg', 'ttgr', 'tth', 'ttj', 'ttk', 'ttkr', 'ttl', 'ttm', 'ttp', 'ttpl', 'ttpr', 'ttr', 'tts', 'ttsch', 'ttsfr', 'ttsp', 'ttspr', 'ttsr', 'ttst', 'ttstr', 'ttv', 'ttw', 'ttz', 'tv', 'tw', 'tz', 'tzb', 'tzbl', 'tzc', 'tzch', 'tzd', 'tzf', 'tzfr', 'tzg', 'tzgr', 'tzh', 'tzk', 'tzl', 'tzm', 'tzn', 'tzp', 'tzpl', 'tzpr', 'tzr', 'tzschl', 'tzsp', 'tzst', 'tzt', 'tzv', 'tzw', 'tzz', 'v', 'vc', 'vf', 'vfl', 'vk', 'vl', 'vm', 'vpr', 'vr', 'vschr', 'vst', 'w', 'wb', 'wh', 'wl', 'wn', 'wnl', 'wr', 'ws', 'ww', 'wwr', 'x', 'xb', 'xc', 'xf', 'xfr', 'xh', 'xk', 'xkl', 'xkr', 'xm', 'xn', 'xp', 'xpl', 'xpr', 'xq', 'xsh', 'xsp', 'xt', 'xtm', 'xtp', 'xtr', 'xxx', 'xz', 'z', 'zb', 'zch', 'zd', 'zf', 'zg', 'zh', 'zk', 'zm', 'zp', 'zschn', 'zst', 'zt', 'zth', 'zw', 'zz', 'zzb', 'zzl', 'zzm', 'zzp']


# vowels = []
# consonants = []
# for item in LOD_lemma_load:
#     for vowel in vowel_clusters(item.lower()):
#         if vowel not in vowels:
#             vowels.append(vowel)
#     for consonant in consonant_clusters(item.lower()):
#         if consonant not in consonants:
#             consonants.append(consonant)
# vowels = sorted(vowels)
# consonants = sorted(consonants)


# for item in LOD_lemma_load:
#     for jtem in vowels:


# for jtem in v_s:
#     print(jtem)
#     for item in LOD_lemma_load:
#         if jtem in vowel_clusters(item):
#             print('\t', item)
#
# for jtem in c_s:
#     print(jtem)
#     for item in LOD_lemma_load:
#         if jtem in consonant_clusters(item):
#             print('\t', item)

# for item in LOD_lemma_load:
#     letter = 'au'
#     if len(vowel_clusters(item.lower())) == 3:
#         if letter in vowel_clusters(item):
#             if letter == vowel_clusters(item)[0]:
#                 print(letter, item)

print(len(LOD_lemma_load))
for item in LOD_lemma_load:
    if 'amm' in item:
        print(item)