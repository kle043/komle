# komle/bindings/v20/_gml.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:c4f74fce23a2f49d6da683416eb2980bfced7e33
# Generated 2020-05-05 12:51:53.526155 by PyXB version 1.2.6 using Python 3.8.2.final.0
# Namespace http://www.opengis.net/gml/3.2 [xmlns:gml]

from __future__ import unicode_literals

import io
import sys

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import pyxb.utils.domutils
import pyxb.utils.six as _six
import pyxb.utils.utility

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier(
    'urn:uuid:52e853d8-8ebe-11ea-ae29-f507f064c4f5'
)

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
Namespace = pyxb.namespace.NamespaceForURI(
    'http://www.opengis.net/gml/3.2', create_if_missing=True
)
Namespace.configureCategories(['typeBinding', 'elementBinding'])


def CreateFromDocument(xml_text, default_namespace=None, location_base=None):
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
        return CreateFromDOM(
            dom.documentElement, default_namespace=default_namespace
        )
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(
        fallback_namespace=default_namespace, location_base=location_base
    )
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance


def CreateFromDOM(node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


from komle.bindings.v20._nsgroup import CTD_ANON  # None
from komle.bindings.v20._nsgroup import CTD_ANON_  # None
from komle.bindings.v20._nsgroup import CTD_ANON_2  # None
from komle.bindings.v20._nsgroup import CTD_ANON_3  # None
from komle.bindings.v20._nsgroup import STD_ANON  # None
from komle.bindings.v20._nsgroup import STD_ANON_  # None
from komle.bindings.v20._nsgroup import STD_ANON_2  # None
from komle.bindings.v20._nsgroup import STD_ANON_3  # None
from komle.bindings.v20._nsgroup import (  # {http://www.opengis.net/gml/3.2}AbstractObject; {http://www.opengis.net/gml/3.2}remarks; {http://www.opengis.net/gml/3.2}scope; {http://www.opengis.net/gml/3.2}minimumValue; {http://www.opengis.net/gml/3.2}maximumValue; {http://www.opengis.net/gml/3.2}realizationEpoch; {http://www.opengis.net/gml/3.2}operationVersion; {http://www.opengis.net/gml/3.2}name; {http://www.opengis.net/gml/3.2}AbstractGML; {http://www.opengis.net/gml/3.2}axisAbbrev; {http://www.opengis.net/gml/3.2}anchorDefinition; {http://www.opengis.net/gml/3.2}semiMajorAxis; {http://www.opengis.net/gml/3.2}secondDefiningParameter; {http://www.opengis.net/gml/3.2}SecondDefiningParameter; {http://www.opengis.net/gml/3.2}identifier; {http://www.opengis.net/gml/3.2}AbstractTimeObject; {http://www.opengis.net/gml/3.2}axisDirection; {http://www.opengis.net/gml/3.2}rangeMeaning; {http://www.opengis.net/gml/3.2}greenwichLongitude; {http://www.opengis.net/gml/3.2}description; {http://www.opengis.net/gml/3.2}descriptionReference; {http://www.opengis.net/gml/3.2}domainOfValidity; {http://www.opengis.net/gml/3.2}AbstractTimePrimitive; {http://www.opengis.net/gml/3.2}Definition; {http://www.opengis.net/gml/3.2}ellipsoidalCS; {http://www.opengis.net/gml/3.2}axis; {http://www.opengis.net/gml/3.2}cartesianCS; {http://www.opengis.net/gml/3.2}sphericalCS; {http://www.opengis.net/gml/3.2}geodeticDatum; {http://www.opengis.net/gml/3.2}primeMeridian; {http://www.opengis.net/gml/3.2}ellipsoid; {http://www.opengis.net/gml/3.2}conversion; {http://www.opengis.net/gml/3.2}coordinateOperationAccuracy; {http://www.opengis.net/gml/3.2}sourceCRS; {http://www.opengis.net/gml/3.2}targetCRS; {http://www.opengis.net/gml/3.2}baseGeodeticCRS; {http://www.opengis.net/gml/3.2}verticalCS; {http://www.opengis.net/gml/3.2}verticalDatum; {http://www.opengis.net/gml/3.2}AbstractCRS; {http://www.opengis.net/gml/3.2}CoordinateSystemAxis; {http://www.opengis.net/gml/3.2}AbstractCoordinateSystem; {http://www.opengis.net/gml/3.2}PrimeMeridian; {http://www.opengis.net/gml/3.2}Ellipsoid; {http://www.opengis.net/gml/3.2}AbstractDatum; {http://www.opengis.net/gml/3.2}AbstractSingleCRS; {http://www.opengis.net/gml/3.2}AbstractOperation; {http://www.opengis.net/gml/3.2}AbstractSingleOperation; {http://www.opengis.net/gml/3.2}AbstractCoordinateOperation; {http://www.opengis.net/gml/3.2}GeodeticCRS; {http://www.opengis.net/gml/3.2}EllipsoidalCS; {http://www.opengis.net/gml/3.2}CartesianCS; {http://www.opengis.net/gml/3.2}SphericalCS; {http://www.opengis.net/gml/3.2}GeodeticDatum; {http://www.opengis.net/gml/3.2}AbstractGeneralConversion; {http://www.opengis.net/gml/3.2}AbstractGeneralDerivedCRS; {http://www.opengis.net/gml/3.2}VerticalCRS; {http://www.opengis.net/gml/3.2}VerticalCS; {http://www.opengis.net/gml/3.2}VerticalDatum; {http://www.opengis.net/gml/3.2}ProjectedCRS; {http://www.opengis.net/gml/3.2}AbstractGMLType; {http://www.opengis.net/gml/3.2}CodeType; {http://www.opengis.net/gml/3.2}UomSymbol; {http://www.opengis.net/gml/3.2}UomURI; {http://www.opengis.net/gml/3.2}AggregationType; {http://www.opengis.net/gml/3.2}MeasureType; {http://www.opengis.net/gml/3.2}DefinitionBaseType; {http://www.opengis.net/gml/3.2}NilReasonType; {http://www.opengis.net/gml/3.2}NilReasonEnumeration; {http://www.opengis.net/gml/3.2}CodeWithAuthorityType; {http://www.opengis.net/gml/3.2}AbstractTimeObjectType; {http://www.opengis.net/gml/3.2}UomIdentifier; {http://www.opengis.net/gml/3.2}AngleType; {http://www.opengis.net/gml/3.2}LengthType; {http://www.opengis.net/gml/3.2}DefinitionType; {http://www.opengis.net/gml/3.2}StringOrRefType; {http://www.opengis.net/gml/3.2}ReferenceType; {http://www.opengis.net/gml/3.2}AbstractTimePrimitiveType; {http://www.opengis.net/gml/3.2}TimePrimitivePropertyType; {http://www.opengis.net/gml/3.2}EllipsoidalCSPropertyType; {http://www.opengis.net/gml/3.2}CoordinateSystemAxisPropertyType; {http://www.opengis.net/gml/3.2}CartesianCSPropertyType; {http://www.opengis.net/gml/3.2}SphericalCSPropertyType; {http://www.opengis.net/gml/3.2}GeodeticDatumPropertyType; {http://www.opengis.net/gml/3.2}PrimeMeridianPropertyType; {http://www.opengis.net/gml/3.2}EllipsoidPropertyType; {http://www.opengis.net/gml/3.2}GeneralConversionPropertyType; {http://www.opengis.net/gml/3.2}CRSPropertyType; {http://www.opengis.net/gml/3.2}GeodeticCRSPropertyType; {http://www.opengis.net/gml/3.2}VerticalCSPropertyType; {http://www.opengis.net/gml/3.2}VerticalDatumPropertyType; {http://www.opengis.net/gml/3.2}IdentifiedObjectType; {http://www.opengis.net/gml/3.2}RelatedTimeType; {http://www.opengis.net/gml/3.2}AbstractCRSType; {http://www.opengis.net/gml/3.2}AbstractCoordinateSystemType; {http://www.opengis.net/gml/3.2}CoordinateSystemAxisType; {http://www.opengis.net/gml/3.2}AbstractDatumType; {http://www.opengis.net/gml/3.2}PrimeMeridianType; {http://www.opengis.net/gml/3.2}EllipsoidType; {http://www.opengis.net/gml/3.2}AbstractCoordinateOperationType; {http://www.opengis.net/gml/3.2}GeodeticCRSType; {http://www.opengis.net/gml/3.2}EllipsoidalCSType; {http://www.opengis.net/gml/3.2}CartesianCSType; {http://www.opengis.net/gml/3.2}SphericalCSType; {http://www.opengis.net/gml/3.2}GeodeticDatumType; {http://www.opengis.net/gml/3.2}AbstractGeneralDerivedCRSType; {http://www.opengis.net/gml/3.2}AbstractGeneralConversionType; {http://www.opengis.net/gml/3.2}VerticalCRSType; {http://www.opengis.net/gml/3.2}VerticalCSType; {http://www.opengis.net/gml/3.2}VerticalDatumType; {http://www.opengis.net/gml/3.2}ProjectedCRSType
    AbstractCoordinateOperation, AbstractCoordinateOperationType,
    AbstractCoordinateSystem, AbstractCoordinateSystemType, AbstractCRS,
    AbstractCRSType, AbstractDatum, AbstractDatumType,
    AbstractGeneralConversion, AbstractGeneralConversionType,
    AbstractGeneralDerivedCRS, AbstractGeneralDerivedCRSType, AbstractGML,
    AbstractGMLType, AbstractObject, AbstractOperation, AbstractSingleCRS,
    AbstractSingleOperation, AbstractTimeObject, AbstractTimeObjectType,
    AbstractTimePrimitive, AbstractTimePrimitiveType, AggregationType,
    AngleType, CartesianCS, CartesianCSPropertyType, CartesianCSType, CodeType,
    CodeWithAuthorityType, CoordinateSystemAxis,
    CoordinateSystemAxisPropertyType, CoordinateSystemAxisType,
    CRSPropertyType, Definition, DefinitionBaseType, DefinitionType, Ellipsoid,
    EllipsoidalCS, EllipsoidalCSPropertyType, EllipsoidalCSType,
    EllipsoidPropertyType, EllipsoidType, GeneralConversionPropertyType,
    GeodeticCRS, GeodeticCRSPropertyType, GeodeticCRSType, GeodeticDatum,
    GeodeticDatumPropertyType, GeodeticDatumType, IdentifiedObjectType,
    LengthType, MeasureType, NilReasonEnumeration, NilReasonType,
    PrimeMeridian, PrimeMeridianPropertyType, PrimeMeridianType, ProjectedCRS,
    ProjectedCRSType, ReferenceType, RelatedTimeType, SecondDefiningParameter,
    SphericalCS, SphericalCSPropertyType, SphericalCSType, StringOrRefType,
    TimePrimitivePropertyType, UomIdentifier, UomSymbol, UomURI, VerticalCRS,
    VerticalCRSType, VerticalCS, VerticalCSPropertyType, VerticalCSType,
    VerticalDatum, VerticalDatumPropertyType, VerticalDatumType,
    anchorDefinition, axis, axisAbbrev, axisDirection, baseGeodeticCRS,
    cartesianCS, conversion, coordinateOperationAccuracy, description,
    descriptionReference, domainOfValidity, ellipsoid, ellipsoidalCS,
    geodeticDatum, greenwichLongitude, identifier, maximumValue, minimumValue,
    name, operationVersion, primeMeridian, rangeMeaning, realizationEpoch,
    remarks, scope, secondDefiningParameter, semiMajorAxis, sourceCRS,
    sphericalCS, targetCRS, verticalCS, verticalDatum)
