from setuptools import setup
setup(name='dats-lab',
      version='0.0.31',
      description='Data Science Utilities & Helpers',
      url='https://github.com/cbalkig/DataScienceUtils.git',
      author='C. Balkı Gemirter',
      author_email='cavide.balki@gmail.com',
      license='MIT',
      packages=['datslab.trends', 'datslab.lr', 'datslab.common'],
      install_requires=['statsmodels==0.13.1',
                        'matplotlib>=3.5.1',
                        'pandas>=1.3.5',
                        'numpy==1.21.4',
                        'arviz==0.11.4',
                        'pymc3==3.11.4',
                        'causalgraphicalmodels>=0.0.4',
                        'daft>=0.1.2'])
