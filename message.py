from dictionnary import *
from words import Text

corne = concept_builder([palisa, lawa, soweli], translation="corne")
rugissement_corne_eberon = concept_builder([kalama, pi, corne, eberon], translation="rugissement de la corne d'Eberon")
loalassien = concept_builder([jan, tan, loalas], translation="Loalassien")
moi_Zadathar = concept_builder([mi, zadathar, jelo], translation="moi, Zadathar le rouge")
zehir_li_noli = concept_builder([Zehir, li, noli])
kon_jan_mute = concept_builder([kon, jan, mute])
jan_utala_suli = concept_builder([jan, utala, suli])
tawa_python = concept_builder([tawa, python])
tu_wan = concept_builder([tu, wan])
moku_utala = concept_builder([moku, utala])
laso_jelo = concept_builder([laso, jelo])
yuhan_ti = concept_builder([jan, lili, Zehir], translation="Yuhan-Ti")
hommes_lezards = concept_builder([jan, lili, narm], translation="hommes lezards")
mi_kama_utala_ala = concept_builder([mi, kama, utala], translation="bonjour")  # j'ai pas 'ala'
o_sina_pilin_pona = concept_builder([o, sina, pilin, pona], translation="bonjour en retour")

# page 1
page_1 = Text(
    [
        (Zehir) + li + noli + li + (poki + anpa + na + telo + kasi),
        narm + li + (lape + noli + noka + (telo + suli + pi + (kiwen + suno))),
        zehir_li_noli + vide + taso + vide + (telo + nasi + ona) + li + (tawa + nasin + anpa) + li + moku_utala,
        hommes_lezards + li + kama + e + yuhan_ti,
        # Zehir pas encadré ?
        yuhan_ti + li + pakala + e + tomo + li + moku_utala + e + jan + li + seli + e + sona,
        (akesi + suli + pi + laso_jelo) + li + (nasin + ike) + e + (kulopo + jan),
        python + la + (jan_utala_suli) + li + (tawa + sinpin + ike),
        ona + li + (tawa + neka) + e + (jan + pona + ona) + li + lukin + e + (kon_jan_mute),
        ona + li + (toki + tawa + (kon_jan_mute)) + e_ni + ((o + pona + tawa + ni) + e + (wawa + sina)),
    ]
)
# page 2
page_2 = Text(
    [
        ((kon + waso) + en + (kon + soweli) + en + (kon + pipi) + en + (kon + kala)) + li + (pana + tawa),
        (jan_utala_suli) + e + (wawa + ona),
        (kepeken + (kon_jan_mute)) + la + ((jan_utala_suli) + li + (tawa + sinpin + (akesi + suli + pi + laso_jelo))),
        (python + en + balthasar) + li + (utala + ona + tenpo + ((tu_wan + suno) + en + (tu_wan + mun))),
        (tenpo + (tu + tu) + suno) + la + (jan_utala_suli) + li + tu + e + (lawa + (akesi + suli + laso_jelo)),
        ona + li + (tawa + na + kala + kiwen) + e + tawa_python,
        tan + la + ((kala + kiwen) + li + lukin + e + tawa_python),
        tan + la + ((pilin + ona) + li + (lon + awen)),
    ]
)

# encadrement porte
encadrement_porte = Text(
    [
        (ilo + utala + mi) + li + (lon + insu + (ni + tomo)) + point,
        (o + nini) + e + (jan + ike) + point,
        (o + kama) + e + (ilo + utala + mi),
    ]
)

dette_Z = Text(
    [
        moi_Zadathar + vide + (mi + toki) + e_ni + ((mani + mi) + li + tawa + e + loalassien),
        (mi + toki + kama) + e + rugissement_corne_eberon,
    ]
)

all = Text([*page_1.sentences, *page_2.sentences, *encadrement_porte.sentences, *dette_Z.sentences])
all.show_common()
