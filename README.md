# komle

komle, the name of a dish, is a python library to make it easier to work with WITSML v1.4.1.1 in python. It uses [PyXB](http://pyxb.sourceforge.net/) to marshal/unmarshal xml files according to the [WITSML version 1.4.1.1 schema](http://w3.energistics.org/schema/WITSML_v1.4.1.1_Data_Schema/witsml_v1.4.1.1_data/index_witsml_schema.html). It also comes with a Soap client to talk to a witsml server, according to the [webservice description](http://w3.energistics.org/schema/witsml_v1.4.0_api/WMLS.WSDL). The documents are validated agains the generated_read_schema of WITSML version 1.4.1.1.

This code is just a fast write up of how to work with witsml.

## Install

``` bash
pip3 install git+ssh://git@github.com/knle88/komle.git
```
Or if cloned the repo

``` bash
pip3 install -U .
```