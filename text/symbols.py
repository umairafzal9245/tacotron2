""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details. '''
from text import cmudict

_pad        = '_'
_punctuation = '!\'(),.:;? '
_special = '-'
_letters = 'ع ث پ ض د خ ط ۶ ۵  ؔ ه ۹ غ ظ ﷲ ة گ ؤ ح ك ن ﺅ ذ ي م ژ ڑ ھ ٹ ٢ چ ج ک ب ڈ ل ۂ ۓ ص ے و ٸ ت ق ﷺ ء ں س ی ش ر ز ف أ ئ ۃ آ ۲ ۳'

# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
_arpabet = ['@' + s for s in cmudict.valid_symbols]

# Export all symbols:
symbols = [_pad] + list(_special) + list(_punctuation) + list(_letters) + _arpabet
