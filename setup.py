from setuptools import setup
setup(name='dats-lab',
      version='0.0.3',
      description='Data Science Utilities & Helpers',
      url='https://github.com/cbalkig/DataScienceUtils.git',
      author='C. Balkı Gemirter',
      author_email='cavide.balki@gmail.com',
      license='MIT',
      packages=['datslab'],
      install_requires=['statsmodels>=0.13.1',
                        'matplotlib>=3.5.1',
                        'pandas>=1.3.5'])
