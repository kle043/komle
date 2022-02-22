# komle/bindings/v1411/write/_gco.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:2bd68004d120daf987d63b2efda66ae3eda8eaea
# Generated 2020-05-05 12:37:19.643084 by PyXB version 1.2.6 using Python 3.8.2.final.0
# Namespace http://www.isotc211.org/2005/gco [xmlns:gco]

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
    'urn:uuid:23c8451a-8ebc-11ea-ae29-f507f064c4f5'
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
import komle.bindings.v1411.write._nsgroup as _ImportedBinding_bindings_v1411_write__nsgroup

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(
    'http://www.isotc211.org/2005/gco', create_if_missing=True
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


from komle.bindings.v1411.write._nsgroup import \
    AbstractGenericName  # {http://www.isotc211.org/2005/gco}CharacterString; {http://www.isotc211.org/2005/gco}Boolean; {http://www.isotc211.org/2005/gco}DateTime; {http://www.isotc211.org/2005/gco}Decimal; {http://www.isotc211.org/2005/gco}Real; {http://www.isotc211.org/2005/gco}Integer; {http://www.isotc211.org/2005/gco}Record; {http://www.isotc211.org/2005/gco}AbstractGenericName; {http://www.isotc211.org/2005/gco}LocalName; {http://www.isotc211.org/2005/gco}ScopedName; {http://www.isotc211.org/2005/gco}Date; {http://www.isotc211.org/2005/gco}UnlimitedInteger; {http://www.isotc211.org/2005/gco}Binary; {http://www.isotc211.org/2005/gco}TypeName; {http://www.isotc211.org/2005/gco}MemberName; {http://www.isotc211.org/2005/gco}Multiplicity; {http://www.isotc211.org/2005/gco}MultiplicityRange; {http://www.isotc211.org/2005/gco}RecordType; {http://www.isotc211.org/2005/gco}Measure; {http://www.isotc211.org/2005/gco}Length; {http://www.isotc211.org/2005/gco}Angle; {http://www.isotc211.org/2005/gco}Scale; {http://www.isotc211.org/2005/gco}Distance; {http://www.isotc211.org/2005/gco}Date_Type; {http://www.isotc211.org/2005/gco}UnlimitedInteger_Type; {http://www.isotc211.org/2005/gco}Binary_Type; {http://www.isotc211.org/2005/gco}AbstractObject_Type; {http://www.isotc211.org/2005/gco}CodeListValue_Type; {http://www.isotc211.org/2005/gco}TypeName_Type; {http://www.isotc211.org/2005/gco}MemberName_Type; {http://www.isotc211.org/2005/gco}Multiplicity_Type; {http://www.isotc211.org/2005/gco}MultiplicityRange_Type; {http://www.isotc211.org/2005/gco}RecordType_Type; {http://www.isotc211.org/2005/gco}TypeName_PropertyType; {http://www.isotc211.org/2005/gco}MemberName_PropertyType; {http://www.isotc211.org/2005/gco}Multiplicity_PropertyType; {http://www.isotc211.org/2005/gco}MultiplicityRange_PropertyType; {http://www.isotc211.org/2005/gco}Measure_PropertyType; {http://www.isotc211.org/2005/gco}Length_PropertyType; {http://www.isotc211.org/2005/gco}Angle_PropertyType; {http://www.isotc211.org/2005/gco}Scale_PropertyType; {http://www.isotc211.org/2005/gco}Distance_PropertyType; {http://www.isotc211.org/2005/gco}CharacterString_PropertyType; {http://www.isotc211.org/2005/gco}Boolean_PropertyType; {http://www.isotc211.org/2005/gco}GenericName_PropertyType; {http://www.isotc211.org/2005/gco}LocalName_PropertyType; {http://www.isotc211.org/2005/gco}ScopedName_PropertyType; {http://www.isotc211.org/2005/gco}UomAngle_PropertyType; {http://www.isotc211.org/2005/gco}UomLength_PropertyType; {http://www.isotc211.org/2005/gco}UomScale_PropertyType; {http://www.isotc211.org/2005/gco}UnitOfMeasure_PropertyType; {http://www.isotc211.org/2005/gco}UomArea_PropertyType; {http://www.isotc211.org/2005/gco}UomVelocity_PropertyType; {http://www.isotc211.org/2005/gco}UomTime_PropertyType; {http://www.isotc211.org/2005/gco}UomVolume_PropertyType; {http://www.isotc211.org/2005/gco}DateTime_PropertyType; {http://www.isotc211.org/2005/gco}Date_PropertyType; {http://www.isotc211.org/2005/gco}Number_PropertyType; {http://www.isotc211.org/2005/gco}Decimal_PropertyType; {http://www.isotc211.org/2005/gco}Real_PropertyType; {http://www.isotc211.org/2005/gco}Integer_PropertyType; {http://www.isotc211.org/2005/gco}UnlimitedInteger_PropertyType; {http://www.isotc211.org/2005/gco}Record_PropertyType; {http://www.isotc211.org/2005/gco}RecordType_PropertyType; {http://www.isotc211.org/2005/gco}Binary_PropertyType; {http://www.isotc211.org/2005/gco}ObjectReference_PropertyType
from komle.bindings.v1411.write._nsgroup import \
    AbstractObject_ as \
    AbstractObject  # {http://www.isotc211.org/2005/gco}AbstractObject
from komle.bindings.v1411.write._nsgroup import (  # {http://www.isotc211.org/2005/gco}CharacterString; {http://www.isotc211.org/2005/gco}Boolean; {http://www.isotc211.org/2005/gco}DateTime; {http://www.isotc211.org/2005/gco}Decimal; {http://www.isotc211.org/2005/gco}Real; {http://www.isotc211.org/2005/gco}Integer; {http://www.isotc211.org/2005/gco}Record; {http://www.isotc211.org/2005/gco}AbstractGenericName; {http://www.isotc211.org/2005/gco}LocalName; {http://www.isotc211.org/2005/gco}ScopedName; {http://www.isotc211.org/2005/gco}Date; {http://www.isotc211.org/2005/gco}UnlimitedInteger; {http://www.isotc211.org/2005/gco}Binary; {http://www.isotc211.org/2005/gco}TypeName; {http://www.isotc211.org/2005/gco}MemberName; {http://www.isotc211.org/2005/gco}Multiplicity; {http://www.isotc211.org/2005/gco}MultiplicityRange; {http://www.isotc211.org/2005/gco}RecordType; {http://www.isotc211.org/2005/gco}Measure; {http://www.isotc211.org/2005/gco}Length; {http://www.isotc211.org/2005/gco}Angle; {http://www.isotc211.org/2005/gco}Scale; {http://www.isotc211.org/2005/gco}Distance; {http://www.isotc211.org/2005/gco}Date_Type; {http://www.isotc211.org/2005/gco}UnlimitedInteger_Type; {http://www.isotc211.org/2005/gco}Binary_Type; {http://www.isotc211.org/2005/gco}AbstractObject_Type; {http://www.isotc211.org/2005/gco}CodeListValue_Type; {http://www.isotc211.org/2005/gco}TypeName_Type; {http://www.isotc211.org/2005/gco}MemberName_Type; {http://www.isotc211.org/2005/gco}Multiplicity_Type; {http://www.isotc211.org/2005/gco}MultiplicityRange_Type; {http://www.isotc211.org/2005/gco}RecordType_Type; {http://www.isotc211.org/2005/gco}TypeName_PropertyType; {http://www.isotc211.org/2005/gco}MemberName_PropertyType; {http://www.isotc211.org/2005/gco}Multiplicity_PropertyType; {http://www.isotc211.org/2005/gco}MultiplicityRange_PropertyType; {http://www.isotc211.org/2005/gco}Measure_PropertyType; {http://www.isotc211.org/2005/gco}Length_PropertyType; {http://www.isotc211.org/2005/gco}Angle_PropertyType; {http://www.isotc211.org/2005/gco}Scale_PropertyType; {http://www.isotc211.org/2005/gco}Distance_PropertyType; {http://www.isotc211.org/2005/gco}CharacterString_PropertyType; {http://www.isotc211.org/2005/gco}Boolean_PropertyType; {http://www.isotc211.org/2005/gco}GenericName_PropertyType; {http://www.isotc211.org/2005/gco}LocalName_PropertyType; {http://www.isotc211.org/2005/gco}ScopedName_PropertyType; {http://www.isotc211.org/2005/gco}UomAngle_PropertyType; {http://www.isotc211.org/2005/gco}UomLength_PropertyType; {http://www.isotc211.org/2005/gco}UomScale_PropertyType; {http://www.isotc211.org/2005/gco}UnitOfMeasure_PropertyType; {http://www.isotc211.org/2005/gco}UomArea_PropertyType; {http://www.isotc211.org/2005/gco}UomVelocity_PropertyType; {http://www.isotc211.org/2005/gco}UomTime_PropertyType; {http://www.isotc211.org/2005/gco}UomVolume_PropertyType; {http://www.isotc211.org/2005/gco}DateTime_PropertyType; {http://www.isotc211.org/2005/gco}Date_PropertyType; {http://www.isotc211.org/2005/gco}Number_PropertyType; {http://www.isotc211.org/2005/gco}Decimal_PropertyType; {http://www.isotc211.org/2005/gco}Real_PropertyType; {http://www.isotc211.org/2005/gco}Integer_PropertyType; {http://www.isotc211.org/2005/gco}UnlimitedInteger_PropertyType; {http://www.isotc211.org/2005/gco}Record_PropertyType; {http://www.isotc211.org/2005/gco}RecordType_PropertyType; {http://www.isotc211.org/2005/gco}Binary_PropertyType; {http://www.isotc211.org/2005/gco}ObjectReference_PropertyType
    AbstractObject_Type, Angle, Angle_PropertyType, Binary,
    Binary_PropertyType, Binary_Type, Boolean, Boolean_PropertyType,
    CharacterString, CharacterString_PropertyType, CodeListValue_Type, Date,
    Date_PropertyType, Date_Type, DateTime, DateTime_PropertyType, Decimal,
    Decimal_PropertyType, Distance, Distance_PropertyType,
    GenericName_PropertyType, Integer, Integer_PropertyType, Length,
    Length_PropertyType, LocalName, LocalName_PropertyType, Measure,
    Measure_PropertyType, MemberName, MemberName_PropertyType, MemberName_Type,
    Multiplicity, Multiplicity_PropertyType, Multiplicity_Type,
    MultiplicityRange, MultiplicityRange_PropertyType, MultiplicityRange_Type,
    Number_PropertyType, ObjectReference_PropertyType, Real, Real_PropertyType,
    Record, Record_PropertyType, RecordType, RecordType_PropertyType,
    RecordType_Type, Scale, Scale_PropertyType, ScopedName,
    ScopedName_PropertyType, TypeName, TypeName_PropertyType, TypeName_Type,
    UnitOfMeasure_PropertyType, UnlimitedInteger,
    UnlimitedInteger_PropertyType, UnlimitedInteger_Type,
    UomAngle_PropertyType, UomArea_PropertyType, UomLength_PropertyType,
    UomScale_PropertyType, UomTime_PropertyType, UomVelocity_PropertyType,
    UomVolume_PropertyType)
