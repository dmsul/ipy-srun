from setuptools import setup, find_packages

desc = (
    'An IPython magic that calls `%run` and then plays a sound when done.'
)


setup(name='srun',
      version='0.0.1',
      description=desc,
      author='Daniel M. Sullivan',
      packages=find_packages(),
      include_package_data=True,        # To copy stuff in `MANIFEST.in`
      license='BSD'
      )
