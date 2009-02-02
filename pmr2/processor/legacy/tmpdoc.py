import re
from pmr2.processor.legacy import apply_xslt, StringIO

def tmpdoc2html(input):
    """\
    Given input CellML file object or string, apply xslt to extract
    the documentation and render it into html.

    input - should be a string.
    """

    if hasattr(input, 'read') and hasattr(input, 'seek'):
        # assume read is file-like, otherwise treat it as string
        input.seek(0)
        input = input.read()

    input = re.sub('<para>\r?\nThe model has been described here in CellML.*sec_download_this_model"/>\)\. *\r?\n</para>', '', input)
    input = makefileTerms(input)

    xslt_file = 'cellml_tmpdoc-to-html.xslt'
    input = StringIO(input)
    try:
        result = apply_xslt(input, xslt_file)
    except:
        # XXX figure out if we want to trap this here or earlier
        raise

    return result


def makefileTerms(input):
    """\
    Replace all Makefile terms with its replacement.
    """

    terms = MAKEFILE_TERMS
    for t in terms:
        input = input.replace(t[0], t[1])
    return input

SITEROOT = 'http://www.cellml.org/models'
MAKEFILE_TERMS = (
    ('${HTML_EXMPL_ALBRECHT_MODEL1}', SITEROOT + '/albrecht_colegrove_hongpaisan_pivovarova_andrews_friel_2001_version01'),
    ('${HTML_EXMPL_B_SAN_MODEL}', SITEROOT + '/boyett_zhang_garny_holden_2001_version01'),
    ('${HTML_EXMPL_BAKKER_MODEL}', SITEROOT + '/bakker_michels_opperdoes_westerhoff_1997_version01'),
    ('${HTML_EXMPL_BAKKER_MODEL2}', SITEROOT + '/bakker_mensonides_teusink_vanhoek_michels_westerhoff_2000_version01'),
    ('${HTML_EXMPL_BERNUS_MODEL}', SITEROOT + '/bernus_wilders_zemlin_verschelde_panfilov_2002_version01'),
    ('${HTML_EXMPL_BERTRAM_MODEL}', SITEROOT + '/bertram_previte_sherman_kinard_satin_2000_version02'),
    ('${HTML_EXMPL_BERTRAM_MODEL04}', SITEROOT + '/bertram_satin_zhang_smolen_sherman_2004_version01'),
    ('${HTML_EXMPL_BI_EGF_INTRO}', 'http://www.cellml.org/examples/examples/signal_transduction_models/bi_egf_pathway_1999/index.html'),
    ('${HTML_EXMPL_BONHOEFFER_MODEL}', SITEROOT + '/bonhoeffer_rembiszewski_ortiz_nixon_2000_version03'),
    ('${HTML_EXMPL_BR_MODEL}', SITEROOT + '/beeler_reuter_1977_version05'),
    ('${HTML_EXMPL_CHAY_MODEL}', SITEROOT + '/chay_lee_fan_1995_version02'),
    ('${HTML_EXMPL_CHAY_MODEL97}', SITEROOT + '/chay_1997_version04'),
    ('${HTML_EXMPL_CHEN_MODEL}', SITEROOT + '/chen_csikasz-nagy_gyorffy_val_novak_tyson_2000_version02'),
    ('${HTML_EXMPL_CILIBERTO_MODEL}', SITEROOT + '/ciliberto_petrus_tyson_sible_2003_version01'),
    ('${HTML_EXMPL_CILIBERTO_MODEL2}', SITEROOT + '/ciliberto_novak_tyson_2003_version01'),
    ('${HTML_EXMPL_COLEGROVE_MODEL}', SITEROOT + '/colegrove_albrecht_friel_2000_version01'),
    ('${HTML_EXMPL_D_SAN_MODEL}', SITEROOT + '/demir_clark_giles_murphey_1994_version01'),
    ('${HTML_EXMPL_D99_SAN_MODEL}', SITEROOT + '/demir_clark_giles_1999_version03'),
    ('${HTML_EXMPL_DFN_MODEL}', SITEROOT + '/difrancesco_noble_1985_version06'),
    ('${HTML_EXMPL_DOKOS_MODEL_II}', SITEROOT + '/dokos_celler_lovell_1996_version06'),
    ('${HTML_EXMPL_DOKOS_MODEL}', SITEROOT + '/dokos_celler_lovell_1996_version06'),
    ('${HTML_EXMPL_DR_MODEL}', SITEROOT + '/drouhard_roberge_1987_version02'),
    ('${HTML_EXMPL_DUMAINE_MODEL}', SITEROOT + '/dumaine_towbin_brugada_vatta_nesterenko_nesterenko_brugada_brugada_antzelevitch_1999_version01'),
    ('${HTML_EXMPL_ERYTHROCYTE_METABOLISM}', SITEROOT + '/mulquiney_kuchel_1999_version11'),
    ('${HTML_EXMPL_FN_SIMPLE}', SITEROOT + '/fitzhugh_1961_version04'),
    ('${HTML_EXMPL_FRIEL_MODEL}', SITEROOT + '/friel_1995_version01'),
    ('${HTML_EXMPL_GALL_MODEL}', SITEROOT + '/gall_susa_1999_version03'),
    ('${HTML_EXMPL_GASTRIC_H_K_ATPASE_MODEL}', SITEROOT + '/joseph_zavros_merchant_kirschner_2003_version01'),
    ('${HTML_EXMPL_GLYCOLYSIS_1997}', SITEROOT + '/rizzi_baltes_reuss_1997_version01'),
    ('${HTML_EXMPL_GLYCOLYSIS}', SITEROOT + '/rizzi_baltes_reuss_1997_version01'),
    ('${HTML_EXMPL_GOLDBETER_MODEL}', SITEROOT + '/goldbeter_1991_version04'),
    ('${HTML_EXMPL_GRAPHICAL_NOTATION}', 'http://www.cellml.org/tutorial/notation'),
    ('${HTML_EXMPL_GROSSMAN_MODEL}', SITEROOT + '/grossman_feinberg_kuznetsov_dimitrov_paul_1998_version01'),
    ('${HTML_EXMPL_HERZ_MODEL}', SITEROOT + '/herz_bonhoeffer_anderson_may_nowak_1996_version01'),
    ('${HTML_EXMPL_HHSA_INTRO}', SITEROOT + '/hodgkin_huxley_1952_version07'),
    ('${HTML_EXMPL_HMN_SIMPLE}', SITEROOT + '/hunter_mcnaughton_noble_1975_version02'),
    ('${HTML_EXMPL_IP3_CA2+_MODEL}', SITEROOT + '/deyoung_keizer_1992_version03'),
    ('${HTML_EXMPL_JRW_MODEL}', SITEROOT + '/jafri_rice_winslow_1998_version03'),
    ('${HTML_EXMPL_KEIZER_MODEL}', SITEROOT + '/keizer_levine_1996_version03'),
    ('${HTML_EXMPL_LAMBETH_MODEL}', SITEROOT + '/lambeth_kushmerick_2002_version01'),
    ('${HTML_EXMPL_LI_MODEL}', SITEROOT + '/li_rinzel_1994_version02'),
    ('${HTML_EXMPL_LR_I_MODEL}', SITEROOT + '/luo_rudy_1991_version04'),
    ('${HTML_EXMPL_LR_II_MODEL}', SITEROOT + '/luo_rudy_1994_version02'),
    ('${HTML_EXMPL_MAGNUS_MODEL}', SITEROOT + '/magnus_keizer_1998_version01'),
    ('${HTML_EXMPL_MAPK_CASCADE}', SITEROOT + '/huang_ferrell_1996_version03'),
    ('${HTML_EXMPL_MARTINOV_MODEL}', SITEROOT + '/martinov_vitvitsky_mosharov_banerjee_ataullakhanov_2000_version01'),
    ('${HTML_EXMPL_MITOCHONDRIAL_CA_HANDLING}', SITEROOT + '/magnus_keizer_1997_version01'),
    ('${HTML_EXMPL_MITTLER_MODEL}', SITEROOT + '/mittler_sulzer_neumann_perelson_1998_version01'),
    ('${HTML_EXMPL_MNT_MODEL}', SITEROOT + '/mcallister_noble_tsien_1975_version05'),
    ('${HTML_EXMPL_MOONEY_RIVLIN_LAW}', SITEROOT + '/rivlin_saunders_1951_version01'),
    ('${HTML_EXMPL_N_MODEL}', SITEROOT + '/noble_1962_version05'),
    ('${HTML_EXMPL_N98_MODEL}', SITEROOT + '/noble_varghese_kohl_noble_1998_version08'),
    ('${HTML_EXMPL_NOVAK_MODEL}', SITEROOT + '/novak_tyson_1997_version01'),
    ('${HTML_EXMPL_NOVAK_MODEL98}', SITEROOT + '/novak_csikasz-nagy_gyorffy_chen_tyson_1998_version01'),
    ('${HTML_EXMPL_NOWAK_MODEL}', SITEROOT + '/nowak_bangham_1996_version03'),
    ('${HTML_EXMPL_OXIDATIVE_PHOSPHORYLATION}', SITEROOT + '/beard_2005_version01'),
    ('${HTML_EXMPL_PERELSON_MODEL}', SITEROOT + '/perelson_neumann_markowitz_leonard_ho_1996_version01'),
    ('${HTML_EXMPL_PRIEBE_MODEL}', SITEROOT + '/priebe_beuckelmann_1998_version01'),
    ('${HTML_EXMPL_RICE_MODEL}', SITEROOT + '/rice_winslow_jafri_1999_version03'),
    ('${HTML_EXMPL_RICE_MODEL2}', SITEROOT + '/rice_jafri_winslow_2000_version02'),
    ('${HTML_EXMPL_RJW_MODEL}', SITEROOT + '/rice_jafri_winslow_2000_version02'),
    ('${HTML_EXMPL_SNEYD_MODEL}', SITEROOT + '/sneyd_dufour_2002_version05'),
    ('${HTML_EXMPL_SNYDER_MODEL}', SITEROOT + '/snyder_palmer_moore_2000_version01'),
    ('${HTML_EXMPL_SOBIE_MODEL}', SITEROOT + '/sobie_dilly_dossantoscruz_lederer_jafri_2002_version01'),
    ('${HTML_EXMPL_STERN_MODEL}', SITEROOT + '/stern_song_sham_yang_boheler_rios_1999_version02'),
    ('${HTML_EXMPL_TEN_TUSSCHER_MODEL04}', SITEROOT + '/tentusscher_noble_noble_panfilov_2004_version05'),
    ('${HTML_EXMPL_TEUSINK_MODEL}', SITEROOT + '/teusink_passarge_reijenga_esgalhado_vanderweijden_schepper_walsh_bakker_vandam_westerhoff_snoep_2000_version03'),
    ('${HTML_EXMPL_UPDATED_LR_II_MODEL}', SITEROOT + '/luo_rudy_1994_version02'),
    ('${HTML_EXMPL_W_MODEL}', SITEROOT + '/winslow_rice_jafri_marban_ororke_1999_version03'),
    ('${HTML_EXMPL_WODARZ_MODEL}', SITEROOT + '/wodarz_nowak_1999_version01'),
    ('${HTML_EXMPL_WOLF_HEINRICH_MODEL}', SITEROOT + '/wolf_heinrich_2000_version02'),
    ('${HTML_EXMPL_WOLF_MODEL}', SITEROOT + '/wolf_passarge_somsen_snoep_heinrich_westerhoff_2000_version02'),
    ('${HTML_EXMPL_Z_SAN_MODEL}', SITEROOT + '/zhang_holden_kodama_honjo_lei_varghese_boyett_2000_version03'),
    ('${HTML_METADATA_20020116_OVERVIEW}', 'http://www.cellml.org/specifications/archive/metadata/20020116/cellml_metadata_specification.pdf/view'),
    ('${HTML_REPOSITORY_INTRODUCTION}', SITEROOT + ''),
    ('${HTML_SPEC_20010810_GROUPING}', 'http://www.cellml.org/specifications/cellml_1.1/#sec_grouping'),
    ('${HTML_SPEC_20010810_UNITS}', 'http://www.cellml.org/specifications/cellml_1.1/#sec_units'),
    ('${HTML_XML_EXMPL_GUIDE}', 'http://www.cellml.org/tutorial/xml_guide'),
)
