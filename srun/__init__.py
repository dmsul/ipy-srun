__version__ = '0.0.1'

from .srun import Srun


def load_ipython_extension(ipython):
    ipython.register_magics(Srun)
