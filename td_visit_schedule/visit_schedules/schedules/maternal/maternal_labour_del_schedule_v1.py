from edc_visit_schedule import Schedule, Visit as BaseVisit

from dateutil.relativedelta import relativedelta

from ...crfs_requisitions import (
    crf_2000, crf_2010, crf_2020,
    crf_2060, crf_2120, crf_2180,
    crf_2240, crf_2300, crf_2360)
from ...crfs_requisitions import maternal_crfs_prn
from ...crfs_requisitions import maternal_crfs_unscheduled
from ...crfs_requisitions import requisitions_followup
from ...crfs_requisitions import requisitions_prn as default_requisitions_prn

default_requisitions = None


class Visit(BaseVisit):

    def __init__(self, crfs_unscheduled=None, requisitions_unscheduled=None,
                 crfs_prn=None, requisitions_prn=None,
                 allow_unscheduled=None, **kwargs):
        super().__init__(
            allow_unscheduled=True if allow_unscheduled is None else allow_unscheduled,
            crfs_unscheduled=crfs_unscheduled or maternal_crfs_unscheduled,
            requisitions_unscheduled=requisitions_unscheduled or default_requisitions,
            crfs_prn=crfs_prn,
            requisitions_prn=requisitions_prn or default_requisitions_prn,
            **kwargs)


# TODO: Add PRN for visits.
maternal_labour_del_schedule_v1 = Schedule(
    name='mld_schedule_1',
    verbose_name='Day 1 to 36 months Follow-up V1',
    onschedule_model='td_maternal.onschedulematernallabourdel',
    offschedule_model='td_maternal.maternaloffschedule',
    consent_model='td_maternal.subjectconsent',
    appointment_model='edc_appointment.appointment')

visit2000 = Visit(
    code='2000M',
    title='Delivery Visit V1',
    timepoint=30,
    rbase=relativedelta(months=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_followup,
    crfs=crf_2000,
    facility_name='5-day clinic')

visit2010 = Visit(
    code='2010M',
    title='1 Month Visit V1',
    timepoint=50,
    rbase=relativedelta(months=1),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_followup,
    crfs=crf_2010,
    facility_name='5-day clinic')

visit2020 = Visit(
    code='2020M',
    title='2 Month Visit V1',
    timepoint=110,
    rbase=relativedelta(months=2),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_followup,
    crfs=crf_2020,
    facility_name='5-day clinic')

visit2060 = Visit(
    code='2060M',
    title='6 Month Visit V1',
    timepoint=170,
    rbase=relativedelta(months=6),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_followup,
    crfs=crf_2060,
    facility_name='5-day clinic')

visit2120 = Visit(
    code='2120M',
    title='12 Month Visit V1',
    timepoint=230,
    rbase=relativedelta(months=12),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_followup,
    crfs=crf_2120,
    crfs_prn=maternal_crfs_prn,
    facility_name='5-day clinic')

visit2180 = Visit(
    code='2180M',
    title='18 Month Visit V1',
    timepoint=290,
    rbase=relativedelta(months=18),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_followup,
    crfs=crf_2180,
    crfs_prn=maternal_crfs_prn,
    facility_name='5-day clinic')

visit2240 = Visit(
    code='2240M',
    title='24 Month Visit V1',
    timepoint=350,
    rbase=relativedelta(months=24),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_followup,
    crfs=crf_2240,
    crfs_prn=maternal_crfs_prn,
    facility_name='5-day clinic')

visit2300 = Visit(
    code='2300M',
    title='30 Month Visit V1',
    timepoint=410,
    rbase=relativedelta(months=30),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_followup,
    crfs=crf_2300,
    crfs_prn=maternal_crfs_prn,
    facility_name='5-day clinic')

visit2360 = Visit(
    code='2360M',
    title='36 Month Visit V1',
    timepoint=470,
    rbase=relativedelta(months=36),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_followup,
    crfs=crf_2360,
    crfs_prn=maternal_crfs_prn,
    facility_name='5-day clinic')

maternal_labour_del_schedule_v1.add_visit(visit2000)
maternal_labour_del_schedule_v1.add_visit(visit2010)
maternal_labour_del_schedule_v1.add_visit(visit2020)
maternal_labour_del_schedule_v1.add_visit(visit2060)
maternal_labour_del_schedule_v1.add_visit(visit2120)
maternal_labour_del_schedule_v1.add_visit(visit2180)
maternal_labour_del_schedule_v1.add_visit(visit2240)
maternal_labour_del_schedule_v1.add_visit(visit2300)
maternal_labour_del_schedule_v1.add_visit(visit2360)
