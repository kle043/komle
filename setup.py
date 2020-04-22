from setuptools import setup, find_packages

setup(
      name='komle',
      version='0.1',
      description='A python library to help with WITSML v1.4.1.1',
      url='https://github.com/knle88/komle',
      packages=find_packages(exclude=('tests',)),
      author='kle043',
      include_package_data=True,
      package_data={
                    'komle': ['WMLS.WSDL', 'witsmlUnitDict.xml'],
                   },
      install_requires=['suds-py3==1.4.0.0',
                        'PyXB==1.2.6',

                       ], 
      tests_require=[
                     'pytest>=3.0'
                    ]
    )
