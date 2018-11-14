from edc_visit_schedule import FormsCollection, Crf


crf_2000 = FormsCollection(
    Crf(show_order=1, model='td_infant.infantbirthdata'),
    Crf(show_order=2, model='td_infant.infantbirthexam'),
    Crf(show_order=3, model='td_infant.infantbirthfeedingvaccine'),
    Crf(show_order=4, model='td_infant.infantbirtharv'),
    Crf(show_order=5, model='td_infant.infantcongenitalanomalies'),
    Crf(show_order=6, model='td_infant.infantdeathreport'),
    Crf(show_order=7, model='td_infant.infantnvpdispensing'),
    name='Birth v3'
)

crf_2010 = FormsCollection(
    Crf(show_order=1, model='td_infant.infantfu'),
    Crf(show_order=2, model='td_infant.infantfuphysical'),
    Crf(show_order=3, model='td_infant.infantfudx'),
    Crf(show_order=4, model='td_infant.infantfunewmed'),
    Crf(show_order=5, model='td_infant.infantarvproph'),
    Crf(show_order=6, model='td_infant.infantfeeding'),
    Crf(show_order=7, model='td_infant.infantnvpadjustment'),
    Crf(show_order=8, model='td_infant.infantfuimmunizations'),
    name='Infant 1 Month Visit v3'
)

crf_2020 = FormsCollection(
    Crf(show_order=1, model='td_infant.infantfu'),
    Crf(show_order=2, model='td_infant.infantfuphysical'),
    Crf(show_order=3, model='td_infant.infantfudx'),
    Crf(show_order=4, model='td_infant.infantfunewmed'),
    Crf(show_order=5, model='td_infant.infantfuimmunizations'),
    Crf(show_order=6, model='td_infant.infantarvproph'),
    Crf(show_order=7, model='td_infant.infantfeeding'),
    name='Infant 6 Month Visit v3'
)

crf_2120 = FormsCollection(
    Crf(show_order=1, model='td_infant.infantfu'),
    Crf(show_order=2, model='td_infant.infantfuphysical'),
    Crf(show_order=3, model='td_infant.infantfudx'),
    Crf(show_order=4, model='td_infant.infantfunewmed'),
    Crf(show_order=5, model='td_infant.infantfeeding'),
    Crf(show_order=5, model='td_infant.solidfoodassessment'),
    Crf(show_order=6, model='td_infant.infantfuimmunizations'),
    name='Infant 12 Month Visit v3'
)

crf_2180 = FormsCollection(
    Crf(show_order=1, model='td_infant.infantfu'),
    Crf(show_order=2, model='td_infant.infantfuphysical'),
    Crf(show_order=3, model='td_infant.infantfudx'),
    Crf(show_order=4, model='td_infant.infantfunewmed'),
    Crf(show_order=5, model='td_infant.infantfeeding'),
    Crf(show_order=5, model='td_infant.solidfoodassessment'),
    Crf(show_order=6, model='td_infant.infantfuimmunizations'),
    name='Infant 18 Month Visit v3'
)

crf_2240 = FormsCollection(
    Crf(show_order=1, model='td_infant.infantfu'),
    Crf(show_order=2, model='td_infant.infantfuphysical'),
    Crf(show_order=3, model='td_infant.infantfudx'),
    Crf(show_order=4, model='td_infant.infantfunewmed'),
    Crf(show_order=5, model='td_infant.infantfeeding'),
    Crf(show_order=5, model='td_infant.solidfoodassessment'),
    Crf(show_order=6, model='td_infant.infantfuimmunizations'),
    name='Infant 24 Month Visit v3'
)

crf_2300 = FormsCollection(
    Crf(show_order=1, model='td_infant.infantfu'),
    Crf(show_order=2, model='td_infant.infantfuphysical'),
    Crf(show_order=3, model='td_infant.infantfudx'),
    Crf(show_order=4, model='td_infant.infantfunewmed'),
    Crf(show_order=5, model='td_infant.infantfeeding'),
    Crf(show_order=5, model='td_infant.solidfoodassessment'),
    Crf(show_order=6, model='td_infant.infantfuimmunizations'),
    name='Infant 30 Month Visit v3'
)

crf_2360 = FormsCollection(
    Crf(show_order=1, model='td_infant.infantfu'),
    Crf(show_order=2, model='td_infant.infantfuphysical'),
    Crf(show_order=3, model='td_infant.infantfudx'),
    Crf(show_order=4, model='td_infant.infantfunewmed'),
    Crf(show_order=5, model='td_infant.infantfeeding'),
    Crf(show_order=5, model='td_infant.solidfoodassessment'),
    Crf(show_order=6, model='td_infant.infantfuimmunizations'),
    name='Infant 36 Month Visit v3'
)
