# Komle Plus

komle-plus is fork from [komle](https://github.com/kle043/komle), a python library for WITSML, uses [PyXB-E](https://github.com/renalreg/PyXB-X) to marshal/unmarshal xml files according to the schemas.

What is this fork for?:

At work I use some closed source tools that use Komle - some of which I keep. This repository has the necessary patches for komle to work for me. Intend to have a published copy of PyPI available and an automated test pipeline.

Some of the features are:

* WITSML data model bindings for schema v1.4.1.1 and v2.0
    - **Note** just one version can be used in the same runtime, due to namespace collision
* WITSML to dict, for use in a pandas dataframe or json
* Unit converter based on [witsmlUnitDict](http://w3.energistics.org/schema/WITSML_v1.4.1.1_Data_Schema/witsml_v1.4.1.1_data/ancillary/witsmlUnitDict.xml)
* Soap client to request data from a witsml server, according to the [webservice description](http://w3.energistics.org/schema/witsml_v1.4.0_api/WMLS.WSDL)
* Validation that xml files conforms to the WITSML schema
* Support for the generated write schemas, to be used for WMLS_AddToStore
    - **Note** that write_bindings can not be imported at the same time as read_bindings. See below for details.

## Instalation by GitHub
### Pre-requisites:
  * [poetry >= 1.0](https://python-poetry.org/docs/managing-environments/)

  * [python >= 3.9](https://www.python.org/)

  * [GNU Make >= 4.3](https://www.gnu.org/software/make/)

``` bash
git clone https://github.com/HemersonRafael/komle-plus
```

if the repo is cloned

``` bash
make install
```
## Instalation by PyPI
``` bash
pip install komle-plus
```
## Getting started

``` bash
from komle.bindings.v1411.read import witsml
from komle import utils as ku
import pandas as pd # Not part of komle setup

with open('log.xml', 'r') as log_file:
    # logs is a regular python object according to the witsml schema
    logs = witsml.CreateFromDocument(log_file.read())

# Print the witsml documentation for logs
print(logs._element().documentation())

# Print the schema location for logCurveInfo, nice to have for reference
print(logs.log[0].logCurveInfo[0]._element().xsdLocation().locationBase)

print([l.name for l in logs.log])

# Convert logdata to a dict
log = logs.log[0]

data_dict = ku.logdata_dict(log)

# Create a dataframe, if you have installed pandas
df_data = pd.DataFrame(data_dict)

# Do the same for the plural logCurveInfo element
df_curve = pd.DataFrame(ku.plural_dict(log.logCurveInfo))
```

`witsml.CreateFromDocument` works on any witsml object, like trajectorys, mudLogs, tubulars etc, and returns a python representation according to 
the schema. Nodes are converted to there corresponding python types and accessed like any other python object, the exception is leaf nodes with attributes where one must call `value()` since primitive types in python does not have custom attributes. For example `mdTop.value()` where mdTop also has the attribute `mdTop.uom`, also see [examples/hello_witsml.py](examples/hello_witsml.py).

## Usage of different schemas

 The difference between the schemas is described [here](http://w3.energistics.org/schema/WITSML_v1.4.1.1_Data_Schema/witsml_v1.4.1.1_data/index_witsml_schema.html). In summary,

* _Read Schemas_: [...] a copy of the normative files except that all choices, elements and attributes are optional. [...] these schema files must represent the XMLout response from the WITSML WMLS_GetFromStore method.
* _Write Schemas_: [...] a copy of the normative files except that some unique identifier attributes have had their optionality changed. [...] these schema files must represent the XMLin input to the WITSML WMLS_AddToStore method.
* _Update Schemas_ (not currently supported): [...] a copy of the normative files with all elements and attributes optional except that all unique identifier attributes and uom attributes are mandatory. [...] these schema files must represent the XMLin input to the WITSML WMLS_UpdateInStore method.
* _Delete Schemas_ (not currently supported): [...] a copy of the normative files with all elements and attributes optional except for all object uids and parentage-pointers which are mandatory. [...] these schema files must represent the QueryIn input to the WITSML WMLS_DeleteFromStore method.

As a practical matter, any program needing to work on both read and write (and update/delete) should only import the **read** bindings, since they have the least restrictions. The read bindings will be valid also for write/update/delete, as long as the mandatory elements and attributes are present. For validation of the write schema, a separate test program which only imports the write bindings must be used. (Note that the multiprocessing module can not easily be used for this purpose, since the child processes will inherit the parent process' imports.)
