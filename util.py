import json
from flask import make_response
from common import DailyPrayer 


def JsonResponse(response_dict):
  """Constructs a JSON response object."""
  response = make_response(json.dumps(response_dict, indent=4))
  response.headers['Content-Type'] = 'application/json'
  return response


def JsonError(error_text):
  """Constructs a JSON response from an error."""
  response = make_response(json.dumps({'error': error_text}, indent=4))
  response.headers['Content-Type'] = 'application/json'
  return response


_PRAYER_METADATA = {
  DailyPrayer.FAJR: {
    'key_name': 'fajr',
    'proper_name': 'Fajr',
  },
  DailyPrayer.DHUHR: {
    'key_name': 'dhuhr',
    'proper_name': 'Dhuhr',
  },
  DailyPrayer.ASR: {
    'key_name': 'asr',
    'proper_name': 'Asr',
  },
  DailyPrayer.MAGHRIB: {
    'key_name': 'maghrib',
    'proper_name': 'Maghrib',
  },
  DailyPrayer.ISHA: {
    'key_name': 'isha',
    'proper_name': 'Isha',
  },
  DailyPrayer.QIYAM: {
    'key_name': 'qiyam',
    'proper_name': 'Qiyam'
  },
  DailyPrayer.UNSPECIFIED: {
    'key_name': 'unpsecified',
    'proper_name': 'unspecified'
  },
}

_KEY_NAME_TO_PRAYER = {
  'fajr': DailyPrayer.FAJR,
  'dhuhr': DailyPrayer.DHUHR,
  'asr': DailyPrayer.ASR,
  'maghrib': DailyPrayer.MAGHRIB,
  'isha': DailyPrayer.ISHA,
  'qiyam': DailyPrayer.QIYAM,
  'unspecified': DailyPrayer.UNSPECIFIED,
}

def GetPrayerKeyName(daily_prayer):
  """Gets the name of a daily prayer (ex: "fajr")."""
  print daily_prayer
  return _PRAYER_METADATA.get(daily_prayer).get('key_name')

def StringToDailyPrayer(prayer_str):
  """Infers a DailyPrayer out of a string."""
  prayer_str = str(prayer_str).lower()
  if prayer_str in _KEY_NAME_TO_PRAYER:
    return _KEY_NAME_TO_PRAYER[prayer_str]
  else:
    return DailyPrayer.UNSPECIFIED

