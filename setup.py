from setuptools import setup, find_packages

setup(
      name='komle',
      version='0.2',
      description='A python library to help with WITSML v1.4.1.1 and v2.0',
      url='https://github.com/kle043/komle',
      packages=find_packages(exclude=('tests',)),
      author='kle043',
      author_email='pale.dorg@gmail.com',
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
