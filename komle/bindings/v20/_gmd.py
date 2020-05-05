# komle/bindings/v20/_gmd.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:410705b36885cae3fa86a581e054e9b962463ed8
# Generated 2020-05-05 12:51:53.525955 by PyXB version 1.2.6 using Python 3.8.2.final.0
# Namespace http://www.isotc211.org/2005/gmd [xmlns:gmd]

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:52e853d8-8ebe-11ea-ae29-f507f064c4f5')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import komle.bindings.v20._nsgroup as _ImportedBinding_bindings_v20__nsgroup

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.isotc211.org/2005/gmd', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)

from komle.bindings.v20._nsgroup import URL # {http://www.isotc211.org/2005/gmd}URL
from komle.bindings.v20._nsgroup import CI_DateTypeCode # {http://www.isotc211.org/2005/gmd}CI_DateTypeCode
from komle.bindings.v20._nsgroup import CI_OnLineFunctionCode # {http://www.isotc211.org/2005/gmd}CI_OnLineFunctionCode
from komle.bindings.v20._nsgroup import CI_RoleCode # {http://www.isotc211.org/2005/gmd}CI_RoleCode
from komle.bindings.v20._nsgroup import CI_PresentationFormCode # {http://www.isotc211.org/2005/gmd}CI_PresentationFormCode
from komle.bindings.v20._nsgroup import DQ_EvaluationMethodTypeCode # {http://www.isotc211.org/2005/gmd}DQ_EvaluationMethodTypeCode
from komle.bindings.v20._nsgroup import EX_Extent # {http://www.isotc211.org/2005/gmd}EX_Extent
from komle.bindings.v20._nsgroup import AbstractEX_GeographicExtent # {http://www.isotc211.org/2005/gmd}AbstractEX_GeographicExtent
from komle.bindings.v20._nsgroup import EX_TemporalExtent # {http://www.isotc211.org/2005/gmd}EX_TemporalExtent
from komle.bindings.v20._nsgroup import EX_VerticalExtent # {http://www.isotc211.org/2005/gmd}EX_VerticalExtent
from komle.bindings.v20._nsgroup import MD_Identifier # {http://www.isotc211.org/2005/gmd}MD_Identifier
from komle.bindings.v20._nsgroup import CI_Citation # {http://www.isotc211.org/2005/gmd}CI_Citation
from komle.bindings.v20._nsgroup import CI_Date # {http://www.isotc211.org/2005/gmd}CI_Date
from komle.bindings.v20._nsgroup import CI_ResponsibleParty # {http://www.isotc211.org/2005/gmd}CI_ResponsibleParty
from komle.bindings.v20._nsgroup import CI_Contact # {http://www.isotc211.org/2005/gmd}CI_Contact
from komle.bindings.v20._nsgroup import CI_Telephone # {http://www.isotc211.org/2005/gmd}CI_Telephone
from komle.bindings.v20._nsgroup import CI_Address # {http://www.isotc211.org/2005/gmd}CI_Address
from komle.bindings.v20._nsgroup import CI_OnlineResource # {http://www.isotc211.org/2005/gmd}CI_OnlineResource
from komle.bindings.v20._nsgroup import CI_Series # {http://www.isotc211.org/2005/gmd}CI_Series
from komle.bindings.v20._nsgroup import AbstractDQ_Result # {http://www.isotc211.org/2005/gmd}AbstractDQ_Result
from komle.bindings.v20._nsgroup import AbstractDQ_Element # {http://www.isotc211.org/2005/gmd}AbstractDQ_Element
from komle.bindings.v20._nsgroup import AbstractDQ_PositionalAccuracy # {http://www.isotc211.org/2005/gmd}AbstractDQ_PositionalAccuracy
from komle.bindings.v20._nsgroup import EX_Extent_Type # {http://www.isotc211.org/2005/gmd}EX_Extent_Type
from komle.bindings.v20._nsgroup import AbstractEX_GeographicExtent_Type # {http://www.isotc211.org/2005/gmd}AbstractEX_GeographicExtent_Type
from komle.bindings.v20._nsgroup import EX_TemporalExtent_Type # {http://www.isotc211.org/2005/gmd}EX_TemporalExtent_Type
from komle.bindings.v20._nsgroup import EX_VerticalExtent_Type # {http://www.isotc211.org/2005/gmd}EX_VerticalExtent_Type
from komle.bindings.v20._nsgroup import AbstractDQ_Element_Type # {http://www.isotc211.org/2005/gmd}AbstractDQ_Element_Type
from komle.bindings.v20._nsgroup import MD_Identifier_Type # {http://www.isotc211.org/2005/gmd}MD_Identifier_Type
from komle.bindings.v20._nsgroup import CI_Citation_Type # {http://www.isotc211.org/2005/gmd}CI_Citation_Type
from komle.bindings.v20._nsgroup import CI_Date_Type # {http://www.isotc211.org/2005/gmd}CI_Date_Type
from komle.bindings.v20._nsgroup import CI_ResponsibleParty_Type # {http://www.isotc211.org/2005/gmd}CI_ResponsibleParty_Type
from komle.bindings.v20._nsgroup import CI_Contact_Type # {http://www.isotc211.org/2005/gmd}CI_Contact_Type
from komle.bindings.v20._nsgroup import CI_Telephone_Type # {http://www.isotc211.org/2005/gmd}CI_Telephone_Type
from komle.bindings.v20._nsgroup import CI_Address_Type # {http://www.isotc211.org/2005/gmd}CI_Address_Type
from komle.bindings.v20._nsgroup import CI_OnlineResource_Type # {http://www.isotc211.org/2005/gmd}CI_OnlineResource_Type
from komle.bindings.v20._nsgroup import CI_Series_Type # {http://www.isotc211.org/2005/gmd}CI_Series_Type
from komle.bindings.v20._nsgroup import AbstractDQ_Result_Type # {http://www.isotc211.org/2005/gmd}AbstractDQ_Result_Type
from komle.bindings.v20._nsgroup import EX_GeographicExtent_PropertyType # {http://www.isotc211.org/2005/gmd}EX_GeographicExtent_PropertyType
from komle.bindings.v20._nsgroup import EX_TemporalExtent_PropertyType # {http://www.isotc211.org/2005/gmd}EX_TemporalExtent_PropertyType
from komle.bindings.v20._nsgroup import EX_VerticalExtent_PropertyType # {http://www.isotc211.org/2005/gmd}EX_VerticalExtent_PropertyType
from komle.bindings.v20._nsgroup import AbstractDQ_PositionalAccuracy_Type # {http://www.isotc211.org/2005/gmd}AbstractDQ_PositionalAccuracy_Type
from komle.bindings.v20._nsgroup import MD_Identifier_PropertyType # {http://www.isotc211.org/2005/gmd}MD_Identifier_PropertyType
from komle.bindings.v20._nsgroup import CI_Citation_PropertyType # {http://www.isotc211.org/2005/gmd}CI_Citation_PropertyType
from komle.bindings.v20._nsgroup import CI_Date_PropertyType # {http://www.isotc211.org/2005/gmd}CI_Date_PropertyType
from komle.bindings.v20._nsgroup import CI_DateTypeCode_PropertyType # {http://www.isotc211.org/2005/gmd}CI_DateTypeCode_PropertyType
from komle.bindings.v20._nsgroup import CI_ResponsibleParty_PropertyType # {http://www.isotc211.org/2005/gmd}CI_ResponsibleParty_PropertyType
from komle.bindings.v20._nsgroup import CI_Contact_PropertyType # {http://www.isotc211.org/2005/gmd}CI_Contact_PropertyType
from komle.bindings.v20._nsgroup import CI_Telephone_PropertyType # {http://www.isotc211.org/2005/gmd}CI_Telephone_PropertyType
from komle.bindings.v20._nsgroup import CI_Address_PropertyType # {http://www.isotc211.org/2005/gmd}CI_Address_PropertyType
from komle.bindings.v20._nsgroup import CI_OnlineResource_PropertyType # {http://www.isotc211.org/2005/gmd}CI_OnlineResource_PropertyType
from komle.bindings.v20._nsgroup import URL_PropertyType # {http://www.isotc211.org/2005/gmd}URL_PropertyType
from komle.bindings.v20._nsgroup import CI_OnLineFunctionCode_PropertyType # {http://www.isotc211.org/2005/gmd}CI_OnLineFunctionCode_PropertyType
from komle.bindings.v20._nsgroup import CI_RoleCode_PropertyType # {http://www.isotc211.org/2005/gmd}CI_RoleCode_PropertyType
from komle.bindings.v20._nsgroup import CI_PresentationFormCode_PropertyType # {http://www.isotc211.org/2005/gmd}CI_PresentationFormCode_PropertyType
from komle.bindings.v20._nsgroup import CI_Series_PropertyType # {http://www.isotc211.org/2005/gmd}CI_Series_PropertyType
from komle.bindings.v20._nsgroup import DQ_EvaluationMethodTypeCode_PropertyType # {http://www.isotc211.org/2005/gmd}DQ_EvaluationMethodTypeCode_PropertyType
from komle.bindings.v20._nsgroup import DQ_Result_PropertyType # {http://www.isotc211.org/2005/gmd}DQ_Result_PropertyType
