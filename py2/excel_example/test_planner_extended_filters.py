from audioop import reverse
from time import sleep
import pytest
import requests
from utils import *
from conftest import file_dir as test_home
from conftest import ref_version
import json
import datetime


class TestsortMajor:
	def test_sort_with_reminderState_1(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title&reminderState=notReminded"))
		assert filter_response.status_code == 200

	def test_sort_with_downloadState_2(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title&downloadState=notStarted"))
		assert filter_response.status_code == 200

	def test_sort_with_downloadState_3(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title&downloadState=inProgress"))
		assert filter_response.status_code == 200

	def test_sort_with_downloadState_4(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title&downloadState=suspended"))
		assert filter_response.status_code == 200

	def test_sort_with_downloadState_5(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title&downloadState=notStarted,inProgress"))
		assert filter_response.status_code == 200

	def test_sort_with_downloadState_6(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title&downloadState=notStarted,inProgress,suspended"))
		assert filter_response.status_code == 200

	def test_sort_with_recordingState_7(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title&recordingState=notStarted"))
		assert filter_response.status_code == 200

	def test_sort_with_recordingState_8(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title&recordingState=inProgress"))
		assert filter_response.status_code == 200

	def test_sort_with_recordingState_9(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title&recordingState=notStarted,inProgress"))
		assert filter_response.status_code == 200

	def test_sort_with_recordingContentState_10(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title&recordingContentState=partial"))
		assert filter_response.status_code == 200

	def test_sort_with_recordingContentState_11(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title&recordingContentState=complete"))
		assert filter_response.status_code == 200

	def test_sort_with_recordingContentState_12(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title&recordingContentState=partial,complete"))
		assert filter_response.status_code == 200

	def test_sort_with_downloadContentState_13(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title&downloadContentState=partial"))
		assert filter_response.status_code == 200

	def test_sort_with_downloadContentState_14(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title&downloadContentState=complete"))
		assert filter_response.status_code == 200

	def test_sort_with_downloadContentState_15(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title&downloadContentState=partial,complete"))
		assert filter_response.status_code == 200

	def test_sort_with_embed_16(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title&embed=eventBooking"))
		assert filter_response.status_code == 200

	def test_sort_with_embed_17(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title&embed=seasonBooking"))
		assert filter_response.status_code == 200

	def test_sort_with_embed_18(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title&embed=transcodeBooking"))
		assert filter_response.status_code == 200

	def test_sort_with_embed_19(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title&embed=transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_sort_with_embed_20(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title&embed=reminderBooking"))
		assert filter_response.status_code == 200

	def test_sort_with_embed_21(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title&embed=eventBooking,seasonBooking"))
		assert filter_response.status_code == 200

	def test_sort_with_embed_22(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title&embed=eventBooking,seasonBooking,transcodeBooking"))
		assert filter_response.status_code == 200

	def test_sort_with_embed_23(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_sort_with_embed_24(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking,reminderBooking"))
		assert filter_response.status_code == 200

	def test_sort_with_bookingType_25(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title&bookingType=manual"))
		assert filter_response.status_code == 200

	def test_sort_with_bookingType_26(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title&bookingType=event"))
		assert filter_response.status_code == 200

	def test_sort_with_bookingType_27(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title&bookingType=manual,event"))
		assert filter_response.status_code == 200

	def test_sort_with_reminderState_28(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=date&reminderState=notReminded"))
		assert filter_response.status_code == 200

	def test_sort_with_downloadState_29(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=date&downloadState=notStarted"))
		assert filter_response.status_code == 200

	def test_sort_with_downloadState_30(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=date&downloadState=inProgress"))
		assert filter_response.status_code == 200

	def test_sort_with_downloadState_31(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=date&downloadState=suspended"))
		assert filter_response.status_code == 200

	def test_sort_with_downloadState_32(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=date&downloadState=notStarted,inProgress"))
		assert filter_response.status_code == 200

	def test_sort_with_downloadState_33(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=date&downloadState=notStarted,inProgress,suspended"))
		assert filter_response.status_code == 200

	def test_sort_with_recordingState_34(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=date&recordingState=notStarted"))
		assert filter_response.status_code == 200

	def test_sort_with_recordingState_35(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=date&recordingState=inProgress"))
		assert filter_response.status_code == 200

	def test_sort_with_recordingState_36(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=date&recordingState=notStarted,inProgress"))
		assert filter_response.status_code == 200

	def test_sort_with_recordingContentState_37(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=date&recordingContentState=partial"))
		assert filter_response.status_code == 200

	def test_sort_with_recordingContentState_38(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=date&recordingContentState=complete"))
		assert filter_response.status_code == 200

	def test_sort_with_recordingContentState_39(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=date&recordingContentState=partial,complete"))
		assert filter_response.status_code == 200

	def test_sort_with_downloadContentState_40(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=date&downloadContentState=partial"))
		assert filter_response.status_code == 200

	def test_sort_with_downloadContentState_41(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=date&downloadContentState=complete"))
		assert filter_response.status_code == 200

	def test_sort_with_downloadContentState_42(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=date&downloadContentState=partial,complete"))
		assert filter_response.status_code == 200

	def test_sort_with_embed_43(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=date&embed=eventBooking"))
		assert filter_response.status_code == 200

	def test_sort_with_embed_44(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=date&embed=seasonBooking"))
		assert filter_response.status_code == 200

	def test_sort_with_embed_45(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=date&embed=transcodeBooking"))
		assert filter_response.status_code == 200

	def test_sort_with_embed_46(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=date&embed=transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_sort_with_embed_47(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=date&embed=reminderBooking"))
		assert filter_response.status_code == 200

	def test_sort_with_embed_48(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=date&embed=eventBooking,seasonBooking"))
		assert filter_response.status_code == 200

	def test_sort_with_embed_49(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=date&embed=eventBooking,seasonBooking,transcodeBooking"))
		assert filter_response.status_code == 200

	def test_sort_with_embed_50(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=date&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_sort_with_embed_51(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=date&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking,reminderBooking"))
		assert filter_response.status_code == 200

	def test_sort_with_bookingType_52(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=date&bookingType=manual"))
		assert filter_response.status_code == 200

	def test_sort_with_bookingType_53(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=date&bookingType=event"))
		assert filter_response.status_code == 200

	def test_sort_with_bookingType_54(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=date&bookingType=manual,event"))
		assert filter_response.status_code == 200

	def test_sort_with_reminderState_55(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title,date&reminderState=notReminded"))
		assert filter_response.status_code == 200

	def test_sort_with_downloadState_56(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title,date&downloadState=notStarted"))
		assert filter_response.status_code == 200

	def test_sort_with_downloadState_57(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title,date&downloadState=inProgress"))
		assert filter_response.status_code == 200

	def test_sort_with_downloadState_58(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title,date&downloadState=suspended"))
		assert filter_response.status_code == 200

	def test_sort_with_downloadState_59(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title,date&downloadState=notStarted,inProgress"))
		assert filter_response.status_code == 200

	def test_sort_with_downloadState_60(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title,date&downloadState=notStarted,inProgress,suspended"))
		assert filter_response.status_code == 200

	def test_sort_with_recordingState_61(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title,date&recordingState=notStarted"))
		assert filter_response.status_code == 200

	def test_sort_with_recordingState_62(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title,date&recordingState=inProgress"))
		assert filter_response.status_code == 200

	def test_sort_with_recordingState_63(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title,date&recordingState=notStarted,inProgress"))
		assert filter_response.status_code == 200

	def test_sort_with_recordingContentState_64(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title,date&recordingContentState=partial"))
		assert filter_response.status_code == 200

	def test_sort_with_recordingContentState_65(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title,date&recordingContentState=complete"))
		assert filter_response.status_code == 200

	def test_sort_with_recordingContentState_66(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title,date&recordingContentState=partial,complete"))
		assert filter_response.status_code == 200

	def test_sort_with_downloadContentState_67(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title,date&downloadContentState=partial"))
		assert filter_response.status_code == 200

	def test_sort_with_downloadContentState_68(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title,date&downloadContentState=complete"))
		assert filter_response.status_code == 200

	def test_sort_with_downloadContentState_69(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title,date&downloadContentState=partial,complete"))
		assert filter_response.status_code == 200

	def test_sort_with_embed_70(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title,date&embed=eventBooking"))
		assert filter_response.status_code == 200

	def test_sort_with_embed_71(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title,date&embed=seasonBooking"))
		assert filter_response.status_code == 200

	def test_sort_with_embed_72(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title,date&embed=transcodeBooking"))
		assert filter_response.status_code == 200

	def test_sort_with_embed_73(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title,date&embed=transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_sort_with_embed_74(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title,date&embed=reminderBooking"))
		assert filter_response.status_code == 200

	def test_sort_with_embed_75(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title,date&embed=eventBooking,seasonBooking"))
		assert filter_response.status_code == 200

	def test_sort_with_embed_76(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title,date&embed=eventBooking,seasonBooking,transcodeBooking"))
		assert filter_response.status_code == 200

	def test_sort_with_embed_77(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title,date&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_sort_with_embed_78(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title,date&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking,reminderBooking"))
		assert filter_response.status_code == 200

	def test_sort_with_bookingType_79(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title,date&bookingType=manual"))
		assert filter_response.status_code == 200

	def test_sort_with_bookingType_80(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title,date&bookingType=event"))
		assert filter_response.status_code == 200

	def test_sort_with_bookingType_81(self):
		filter_response = call_ref_url("get", make_booking_filter_url("sort=title,date&bookingType=manual,event"))
		assert filter_response.status_code == 200


class TestreminderStateMajor:
	def test_reminderState_with_downloadState_1(self):
		filter_response = call_ref_url("get", make_booking_filter_url("reminderState=notReminded&downloadState=notStarted"))
		assert filter_response.status_code == 200

	def test_reminderState_with_downloadState_2(self):
		filter_response = call_ref_url("get", make_booking_filter_url("reminderState=notReminded&downloadState=inProgress"))
		assert filter_response.status_code == 200

	def test_reminderState_with_downloadState_3(self):
		filter_response = call_ref_url("get", make_booking_filter_url("reminderState=notReminded&downloadState=suspended"))
		assert filter_response.status_code == 200

	def test_reminderState_with_downloadState_4(self):
		filter_response = call_ref_url("get", make_booking_filter_url("reminderState=notReminded&downloadState=notStarted,inProgress"))
		assert filter_response.status_code == 200

	def test_reminderState_with_downloadState_5(self):
		filter_response = call_ref_url("get", make_booking_filter_url("reminderState=notReminded&downloadState=notStarted,inProgress,suspended"))
		assert filter_response.status_code == 200

	def test_reminderState_with_recordingState_6(self):
		filter_response = call_ref_url("get", make_booking_filter_url("reminderState=notReminded&recordingState=notStarted"))
		assert filter_response.status_code == 200

	def test_reminderState_with_recordingState_7(self):
		filter_response = call_ref_url("get", make_booking_filter_url("reminderState=notReminded&recordingState=inProgress"))
		assert filter_response.status_code == 200

	def test_reminderState_with_recordingState_8(self):
		filter_response = call_ref_url("get", make_booking_filter_url("reminderState=notReminded&recordingState=notStarted,inProgress"))
		assert filter_response.status_code == 200

	def test_reminderState_with_recordingContentState_9(self):
		filter_response = call_ref_url("get", make_booking_filter_url("reminderState=notReminded&recordingContentState=partial"))
		assert filter_response.status_code == 200

	def test_reminderState_with_recordingContentState_10(self):
		filter_response = call_ref_url("get", make_booking_filter_url("reminderState=notReminded&recordingContentState=complete"))
		assert filter_response.status_code == 200

	def test_reminderState_with_recordingContentState_11(self):
		filter_response = call_ref_url("get", make_booking_filter_url("reminderState=notReminded&recordingContentState=partial,complete"))
		assert filter_response.status_code == 200

	def test_reminderState_with_downloadContentState_12(self):
		filter_response = call_ref_url("get", make_booking_filter_url("reminderState=notReminded&downloadContentState=partial"))
		assert filter_response.status_code == 200

	def test_reminderState_with_downloadContentState_13(self):
		filter_response = call_ref_url("get", make_booking_filter_url("reminderState=notReminded&downloadContentState=complete"))
		assert filter_response.status_code == 200

	def test_reminderState_with_downloadContentState_14(self):
		filter_response = call_ref_url("get", make_booking_filter_url("reminderState=notReminded&downloadContentState=partial,complete"))
		assert filter_response.status_code == 200

	def test_reminderState_with_embed_15(self):
		filter_response = call_ref_url("get", make_booking_filter_url("reminderState=notReminded&embed=eventBooking"))
		assert filter_response.status_code == 200

	def test_reminderState_with_embed_16(self):
		filter_response = call_ref_url("get", make_booking_filter_url("reminderState=notReminded&embed=seasonBooking"))
		assert filter_response.status_code == 200

	def test_reminderState_with_embed_17(self):
		filter_response = call_ref_url("get", make_booking_filter_url("reminderState=notReminded&embed=transcodeBooking"))
		assert filter_response.status_code == 200

	def test_reminderState_with_embed_18(self):
		filter_response = call_ref_url("get", make_booking_filter_url("reminderState=notReminded&embed=transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_reminderState_with_embed_19(self):
		filter_response = call_ref_url("get", make_booking_filter_url("reminderState=notReminded&embed=reminderBooking"))
		assert filter_response.status_code == 200

	def test_reminderState_with_embed_20(self):
		filter_response = call_ref_url("get", make_booking_filter_url("reminderState=notReminded&embed=eventBooking,seasonBooking"))
		assert filter_response.status_code == 200

	def test_reminderState_with_embed_21(self):
		filter_response = call_ref_url("get", make_booking_filter_url("reminderState=notReminded&embed=eventBooking,seasonBooking,transcodeBooking"))
		assert filter_response.status_code == 200

	def test_reminderState_with_embed_22(self):
		filter_response = call_ref_url("get", make_booking_filter_url("reminderState=notReminded&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_reminderState_with_embed_23(self):
		filter_response = call_ref_url("get", make_booking_filter_url("reminderState=notReminded&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking,reminderBooking"))
		assert filter_response.status_code == 200

	def test_reminderState_with_bookingType_24(self):
		filter_response = call_ref_url("get", make_booking_filter_url("reminderState=notReminded&bookingType=manual"))
		assert filter_response.status_code == 200

	def test_reminderState_with_bookingType_25(self):
		filter_response = call_ref_url("get", make_booking_filter_url("reminderState=notReminded&bookingType=event"))
		assert filter_response.status_code == 200

	def test_reminderState_with_bookingType_26(self):
		filter_response = call_ref_url("get", make_booking_filter_url("reminderState=notReminded&bookingType=manual,event"))
		assert filter_response.status_code == 200


class TestdownloadStateMajor:
	def test_downloadState_with_recordingState_1(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted&recordingState=notStarted"))
		assert filter_response.status_code == 200

	def test_downloadState_with_recordingState_2(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted&recordingState=inProgress"))
		assert filter_response.status_code == 200

	def test_downloadState_with_recordingState_3(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted&recordingState=notStarted,inProgress"))
		assert filter_response.status_code == 200

	def test_downloadState_with_recordingContentState_4(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted&recordingContentState=partial"))
		assert filter_response.status_code == 200

	def test_downloadState_with_recordingContentState_5(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted&recordingContentState=complete"))
		assert filter_response.status_code == 200

	def test_downloadState_with_recordingContentState_6(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted&recordingContentState=partial,complete"))
		assert filter_response.status_code == 200

	def test_downloadState_with_downloadContentState_7(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted&downloadContentState=partial"))
		assert filter_response.status_code == 200

	def test_downloadState_with_downloadContentState_8(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted&downloadContentState=complete"))
		assert filter_response.status_code == 200

	def test_downloadState_with_downloadContentState_9(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted&downloadContentState=partial,complete"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_10(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted&embed=eventBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_11(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted&embed=seasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_12(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted&embed=transcodeBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_13(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted&embed=transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_14(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted&embed=reminderBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_15(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted&embed=eventBooking,seasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_16(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted&embed=eventBooking,seasonBooking,transcodeBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_17(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_18(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking,reminderBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_bookingType_19(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted&bookingType=manual"))
		assert filter_response.status_code == 200

	def test_downloadState_with_bookingType_20(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted&bookingType=event"))
		assert filter_response.status_code == 200

	def test_downloadState_with_bookingType_21(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted&bookingType=manual,event"))
		assert filter_response.status_code == 200

	def test_downloadState_with_recordingState_22(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=inProgress&recordingState=notStarted"))
		assert filter_response.status_code == 200

	def test_downloadState_with_recordingState_23(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=inProgress&recordingState=inProgress"))
		assert filter_response.status_code == 200

	def test_downloadState_with_recordingState_24(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=inProgress&recordingState=notStarted,inProgress"))
		assert filter_response.status_code == 200

	def test_downloadState_with_recordingContentState_25(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=inProgress&recordingContentState=partial"))
		assert filter_response.status_code == 200

	def test_downloadState_with_recordingContentState_26(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=inProgress&recordingContentState=complete"))
		assert filter_response.status_code == 200

	def test_downloadState_with_recordingContentState_27(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=inProgress&recordingContentState=partial,complete"))
		assert filter_response.status_code == 200

	def test_downloadState_with_downloadContentState_28(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=inProgress&downloadContentState=partial"))
		assert filter_response.status_code == 200

	def test_downloadState_with_downloadContentState_29(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=inProgress&downloadContentState=complete"))
		assert filter_response.status_code == 200

	def test_downloadState_with_downloadContentState_30(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=inProgress&downloadContentState=partial,complete"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_31(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=inProgress&embed=eventBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_32(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=inProgress&embed=seasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_33(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=inProgress&embed=transcodeBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_34(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=inProgress&embed=transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_35(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=inProgress&embed=reminderBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_36(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=inProgress&embed=eventBooking,seasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_37(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=inProgress&embed=eventBooking,seasonBooking,transcodeBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_38(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=inProgress&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_39(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=inProgress&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking,reminderBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_bookingType_40(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=inProgress&bookingType=manual"))
		assert filter_response.status_code == 200

	def test_downloadState_with_bookingType_41(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=inProgress&bookingType=event"))
		assert filter_response.status_code == 200

	def test_downloadState_with_bookingType_42(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=inProgress&bookingType=manual,event"))
		assert filter_response.status_code == 200

	def test_downloadState_with_recordingState_43(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=suspended&recordingState=notStarted"))
		assert filter_response.status_code == 200

	def test_downloadState_with_recordingState_44(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=suspended&recordingState=inProgress"))
		assert filter_response.status_code == 200

	def test_downloadState_with_recordingState_45(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=suspended&recordingState=notStarted,inProgress"))
		assert filter_response.status_code == 200

	def test_downloadState_with_recordingContentState_46(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=suspended&recordingContentState=partial"))
		assert filter_response.status_code == 200

	def test_downloadState_with_recordingContentState_47(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=suspended&recordingContentState=complete"))
		assert filter_response.status_code == 200

	def test_downloadState_with_recordingContentState_48(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=suspended&recordingContentState=partial,complete"))
		assert filter_response.status_code == 200

	def test_downloadState_with_downloadContentState_49(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=suspended&downloadContentState=partial"))
		assert filter_response.status_code == 200

	def test_downloadState_with_downloadContentState_50(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=suspended&downloadContentState=complete"))
		assert filter_response.status_code == 200

	def test_downloadState_with_downloadContentState_51(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=suspended&downloadContentState=partial,complete"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_52(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=suspended&embed=eventBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_53(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=suspended&embed=seasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_54(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=suspended&embed=transcodeBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_55(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=suspended&embed=transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_56(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=suspended&embed=reminderBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_57(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=suspended&embed=eventBooking,seasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_58(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=suspended&embed=eventBooking,seasonBooking,transcodeBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_59(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=suspended&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_60(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=suspended&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking,reminderBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_bookingType_61(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=suspended&bookingType=manual"))
		assert filter_response.status_code == 200

	def test_downloadState_with_bookingType_62(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=suspended&bookingType=event"))
		assert filter_response.status_code == 200

	def test_downloadState_with_bookingType_63(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=suspended&bookingType=manual,event"))
		assert filter_response.status_code == 200

	def test_downloadState_with_recordingState_64(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress&recordingState=notStarted"))
		assert filter_response.status_code == 200

	def test_downloadState_with_recordingState_65(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress&recordingState=inProgress"))
		assert filter_response.status_code == 200

	def test_downloadState_with_recordingState_66(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress&recordingState=notStarted,inProgress"))
		assert filter_response.status_code == 200

	def test_downloadState_with_recordingContentState_67(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress&recordingContentState=partial"))
		assert filter_response.status_code == 200

	def test_downloadState_with_recordingContentState_68(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress&recordingContentState=complete"))
		assert filter_response.status_code == 200

	def test_downloadState_with_recordingContentState_69(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress&recordingContentState=partial,complete"))
		assert filter_response.status_code == 200

	def test_downloadState_with_downloadContentState_70(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress&downloadContentState=partial"))
		assert filter_response.status_code == 200

	def test_downloadState_with_downloadContentState_71(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress&downloadContentState=complete"))
		assert filter_response.status_code == 200

	def test_downloadState_with_downloadContentState_72(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress&downloadContentState=partial,complete"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_73(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress&embed=eventBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_74(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress&embed=seasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_75(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress&embed=transcodeBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_76(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress&embed=transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_77(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress&embed=reminderBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_78(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress&embed=eventBooking,seasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_79(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress&embed=eventBooking,seasonBooking,transcodeBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_80(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_81(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking,reminderBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_bookingType_82(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress&bookingType=manual"))
		assert filter_response.status_code == 200

	def test_downloadState_with_bookingType_83(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress&bookingType=event"))
		assert filter_response.status_code == 200

	def test_downloadState_with_bookingType_84(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress&bookingType=manual,event"))
		assert filter_response.status_code == 200

	def test_downloadState_with_recordingState_85(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress,suspended&recordingState=notStarted"))
		assert filter_response.status_code == 200

	def test_downloadState_with_recordingState_86(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress,suspended&recordingState=inProgress"))
		assert filter_response.status_code == 200

	def test_downloadState_with_recordingState_87(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress,suspended&recordingState=notStarted,inProgress"))
		assert filter_response.status_code == 200

	def test_downloadState_with_recordingContentState_88(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress,suspended&recordingContentState=partial"))
		assert filter_response.status_code == 200

	def test_downloadState_with_recordingContentState_89(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress,suspended&recordingContentState=complete"))
		assert filter_response.status_code == 200

	def test_downloadState_with_recordingContentState_90(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress,suspended&recordingContentState=partial,complete"))
		assert filter_response.status_code == 200

	def test_downloadState_with_downloadContentState_91(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress,suspended&downloadContentState=partial"))
		assert filter_response.status_code == 200

	def test_downloadState_with_downloadContentState_92(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress,suspended&downloadContentState=complete"))
		assert filter_response.status_code == 200

	def test_downloadState_with_downloadContentState_93(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress,suspended&downloadContentState=partial,complete"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_94(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress,suspended&embed=eventBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_95(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress,suspended&embed=seasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_96(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress,suspended&embed=transcodeBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_97(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress,suspended&embed=transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_98(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress,suspended&embed=reminderBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_99(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress,suspended&embed=eventBooking,seasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_100(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress,suspended&embed=eventBooking,seasonBooking,transcodeBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_101(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress,suspended&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_embed_102(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress,suspended&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking,reminderBooking"))
		assert filter_response.status_code == 200

	def test_downloadState_with_bookingType_103(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress,suspended&bookingType=manual"))
		assert filter_response.status_code == 200

	def test_downloadState_with_bookingType_104(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress,suspended&bookingType=event"))
		assert filter_response.status_code == 200

	def test_downloadState_with_bookingType_105(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadState=notStarted,inProgress,suspended&bookingType=manual,event"))
		assert filter_response.status_code == 200


class TestrecordingStateMajor:
	def test_recordingState_with_recordingContentState_1(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted&recordingContentState=partial"))
		assert filter_response.status_code == 200

	def test_recordingState_with_recordingContentState_2(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted&recordingContentState=complete"))
		assert filter_response.status_code == 200

	def test_recordingState_with_recordingContentState_3(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted&recordingContentState=partial,complete"))
		assert filter_response.status_code == 200

	def test_recordingState_with_downloadContentState_4(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted&downloadContentState=partial"))
		assert filter_response.status_code == 200

	def test_recordingState_with_downloadContentState_5(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted&downloadContentState=complete"))
		assert filter_response.status_code == 200

	def test_recordingState_with_downloadContentState_6(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted&downloadContentState=partial,complete"))
		assert filter_response.status_code == 200

	def test_recordingState_with_embed_7(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted&embed=eventBooking"))
		assert filter_response.status_code == 200

	def test_recordingState_with_embed_8(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted&embed=seasonBooking"))
		assert filter_response.status_code == 200

	def test_recordingState_with_embed_9(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted&embed=transcodeBooking"))
		assert filter_response.status_code == 200

	def test_recordingState_with_embed_10(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted&embed=transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_recordingState_with_embed_11(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted&embed=reminderBooking"))
		assert filter_response.status_code == 200

	def test_recordingState_with_embed_12(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted&embed=eventBooking,seasonBooking"))
		assert filter_response.status_code == 200

	def test_recordingState_with_embed_13(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted&embed=eventBooking,seasonBooking,transcodeBooking"))
		assert filter_response.status_code == 200

	def test_recordingState_with_embed_14(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_recordingState_with_embed_15(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking,reminderBooking"))
		assert filter_response.status_code == 200

	def test_recordingState_with_bookingType_16(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted&bookingType=manual"))
		assert filter_response.status_code == 200

	def test_recordingState_with_bookingType_17(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted&bookingType=event"))
		assert filter_response.status_code == 200

	def test_recordingState_with_bookingType_18(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted&bookingType=manual,event"))
		assert filter_response.status_code == 200

	def test_recordingState_with_recordingContentState_19(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=inProgress&recordingContentState=partial"))
		assert filter_response.status_code == 200

	def test_recordingState_with_recordingContentState_20(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=inProgress&recordingContentState=complete"))
		assert filter_response.status_code == 200

	def test_recordingState_with_recordingContentState_21(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=inProgress&recordingContentState=partial,complete"))
		assert filter_response.status_code == 200

	def test_recordingState_with_downloadContentState_22(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=inProgress&downloadContentState=partial"))
		assert filter_response.status_code == 200

	def test_recordingState_with_downloadContentState_23(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=inProgress&downloadContentState=complete"))
		assert filter_response.status_code == 200

	def test_recordingState_with_downloadContentState_24(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=inProgress&downloadContentState=partial,complete"))
		assert filter_response.status_code == 200

	def test_recordingState_with_embed_25(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=inProgress&embed=eventBooking"))
		assert filter_response.status_code == 200

	def test_recordingState_with_embed_26(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=inProgress&embed=seasonBooking"))
		assert filter_response.status_code == 200

	def test_recordingState_with_embed_27(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=inProgress&embed=transcodeBooking"))
		assert filter_response.status_code == 200

	def test_recordingState_with_embed_28(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=inProgress&embed=transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_recordingState_with_embed_29(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=inProgress&embed=reminderBooking"))
		assert filter_response.status_code == 200

	def test_recordingState_with_embed_30(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=inProgress&embed=eventBooking,seasonBooking"))
		assert filter_response.status_code == 200

	def test_recordingState_with_embed_31(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=inProgress&embed=eventBooking,seasonBooking,transcodeBooking"))
		assert filter_response.status_code == 200

	def test_recordingState_with_embed_32(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=inProgress&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_recordingState_with_embed_33(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=inProgress&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking,reminderBooking"))
		assert filter_response.status_code == 200

	def test_recordingState_with_bookingType_34(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=inProgress&bookingType=manual"))
		assert filter_response.status_code == 200

	def test_recordingState_with_bookingType_35(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=inProgress&bookingType=event"))
		assert filter_response.status_code == 200

	def test_recordingState_with_bookingType_36(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=inProgress&bookingType=manual,event"))
		assert filter_response.status_code == 200

	def test_recordingState_with_recordingContentState_37(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted,inProgress&recordingContentState=partial"))
		assert filter_response.status_code == 200

	def test_recordingState_with_recordingContentState_38(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted,inProgress&recordingContentState=complete"))
		assert filter_response.status_code == 200

	def test_recordingState_with_recordingContentState_39(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted,inProgress&recordingContentState=partial,complete"))
		assert filter_response.status_code == 200

	def test_recordingState_with_downloadContentState_40(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted,inProgress&downloadContentState=partial"))
		assert filter_response.status_code == 200

	def test_recordingState_with_downloadContentState_41(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted,inProgress&downloadContentState=complete"))
		assert filter_response.status_code == 200

	def test_recordingState_with_downloadContentState_42(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted,inProgress&downloadContentState=partial,complete"))
		assert filter_response.status_code == 200

	def test_recordingState_with_embed_43(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted,inProgress&embed=eventBooking"))
		assert filter_response.status_code == 200

	def test_recordingState_with_embed_44(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted,inProgress&embed=seasonBooking"))
		assert filter_response.status_code == 200

	def test_recordingState_with_embed_45(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted,inProgress&embed=transcodeBooking"))
		assert filter_response.status_code == 200

	def test_recordingState_with_embed_46(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted,inProgress&embed=transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_recordingState_with_embed_47(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted,inProgress&embed=reminderBooking"))
		assert filter_response.status_code == 200

	def test_recordingState_with_embed_48(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted,inProgress&embed=eventBooking,seasonBooking"))
		assert filter_response.status_code == 200

	def test_recordingState_with_embed_49(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted,inProgress&embed=eventBooking,seasonBooking,transcodeBooking"))
		assert filter_response.status_code == 200

	def test_recordingState_with_embed_50(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted,inProgress&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_recordingState_with_embed_51(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted,inProgress&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking,reminderBooking"))
		assert filter_response.status_code == 200

	def test_recordingState_with_bookingType_52(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted,inProgress&bookingType=manual"))
		assert filter_response.status_code == 200

	def test_recordingState_with_bookingType_53(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted,inProgress&bookingType=event"))
		assert filter_response.status_code == 200

	def test_recordingState_with_bookingType_54(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingState=notStarted,inProgress&bookingType=manual,event"))
		assert filter_response.status_code == 200


class TestrecordingContentStateMajor:
	def test_recordingContentState_with_downloadContentState_1(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial&downloadContentState=partial"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_downloadContentState_2(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial&downloadContentState=complete"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_downloadContentState_3(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial&downloadContentState=partial,complete"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_embed_4(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial&embed=eventBooking"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_embed_5(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial&embed=seasonBooking"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_embed_6(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial&embed=transcodeBooking"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_embed_7(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial&embed=transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_embed_8(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial&embed=reminderBooking"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_embed_9(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial&embed=eventBooking,seasonBooking"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_embed_10(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial&embed=eventBooking,seasonBooking,transcodeBooking"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_embed_11(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_embed_12(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking,reminderBooking"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_bookingType_13(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial&bookingType=manual"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_bookingType_14(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial&bookingType=event"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_bookingType_15(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial&bookingType=manual,event"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_downloadContentState_16(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=complete&downloadContentState=partial"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_downloadContentState_17(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=complete&downloadContentState=complete"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_downloadContentState_18(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=complete&downloadContentState=partial,complete"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_embed_19(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=complete&embed=eventBooking"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_embed_20(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=complete&embed=seasonBooking"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_embed_21(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=complete&embed=transcodeBooking"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_embed_22(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=complete&embed=transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_embed_23(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=complete&embed=reminderBooking"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_embed_24(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=complete&embed=eventBooking,seasonBooking"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_embed_25(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=complete&embed=eventBooking,seasonBooking,transcodeBooking"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_embed_26(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=complete&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_embed_27(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=complete&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking,reminderBooking"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_bookingType_28(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=complete&bookingType=manual"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_bookingType_29(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=complete&bookingType=event"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_bookingType_30(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=complete&bookingType=manual,event"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_downloadContentState_31(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial,complete&downloadContentState=partial"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_downloadContentState_32(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial,complete&downloadContentState=complete"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_downloadContentState_33(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial,complete&downloadContentState=partial,complete"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_embed_34(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial,complete&embed=eventBooking"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_embed_35(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial,complete&embed=seasonBooking"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_embed_36(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial,complete&embed=transcodeBooking"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_embed_37(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial,complete&embed=transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_embed_38(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial,complete&embed=reminderBooking"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_embed_39(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial,complete&embed=eventBooking,seasonBooking"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_embed_40(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial,complete&embed=eventBooking,seasonBooking,transcodeBooking"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_embed_41(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial,complete&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_embed_42(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial,complete&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking,reminderBooking"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_bookingType_43(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial,complete&bookingType=manual"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_bookingType_44(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial,complete&bookingType=event"))
		assert filter_response.status_code == 200

	def test_recordingContentState_with_bookingType_45(self):
		filter_response = call_ref_url("get", make_booking_filter_url("recordingContentState=partial,complete&bookingType=manual,event"))
		assert filter_response.status_code == 200


class TestdownloadContentStateMajor:
	def test_downloadContentState_with_embed_1(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=partial&embed=eventBooking"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_embed_2(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=partial&embed=seasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_embed_3(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=partial&embed=transcodeBooking"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_embed_4(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=partial&embed=transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_embed_5(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=partial&embed=reminderBooking"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_embed_6(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=partial&embed=eventBooking,seasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_embed_7(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=partial&embed=eventBooking,seasonBooking,transcodeBooking"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_embed_8(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=partial&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_embed_9(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=partial&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking,reminderBooking"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_bookingType_10(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=partial&bookingType=manual"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_bookingType_11(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=partial&bookingType=event"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_bookingType_12(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=partial&bookingType=manual,event"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_embed_13(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=complete&embed=eventBooking"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_embed_14(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=complete&embed=seasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_embed_15(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=complete&embed=transcodeBooking"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_embed_16(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=complete&embed=transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_embed_17(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=complete&embed=reminderBooking"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_embed_18(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=complete&embed=eventBooking,seasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_embed_19(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=complete&embed=eventBooking,seasonBooking,transcodeBooking"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_embed_20(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=complete&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_embed_21(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=complete&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking,reminderBooking"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_bookingType_22(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=complete&bookingType=manual"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_bookingType_23(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=complete&bookingType=event"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_bookingType_24(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=complete&bookingType=manual,event"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_embed_25(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=partial,complete&embed=eventBooking"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_embed_26(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=partial,complete&embed=seasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_embed_27(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=partial,complete&embed=transcodeBooking"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_embed_28(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=partial,complete&embed=transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_embed_29(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=partial,complete&embed=reminderBooking"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_embed_30(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=partial,complete&embed=eventBooking,seasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_embed_31(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=partial,complete&embed=eventBooking,seasonBooking,transcodeBooking"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_embed_32(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=partial,complete&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_embed_33(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=partial,complete&embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking,reminderBooking"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_bookingType_34(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=partial,complete&bookingType=manual"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_bookingType_35(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=partial,complete&bookingType=event"))
		assert filter_response.status_code == 200

	def test_downloadContentState_with_bookingType_36(self):
		filter_response = call_ref_url("get", make_booking_filter_url("downloadContentState=partial,complete&bookingType=manual,event"))
		assert filter_response.status_code == 200


class TestembedMajor:
	def test_embed_with_bookingType_1(self):
		filter_response = call_ref_url("get", make_booking_filter_url("embed=eventBooking&bookingType=manual"))
		assert filter_response.status_code == 200

	def test_embed_with_bookingType_2(self):
		filter_response = call_ref_url("get", make_booking_filter_url("embed=eventBooking&bookingType=event"))
		assert filter_response.status_code == 200

	def test_embed_with_bookingType_3(self):
		filter_response = call_ref_url("get", make_booking_filter_url("embed=eventBooking&bookingType=manual,event"))
		assert filter_response.status_code == 200

	def test_embed_with_bookingType_4(self):
		filter_response = call_ref_url("get", make_booking_filter_url("embed=seasonBooking&bookingType=manual"))
		assert filter_response.status_code == 200

	def test_embed_with_bookingType_5(self):
		filter_response = call_ref_url("get", make_booking_filter_url("embed=seasonBooking&bookingType=event"))
		assert filter_response.status_code == 200

	def test_embed_with_bookingType_6(self):
		filter_response = call_ref_url("get", make_booking_filter_url("embed=seasonBooking&bookingType=manual,event"))
		assert filter_response.status_code == 200

	def test_embed_with_bookingType_7(self):
		filter_response = call_ref_url("get", make_booking_filter_url("embed=transcodeBooking&bookingType=manual"))
		assert filter_response.status_code == 200

	def test_embed_with_bookingType_8(self):
		filter_response = call_ref_url("get", make_booking_filter_url("embed=transcodeBooking&bookingType=event"))
		assert filter_response.status_code == 200

	def test_embed_with_bookingType_9(self):
		filter_response = call_ref_url("get", make_booking_filter_url("embed=transcodeBooking&bookingType=manual,event"))
		assert filter_response.status_code == 200

	def test_embed_with_bookingType_10(self):
		filter_response = call_ref_url("get", make_booking_filter_url("embed=transcodeSeasonBooking&bookingType=manual"))
		assert filter_response.status_code == 200

	def test_embed_with_bookingType_11(self):
		filter_response = call_ref_url("get", make_booking_filter_url("embed=transcodeSeasonBooking&bookingType=event"))
		assert filter_response.status_code == 200

	def test_embed_with_bookingType_12(self):
		filter_response = call_ref_url("get", make_booking_filter_url("embed=transcodeSeasonBooking&bookingType=manual,event"))
		assert filter_response.status_code == 200

	def test_embed_with_bookingType_13(self):
		filter_response = call_ref_url("get", make_booking_filter_url("embed=reminderBooking&bookingType=manual"))
		assert filter_response.status_code == 200

	def test_embed_with_bookingType_14(self):
		filter_response = call_ref_url("get", make_booking_filter_url("embed=reminderBooking&bookingType=event"))
		assert filter_response.status_code == 200

	def test_embed_with_bookingType_15(self):
		filter_response = call_ref_url("get", make_booking_filter_url("embed=reminderBooking&bookingType=manual,event"))
		assert filter_response.status_code == 200

	def test_embed_with_bookingType_16(self):
		filter_response = call_ref_url("get", make_booking_filter_url("embed=eventBooking,seasonBooking&bookingType=manual"))
		assert filter_response.status_code == 200

	def test_embed_with_bookingType_17(self):
		filter_response = call_ref_url("get", make_booking_filter_url("embed=eventBooking,seasonBooking&bookingType=event"))
		assert filter_response.status_code == 200

	def test_embed_with_bookingType_18(self):
		filter_response = call_ref_url("get", make_booking_filter_url("embed=eventBooking,seasonBooking&bookingType=manual,event"))
		assert filter_response.status_code == 200

	def test_embed_with_bookingType_19(self):
		filter_response = call_ref_url("get", make_booking_filter_url("embed=eventBooking,seasonBooking,transcodeBooking&bookingType=manual"))
		assert filter_response.status_code == 200

	def test_embed_with_bookingType_20(self):
		filter_response = call_ref_url("get", make_booking_filter_url("embed=eventBooking,seasonBooking,transcodeBooking&bookingType=event"))
		assert filter_response.status_code == 200

	def test_embed_with_bookingType_21(self):
		filter_response = call_ref_url("get", make_booking_filter_url("embed=eventBooking,seasonBooking,transcodeBooking&bookingType=manual,event"))
		assert filter_response.status_code == 200

	def test_embed_with_bookingType_22(self):
		filter_response = call_ref_url("get", make_booking_filter_url("embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking&bookingType=manual"))
		assert filter_response.status_code == 200

	def test_embed_with_bookingType_23(self):
		filter_response = call_ref_url("get", make_booking_filter_url("embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking&bookingType=event"))
		assert filter_response.status_code == 200

	def test_embed_with_bookingType_24(self):
		filter_response = call_ref_url("get", make_booking_filter_url("embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking&bookingType=manual,event"))
		assert filter_response.status_code == 200

	def test_embed_with_bookingType_25(self):
		filter_response = call_ref_url("get", make_booking_filter_url("embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking,reminderBooking&bookingType=manual"))
		assert filter_response.status_code == 200

	def test_embed_with_bookingType_26(self):
		filter_response = call_ref_url("get", make_booking_filter_url("embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking,reminderBooking&bookingType=event"))
		assert filter_response.status_code == 200

	def test_embed_with_bookingType_27(self):
		filter_response = call_ref_url("get", make_booking_filter_url("embed=eventBooking,seasonBooking,transcodeBooking,transcodeSeasonBooking,reminderBooking&bookingType=manual,event"))
		assert filter_response.status_code == 200

