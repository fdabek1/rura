from setuptools import setup
from setuptools import find_packages

long_description = '''
Rura is a pipeline for machine learning.
'''

setup(name='rura',
      version='0.1.0',
      description='Pipelines for machine learning',
      long_description=long_description,
      author='Filip Dabek',
      url='https://github.com/fdabek1/rura',
      download_url='https://github.com/fdabek1/rura/tarball/0.1.0',
      license='MIT',
      install_requires=[
          'mlflow',
          'numpy>=1.9.1',
          'scipy>=0.14',
          'six>=1.9.0',
          'pyyaml',
          'h5py',
          'python-dotenv',
      ],
      extras_require={
          'tests': ['pytest',
                    'pytest-pep8',
                    'pytest-xdist',
                    'flaky',
                    'pytest-cov',
                    'pandas',
                    'requests',
                    'markdown'],
      },
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      packages=find_packages())
