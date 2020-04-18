# komle

komle, the name of a dish, is a python library to make it easier to work with WITSML v1.4.1.1 in python. It uses [PyXB](http://pyxb.sourceforge.net/) to marshal/unmarshal xml files according to the [WITSML version 1.4.1.1 schema](http://w3.energistics.org/schema/WITSML_v1.4.1.1_Data_Schema/witsml_v1.4.1.1_data/index_witsml_schema.html). It also comes with a Soap client to talk to a witsml server, according to the [webservice description](http://w3.energistics.org/schema/witsml_v1.4.0_api/WMLS.WSDL). The documents are validated agains the generated_read_schema of WITSML version 1.4.1.1.

This code is just a fast write up of how to work with witsml in python.

## Install

``` bash
pip3 install git+ssh://git@github.com/knle88/komle.git
```
Or if cloned the repo

``` bash
pip3 install -U .
```

## Get started

``` bash
from komle.read_bindings import witsml

with open('log.xml', 'r') as log_file:
    # logs is a regular python object according to the witsml schema
    logs = witsml.CreateFromDocument(log_file.read())

# Print the witsml documentation for logs
print(logs._element().documentation())

print([l.name for l in logs.log])

```