from setuptools import setup
setup(name='data-science-utils',
      version='0.1',
      description='Data Science Utilities',
      url='https://github.com/cbalkig/DataScienceUtils.git',
      author='C. Balkı Gemirter',
      author_email='cavide.balki@gmail.com',
      license='MIT',
      packages=['module'],
      install_requires=['statsmodels>=0.13.1',
                        'matplotlib>=3.5.1',
                        'pandas>=1.3.5'])
