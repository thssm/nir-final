import ctypes
from constants import *

class CONFIG_HEAD(ctypes.Structure):
	_fields_ = [
		("scan_type", ctypes.c_uint8),
		("scanConfigIndex", ctypes.c_uint16),
		("ScanConfig_serial_number", ctypes.c_char * SER_NUM_LEN),
		("config_name", ctypes.c_char * SCAN_CFG_FILENAME_LEN),
		("num_repeats", ctypes.c_uint16),
		("num_sections", ctypes.c_uint8),
	]

class ScanSection(ctypes.Structure):
	_fields_ = [
		("section_scan_type", ctypes.c_uint8),
		("width_px", ctypes.c_uint8),
		("wavelength_start_nm", ctypes.c_uint16),
		("wavelength_end_nm", ctypes.c_uint16),
		("num_patterns", ctypes.c_uint16),
		("exposure_time", ctypes.c_uint16),
	]

class calibCoeffs(ctypes.Structure):
	_fields_ = [
		("ShiftVectorCoeffs", ctypes.c_double * 3),
		("PixelToWavelengthCoeffs", ctypes.c_double * 3),
	]

class ScanConfig(ctypes.Structure):
	_fields_ = [
		("head", CONFIG_HEAD),
		("section", ScanSection * SCAN_MAX_SECTIONS)
	]

class ScanResult(ctypes.Structure):
	_fields_ = [
		("wavelength", ctypes.c_double * 864),
		("intensity", ctypes.c_long * 864),
		("length", ctypes.c_int),
	]