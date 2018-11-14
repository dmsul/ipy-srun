import os

from IPython import get_ipython
from IPython.core.magic import (Magics, magics_class, line_magic)
import winsound

ipy = get_ipython()

this_dir, this_filename = os.path.split(__file__)
WAVE_PATH = os.path.join(this_dir, 'Startup1.wav')


@magics_class
class Srun(Magics):

    @line_magic
    def srun(self, line):
        ipy.run_line_magic('run', line)
        winsound.Beep(440, 300)
        winsound.Beep(440, 300)
        winsound.Beep(440, 300)
        winsound.Beep(340, 1000)
        winsound.PlaySound(WAVE_PATH,
                           winsound.SND_FILENAME | winsound.SND_ASYNC)
