# Решение загружать настройки через `sys.modules[__name__] = ...` может не
# сильно понравиться в начале. Но самое решение very pythonic:
#   * Beautiful is better than ugly.
#   * Simple is better than complex
#   * Readability counts.
#   * If the implementation is hard to explain, it's a bad idea.
#   (Zen of python)
#
# Так это ещё и 'hack that is occasionally used and recommended'
# https://mail.python.org/pipermail/python-ideas/2012-May/014969.html (Guido van Rossum)

import os
import sys


if os.getenv('ENVIRONMENT') == 'PROD':
    from ._prod import Settings
else:
    from ._dev import Settings

sys.modules[__name__] = Settings()  # type: ignore[assignment]
