# komle

komle, a python library for WITSML, uses [PyXB](http://pyxb.sourceforge.net/) to marshal/unmarshal xml files according to the schemas. 

Some of the features are:

* WITSML data model bindings for schema v1.4.1.1 and v2.0
    - **Note** just one version can be used in the same runtime, due to namespace collision
* WITSML to dict, for use in a pandas dataframe or json
* Unit converter based on [witsmlUnitDict](http://w3.energistics.org/schema/WITSML_v1.4.1.1_Data_Schema/witsml_v1.4.1.1_data/ancillary/witsmlUnitDict.xml)
* Soap client to request data from a witsml server, according to the [webservice description](http://w3.energistics.org/schema/witsml_v1.4.0_api/WMLS.WSDL)
* Validation that xml files conforms to the WITSML schema
* Support for the generated write schemas, to be used for WMLS_AddToStore
    - **Note** that write_bindings can not be imported at the same time as read_bindings

## Install

``` bash
pip3 install git+ssh://git@github.com/kle043/komle.git
```

Or if the repo is cloned

``` bash
pip3 install -U .
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