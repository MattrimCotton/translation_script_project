from translate import Translator

class TextTranslator:
    def __init__(self):
        # Initialisation sans langue cible, elle sera définie dynamiquement
        self.translator = None

    def _split_text(self, text, max_length=500):
        # Divise le texte en segments plus petits pour respecter la limite de caractères
        segments = []
        current_segment = ''
        for line in text.splitlines(keepends=True):  # Maintient les nouvelles lignes
            if len(current_segment) + len(line) > max_length:
                segments.append(current_segment)
                current_segment = line
            else:
                current_segment += line
        if current_segment:
            segments.append(current_segment)
        return segments

    def _translate_text(self, text):
        segments = self._split_text(text)
        translated_text = ''
        for segment in segments:
            translated_text += self.translator.translate(segment) + ' '
        return translated_text.strip()

    def translate_to_french(self, text):
        # Configurer le traducteur pour traduire en français
        self.translator = Translator(to_lang='fr')
        return self._translate_text(text)

    def translate_to_english(self, text):
        # Configurer le traducteur pour traduire en anglais
        self.translator = Translator(to_lang='en')
        return self._translate_text(text)
