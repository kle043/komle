"""Generate python bindings

Generate bindings from xml schema files using pyxb and download WSDL file for the given version.
This is a one time run to get the python bindings, but the energistics server can timeout, just try again if that happens.

Also see, http://w3.energistics.org/schema/WITSML_v1.4.1.1_Data_Schema/witsml_v1.4.1.1_data/index_witsml_schema.html and
http://w3.energistics.org/schema/WITSML_v1.4.1.1_Data_Schema/witsml_v1.4.1.1_data/generated_read_schemas/obj_attachment.xsd for the schema.
"""

import os
import subprocess

import requests

version = 'v1.4.1.1'
host = f'http://w3.energistics.org/schema/WITSML_{version}_Data_Schema/witsml_{version}_data'
target = 'write'
schema = f'generated_{target}_schemas'
root = 'komle'
package_name = f'{target}_bindings'
module_name = 'witsml'

obj_files = [
    "obj_bhaRun.xsd",
    "obj_cementJob.xsd",
    "obj_convCore.xsd",
    "obj_coordinateReferenceSystem.xsd",
    "obj_drillReport.xsd",
    "obj_fluidsReport.xsd",
    "obj_formationMarker.xsd",
    "obj_log.xsd",
    "obj_message.xsd",
    "obj_mudLog.xsd",
    "obj_objectGroup.xsd",
    "obj_opsReport.xsd",
    "obj_rig.xsd",
    "obj_risk.xsd",
    "obj_sidewallCore.xsd",
    "obj_stimJob.xsd",
    "obj_surveyProgram.xsd",
    "obj_target.xsd",
    "obj_toolErrorModel.xsd",
    "obj_toolErrorTermSet.xsd",
    "obj_trajectory.xsd",
    "obj_tubular.xsd",
    "obj_wbGeometry.xsd",
    "obj_well.xsd",
    "obj_wellbore.xsd",
]

cmd = ['pyxbgen']
for obj_file in obj_files:
    obj_path = os.path.join(host, schema, obj_file)
    cmd.extend(['--schema-location', obj_path, '--module', module_name])

cmd.extend(['--module-prefix', package_name])
cmd.extend(['--binding-root', root])
res = subprocess.run(cmd)

print('Generated:')
print(f'Module {module_name} from')
print(f'{obj_path} ++')

wits_path = os.path.join(root, package_name, module_name) + '.py'

with open(wits_path, "r") as no_version_file:
    data = no_version_file.read()


with open(wits_path, "w") as with_version_file:
    with_version_file.write(data + f'__version__ = "{version[1:]}"\n')

py_path = os.path.join(root, package_name)
for f in os.listdir(py_path):
    if f.endswith('.py'):
        f_path = os.path.join(py_path, f)
        with open(f_path, 'r') as py_file:
            code = py_file.read()

        code = code.replace(f"import {package_name}.", f"import {root}.{package_name}.")
        code = code.replace(f"from {package_name}.", f"from {root}.{package_name}.")

        with open(f_path, 'w') as fixed_py_file:
            fixed_py_file.write(code)


# Get the webservice descrition for soap
# witsml 1.3.1 uses http://w3.energistics.org/schema/witsml_v1.3.1_api/WMLS.WSDL
wsdl = requests.get(f"http://w3.energistics.org/schema/witsml_v1.4.0_api/WMLS.WSDL")

with open(os.path.join(root, 'WMLS.WSDL'), 'w') as wsdl_file:
    wsdl_file.write(wsdl.text)
