"""Common data objects referenced across the app."""

# pylint: disable=too-few-public-methods


class DailyPrayer(object):
  """Server-wide canonical representation for daily prayers."""
  UNSPECIFIED = 0
  FAJR = 1
  SUNRISE = 2
  DHUHR = 3
  ASR = 4
  MAGHRIB = 5
  ISHA = 6
  QIYAM = 7


class Intent(object):
  """Server-wide canonical representation for Intents from API.AI."""
  UNSPECIFIED = 0
  WHEN_IS_PRAYER = 1
  WHEN_IS_PRAYER_NAME = 2


class Locality(object):
  """Locality implies the type of query - whether city-based or masjid-based."""
  UNSPECIFIED = 0
  CITY = 1
  MASJID = 2


class CalculationMethod(object):
  UNSPECIFIED = 0
  KAR = 1
  ISNA = 2
  MWL = 3
  MAKKAH = 4
  EGYPT = 5
  TEHRAN = 7
  GULF = 8
  KUWAIT = 9
  QATAR = 10
  SINGAPORE = 11
  FRANCE = 12
  TURKEY = 13

