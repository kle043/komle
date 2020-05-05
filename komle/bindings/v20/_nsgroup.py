# komle/bindings/v20/_nsgroup.py
# -*- coding: utf-8 -*-
# PyXB bindings for NGM:028a0d50d977330081c6c39e8cc2382e79fdb102
# Generated 2020-05-05 12:51:53.526459 by PyXB version 1.2.6 using Python 3.8.2.final.0
# Group contents:
# Namespace http://www.isotc211.org/2005/gco [xmlns:gco]
# Namespace http://www.isotc211.org/2005/gmd [xmlns:gmd]
# Namespace http://www.isotc211.org/2005/gsr [xmlns:gsr]
# Namespace http://www.isotc211.org/2005/gts [xmlns:gts]
# Namespace http://www.opengis.net/gml/3.2 [xmlns:gml]


from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.utils.utility
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
import pyxb.binding.datatypes
import komle.bindings.v20._xlink as _ImportedBinding_bindings_v20__xlink

# NOTE: All namespace declarations are reserved within the binding
_Namespace_gco = pyxb.namespace.NamespaceForURI('http://www.isotc211.org/2005/gco', create_if_missing=True)
_Namespace_gco.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_gml = pyxb.namespace.NamespaceForURI('http://www.opengis.net/gml/3.2', create_if_missing=True)
_Namespace_gml.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_gmd = pyxb.namespace.NamespaceForURI('http://www.isotc211.org/2005/gmd', create_if_missing=True)
_Namespace_gmd.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_xlink = _ImportedBinding_bindings_v20__xlink.Namespace
_Namespace_xlink.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_gsr = pyxb.namespace.NamespaceForURI('http://www.isotc211.org/2005/gsr', create_if_missing=True)
_Namespace_gsr.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_gts = pyxb.namespace.NamespaceForURI('http://www.isotc211.org/2005/gts', create_if_missing=True)
_Namespace_gts.configureCategories(['typeBinding', 'elementBinding'])

# Union simple type: {http://www.isotc211.org/2005/gco}Date_Type
# superclasses pyxb.binding.datatypes.anySimpleType
class Date_Type (pyxb.binding.basis.STD_union):

    """Simple type that is a union of pyxb.binding.datatypes.date, pyxb.binding.datatypes.gYearMonth, pyxb.binding.datatypes.gYear."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gco, 'Date_Type')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 93, 3)
    _Documentation = None

    _MemberTypes = ( pyxb.binding.datatypes.date, pyxb.binding.datatypes.gYearMonth, pyxb.binding.datatypes.gYear, )
Date_Type._CF_pattern = pyxb.binding.facets.CF_pattern()
Date_Type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Date_Type)
Date_Type._InitializeFacetMap(Date_Type._CF_pattern,
   Date_Type._CF_enumeration)
_Namespace_gco.addCategoryObject('typeBinding', 'Date_Type', Date_Type)
_module_typeBindings.Date_Type = Date_Type

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 154, 9)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.inapplicable = STD_ANON._CF_enumeration.addEnumeration(unicode_value='inapplicable', tag='inapplicable')
STD_ANON.missing = STD_ANON._CF_enumeration.addEnumeration(unicode_value='missing', tag='missing')
STD_ANON.template = STD_ANON._CF_enumeration.addEnumeration(unicode_value='template', tag='template')
STD_ANON.unknown = STD_ANON._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
STD_ANON.withheld = STD_ANON._CF_enumeration.addEnumeration(unicode_value='withheld', tag='withheld')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 163, 9)
    _Documentation = None
STD_ANON_._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_._CF_pattern.addPattern(pattern='other:\\w{2,}')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_pattern)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 221, 3)
    _Documentation = None
STD_ANON_2._InitializeFacetMap()
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 302, 15)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_3, enum_prefix=None)
STD_ANON_3.Before = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Before', tag='Before')
STD_ANON_3.After = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='After', tag='After')
STD_ANON_3.Begins = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Begins', tag='Begins')
STD_ANON_3.Ends = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Ends', tag='Ends')
STD_ANON_3.During = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='During', tag='During')
STD_ANON_3.Equals = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Equals', tag='Equals')
STD_ANON_3.Contains = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Contains', tag='Contains')
STD_ANON_3.Overlaps = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Overlaps', tag='Overlaps')
STD_ANON_3.Meets = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Meets', tag='Meets')
STD_ANON_3.OverlappedBy = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='OverlappedBy', tag='OverlappedBy')
STD_ANON_3.MetBy = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='MetBy', tag='MetBy')
STD_ANON_3.BegunBy = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='BegunBy', tag='BegunBy')
STD_ANON_3.EndedBy = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='EndedBy', tag='EndedBy')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)
_module_typeBindings.STD_ANON_3 = STD_ANON_3

# Atomic simple type: {http://www.opengis.net/gml/3.2}UomSymbol
class UomSymbol (pyxb.binding.datatypes.string):

    """This type specifies a character string of length at least one, and restricted such that it must not contain any of the following characters: ":" (colon), " " (space), (newline), (carriage return), (tab). This allows values corresponding to familiar abbreviations, such as "kg", "m/s", etc. 
It is recommended that the symbol be an identifier for a unit of measure as specified in the "Unified Code of Units of Measure" (UCUM) (http://aurora.regenstrief.org/UCUM). This provides a set of symbols and a grammar for constructing identifiers for units of measure that are unique, and may be easily entered with a keyboard supporting the limited character set known as 7-bit ASCII. ISO 2955 formerly provided a specification with this scope, but was withdrawn in 2001. UCUM largely follows ISO 2955 with modifications to remove ambiguities and other problems."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'UomSymbol')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 492, 3)
    _Documentation = 'This type specifies a character string of length at least one, and restricted such that it must not contain any of the following characters: ":" (colon), " " (space), (newline), (carriage return), (tab). This allows values corresponding to familiar abbreviations, such as "kg", "m/s", etc. \nIt is recommended that the symbol be an identifier for a unit of measure as specified in the "Unified Code of Units of Measure" (UCUM) (http://aurora.regenstrief.org/UCUM). This provides a set of symbols and a grammar for constructing identifiers for units of measure that are unique, and may be easily entered with a keyboard supporting the limited character set known as 7-bit ASCII. ISO 2955 formerly provided a specification with this scope, but was withdrawn in 2001. UCUM largely follows ISO 2955 with modifications to remove ambiguities and other problems.'
UomSymbol._CF_pattern = pyxb.binding.facets.CF_pattern()
UomSymbol._CF_pattern.addPattern(pattern='[^: \\n\\r\\t]+')
UomSymbol._InitializeFacetMap(UomSymbol._CF_pattern)
_Namespace_gml.addCategoryObject('typeBinding', 'UomSymbol', UomSymbol)
_module_typeBindings.UomSymbol = UomSymbol

# Atomic simple type: {http://www.opengis.net/gml/3.2}UomURI
class UomURI (pyxb.binding.datatypes.anyURI):

    """This type specifies a URI, restricted such that it must start with one of the following sequences: "#", "./", "../", or a string of characters followed by a ":". These patterns ensure that the most common URI forms are supported, including absolute and relative URIs and URIs that are simple fragment identifiers, but prohibits certain forms of relative URI that could be mistaken for unit of measure symbol . 
NOTE	It is possible to re-write such a relative URI to conform to the restriction (e.g. "./m/s").
In an instance document, on elements of type gml:MeasureType the mandatory uom attribute shall carry a value corresponding to either 
-	a conventional unit of measure symbol,
-	a link to a definition of a unit of measure that does not have a conventional symbol, or when it is desired to indicate a precise or variant definition."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'UomURI')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 502, 3)
    _Documentation = 'This type specifies a URI, restricted such that it must start with one of the following sequences: "#", "./", "../", or a string of characters followed by a ":". These patterns ensure that the most common URI forms are supported, including absolute and relative URIs and URIs that are simple fragment identifiers, but prohibits certain forms of relative URI that could be mistaken for unit of measure symbol . \nNOTE\tIt is possible to re-write such a relative URI to conform to the restriction (e.g. "./m/s").\nIn an instance document, on elements of type gml:MeasureType the mandatory uom attribute shall carry a value corresponding to either \n-\ta conventional unit of measure symbol,\n-\ta link to a definition of a unit of measure that does not have a conventional symbol, or when it is desired to indicate a precise or variant definition.'
UomURI._CF_pattern = pyxb.binding.facets.CF_pattern()
UomURI._CF_pattern.addPattern(pattern='([a-zA-Z][a-zA-Z0-9\\-\\+\\.]*:|\\.\\./|\\./|#).*')
UomURI._InitializeFacetMap(UomURI._CF_pattern)
_Namespace_gml.addCategoryObject('typeBinding', 'UomURI', UomURI)
_module_typeBindings.UomURI = UomURI

# Atomic simple type: {http://www.opengis.net/gml/3.2}AggregationType
class AggregationType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'AggregationType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 524, 3)
    _Documentation = None
AggregationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AggregationType, enum_prefix=None)
AggregationType.set_ = AggregationType._CF_enumeration.addEnumeration(unicode_value='set', tag='set_')
AggregationType.bag = AggregationType._CF_enumeration.addEnumeration(unicode_value='bag', tag='bag')
AggregationType.sequence = AggregationType._CF_enumeration.addEnumeration(unicode_value='sequence', tag='sequence')
AggregationType.array = AggregationType._CF_enumeration.addEnumeration(unicode_value='array', tag='array')
AggregationType.record = AggregationType._CF_enumeration.addEnumeration(unicode_value='record', tag='record')
AggregationType.table = AggregationType._CF_enumeration.addEnumeration(unicode_value='table', tag='table')
AggregationType._InitializeFacetMap(AggregationType._CF_enumeration)
_Namespace_gml.addCategoryObject('typeBinding', 'AggregationType', AggregationType)
_module_typeBindings.AggregationType = AggregationType

# Union simple type: {http://www.opengis.net/gml/3.2}NilReasonType
# superclasses pyxb.binding.datatypes.anySimpleType
class NilReasonType (pyxb.binding.basis.STD_union):

    """gml:NilReasonType defines a content model that allows recording of an explanation for a void value or other exception.
gml:NilReasonType is a union of the following enumerated values:
-	inapplicable there is no value
-	missing the correct value is not readily available to the sender of this data. Furthermore, a correct value may not exist
-	template the value will be available later
-	unknown the correct value is not known to, and not computable by, the sender of this data. However, a correct value probably exists
-	withheld the value is not divulged
-	other:text other brief explanation, where text is a string of two or more characters with no included spaces
and
-	anyURI which should refer to a resource which describes the reason for the exception
A particular community may choose to assign more detailed semantics to the standard values provided. Alternatively, the URI method enables a specific or more complete explanation for the absence of a value to be provided elsewhere and indicated by-reference in an instance document.
gml:NilReasonType is used as a member of a union in a number of simple content types where it is necessary to permit a value from the NilReasonType union as an alternative to the primary type."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'NilReasonType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 134, 3)
    _Documentation = 'gml:NilReasonType defines a content model that allows recording of an explanation for a void value or other exception.\ngml:NilReasonType is a union of the following enumerated values:\n-\tinapplicable there is no value\n-\tmissing the correct value is not readily available to the sender of this data. Furthermore, a correct value may not exist\n-\ttemplate the value will be available later\n-\tunknown the correct value is not known to, and not computable by, the sender of this data. However, a correct value probably exists\n-\twithheld the value is not divulged\n-\tother:text other brief explanation, where text is a string of two or more characters with no included spaces\nand\n-\tanyURI which should refer to a resource which describes the reason for the exception\nA particular community may choose to assign more detailed semantics to the standard values provided. Alternatively, the URI method enables a specific or more complete explanation for the absence of a value to be provided elsewhere and indicated by-reference in an instance document.\ngml:NilReasonType is used as a member of a union in a number of simple content types where it is necessary to permit a value from the NilReasonType union as an alternative to the primary type.'

    _MemberTypes = ( STD_ANON, STD_ANON_, pyxb.binding.datatypes.anyURI, )
NilReasonType._CF_pattern = pyxb.binding.facets.CF_pattern()
NilReasonType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NilReasonType)
NilReasonType.inapplicable = 'inapplicable'       # originally STD_ANON.inapplicable
NilReasonType.missing = 'missing'                 # originally STD_ANON.missing
NilReasonType.template = 'template'               # originally STD_ANON.template
NilReasonType.unknown = 'unknown'                 # originally STD_ANON.unknown
NilReasonType.withheld = 'withheld'               # originally STD_ANON.withheld
NilReasonType._InitializeFacetMap(NilReasonType._CF_pattern,
   NilReasonType._CF_enumeration)
_Namespace_gml.addCategoryObject('typeBinding', 'NilReasonType', NilReasonType)
_module_typeBindings.NilReasonType = NilReasonType

# Union simple type: {http://www.opengis.net/gml/3.2}NilReasonEnumeration
# superclasses pyxb.binding.datatypes.anySimpleType
class NilReasonEnumeration (pyxb.binding.basis.STD_union):

    """Simple type that is a union of STD_ANON, STD_ANON_."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'NilReasonEnumeration')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 152, 3)
    _Documentation = None

    _MemberTypes = ( STD_ANON, STD_ANON_, )
NilReasonEnumeration._CF_pattern = pyxb.binding.facets.CF_pattern()
NilReasonEnumeration._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NilReasonEnumeration)
NilReasonEnumeration.inapplicable = 'inapplicable'# originally STD_ANON.inapplicable
NilReasonEnumeration.missing = 'missing'          # originally STD_ANON.missing
NilReasonEnumeration.template = 'template'        # originally STD_ANON.template
NilReasonEnumeration.unknown = 'unknown'          # originally STD_ANON.unknown
NilReasonEnumeration.withheld = 'withheld'        # originally STD_ANON.withheld
NilReasonEnumeration._InitializeFacetMap(NilReasonEnumeration._CF_pattern,
   NilReasonEnumeration._CF_enumeration)
_Namespace_gml.addCategoryObject('typeBinding', 'NilReasonEnumeration', NilReasonEnumeration)
_module_typeBindings.NilReasonEnumeration = NilReasonEnumeration

# Union simple type: {http://www.opengis.net/gml/3.2}UomIdentifier
# superclasses pyxb.binding.datatypes.anySimpleType
class UomIdentifier (pyxb.binding.basis.STD_union):

    """The simple type gml:UomIdentifer defines the syntax and value space of the unit of measure identifier."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'UomIdentifier')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 485, 3)
    _Documentation = 'The simple type gml:UomIdentifer defines the syntax and value space of the unit of measure identifier.'

    _MemberTypes = ( UomSymbol, UomURI, )
UomIdentifier._CF_pattern = pyxb.binding.facets.CF_pattern()
UomIdentifier._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UomIdentifier)
UomIdentifier._InitializeFacetMap(UomIdentifier._CF_pattern,
   UomIdentifier._CF_enumeration)
_Namespace_gml.addCategoryObject('typeBinding', 'UomIdentifier', UomIdentifier)
_module_typeBindings.UomIdentifier = UomIdentifier

# Complex type {http://www.isotc211.org/2005/gco}AbstractObject_Type with content type EMPTY
class AbstractObject_Type (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.isotc211.org/2005/gco}AbstractObject_Type with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gco, 'AbstractObject_Type')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 31, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_isotc211_org2005gco_AbstractObject_Type_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 37, 6)
    __id._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 37, 6)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute uuid uses Python identifier uuid
    __uuid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uuid'), 'uuid', '__httpwww_isotc211_org2005gco_AbstractObject_Type_uuid', pyxb.binding.datatypes.string)
    __uuid._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 38, 6)
    __uuid._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 38, 6)
    
    uuid = property(__uuid.value, __uuid.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __uuid.name() : __uuid
    })
_module_typeBindings.AbstractObject_Type = AbstractObject_Type
_Namespace_gco.addCategoryObject('typeBinding', 'AbstractObject_Type', AbstractObject_Type)


# Complex type {http://www.isotc211.org/2005/gco}CodeListValue_Type with content type SIMPLE
class CodeListValue_Type (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.isotc211.org/2005/gco}CodeListValue_Type with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gco, 'CodeListValue_Type')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 107, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute codeList uses Python identifier codeList
    __codeList = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'codeList'), 'codeList', '__httpwww_isotc211_org2005gco_CodeListValue_Type_codeList', pyxb.binding.datatypes.anyURI, required=True)
    __codeList._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 110, 12)
    __codeList._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 110, 12)
    
    codeList = property(__codeList.value, __codeList.set, None, None)

    
    # Attribute codeListValue uses Python identifier codeListValue
    __codeListValue = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'codeListValue'), 'codeListValue', '__httpwww_isotc211_org2005gco_CodeListValue_Type_codeListValue', pyxb.binding.datatypes.anyURI, required=True)
    __codeListValue._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 111, 12)
    __codeListValue._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 111, 12)
    
    codeListValue = property(__codeListValue.value, __codeListValue.set, None, None)

    
    # Attribute codeSpace uses Python identifier codeSpace
    __codeSpace = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'codeSpace'), 'codeSpace', '__httpwww_isotc211_org2005gco_CodeListValue_Type_codeSpace', pyxb.binding.datatypes.anyURI)
    __codeSpace._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 112, 12)
    __codeSpace._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 112, 12)
    
    codeSpace = property(__codeSpace.value, __codeSpace.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __codeList.name() : __codeList,
        __codeListValue.name() : __codeListValue,
        __codeSpace.name() : __codeSpace
    })
_module_typeBindings.CodeListValue_Type = CodeListValue_Type
_Namespace_gco.addCategoryObject('typeBinding', 'CodeListValue_Type', CodeListValue_Type)


# Complex type {http://www.opengis.net/gml/3.2}AbstractGMLType with content type ELEMENT_ONLY
class AbstractGMLType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/gml/3.2}AbstractGMLType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractGMLType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 96, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml/3.2}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'description'), 'description', '__httpwww_opengis_netgml3_2_AbstractGMLType_httpwww_opengis_netgml3_2description', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 173, 3), )

    
    description = property(__description.value, __description.set, None, 'The value of this property is a text description of the object. gml:description uses gml:StringOrRefType as its content model, so it may contain a simple text string content, or carry a reference to an external description. The use of gml:description to reference an external description has been deprecated and replaced by the gml:descriptionReference property.')

    
    # Element {http://www.opengis.net/gml/3.2}descriptionReference uses Python identifier descriptionReference
    __descriptionReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference'), 'descriptionReference', '__httpwww_opengis_netgml3_2_AbstractGMLType_httpwww_opengis_netgml3_2descriptionReference', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 192, 3), )

    
    descriptionReference = property(__descriptionReference.value, __descriptionReference.set, None, 'The value of this property is a remote text description of the object. The xlink:href attribute of the gml:descriptionReference property references the external description.')

    
    # Element {http://www.opengis.net/gml/3.2}identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier'), 'identifier', '__httpwww_opengis_netgml3_2_AbstractGMLType_httpwww_opengis_netgml3_2identifier', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 215, 3), )

    
    identifier = property(__identifier.value, __identifier.set, None, 'Often, a special identifier is assigned to an object by the maintaining authority with the intention that it is used in references to the object For such cases, the codeSpace shall be provided. That identifier is usually unique either globally or within an application domain. gml:identifier is a pre-defined property for such identifiers.')

    
    # Element {http://www.opengis.net/gml/3.2}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'name'), 'name', '__httpwww_opengis_netgml3_2_AbstractGMLType_httpwww_opengis_netgml3_2name', True, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 244, 3), )

    
    name = property(__name.value, __name.set, None, 'The gml:name property provides a label or identifier for the object, commonly a descriptive name. An object may have several names, typically assigned by different authorities. gml:name uses the gml:CodeType content model.  The authority for a name is indicated by the value of its (optional) codeSpace attribute.  The name may or may not be unique, as determined by the rules of the organization responsible for the codeSpace.  In common usage there will be one name per authority, so a processing application may select the name from its preferred codeSpace.')

    
    # Attribute {http://www.opengis.net/gml/3.2}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'id'), 'id', '__httpwww_opengis_netgml3_2_AbstractGMLType_httpwww_opengis_netgml3_2id', pyxb.binding.datatypes.ID, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 113, 3)
    __id._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 100, 6)
    
    id = property(__id.value, __id.set, None, 'The attribute gml:id supports provision of a handle for the XML element representing a GML Object. Its use is mandatory for all GML objects. It is of XML type ID, so is constrained to be unique in the XML document within which it occurs.')

    _ElementMap.update({
        __description.name() : __description,
        __descriptionReference.name() : __descriptionReference,
        __identifier.name() : __identifier,
        __name.name() : __name
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.AbstractGMLType = AbstractGMLType
_Namespace_gml.addCategoryObject('typeBinding', 'AbstractGMLType', AbstractGMLType)


# Complex type {http://www.opengis.net/gml/3.2}CodeType with content type SIMPLE
class CodeType (pyxb.binding.basis.complexTypeDefinition):
    """gml:CodeType is a generalized type to be used for a term, keyword or name.
It adds a XML attribute codeSpace to a term, where the value of the codeSpace attribute (if present) shall indicate a dictionary, thesaurus, classification scheme, authority, or pattern for the term."""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'CodeType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 232, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute codeSpace uses Python identifier codeSpace
    __codeSpace = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'codeSpace'), 'codeSpace', '__httpwww_opengis_netgml3_2_CodeType_codeSpace', pyxb.binding.datatypes.anyURI)
    __codeSpace._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 239, 12)
    __codeSpace._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 239, 12)
    
    codeSpace = property(__codeSpace.value, __codeSpace.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __codeSpace.name() : __codeSpace
    })
_module_typeBindings.CodeType = CodeType
_Namespace_gml.addCategoryObject('typeBinding', 'CodeType', CodeType)


# Complex type {http://www.opengis.net/gml/3.2}MeasureType with content type SIMPLE
class MeasureType (pyxb.binding.basis.complexTypeDefinition):
    """gml:MeasureType supports recording an amount encoded as a value of XML Schema double, together with a units of measure indicated by an attribute uom, short for "units Of measure". The value of the uom attribute identifies a reference system for the amount, usually a ratio or interval scale."""
    _TypeDefinition = pyxb.binding.datatypes.double
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'MeasureType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 710, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.double
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MeasureType = MeasureType
_Namespace_gml.addCategoryObject('typeBinding', 'MeasureType', MeasureType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """gml:secondDefiningParameter is a property containing the definition of the second parameter that defines the shape of an ellipsoid. An ellipsoid requires two defining parameters: semi-major axis and inverse flattening or semi-major axis and semi-minor axis. When the reference body is a sphere rather than an ellipsoid, only a single defining parameter is required, namely the radius of the sphere; in that case, the semi-major axis "degenerates" into the radius of the sphere.
The inverseFlattening element contains the inverse flattening value of the ellipsoid. This value is a scale factor (or ratio). It uses gml:LengthType with the restriction that the unit of measure referenced by the uom attribute must be suitable for a scale factor, such as percent, permil, or parts-per-million.
The semiMinorAxis element contains the length of the semi-minor axis of the ellipsoid. When the isSphere element is included, the ellipsoid is degenerate and is actually a sphere. The sphere is completely defined by the semi-major axis, which is the radius of the sphere."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 766, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml/3.2}SecondDefiningParameter uses Python identifier SecondDefiningParameter
    __SecondDefiningParameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'SecondDefiningParameter'), 'SecondDefiningParameter', '__httpwww_opengis_netgml3_2_CTD_ANON_httpwww_opengis_netgml3_2SecondDefiningParameter', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 773, 3), )

    
    SecondDefiningParameter = property(__SecondDefiningParameter.value, __SecondDefiningParameter.set, None, None)

    _ElementMap.update({
        __SecondDefiningParameter.name() : __SecondDefiningParameter
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 774, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml/3.2}inverseFlattening uses Python identifier inverseFlattening
    __inverseFlattening = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'inverseFlattening'), 'inverseFlattening', '__httpwww_opengis_netgml3_2_CTD_ANON__httpwww_opengis_netgml3_2inverseFlattening', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 776, 12), )

    
    inverseFlattening = property(__inverseFlattening.value, __inverseFlattening.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.2}semiMinorAxis uses Python identifier semiMinorAxis
    __semiMinorAxis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'semiMinorAxis'), 'semiMinorAxis', '__httpwww_opengis_netgml3_2_CTD_ANON__httpwww_opengis_netgml3_2semiMinorAxis', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 777, 12), )

    
    semiMinorAxis = property(__semiMinorAxis.value, __semiMinorAxis.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.2}isSphere uses Python identifier isSphere
    __isSphere = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'isSphere'), 'isSphere', '__httpwww_opengis_netgml3_2_CTD_ANON__httpwww_opengis_netgml3_2isSphere', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 778, 12), )

    
    isSphere = property(__isSphere.value, __isSphere.set, None, None)

    _ElementMap.update({
        __inverseFlattening.name() : __inverseFlattening,
        __semiMinorAxis.name() : __semiMinorAxis,
        __isSphere.name() : __isSphere
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type {http://www.isotc211.org/2005/gmd}EX_Extent_Type with content type ELEMENT_ONLY
class EX_Extent_Type (AbstractObject_Type):
    """Information about spatial, vertical, and temporal extent"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'EX_Extent_Type')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 35, 3)
    _ElementMap = AbstractObject_Type._ElementMap.copy()
    _AttributeMap = AbstractObject_Type._AttributeMap.copy()
    # Base type is AbstractObject_Type
    
    # Element {http://www.isotc211.org/2005/gmd}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'description'), 'description', '__httpwww_isotc211_org2005gmd_EX_Extent_Type_httpwww_isotc211_org2005gmddescription', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 42, 15), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}geographicElement uses Python identifier geographicElement
    __geographicElement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'geographicElement'), 'geographicElement', '__httpwww_isotc211_org2005gmd_EX_Extent_Type_httpwww_isotc211_org2005gmdgeographicElement', True, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 43, 15), )

    
    geographicElement = property(__geographicElement.value, __geographicElement.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}temporalElement uses Python identifier temporalElement
    __temporalElement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'temporalElement'), 'temporalElement', '__httpwww_isotc211_org2005gmd_EX_Extent_Type_httpwww_isotc211_org2005gmdtemporalElement', True, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 46, 15), )

    
    temporalElement = property(__temporalElement.value, __temporalElement.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}verticalElement uses Python identifier verticalElement
    __verticalElement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'verticalElement'), 'verticalElement', '__httpwww_isotc211_org2005gmd_EX_Extent_Type_httpwww_isotc211_org2005gmdverticalElement', True, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 48, 15), )

    
    verticalElement = property(__verticalElement.value, __verticalElement.set, None, None)

    
    # Attribute id inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    
    # Attribute uuid inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    _ElementMap.update({
        __description.name() : __description,
        __geographicElement.name() : __geographicElement,
        __temporalElement.name() : __temporalElement,
        __verticalElement.name() : __verticalElement
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.EX_Extent_Type = EX_Extent_Type
_Namespace_gmd.addCategoryObject('typeBinding', 'EX_Extent_Type', EX_Extent_Type)


# Complex type {http://www.isotc211.org/2005/gmd}AbstractEX_GeographicExtent_Type with content type ELEMENT_ONLY
class AbstractEX_GeographicExtent_Type (AbstractObject_Type):
    """Geographic area of the dataset"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'AbstractEX_GeographicExtent_Type')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 70, 3)
    _ElementMap = AbstractObject_Type._ElementMap.copy()
    _AttributeMap = AbstractObject_Type._AttributeMap.copy()
    # Base type is AbstractObject_Type
    
    # Element {http://www.isotc211.org/2005/gmd}extentTypeCode uses Python identifier extentTypeCode
    __extentTypeCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'extentTypeCode'), 'extentTypeCode', '__httpwww_isotc211_org2005gmd_AbstractEX_GeographicExtent_Type_httpwww_isotc211_org2005gmdextentTypeCode', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 77, 15), )

    
    extentTypeCode = property(__extentTypeCode.value, __extentTypeCode.set, None, None)

    
    # Attribute id inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    
    # Attribute uuid inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    _ElementMap.update({
        __extentTypeCode.name() : __extentTypeCode
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AbstractEX_GeographicExtent_Type = AbstractEX_GeographicExtent_Type
_Namespace_gmd.addCategoryObject('typeBinding', 'AbstractEX_GeographicExtent_Type', AbstractEX_GeographicExtent_Type)


# Complex type {http://www.isotc211.org/2005/gmd}EX_TemporalExtent_Type with content type ELEMENT_ONLY
class EX_TemporalExtent_Type (AbstractObject_Type):
    """Time period covered by the content of the dataset"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'EX_TemporalExtent_Type')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 95, 3)
    _ElementMap = AbstractObject_Type._ElementMap.copy()
    _AttributeMap = AbstractObject_Type._AttributeMap.copy()
    # Base type is AbstractObject_Type
    
    # Element {http://www.isotc211.org/2005/gmd}extent uses Python identifier extent
    __extent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'extent'), 'extent', '__httpwww_isotc211_org2005gmd_EX_TemporalExtent_Type_httpwww_isotc211_org2005gmdextent', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 102, 15), )

    
    extent = property(__extent.value, __extent.set, None, None)

    
    # Attribute id inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    
    # Attribute uuid inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    _ElementMap.update({
        __extent.name() : __extent
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.EX_TemporalExtent_Type = EX_TemporalExtent_Type
_Namespace_gmd.addCategoryObject('typeBinding', 'EX_TemporalExtent_Type', EX_TemporalExtent_Type)


# Complex type {http://www.isotc211.org/2005/gmd}EX_VerticalExtent_Type with content type ELEMENT_ONLY
class EX_VerticalExtent_Type (AbstractObject_Type):
    """Vertical domain of dataset"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'EX_VerticalExtent_Type')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 118, 3)
    _ElementMap = AbstractObject_Type._ElementMap.copy()
    _AttributeMap = AbstractObject_Type._AttributeMap.copy()
    # Base type is AbstractObject_Type
    
    # Element {http://www.isotc211.org/2005/gmd}minimumValue uses Python identifier minimumValue
    __minimumValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'minimumValue'), 'minimumValue', '__httpwww_isotc211_org2005gmd_EX_VerticalExtent_Type_httpwww_isotc211_org2005gmdminimumValue', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 125, 15), )

    
    minimumValue = property(__minimumValue.value, __minimumValue.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}maximumValue uses Python identifier maximumValue
    __maximumValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'maximumValue'), 'maximumValue', '__httpwww_isotc211_org2005gmd_EX_VerticalExtent_Type_httpwww_isotc211_org2005gmdmaximumValue', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 126, 15), )

    
    maximumValue = property(__maximumValue.value, __maximumValue.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}verticalCRS uses Python identifier verticalCRS
    __verticalCRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'verticalCRS'), 'verticalCRS', '__httpwww_isotc211_org2005gmd_EX_VerticalExtent_Type_httpwww_isotc211_org2005gmdverticalCRS', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 127, 15), )

    
    verticalCRS = property(__verticalCRS.value, __verticalCRS.set, None, None)

    
    # Attribute id inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    
    # Attribute uuid inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    _ElementMap.update({
        __minimumValue.name() : __minimumValue,
        __maximumValue.name() : __maximumValue,
        __verticalCRS.name() : __verticalCRS
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.EX_VerticalExtent_Type = EX_VerticalExtent_Type
_Namespace_gmd.addCategoryObject('typeBinding', 'EX_VerticalExtent_Type', EX_VerticalExtent_Type)


# Complex type {http://www.isotc211.org/2005/gmd}AbstractDQ_Element_Type with content type ELEMENT_ONLY
class AbstractDQ_Element_Type (AbstractObject_Type):
    """Complex type {http://www.isotc211.org/2005/gmd}AbstractDQ_Element_Type with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'AbstractDQ_Element_Type')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 146, 3)
    _ElementMap = AbstractObject_Type._ElementMap.copy()
    _AttributeMap = AbstractObject_Type._AttributeMap.copy()
    # Base type is AbstractObject_Type
    
    # Element {http://www.isotc211.org/2005/gmd}nameOfMeasure uses Python identifier nameOfMeasure
    __nameOfMeasure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'nameOfMeasure'), 'nameOfMeasure', '__httpwww_isotc211_org2005gmd_AbstractDQ_Element_Type_httpwww_isotc211_org2005gmdnameOfMeasure', True, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 150, 15), )

    
    nameOfMeasure = property(__nameOfMeasure.value, __nameOfMeasure.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}measureIdentification uses Python identifier measureIdentification
    __measureIdentification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'measureIdentification'), 'measureIdentification', '__httpwww_isotc211_org2005gmd_AbstractDQ_Element_Type_httpwww_isotc211_org2005gmdmeasureIdentification', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 152, 15), )

    
    measureIdentification = property(__measureIdentification.value, __measureIdentification.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}measureDescription uses Python identifier measureDescription
    __measureDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'measureDescription'), 'measureDescription', '__httpwww_isotc211_org2005gmd_AbstractDQ_Element_Type_httpwww_isotc211_org2005gmdmeasureDescription', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 154, 15), )

    
    measureDescription = property(__measureDescription.value, __measureDescription.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}evaluationMethodType uses Python identifier evaluationMethodType
    __evaluationMethodType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'evaluationMethodType'), 'evaluationMethodType', '__httpwww_isotc211_org2005gmd_AbstractDQ_Element_Type_httpwww_isotc211_org2005gmdevaluationMethodType', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 155, 15), )

    
    evaluationMethodType = property(__evaluationMethodType.value, __evaluationMethodType.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}evaluationMethodDescription uses Python identifier evaluationMethodDescription
    __evaluationMethodDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'evaluationMethodDescription'), 'evaluationMethodDescription', '__httpwww_isotc211_org2005gmd_AbstractDQ_Element_Type_httpwww_isotc211_org2005gmdevaluationMethodDescription', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 157, 15), )

    
    evaluationMethodDescription = property(__evaluationMethodDescription.value, __evaluationMethodDescription.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}evaluationProcedure uses Python identifier evaluationProcedure
    __evaluationProcedure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'evaluationProcedure'), 'evaluationProcedure', '__httpwww_isotc211_org2005gmd_AbstractDQ_Element_Type_httpwww_isotc211_org2005gmdevaluationProcedure', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 159, 15), )

    
    evaluationProcedure = property(__evaluationProcedure.value, __evaluationProcedure.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}dateTime uses Python identifier dateTime
    __dateTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'dateTime'), 'dateTime', '__httpwww_isotc211_org2005gmd_AbstractDQ_Element_Type_httpwww_isotc211_org2005gmddateTime', True, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 160, 15), )

    
    dateTime = property(__dateTime.value, __dateTime.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}result uses Python identifier result
    __result = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'result'), 'result', '__httpwww_isotc211_org2005gmd_AbstractDQ_Element_Type_httpwww_isotc211_org2005gmdresult', True, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 162, 15), )

    
    result = property(__result.value, __result.set, None, None)

    
    # Attribute id inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    
    # Attribute uuid inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    _ElementMap.update({
        __nameOfMeasure.name() : __nameOfMeasure,
        __measureIdentification.name() : __measureIdentification,
        __measureDescription.name() : __measureDescription,
        __evaluationMethodType.name() : __evaluationMethodType,
        __evaluationMethodDescription.name() : __evaluationMethodDescription,
        __evaluationProcedure.name() : __evaluationProcedure,
        __dateTime.name() : __dateTime,
        __result.name() : __result
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AbstractDQ_Element_Type = AbstractDQ_Element_Type
_Namespace_gmd.addCategoryObject('typeBinding', 'AbstractDQ_Element_Type', AbstractDQ_Element_Type)


# Complex type {http://www.isotc211.org/2005/gmd}MD_Identifier_Type with content type ELEMENT_ONLY
class MD_Identifier_Type (AbstractObject_Type):
    """Complex type {http://www.isotc211.org/2005/gmd}MD_Identifier_Type with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'MD_Identifier_Type')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 178, 3)
    _ElementMap = AbstractObject_Type._ElementMap.copy()
    _AttributeMap = AbstractObject_Type._AttributeMap.copy()
    # Base type is AbstractObject_Type
    
    # Element {http://www.isotc211.org/2005/gmd}authority uses Python identifier authority
    __authority = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'authority'), 'authority', '__httpwww_isotc211_org2005gmd_MD_Identifier_Type_httpwww_isotc211_org2005gmdauthority', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 182, 15), )

    
    authority = property(__authority.value, __authority.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}code uses Python identifier code
    __code = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'code'), 'code', '__httpwww_isotc211_org2005gmd_MD_Identifier_Type_httpwww_isotc211_org2005gmdcode', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 183, 15), )

    
    code = property(__code.value, __code.set, None, None)

    
    # Attribute id inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    
    # Attribute uuid inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    _ElementMap.update({
        __authority.name() : __authority,
        __code.name() : __code
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MD_Identifier_Type = MD_Identifier_Type
_Namespace_gmd.addCategoryObject('typeBinding', 'MD_Identifier_Type', MD_Identifier_Type)


# Complex type {http://www.isotc211.org/2005/gmd}CI_Citation_Type with content type ELEMENT_ONLY
class CI_Citation_Type (AbstractObject_Type):
    """Standardized resource reference"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Citation_Type')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 199, 3)
    _ElementMap = AbstractObject_Type._ElementMap.copy()
    _AttributeMap = AbstractObject_Type._AttributeMap.copy()
    # Base type is AbstractObject_Type
    
    # Element {http://www.isotc211.org/2005/gmd}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'title'), 'title', '__httpwww_isotc211_org2005gmd_CI_Citation_Type_httpwww_isotc211_org2005gmdtitle', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 206, 15), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}alternateTitle uses Python identifier alternateTitle
    __alternateTitle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'alternateTitle'), 'alternateTitle', '__httpwww_isotc211_org2005gmd_CI_Citation_Type_httpwww_isotc211_org2005gmdalternateTitle', True, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 207, 15), )

    
    alternateTitle = property(__alternateTitle.value, __alternateTitle.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}date uses Python identifier date
    __date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'date'), 'date', '__httpwww_isotc211_org2005gmd_CI_Citation_Type_httpwww_isotc211_org2005gmddate', True, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 209, 15), )

    
    date = property(__date.value, __date.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}edition uses Python identifier edition
    __edition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'edition'), 'edition', '__httpwww_isotc211_org2005gmd_CI_Citation_Type_httpwww_isotc211_org2005gmdedition', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 210, 15), )

    
    edition = property(__edition.value, __edition.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}editionDate uses Python identifier editionDate
    __editionDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'editionDate'), 'editionDate', '__httpwww_isotc211_org2005gmd_CI_Citation_Type_httpwww_isotc211_org2005gmdeditionDate', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 211, 15), )

    
    editionDate = property(__editionDate.value, __editionDate.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'identifier'), 'identifier', '__httpwww_isotc211_org2005gmd_CI_Citation_Type_httpwww_isotc211_org2005gmdidentifier', True, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 212, 15), )

    
    identifier = property(__identifier.value, __identifier.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}citedResponsibleParty uses Python identifier citedResponsibleParty
    __citedResponsibleParty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'citedResponsibleParty'), 'citedResponsibleParty', '__httpwww_isotc211_org2005gmd_CI_Citation_Type_httpwww_isotc211_org2005gmdcitedResponsibleParty', True, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 214, 15), )

    
    citedResponsibleParty = property(__citedResponsibleParty.value, __citedResponsibleParty.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}presentationForm uses Python identifier presentationForm
    __presentationForm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'presentationForm'), 'presentationForm', '__httpwww_isotc211_org2005gmd_CI_Citation_Type_httpwww_isotc211_org2005gmdpresentationForm', True, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 217, 15), )

    
    presentationForm = property(__presentationForm.value, __presentationForm.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}series uses Python identifier series
    __series = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'series'), 'series', '__httpwww_isotc211_org2005gmd_CI_Citation_Type_httpwww_isotc211_org2005gmdseries', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 220, 15), )

    
    series = property(__series.value, __series.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}otherCitationDetails uses Python identifier otherCitationDetails
    __otherCitationDetails = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'otherCitationDetails'), 'otherCitationDetails', '__httpwww_isotc211_org2005gmd_CI_Citation_Type_httpwww_isotc211_org2005gmdotherCitationDetails', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 221, 15), )

    
    otherCitationDetails = property(__otherCitationDetails.value, __otherCitationDetails.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}collectiveTitle uses Python identifier collectiveTitle
    __collectiveTitle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'collectiveTitle'), 'collectiveTitle', '__httpwww_isotc211_org2005gmd_CI_Citation_Type_httpwww_isotc211_org2005gmdcollectiveTitle', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 223, 15), )

    
    collectiveTitle = property(__collectiveTitle.value, __collectiveTitle.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}ISBN uses Python identifier ISBN
    __ISBN = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'ISBN'), 'ISBN', '__httpwww_isotc211_org2005gmd_CI_Citation_Type_httpwww_isotc211_org2005gmdISBN', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 224, 15), )

    
    ISBN = property(__ISBN.value, __ISBN.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}ISSN uses Python identifier ISSN
    __ISSN = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'ISSN'), 'ISSN', '__httpwww_isotc211_org2005gmd_CI_Citation_Type_httpwww_isotc211_org2005gmdISSN', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 225, 15), )

    
    ISSN = property(__ISSN.value, __ISSN.set, None, None)

    
    # Attribute id inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    
    # Attribute uuid inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    _ElementMap.update({
        __title.name() : __title,
        __alternateTitle.name() : __alternateTitle,
        __date.name() : __date,
        __edition.name() : __edition,
        __editionDate.name() : __editionDate,
        __identifier.name() : __identifier,
        __citedResponsibleParty.name() : __citedResponsibleParty,
        __presentationForm.name() : __presentationForm,
        __series.name() : __series,
        __otherCitationDetails.name() : __otherCitationDetails,
        __collectiveTitle.name() : __collectiveTitle,
        __ISBN.name() : __ISBN,
        __ISSN.name() : __ISSN
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CI_Citation_Type = CI_Citation_Type
_Namespace_gmd.addCategoryObject('typeBinding', 'CI_Citation_Type', CI_Citation_Type)


# Complex type {http://www.isotc211.org/2005/gmd}CI_Date_Type with content type ELEMENT_ONLY
class CI_Date_Type (AbstractObject_Type):
    """Complex type {http://www.isotc211.org/2005/gmd}CI_Date_Type with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Date_Type')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 241, 3)
    _ElementMap = AbstractObject_Type._ElementMap.copy()
    _AttributeMap = AbstractObject_Type._AttributeMap.copy()
    # Base type is AbstractObject_Type
    
    # Element {http://www.isotc211.org/2005/gmd}date uses Python identifier date
    __date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'date'), 'date', '__httpwww_isotc211_org2005gmd_CI_Date_Type_httpwww_isotc211_org2005gmddate', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 245, 15), )

    
    date = property(__date.value, __date.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}dateType uses Python identifier dateType
    __dateType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'dateType'), 'dateType', '__httpwww_isotc211_org2005gmd_CI_Date_Type_httpwww_isotc211_org2005gmddateType', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 246, 15), )

    
    dateType = property(__dateType.value, __dateType.set, None, None)

    
    # Attribute id inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    
    # Attribute uuid inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    _ElementMap.update({
        __date.name() : __date,
        __dateType.name() : __dateType
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CI_Date_Type = CI_Date_Type
_Namespace_gmd.addCategoryObject('typeBinding', 'CI_Date_Type', CI_Date_Type)


# Complex type {http://www.isotc211.org/2005/gmd}CI_ResponsibleParty_Type with content type ELEMENT_ONLY
class CI_ResponsibleParty_Type (AbstractObject_Type):
    """Identification of, and means of communication with, person(s) and organisations associated with the dataset"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_ResponsibleParty_Type')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 282, 3)
    _ElementMap = AbstractObject_Type._ElementMap.copy()
    _AttributeMap = AbstractObject_Type._AttributeMap.copy()
    # Base type is AbstractObject_Type
    
    # Element {http://www.isotc211.org/2005/gmd}individualName uses Python identifier individualName
    __individualName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'individualName'), 'individualName', '__httpwww_isotc211_org2005gmd_CI_ResponsibleParty_Type_httpwww_isotc211_org2005gmdindividualName', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 289, 15), )

    
    individualName = property(__individualName.value, __individualName.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}organisationName uses Python identifier organisationName
    __organisationName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'organisationName'), 'organisationName', '__httpwww_isotc211_org2005gmd_CI_ResponsibleParty_Type_httpwww_isotc211_org2005gmdorganisationName', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 290, 15), )

    
    organisationName = property(__organisationName.value, __organisationName.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}positionName uses Python identifier positionName
    __positionName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'positionName'), 'positionName', '__httpwww_isotc211_org2005gmd_CI_ResponsibleParty_Type_httpwww_isotc211_org2005gmdpositionName', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 291, 15), )

    
    positionName = property(__positionName.value, __positionName.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}contactInfo uses Python identifier contactInfo
    __contactInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'contactInfo'), 'contactInfo', '__httpwww_isotc211_org2005gmd_CI_ResponsibleParty_Type_httpwww_isotc211_org2005gmdcontactInfo', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 292, 15), )

    
    contactInfo = property(__contactInfo.value, __contactInfo.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}role uses Python identifier role
    __role = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'role'), 'role', '__httpwww_isotc211_org2005gmd_CI_ResponsibleParty_Type_httpwww_isotc211_org2005gmdrole', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 293, 15), )

    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute id inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    
    # Attribute uuid inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    _ElementMap.update({
        __individualName.name() : __individualName,
        __organisationName.name() : __organisationName,
        __positionName.name() : __positionName,
        __contactInfo.name() : __contactInfo,
        __role.name() : __role
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CI_ResponsibleParty_Type = CI_ResponsibleParty_Type
_Namespace_gmd.addCategoryObject('typeBinding', 'CI_ResponsibleParty_Type', CI_ResponsibleParty_Type)


# Complex type {http://www.isotc211.org/2005/gmd}CI_Contact_Type with content type ELEMENT_ONLY
class CI_Contact_Type (AbstractObject_Type):
    """Information required enabling contact with the  responsible person and/or organisation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Contact_Type')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 309, 3)
    _ElementMap = AbstractObject_Type._ElementMap.copy()
    _AttributeMap = AbstractObject_Type._AttributeMap.copy()
    # Base type is AbstractObject_Type
    
    # Element {http://www.isotc211.org/2005/gmd}phone uses Python identifier phone
    __phone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'phone'), 'phone', '__httpwww_isotc211_org2005gmd_CI_Contact_Type_httpwww_isotc211_org2005gmdphone', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 316, 15), )

    
    phone = property(__phone.value, __phone.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}address uses Python identifier address
    __address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'address'), 'address', '__httpwww_isotc211_org2005gmd_CI_Contact_Type_httpwww_isotc211_org2005gmdaddress', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 317, 15), )

    
    address = property(__address.value, __address.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}onlineResource uses Python identifier onlineResource
    __onlineResource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'onlineResource'), 'onlineResource', '__httpwww_isotc211_org2005gmd_CI_Contact_Type_httpwww_isotc211_org2005gmdonlineResource', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 318, 15), )

    
    onlineResource = property(__onlineResource.value, __onlineResource.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}hoursOfService uses Python identifier hoursOfService
    __hoursOfService = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'hoursOfService'), 'hoursOfService', '__httpwww_isotc211_org2005gmd_CI_Contact_Type_httpwww_isotc211_org2005gmdhoursOfService', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 319, 15), )

    
    hoursOfService = property(__hoursOfService.value, __hoursOfService.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}contactInstructions uses Python identifier contactInstructions
    __contactInstructions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'contactInstructions'), 'contactInstructions', '__httpwww_isotc211_org2005gmd_CI_Contact_Type_httpwww_isotc211_org2005gmdcontactInstructions', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 320, 15), )

    
    contactInstructions = property(__contactInstructions.value, __contactInstructions.set, None, None)

    
    # Attribute id inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    
    # Attribute uuid inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    _ElementMap.update({
        __phone.name() : __phone,
        __address.name() : __address,
        __onlineResource.name() : __onlineResource,
        __hoursOfService.name() : __hoursOfService,
        __contactInstructions.name() : __contactInstructions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CI_Contact_Type = CI_Contact_Type
_Namespace_gmd.addCategoryObject('typeBinding', 'CI_Contact_Type', CI_Contact_Type)


# Complex type {http://www.isotc211.org/2005/gmd}CI_Telephone_Type with content type ELEMENT_ONLY
class CI_Telephone_Type (AbstractObject_Type):
    """Telephone numbers for contacting the responsible individual or organisation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Telephone_Type')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 337, 3)
    _ElementMap = AbstractObject_Type._ElementMap.copy()
    _AttributeMap = AbstractObject_Type._AttributeMap.copy()
    # Base type is AbstractObject_Type
    
    # Element {http://www.isotc211.org/2005/gmd}voice uses Python identifier voice
    __voice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'voice'), 'voice', '__httpwww_isotc211_org2005gmd_CI_Telephone_Type_httpwww_isotc211_org2005gmdvoice', True, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 344, 15), )

    
    voice = property(__voice.value, __voice.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}facsimile uses Python identifier facsimile
    __facsimile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'facsimile'), 'facsimile', '__httpwww_isotc211_org2005gmd_CI_Telephone_Type_httpwww_isotc211_org2005gmdfacsimile', True, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 346, 15), )

    
    facsimile = property(__facsimile.value, __facsimile.set, None, None)

    
    # Attribute id inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    
    # Attribute uuid inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    _ElementMap.update({
        __voice.name() : __voice,
        __facsimile.name() : __facsimile
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CI_Telephone_Type = CI_Telephone_Type
_Namespace_gmd.addCategoryObject('typeBinding', 'CI_Telephone_Type', CI_Telephone_Type)


# Complex type {http://www.isotc211.org/2005/gmd}CI_Address_Type with content type ELEMENT_ONLY
class CI_Address_Type (AbstractObject_Type):
    """Location of the responsible individual or organisation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Address_Type')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 363, 3)
    _ElementMap = AbstractObject_Type._ElementMap.copy()
    _AttributeMap = AbstractObject_Type._AttributeMap.copy()
    # Base type is AbstractObject_Type
    
    # Element {http://www.isotc211.org/2005/gmd}deliveryPoint uses Python identifier deliveryPoint
    __deliveryPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'deliveryPoint'), 'deliveryPoint', '__httpwww_isotc211_org2005gmd_CI_Address_Type_httpwww_isotc211_org2005gmddeliveryPoint', True, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 370, 15), )

    
    deliveryPoint = property(__deliveryPoint.value, __deliveryPoint.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'city'), 'city', '__httpwww_isotc211_org2005gmd_CI_Address_Type_httpwww_isotc211_org2005gmdcity', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 372, 15), )

    
    city = property(__city.value, __city.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}administrativeArea uses Python identifier administrativeArea
    __administrativeArea = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'administrativeArea'), 'administrativeArea', '__httpwww_isotc211_org2005gmd_CI_Address_Type_httpwww_isotc211_org2005gmdadministrativeArea', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 373, 15), )

    
    administrativeArea = property(__administrativeArea.value, __administrativeArea.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}postalCode uses Python identifier postalCode
    __postalCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'postalCode'), 'postalCode', '__httpwww_isotc211_org2005gmd_CI_Address_Type_httpwww_isotc211_org2005gmdpostalCode', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 374, 15), )

    
    postalCode = property(__postalCode.value, __postalCode.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}country uses Python identifier country
    __country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'country'), 'country', '__httpwww_isotc211_org2005gmd_CI_Address_Type_httpwww_isotc211_org2005gmdcountry', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 375, 15), )

    
    country = property(__country.value, __country.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}electronicMailAddress uses Python identifier electronicMailAddress
    __electronicMailAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'electronicMailAddress'), 'electronicMailAddress', '__httpwww_isotc211_org2005gmd_CI_Address_Type_httpwww_isotc211_org2005gmdelectronicMailAddress', True, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 376, 15), )

    
    electronicMailAddress = property(__electronicMailAddress.value, __electronicMailAddress.set, None, None)

    
    # Attribute id inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    
    # Attribute uuid inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    _ElementMap.update({
        __deliveryPoint.name() : __deliveryPoint,
        __city.name() : __city,
        __administrativeArea.name() : __administrativeArea,
        __postalCode.name() : __postalCode,
        __country.name() : __country,
        __electronicMailAddress.name() : __electronicMailAddress
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CI_Address_Type = CI_Address_Type
_Namespace_gmd.addCategoryObject('typeBinding', 'CI_Address_Type', CI_Address_Type)


# Complex type {http://www.isotc211.org/2005/gmd}CI_OnlineResource_Type with content type ELEMENT_ONLY
class CI_OnlineResource_Type (AbstractObject_Type):
    """Information about online sources from which the dataset, specification, or community profile name and extended metadata elements can be obtained."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_OnlineResource_Type')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 394, 3)
    _ElementMap = AbstractObject_Type._ElementMap.copy()
    _AttributeMap = AbstractObject_Type._AttributeMap.copy()
    # Base type is AbstractObject_Type
    
    # Element {http://www.isotc211.org/2005/gmd}linkage uses Python identifier linkage
    __linkage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'linkage'), 'linkage', '__httpwww_isotc211_org2005gmd_CI_OnlineResource_Type_httpwww_isotc211_org2005gmdlinkage', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 401, 15), )

    
    linkage = property(__linkage.value, __linkage.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}protocol uses Python identifier protocol
    __protocol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'protocol'), 'protocol', '__httpwww_isotc211_org2005gmd_CI_OnlineResource_Type_httpwww_isotc211_org2005gmdprotocol', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 402, 15), )

    
    protocol = property(__protocol.value, __protocol.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}applicationProfile uses Python identifier applicationProfile
    __applicationProfile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'applicationProfile'), 'applicationProfile', '__httpwww_isotc211_org2005gmd_CI_OnlineResource_Type_httpwww_isotc211_org2005gmdapplicationProfile', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 403, 15), )

    
    applicationProfile = property(__applicationProfile.value, __applicationProfile.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'name'), 'name', '__httpwww_isotc211_org2005gmd_CI_OnlineResource_Type_httpwww_isotc211_org2005gmdname', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 404, 15), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'description'), 'description', '__httpwww_isotc211_org2005gmd_CI_OnlineResource_Type_httpwww_isotc211_org2005gmddescription', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 405, 15), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}function uses Python identifier function
    __function = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'function'), 'function', '__httpwww_isotc211_org2005gmd_CI_OnlineResource_Type_httpwww_isotc211_org2005gmdfunction', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 406, 15), )

    
    function = property(__function.value, __function.set, None, None)

    
    # Attribute id inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    
    # Attribute uuid inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    _ElementMap.update({
        __linkage.name() : __linkage,
        __protocol.name() : __protocol,
        __applicationProfile.name() : __applicationProfile,
        __name.name() : __name,
        __description.name() : __description,
        __function.name() : __function
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CI_OnlineResource_Type = CI_OnlineResource_Type
_Namespace_gmd.addCategoryObject('typeBinding', 'CI_OnlineResource_Type', CI_OnlineResource_Type)


# Complex type {http://www.isotc211.org/2005/gmd}CI_Series_Type with content type ELEMENT_ONLY
class CI_Series_Type (AbstractObject_Type):
    """Complex type {http://www.isotc211.org/2005/gmd}CI_Series_Type with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Series_Type')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 461, 3)
    _ElementMap = AbstractObject_Type._ElementMap.copy()
    _AttributeMap = AbstractObject_Type._AttributeMap.copy()
    # Base type is AbstractObject_Type
    
    # Element {http://www.isotc211.org/2005/gmd}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'name'), 'name', '__httpwww_isotc211_org2005gmd_CI_Series_Type_httpwww_isotc211_org2005gmdname', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 465, 15), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}issueIdentification uses Python identifier issueIdentification
    __issueIdentification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'issueIdentification'), 'issueIdentification', '__httpwww_isotc211_org2005gmd_CI_Series_Type_httpwww_isotc211_org2005gmdissueIdentification', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 466, 15), )

    
    issueIdentification = property(__issueIdentification.value, __issueIdentification.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gmd}page uses Python identifier page
    __page = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'page'), 'page', '__httpwww_isotc211_org2005gmd_CI_Series_Type_httpwww_isotc211_org2005gmdpage', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 468, 15), )

    
    page = property(__page.value, __page.set, None, None)

    
    # Attribute id inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    
    # Attribute uuid inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    _ElementMap.update({
        __name.name() : __name,
        __issueIdentification.name() : __issueIdentification,
        __page.name() : __page
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CI_Series_Type = CI_Series_Type
_Namespace_gmd.addCategoryObject('typeBinding', 'CI_Series_Type', CI_Series_Type)


# Complex type {http://www.isotc211.org/2005/gmd}AbstractDQ_Result_Type with content type EMPTY
class AbstractDQ_Result_Type (AbstractObject_Type):
    """Complex type {http://www.isotc211.org/2005/gmd}AbstractDQ_Result_Type with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'AbstractDQ_Result_Type')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 494, 3)
    _ElementMap = AbstractObject_Type._ElementMap.copy()
    _AttributeMap = AbstractObject_Type._AttributeMap.copy()
    # Base type is AbstractObject_Type
    
    # Attribute id inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    
    # Attribute uuid inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AbstractDQ_Result_Type = AbstractDQ_Result_Type
_Namespace_gmd.addCategoryObject('typeBinding', 'AbstractDQ_Result_Type', AbstractDQ_Result_Type)


# Complex type {http://www.opengis.net/gml/3.2}DefinitionBaseType with content type ELEMENT_ONLY
class DefinitionBaseType (AbstractGMLType):
    """Complex type {http://www.opengis.net/gml/3.2}DefinitionBaseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'DefinitionBaseType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 81, 3)
    _ElementMap = AbstractGMLType._ElementMap.copy()
    _AttributeMap = AbstractGMLType._AttributeMap.copy()
    # Base type is AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Attribute id is restricted from parent
    
    # Attribute {http://www.opengis.net/gml/3.2}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'id'), 'id', '__httpwww_opengis_netgml3_2_AbstractGMLType_httpwww_opengis_netgml3_2id', pyxb.binding.datatypes.ID, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 113, 3)
    __id._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 91, 12)
    
    id = property(__id.value, __id.set, None, 'The attribute gml:id supports provision of a handle for the XML element representing a GML Object. Its use is mandatory for all GML objects. It is of XML type ID, so is constrained to be unique in the XML document within which it occurs.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.DefinitionBaseType = DefinitionBaseType
_Namespace_gml.addCategoryObject('typeBinding', 'DefinitionBaseType', DefinitionBaseType)


# Complex type {http://www.opengis.net/gml/3.2}CodeWithAuthorityType with content type SIMPLE
class CodeWithAuthorityType (CodeType):
    """gml:CodeWithAuthorityType requires that the codeSpace attribute is provided in an instance."""
    _TypeDefinition = STD_ANON_2
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'CodeWithAuthorityType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 221, 3)
    _ElementMap = CodeType._ElementMap.copy()
    _AttributeMap = CodeType._AttributeMap.copy()
    # Base type is CodeType
    
    # Attribute codeSpace is restricted from parent
    
    # Attribute codeSpace uses Python identifier codeSpace
    __codeSpace = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'codeSpace'), 'codeSpace', '__httpwww_opengis_netgml3_2_CodeType_codeSpace', pyxb.binding.datatypes.anyURI, required=True)
    __codeSpace._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 227, 12)
    __codeSpace._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 227, 12)
    
    codeSpace = property(__codeSpace.value, __codeSpace.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __codeSpace.name() : __codeSpace
    })
_module_typeBindings.CodeWithAuthorityType = CodeWithAuthorityType
_Namespace_gml.addCategoryObject('typeBinding', 'CodeWithAuthorityType', CodeWithAuthorityType)


# Complex type {http://www.opengis.net/gml/3.2}AbstractTimeObjectType with content type ELEMENT_ONLY
class AbstractTimeObjectType (AbstractGMLType):
    """Complex type {http://www.opengis.net/gml/3.2}AbstractTimeObjectType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractTimeObjectType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 289, 3)
    _ElementMap = AbstractGMLType._ElementMap.copy()
    _AttributeMap = AbstractGMLType._AttributeMap.copy()
    # Base type is AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AbstractTimeObjectType = AbstractTimeObjectType
_Namespace_gml.addCategoryObject('typeBinding', 'AbstractTimeObjectType', AbstractTimeObjectType)


# Complex type {http://www.opengis.net/gml/3.2}AngleType with content type SIMPLE
class AngleType (MeasureType):
    """Complex type {http://www.opengis.net/gml/3.2}AngleType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.double
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'AngleType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 704, 3)
    _ElementMap = MeasureType._ElementMap.copy()
    _AttributeMap = MeasureType._AttributeMap.copy()
    # Base type is MeasureType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AngleType = AngleType
_Namespace_gml.addCategoryObject('typeBinding', 'AngleType', AngleType)


# Complex type {http://www.opengis.net/gml/3.2}LengthType with content type SIMPLE
class LengthType (MeasureType):
    """This is a prototypical definition for a specific measure type defined as a vacuous extension (i.e. aliases) of gml:MeasureType. In this case, the content model supports the description of a length (or distance) quantity, with its units. The unit of measure referenced by uom shall be suitable for a length, such as metres or feet."""
    _TypeDefinition = pyxb.binding.datatypes.double
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'LengthType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 783, 3)
    _ElementMap = MeasureType._ElementMap.copy()
    _AttributeMap = MeasureType._AttributeMap.copy()
    # Base type is MeasureType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LengthType = LengthType
_Namespace_gml.addCategoryObject('typeBinding', 'LengthType', LengthType)


# Complex type {http://www.isotc211.org/2005/gco}CharacterString_PropertyType with content type ELEMENT_ONLY
class CharacterString_PropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.isotc211.org/2005/gco}CharacterString_PropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gco, 'CharacterString_PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 45, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.isotc211.org/2005/gco}CharacterString uses Python identifier CharacterString
    __CharacterString = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gco, 'CharacterString'), 'CharacterString', '__httpwww_isotc211_org2005gco_CharacterString_PropertyType_httpwww_isotc211_org2005gcoCharacterString', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 52, 3), )

    
    CharacterString = property(__CharacterString.value, __CharacterString.set, None, None)

    
    # Attribute {http://www.isotc211.org/2005/gco}nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gco, 'nilReason'), 'nilReason', '__httpwww_isotc211_org2005gco_CharacterString_PropertyType_httpwww_isotc211_org2005gconilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 54, 3)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 49, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    _ElementMap.update({
        __CharacterString.name() : __CharacterString
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason
    })
_module_typeBindings.CharacterString_PropertyType = CharacterString_PropertyType
_Namespace_gco.addCategoryObject('typeBinding', 'CharacterString_PropertyType', CharacterString_PropertyType)


# Complex type {http://www.isotc211.org/2005/gco}Boolean_PropertyType with content type ELEMENT_ONLY
class Boolean_PropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.isotc211.org/2005/gco}Boolean_PropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gco, 'Boolean_PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 56, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.isotc211.org/2005/gco}Boolean uses Python identifier Boolean
    __Boolean = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gco, 'Boolean'), 'Boolean', '__httpwww_isotc211_org2005gco_Boolean_PropertyType_httpwww_isotc211_org2005gcoBoolean', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 63, 3), )

    
    Boolean = property(__Boolean.value, __Boolean.set, None, None)

    
    # Attribute {http://www.isotc211.org/2005/gco}nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gco, 'nilReason'), 'nilReason', '__httpwww_isotc211_org2005gco_Boolean_PropertyType_httpwww_isotc211_org2005gconilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 54, 3)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 60, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    _ElementMap.update({
        __Boolean.name() : __Boolean
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason
    })
_module_typeBindings.Boolean_PropertyType = Boolean_PropertyType
_Namespace_gco.addCategoryObject('typeBinding', 'Boolean_PropertyType', Boolean_PropertyType)


# Complex type {http://www.isotc211.org/2005/gco}Real_PropertyType with content type ELEMENT_ONLY
class Real_PropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.isotc211.org/2005/gco}Real_PropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gco, 'Real_PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 72, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.isotc211.org/2005/gco}Real uses Python identifier Real
    __Real = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gco, 'Real'), 'Real', '__httpwww_isotc211_org2005gco_Real_PropertyType_httpwww_isotc211_org2005gcoReal', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 79, 3), )

    
    Real = property(__Real.value, __Real.set, None, None)

    
    # Attribute {http://www.isotc211.org/2005/gco}nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gco, 'nilReason'), 'nilReason', '__httpwww_isotc211_org2005gco_Real_PropertyType_httpwww_isotc211_org2005gconilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 54, 3)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 76, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    _ElementMap.update({
        __Real.name() : __Real
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason
    })
_module_typeBindings.Real_PropertyType = Real_PropertyType
_Namespace_gco.addCategoryObject('typeBinding', 'Real_PropertyType', Real_PropertyType)


# Complex type {http://www.isotc211.org/2005/gco}Date_PropertyType with content type ELEMENT_ONLY
class Date_PropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.isotc211.org/2005/gco}Date_PropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gco, 'Date_PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 83, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.isotc211.org/2005/gco}Date uses Python identifier Date
    __Date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gco, 'Date'), 'Date', '__httpwww_isotc211_org2005gco_Date_PropertyType_httpwww_isotc211_org2005gcoDate', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 91, 3), )

    
    Date = property(__Date.value, __Date.set, None, None)

    
    # Element {http://www.isotc211.org/2005/gco}DateTime uses Python identifier DateTime
    __DateTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gco, 'DateTime'), 'DateTime', '__httpwww_isotc211_org2005gco_Date_PropertyType_httpwww_isotc211_org2005gcoDateTime', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 103, 3), )

    
    DateTime = property(__DateTime.value, __DateTime.set, None, None)

    
    # Attribute {http://www.isotc211.org/2005/gco}nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gco, 'nilReason'), 'nilReason', '__httpwww_isotc211_org2005gco_Date_PropertyType_httpwww_isotc211_org2005gconilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 54, 3)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 88, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    _ElementMap.update({
        __Date.name() : __Date,
        __DateTime.name() : __DateTime
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason
    })
_module_typeBindings.Date_PropertyType = Date_PropertyType
_Namespace_gco.addCategoryObject('typeBinding', 'Date_PropertyType', Date_PropertyType)


# Complex type {http://www.isotc211.org/2005/gco}DateTime_PropertyType with content type ELEMENT_ONLY
class DateTime_PropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.isotc211.org/2005/gco}DateTime_PropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gco, 'DateTime_PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 119, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.isotc211.org/2005/gco}DateTime uses Python identifier DateTime
    __DateTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gco, 'DateTime'), 'DateTime', '__httpwww_isotc211_org2005gco_DateTime_PropertyType_httpwww_isotc211_org2005gcoDateTime', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 103, 3), )

    
    DateTime = property(__DateTime.value, __DateTime.set, None, None)

    
    # Attribute {http://www.isotc211.org/2005/gco}nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gco, 'nilReason'), 'nilReason', '__httpwww_isotc211_org2005gco_DateTime_PropertyType_httpwww_isotc211_org2005gconilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 54, 3)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 123, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    _ElementMap.update({
        __DateTime.name() : __DateTime
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason
    })
_module_typeBindings.DateTime_PropertyType = DateTime_PropertyType
_Namespace_gco.addCategoryObject('typeBinding', 'DateTime_PropertyType', DateTime_PropertyType)


# Complex type {http://www.isotc211.org/2005/gmd}EX_GeographicExtent_PropertyType with content type ELEMENT_ONLY
class EX_GeographicExtent_PropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.isotc211.org/2005/gmd}EX_GeographicExtent_PropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'EX_GeographicExtent_PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 59, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.isotc211.org/2005/gmd}AbstractEX_GeographicExtent uses Python identifier AbstractEX_GeographicExtent
    __AbstractEX_GeographicExtent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'AbstractEX_GeographicExtent'), 'AbstractEX_GeographicExtent', '__httpwww_isotc211_org2005gmd_EX_GeographicExtent_PropertyType_httpwww_isotc211_org2005gmdAbstractEX_GeographicExtent', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 67, 3), )

    
    AbstractEX_GeographicExtent = property(__AbstractEX_GeographicExtent.value, __AbstractEX_GeographicExtent.set, None, None)

    
    # Attribute {http://www.isotc211.org/2005/gco}nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gco, 'nilReason'), 'nilReason', '__httpwww_isotc211_org2005gmd_EX_GeographicExtent_PropertyType_httpwww_isotc211_org2005gconilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 54, 3)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 64, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute uuidref uses Python identifier uuidref
    __uuidref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uuidref'), 'uuidref', '__httpwww_isotc211_org2005gmd_EX_GeographicExtent_PropertyType_uuidref', pyxb.binding.datatypes.string)
    __uuidref._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    __uuidref._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    
    uuidref = property(__uuidref.value, __uuidref.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_isotc211_org2005gmd_EX_GeographicExtent_PropertyType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_isotc211_org2005gmd_EX_GeographicExtent_PropertyType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_isotc211_org2005gmd_EX_GeographicExtent_PropertyType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_isotc211_org2005gmd_EX_GeographicExtent_PropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_isotc211_org2005gmd_EX_GeographicExtent_PropertyType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_isotc211_org2005gmd_EX_GeographicExtent_PropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_isotc211_org2005gmd_EX_GeographicExtent_PropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __AbstractEX_GeographicExtent.name() : __AbstractEX_GeographicExtent
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __uuidref.name() : __uuidref,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.EX_GeographicExtent_PropertyType = EX_GeographicExtent_PropertyType
_Namespace_gmd.addCategoryObject('typeBinding', 'EX_GeographicExtent_PropertyType', EX_GeographicExtent_PropertyType)


# Complex type {http://www.isotc211.org/2005/gmd}EX_TemporalExtent_PropertyType with content type ELEMENT_ONLY
class EX_TemporalExtent_PropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.isotc211.org/2005/gmd}EX_TemporalExtent_PropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'EX_TemporalExtent_PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 85, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.isotc211.org/2005/gmd}EX_TemporalExtent uses Python identifier EX_TemporalExtent
    __EX_TemporalExtent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'EX_TemporalExtent'), 'EX_TemporalExtent', '__httpwww_isotc211_org2005gmd_EX_TemporalExtent_PropertyType_httpwww_isotc211_org2005gmdEX_TemporalExtent', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 93, 3), )

    
    EX_TemporalExtent = property(__EX_TemporalExtent.value, __EX_TemporalExtent.set, None, None)

    
    # Attribute {http://www.isotc211.org/2005/gco}nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gco, 'nilReason'), 'nilReason', '__httpwww_isotc211_org2005gmd_EX_TemporalExtent_PropertyType_httpwww_isotc211_org2005gconilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 54, 3)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 90, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute uuidref uses Python identifier uuidref
    __uuidref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uuidref'), 'uuidref', '__httpwww_isotc211_org2005gmd_EX_TemporalExtent_PropertyType_uuidref', pyxb.binding.datatypes.string)
    __uuidref._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    __uuidref._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    
    uuidref = property(__uuidref.value, __uuidref.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_isotc211_org2005gmd_EX_TemporalExtent_PropertyType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_isotc211_org2005gmd_EX_TemporalExtent_PropertyType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_isotc211_org2005gmd_EX_TemporalExtent_PropertyType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_isotc211_org2005gmd_EX_TemporalExtent_PropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_isotc211_org2005gmd_EX_TemporalExtent_PropertyType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_isotc211_org2005gmd_EX_TemporalExtent_PropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_isotc211_org2005gmd_EX_TemporalExtent_PropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __EX_TemporalExtent.name() : __EX_TemporalExtent
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __uuidref.name() : __uuidref,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.EX_TemporalExtent_PropertyType = EX_TemporalExtent_PropertyType
_Namespace_gmd.addCategoryObject('typeBinding', 'EX_TemporalExtent_PropertyType', EX_TemporalExtent_PropertyType)


# Complex type {http://www.isotc211.org/2005/gmd}EX_VerticalExtent_PropertyType with content type ELEMENT_ONLY
class EX_VerticalExtent_PropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.isotc211.org/2005/gmd}EX_VerticalExtent_PropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'EX_VerticalExtent_PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 108, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.isotc211.org/2005/gmd}EX_VerticalExtent uses Python identifier EX_VerticalExtent
    __EX_VerticalExtent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'EX_VerticalExtent'), 'EX_VerticalExtent', '__httpwww_isotc211_org2005gmd_EX_VerticalExtent_PropertyType_httpwww_isotc211_org2005gmdEX_VerticalExtent', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 116, 3), )

    
    EX_VerticalExtent = property(__EX_VerticalExtent.value, __EX_VerticalExtent.set, None, None)

    
    # Attribute {http://www.isotc211.org/2005/gco}nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gco, 'nilReason'), 'nilReason', '__httpwww_isotc211_org2005gmd_EX_VerticalExtent_PropertyType_httpwww_isotc211_org2005gconilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 54, 3)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 113, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute uuidref uses Python identifier uuidref
    __uuidref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uuidref'), 'uuidref', '__httpwww_isotc211_org2005gmd_EX_VerticalExtent_PropertyType_uuidref', pyxb.binding.datatypes.string)
    __uuidref._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    __uuidref._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    
    uuidref = property(__uuidref.value, __uuidref.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_isotc211_org2005gmd_EX_VerticalExtent_PropertyType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_isotc211_org2005gmd_EX_VerticalExtent_PropertyType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_isotc211_org2005gmd_EX_VerticalExtent_PropertyType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_isotc211_org2005gmd_EX_VerticalExtent_PropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_isotc211_org2005gmd_EX_VerticalExtent_PropertyType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_isotc211_org2005gmd_EX_VerticalExtent_PropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_isotc211_org2005gmd_EX_VerticalExtent_PropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __EX_VerticalExtent.name() : __EX_VerticalExtent
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __uuidref.name() : __uuidref,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.EX_VerticalExtent_PropertyType = EX_VerticalExtent_PropertyType
_Namespace_gmd.addCategoryObject('typeBinding', 'EX_VerticalExtent_PropertyType', EX_VerticalExtent_PropertyType)


# Complex type {http://www.isotc211.org/2005/gmd}AbstractDQ_PositionalAccuracy_Type with content type ELEMENT_ONLY
class AbstractDQ_PositionalAccuracy_Type (AbstractDQ_Element_Type):
    """Complex type {http://www.isotc211.org/2005/gmd}AbstractDQ_PositionalAccuracy_Type with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'AbstractDQ_PositionalAccuracy_Type')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 140, 3)
    _ElementMap = AbstractDQ_Element_Type._ElementMap.copy()
    _AttributeMap = AbstractDQ_Element_Type._AttributeMap.copy()
    # Base type is AbstractDQ_Element_Type
    
    # Element nameOfMeasure ({http://www.isotc211.org/2005/gmd}nameOfMeasure) inherited from {http://www.isotc211.org/2005/gmd}AbstractDQ_Element_Type
    
    # Element measureIdentification ({http://www.isotc211.org/2005/gmd}measureIdentification) inherited from {http://www.isotc211.org/2005/gmd}AbstractDQ_Element_Type
    
    # Element measureDescription ({http://www.isotc211.org/2005/gmd}measureDescription) inherited from {http://www.isotc211.org/2005/gmd}AbstractDQ_Element_Type
    
    # Element evaluationMethodType ({http://www.isotc211.org/2005/gmd}evaluationMethodType) inherited from {http://www.isotc211.org/2005/gmd}AbstractDQ_Element_Type
    
    # Element evaluationMethodDescription ({http://www.isotc211.org/2005/gmd}evaluationMethodDescription) inherited from {http://www.isotc211.org/2005/gmd}AbstractDQ_Element_Type
    
    # Element evaluationProcedure ({http://www.isotc211.org/2005/gmd}evaluationProcedure) inherited from {http://www.isotc211.org/2005/gmd}AbstractDQ_Element_Type
    
    # Element dateTime ({http://www.isotc211.org/2005/gmd}dateTime) inherited from {http://www.isotc211.org/2005/gmd}AbstractDQ_Element_Type
    
    # Element result ({http://www.isotc211.org/2005/gmd}result) inherited from {http://www.isotc211.org/2005/gmd}AbstractDQ_Element_Type
    
    # Attribute id inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    
    # Attribute uuid inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AbstractDQ_PositionalAccuracy_Type = AbstractDQ_PositionalAccuracy_Type
_Namespace_gmd.addCategoryObject('typeBinding', 'AbstractDQ_PositionalAccuracy_Type', AbstractDQ_PositionalAccuracy_Type)


# Complex type {http://www.isotc211.org/2005/gmd}MD_Identifier_PropertyType with content type ELEMENT_ONLY
class MD_Identifier_PropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.isotc211.org/2005/gmd}MD_Identifier_PropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'MD_Identifier_PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 168, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.isotc211.org/2005/gmd}MD_Identifier uses Python identifier MD_Identifier
    __MD_Identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'MD_Identifier'), 'MD_Identifier', '__httpwww_isotc211_org2005gmd_MD_Identifier_PropertyType_httpwww_isotc211_org2005gmdMD_Identifier', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 176, 3), )

    
    MD_Identifier = property(__MD_Identifier.value, __MD_Identifier.set, None, None)

    
    # Attribute {http://www.isotc211.org/2005/gco}nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gco, 'nilReason'), 'nilReason', '__httpwww_isotc211_org2005gmd_MD_Identifier_PropertyType_httpwww_isotc211_org2005gconilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 54, 3)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 173, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute uuidref uses Python identifier uuidref
    __uuidref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uuidref'), 'uuidref', '__httpwww_isotc211_org2005gmd_MD_Identifier_PropertyType_uuidref', pyxb.binding.datatypes.string)
    __uuidref._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    __uuidref._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    
    uuidref = property(__uuidref.value, __uuidref.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_isotc211_org2005gmd_MD_Identifier_PropertyType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_isotc211_org2005gmd_MD_Identifier_PropertyType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_isotc211_org2005gmd_MD_Identifier_PropertyType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_isotc211_org2005gmd_MD_Identifier_PropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_isotc211_org2005gmd_MD_Identifier_PropertyType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_isotc211_org2005gmd_MD_Identifier_PropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_isotc211_org2005gmd_MD_Identifier_PropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __MD_Identifier.name() : __MD_Identifier
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __uuidref.name() : __uuidref,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.MD_Identifier_PropertyType = MD_Identifier_PropertyType
_Namespace_gmd.addCategoryObject('typeBinding', 'MD_Identifier_PropertyType', MD_Identifier_PropertyType)


# Complex type {http://www.isotc211.org/2005/gmd}CI_Citation_PropertyType with content type ELEMENT_ONLY
class CI_Citation_PropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.isotc211.org/2005/gmd}CI_Citation_PropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Citation_PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 189, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.isotc211.org/2005/gmd}CI_Citation uses Python identifier CI_Citation
    __CI_Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Citation'), 'CI_Citation', '__httpwww_isotc211_org2005gmd_CI_Citation_PropertyType_httpwww_isotc211_org2005gmdCI_Citation', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 197, 3), )

    
    CI_Citation = property(__CI_Citation.value, __CI_Citation.set, None, None)

    
    # Attribute {http://www.isotc211.org/2005/gco}nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gco, 'nilReason'), 'nilReason', '__httpwww_isotc211_org2005gmd_CI_Citation_PropertyType_httpwww_isotc211_org2005gconilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 54, 3)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 194, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute uuidref uses Python identifier uuidref
    __uuidref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uuidref'), 'uuidref', '__httpwww_isotc211_org2005gmd_CI_Citation_PropertyType_uuidref', pyxb.binding.datatypes.string)
    __uuidref._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    __uuidref._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    
    uuidref = property(__uuidref.value, __uuidref.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_isotc211_org2005gmd_CI_Citation_PropertyType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_isotc211_org2005gmd_CI_Citation_PropertyType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_isotc211_org2005gmd_CI_Citation_PropertyType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_isotc211_org2005gmd_CI_Citation_PropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_isotc211_org2005gmd_CI_Citation_PropertyType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_isotc211_org2005gmd_CI_Citation_PropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_isotc211_org2005gmd_CI_Citation_PropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __CI_Citation.name() : __CI_Citation
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __uuidref.name() : __uuidref,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.CI_Citation_PropertyType = CI_Citation_PropertyType
_Namespace_gmd.addCategoryObject('typeBinding', 'CI_Citation_PropertyType', CI_Citation_PropertyType)


# Complex type {http://www.isotc211.org/2005/gmd}CI_Date_PropertyType with content type ELEMENT_ONLY
class CI_Date_PropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.isotc211.org/2005/gmd}CI_Date_PropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Date_PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 231, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.isotc211.org/2005/gmd}CI_Date uses Python identifier CI_Date
    __CI_Date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Date'), 'CI_Date', '__httpwww_isotc211_org2005gmd_CI_Date_PropertyType_httpwww_isotc211_org2005gmdCI_Date', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 239, 3), )

    
    CI_Date = property(__CI_Date.value, __CI_Date.set, None, None)

    
    # Attribute {http://www.isotc211.org/2005/gco}nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gco, 'nilReason'), 'nilReason', '__httpwww_isotc211_org2005gmd_CI_Date_PropertyType_httpwww_isotc211_org2005gconilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 54, 3)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 236, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute uuidref uses Python identifier uuidref
    __uuidref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uuidref'), 'uuidref', '__httpwww_isotc211_org2005gmd_CI_Date_PropertyType_uuidref', pyxb.binding.datatypes.string)
    __uuidref._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    __uuidref._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    
    uuidref = property(__uuidref.value, __uuidref.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_isotc211_org2005gmd_CI_Date_PropertyType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_isotc211_org2005gmd_CI_Date_PropertyType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_isotc211_org2005gmd_CI_Date_PropertyType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_isotc211_org2005gmd_CI_Date_PropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_isotc211_org2005gmd_CI_Date_PropertyType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_isotc211_org2005gmd_CI_Date_PropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_isotc211_org2005gmd_CI_Date_PropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __CI_Date.name() : __CI_Date
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __uuidref.name() : __uuidref,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.CI_Date_PropertyType = CI_Date_PropertyType
_Namespace_gmd.addCategoryObject('typeBinding', 'CI_Date_PropertyType', CI_Date_PropertyType)


# Complex type {http://www.isotc211.org/2005/gmd}CI_DateTypeCode_PropertyType with content type ELEMENT_ONLY
class CI_DateTypeCode_PropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.isotc211.org/2005/gmd}CI_DateTypeCode_PropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_DateTypeCode_PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 260, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.isotc211.org/2005/gmd}CI_DateTypeCode uses Python identifier CI_DateTypeCode
    __CI_DateTypeCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_DateTypeCode'), 'CI_DateTypeCode', '__httpwww_isotc211_org2005gmd_CI_DateTypeCode_PropertyType_httpwww_isotc211_org2005gmdCI_DateTypeCode', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 267, 3), )

    
    CI_DateTypeCode = property(__CI_DateTypeCode.value, __CI_DateTypeCode.set, None, None)

    
    # Attribute {http://www.isotc211.org/2005/gco}nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gco, 'nilReason'), 'nilReason', '__httpwww_isotc211_org2005gmd_CI_DateTypeCode_PropertyType_httpwww_isotc211_org2005gconilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 54, 3)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 264, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    _ElementMap.update({
        __CI_DateTypeCode.name() : __CI_DateTypeCode
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason
    })
_module_typeBindings.CI_DateTypeCode_PropertyType = CI_DateTypeCode_PropertyType
_Namespace_gmd.addCategoryObject('typeBinding', 'CI_DateTypeCode_PropertyType', CI_DateTypeCode_PropertyType)


# Complex type {http://www.isotc211.org/2005/gmd}CI_ResponsibleParty_PropertyType with content type ELEMENT_ONLY
class CI_ResponsibleParty_PropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.isotc211.org/2005/gmd}CI_ResponsibleParty_PropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_ResponsibleParty_PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 272, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.isotc211.org/2005/gmd}CI_ResponsibleParty uses Python identifier CI_ResponsibleParty
    __CI_ResponsibleParty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_ResponsibleParty'), 'CI_ResponsibleParty', '__httpwww_isotc211_org2005gmd_CI_ResponsibleParty_PropertyType_httpwww_isotc211_org2005gmdCI_ResponsibleParty', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 280, 3), )

    
    CI_ResponsibleParty = property(__CI_ResponsibleParty.value, __CI_ResponsibleParty.set, None, None)

    
    # Attribute {http://www.isotc211.org/2005/gco}nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gco, 'nilReason'), 'nilReason', '__httpwww_isotc211_org2005gmd_CI_ResponsibleParty_PropertyType_httpwww_isotc211_org2005gconilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 54, 3)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 277, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute uuidref uses Python identifier uuidref
    __uuidref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uuidref'), 'uuidref', '__httpwww_isotc211_org2005gmd_CI_ResponsibleParty_PropertyType_uuidref', pyxb.binding.datatypes.string)
    __uuidref._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    __uuidref._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    
    uuidref = property(__uuidref.value, __uuidref.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_isotc211_org2005gmd_CI_ResponsibleParty_PropertyType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_isotc211_org2005gmd_CI_ResponsibleParty_PropertyType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_isotc211_org2005gmd_CI_ResponsibleParty_PropertyType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_isotc211_org2005gmd_CI_ResponsibleParty_PropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_isotc211_org2005gmd_CI_ResponsibleParty_PropertyType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_isotc211_org2005gmd_CI_ResponsibleParty_PropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_isotc211_org2005gmd_CI_ResponsibleParty_PropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __CI_ResponsibleParty.name() : __CI_ResponsibleParty
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __uuidref.name() : __uuidref,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.CI_ResponsibleParty_PropertyType = CI_ResponsibleParty_PropertyType
_Namespace_gmd.addCategoryObject('typeBinding', 'CI_ResponsibleParty_PropertyType', CI_ResponsibleParty_PropertyType)


# Complex type {http://www.isotc211.org/2005/gmd}CI_Contact_PropertyType with content type ELEMENT_ONLY
class CI_Contact_PropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.isotc211.org/2005/gmd}CI_Contact_PropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Contact_PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 299, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.isotc211.org/2005/gmd}CI_Contact uses Python identifier CI_Contact
    __CI_Contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Contact'), 'CI_Contact', '__httpwww_isotc211_org2005gmd_CI_Contact_PropertyType_httpwww_isotc211_org2005gmdCI_Contact', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 307, 3), )

    
    CI_Contact = property(__CI_Contact.value, __CI_Contact.set, None, None)

    
    # Attribute {http://www.isotc211.org/2005/gco}nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gco, 'nilReason'), 'nilReason', '__httpwww_isotc211_org2005gmd_CI_Contact_PropertyType_httpwww_isotc211_org2005gconilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 54, 3)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 304, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute uuidref uses Python identifier uuidref
    __uuidref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uuidref'), 'uuidref', '__httpwww_isotc211_org2005gmd_CI_Contact_PropertyType_uuidref', pyxb.binding.datatypes.string)
    __uuidref._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    __uuidref._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    
    uuidref = property(__uuidref.value, __uuidref.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_isotc211_org2005gmd_CI_Contact_PropertyType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_isotc211_org2005gmd_CI_Contact_PropertyType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_isotc211_org2005gmd_CI_Contact_PropertyType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_isotc211_org2005gmd_CI_Contact_PropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_isotc211_org2005gmd_CI_Contact_PropertyType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_isotc211_org2005gmd_CI_Contact_PropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_isotc211_org2005gmd_CI_Contact_PropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __CI_Contact.name() : __CI_Contact
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __uuidref.name() : __uuidref,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.CI_Contact_PropertyType = CI_Contact_PropertyType
_Namespace_gmd.addCategoryObject('typeBinding', 'CI_Contact_PropertyType', CI_Contact_PropertyType)


# Complex type {http://www.isotc211.org/2005/gmd}CI_Telephone_PropertyType with content type ELEMENT_ONLY
class CI_Telephone_PropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.isotc211.org/2005/gmd}CI_Telephone_PropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Telephone_PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 327, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.isotc211.org/2005/gmd}CI_Telephone uses Python identifier CI_Telephone
    __CI_Telephone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Telephone'), 'CI_Telephone', '__httpwww_isotc211_org2005gmd_CI_Telephone_PropertyType_httpwww_isotc211_org2005gmdCI_Telephone', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 335, 3), )

    
    CI_Telephone = property(__CI_Telephone.value, __CI_Telephone.set, None, None)

    
    # Attribute {http://www.isotc211.org/2005/gco}nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gco, 'nilReason'), 'nilReason', '__httpwww_isotc211_org2005gmd_CI_Telephone_PropertyType_httpwww_isotc211_org2005gconilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 54, 3)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 332, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute uuidref uses Python identifier uuidref
    __uuidref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uuidref'), 'uuidref', '__httpwww_isotc211_org2005gmd_CI_Telephone_PropertyType_uuidref', pyxb.binding.datatypes.string)
    __uuidref._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    __uuidref._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    
    uuidref = property(__uuidref.value, __uuidref.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_isotc211_org2005gmd_CI_Telephone_PropertyType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_isotc211_org2005gmd_CI_Telephone_PropertyType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_isotc211_org2005gmd_CI_Telephone_PropertyType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_isotc211_org2005gmd_CI_Telephone_PropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_isotc211_org2005gmd_CI_Telephone_PropertyType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_isotc211_org2005gmd_CI_Telephone_PropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_isotc211_org2005gmd_CI_Telephone_PropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __CI_Telephone.name() : __CI_Telephone
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __uuidref.name() : __uuidref,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.CI_Telephone_PropertyType = CI_Telephone_PropertyType
_Namespace_gmd.addCategoryObject('typeBinding', 'CI_Telephone_PropertyType', CI_Telephone_PropertyType)


# Complex type {http://www.isotc211.org/2005/gmd}CI_Address_PropertyType with content type ELEMENT_ONLY
class CI_Address_PropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.isotc211.org/2005/gmd}CI_Address_PropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Address_PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 353, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.isotc211.org/2005/gmd}CI_Address uses Python identifier CI_Address
    __CI_Address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Address'), 'CI_Address', '__httpwww_isotc211_org2005gmd_CI_Address_PropertyType_httpwww_isotc211_org2005gmdCI_Address', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 361, 3), )

    
    CI_Address = property(__CI_Address.value, __CI_Address.set, None, None)

    
    # Attribute {http://www.isotc211.org/2005/gco}nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gco, 'nilReason'), 'nilReason', '__httpwww_isotc211_org2005gmd_CI_Address_PropertyType_httpwww_isotc211_org2005gconilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 54, 3)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 358, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute uuidref uses Python identifier uuidref
    __uuidref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uuidref'), 'uuidref', '__httpwww_isotc211_org2005gmd_CI_Address_PropertyType_uuidref', pyxb.binding.datatypes.string)
    __uuidref._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    __uuidref._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    
    uuidref = property(__uuidref.value, __uuidref.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_isotc211_org2005gmd_CI_Address_PropertyType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_isotc211_org2005gmd_CI_Address_PropertyType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_isotc211_org2005gmd_CI_Address_PropertyType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_isotc211_org2005gmd_CI_Address_PropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_isotc211_org2005gmd_CI_Address_PropertyType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_isotc211_org2005gmd_CI_Address_PropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_isotc211_org2005gmd_CI_Address_PropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __CI_Address.name() : __CI_Address
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __uuidref.name() : __uuidref,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.CI_Address_PropertyType = CI_Address_PropertyType
_Namespace_gmd.addCategoryObject('typeBinding', 'CI_Address_PropertyType', CI_Address_PropertyType)


# Complex type {http://www.isotc211.org/2005/gmd}CI_OnlineResource_PropertyType with content type ELEMENT_ONLY
class CI_OnlineResource_PropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.isotc211.org/2005/gmd}CI_OnlineResource_PropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_OnlineResource_PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 384, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.isotc211.org/2005/gmd}CI_OnlineResource uses Python identifier CI_OnlineResource
    __CI_OnlineResource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_OnlineResource'), 'CI_OnlineResource', '__httpwww_isotc211_org2005gmd_CI_OnlineResource_PropertyType_httpwww_isotc211_org2005gmdCI_OnlineResource', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 392, 3), )

    
    CI_OnlineResource = property(__CI_OnlineResource.value, __CI_OnlineResource.set, None, None)

    
    # Attribute {http://www.isotc211.org/2005/gco}nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gco, 'nilReason'), 'nilReason', '__httpwww_isotc211_org2005gmd_CI_OnlineResource_PropertyType_httpwww_isotc211_org2005gconilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 54, 3)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 389, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute uuidref uses Python identifier uuidref
    __uuidref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uuidref'), 'uuidref', '__httpwww_isotc211_org2005gmd_CI_OnlineResource_PropertyType_uuidref', pyxb.binding.datatypes.string)
    __uuidref._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    __uuidref._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    
    uuidref = property(__uuidref.value, __uuidref.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_isotc211_org2005gmd_CI_OnlineResource_PropertyType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_isotc211_org2005gmd_CI_OnlineResource_PropertyType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_isotc211_org2005gmd_CI_OnlineResource_PropertyType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_isotc211_org2005gmd_CI_OnlineResource_PropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_isotc211_org2005gmd_CI_OnlineResource_PropertyType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_isotc211_org2005gmd_CI_OnlineResource_PropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_isotc211_org2005gmd_CI_OnlineResource_PropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __CI_OnlineResource.name() : __CI_OnlineResource
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __uuidref.name() : __uuidref,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.CI_OnlineResource_PropertyType = CI_OnlineResource_PropertyType
_Namespace_gmd.addCategoryObject('typeBinding', 'CI_OnlineResource_PropertyType', CI_OnlineResource_PropertyType)


# Complex type {http://www.isotc211.org/2005/gmd}URL_PropertyType with content type ELEMENT_ONLY
class URL_PropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.isotc211.org/2005/gmd}URL_PropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'URL_PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 412, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.isotc211.org/2005/gmd}URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'URL'), 'URL', '__httpwww_isotc211_org2005gmd_URL_PropertyType_httpwww_isotc211_org2005gmdURL', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 419, 3), )

    
    URL = property(__URL.value, __URL.set, None, None)

    
    # Attribute {http://www.isotc211.org/2005/gco}nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gco, 'nilReason'), 'nilReason', '__httpwww_isotc211_org2005gmd_URL_PropertyType_httpwww_isotc211_org2005gconilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 54, 3)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 416, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    _ElementMap.update({
        __URL.name() : __URL
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason
    })
_module_typeBindings.URL_PropertyType = URL_PropertyType
_Namespace_gmd.addCategoryObject('typeBinding', 'URL_PropertyType', URL_PropertyType)


# Complex type {http://www.isotc211.org/2005/gmd}CI_OnLineFunctionCode_PropertyType with content type ELEMENT_ONLY
class CI_OnLineFunctionCode_PropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.isotc211.org/2005/gmd}CI_OnLineFunctionCode_PropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_OnLineFunctionCode_PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 421, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.isotc211.org/2005/gmd}CI_OnLineFunctionCode uses Python identifier CI_OnLineFunctionCode
    __CI_OnLineFunctionCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_OnLineFunctionCode'), 'CI_OnLineFunctionCode', '__httpwww_isotc211_org2005gmd_CI_OnLineFunctionCode_PropertyType_httpwww_isotc211_org2005gmdCI_OnLineFunctionCode', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 428, 3), )

    
    CI_OnLineFunctionCode = property(__CI_OnLineFunctionCode.value, __CI_OnLineFunctionCode.set, None, None)

    
    # Attribute {http://www.isotc211.org/2005/gco}nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gco, 'nilReason'), 'nilReason', '__httpwww_isotc211_org2005gmd_CI_OnLineFunctionCode_PropertyType_httpwww_isotc211_org2005gconilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 54, 3)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 425, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    _ElementMap.update({
        __CI_OnLineFunctionCode.name() : __CI_OnLineFunctionCode
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason
    })
_module_typeBindings.CI_OnLineFunctionCode_PropertyType = CI_OnLineFunctionCode_PropertyType
_Namespace_gmd.addCategoryObject('typeBinding', 'CI_OnLineFunctionCode_PropertyType', CI_OnLineFunctionCode_PropertyType)


# Complex type {http://www.isotc211.org/2005/gmd}CI_RoleCode_PropertyType with content type ELEMENT_ONLY
class CI_RoleCode_PropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.isotc211.org/2005/gmd}CI_RoleCode_PropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_RoleCode_PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 431, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.isotc211.org/2005/gmd}CI_RoleCode uses Python identifier CI_RoleCode
    __CI_RoleCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_RoleCode'), 'CI_RoleCode', '__httpwww_isotc211_org2005gmd_CI_RoleCode_PropertyType_httpwww_isotc211_org2005gmdCI_RoleCode', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 438, 3), )

    
    CI_RoleCode = property(__CI_RoleCode.value, __CI_RoleCode.set, None, None)

    
    # Attribute {http://www.isotc211.org/2005/gco}nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gco, 'nilReason'), 'nilReason', '__httpwww_isotc211_org2005gmd_CI_RoleCode_PropertyType_httpwww_isotc211_org2005gconilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 54, 3)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 435, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    _ElementMap.update({
        __CI_RoleCode.name() : __CI_RoleCode
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason
    })
_module_typeBindings.CI_RoleCode_PropertyType = CI_RoleCode_PropertyType
_Namespace_gmd.addCategoryObject('typeBinding', 'CI_RoleCode_PropertyType', CI_RoleCode_PropertyType)


# Complex type {http://www.isotc211.org/2005/gmd}CI_PresentationFormCode_PropertyType with content type ELEMENT_ONLY
class CI_PresentationFormCode_PropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.isotc211.org/2005/gmd}CI_PresentationFormCode_PropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_PresentationFormCode_PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 441, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.isotc211.org/2005/gmd}CI_PresentationFormCode uses Python identifier CI_PresentationFormCode
    __CI_PresentationFormCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_PresentationFormCode'), 'CI_PresentationFormCode', '__httpwww_isotc211_org2005gmd_CI_PresentationFormCode_PropertyType_httpwww_isotc211_org2005gmdCI_PresentationFormCode', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 448, 3), )

    
    CI_PresentationFormCode = property(__CI_PresentationFormCode.value, __CI_PresentationFormCode.set, None, None)

    
    # Attribute {http://www.isotc211.org/2005/gco}nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gco, 'nilReason'), 'nilReason', '__httpwww_isotc211_org2005gmd_CI_PresentationFormCode_PropertyType_httpwww_isotc211_org2005gconilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 54, 3)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 445, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    _ElementMap.update({
        __CI_PresentationFormCode.name() : __CI_PresentationFormCode
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason
    })
_module_typeBindings.CI_PresentationFormCode_PropertyType = CI_PresentationFormCode_PropertyType
_Namespace_gmd.addCategoryObject('typeBinding', 'CI_PresentationFormCode_PropertyType', CI_PresentationFormCode_PropertyType)


# Complex type {http://www.isotc211.org/2005/gmd}CI_Series_PropertyType with content type ELEMENT_ONLY
class CI_Series_PropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.isotc211.org/2005/gmd}CI_Series_PropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Series_PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 451, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.isotc211.org/2005/gmd}CI_Series uses Python identifier CI_Series
    __CI_Series = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Series'), 'CI_Series', '__httpwww_isotc211_org2005gmd_CI_Series_PropertyType_httpwww_isotc211_org2005gmdCI_Series', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 459, 3), )

    
    CI_Series = property(__CI_Series.value, __CI_Series.set, None, None)

    
    # Attribute {http://www.isotc211.org/2005/gco}nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gco, 'nilReason'), 'nilReason', '__httpwww_isotc211_org2005gmd_CI_Series_PropertyType_httpwww_isotc211_org2005gconilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 54, 3)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 456, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute uuidref uses Python identifier uuidref
    __uuidref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uuidref'), 'uuidref', '__httpwww_isotc211_org2005gmd_CI_Series_PropertyType_uuidref', pyxb.binding.datatypes.string)
    __uuidref._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    __uuidref._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    
    uuidref = property(__uuidref.value, __uuidref.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_isotc211_org2005gmd_CI_Series_PropertyType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_isotc211_org2005gmd_CI_Series_PropertyType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_isotc211_org2005gmd_CI_Series_PropertyType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_isotc211_org2005gmd_CI_Series_PropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_isotc211_org2005gmd_CI_Series_PropertyType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_isotc211_org2005gmd_CI_Series_PropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_isotc211_org2005gmd_CI_Series_PropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __CI_Series.name() : __CI_Series
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __uuidref.name() : __uuidref,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.CI_Series_PropertyType = CI_Series_PropertyType
_Namespace_gmd.addCategoryObject('typeBinding', 'CI_Series_PropertyType', CI_Series_PropertyType)


# Complex type {http://www.isotc211.org/2005/gmd}DQ_EvaluationMethodTypeCode_PropertyType with content type ELEMENT_ONLY
class DQ_EvaluationMethodTypeCode_PropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.isotc211.org/2005/gmd}DQ_EvaluationMethodTypeCode_PropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'DQ_EvaluationMethodTypeCode_PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 474, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.isotc211.org/2005/gmd}DQ_EvaluationMethodTypeCode uses Python identifier DQ_EvaluationMethodTypeCode
    __DQ_EvaluationMethodTypeCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'DQ_EvaluationMethodTypeCode'), 'DQ_EvaluationMethodTypeCode', '__httpwww_isotc211_org2005gmd_DQ_EvaluationMethodTypeCode_PropertyType_httpwww_isotc211_org2005gmdDQ_EvaluationMethodTypeCode', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 481, 3), )

    
    DQ_EvaluationMethodTypeCode = property(__DQ_EvaluationMethodTypeCode.value, __DQ_EvaluationMethodTypeCode.set, None, None)

    
    # Attribute {http://www.isotc211.org/2005/gco}nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gco, 'nilReason'), 'nilReason', '__httpwww_isotc211_org2005gmd_DQ_EvaluationMethodTypeCode_PropertyType_httpwww_isotc211_org2005gconilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 54, 3)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 478, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    _ElementMap.update({
        __DQ_EvaluationMethodTypeCode.name() : __DQ_EvaluationMethodTypeCode
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason
    })
_module_typeBindings.DQ_EvaluationMethodTypeCode_PropertyType = DQ_EvaluationMethodTypeCode_PropertyType
_Namespace_gmd.addCategoryObject('typeBinding', 'DQ_EvaluationMethodTypeCode_PropertyType', DQ_EvaluationMethodTypeCode_PropertyType)


# Complex type {http://www.isotc211.org/2005/gmd}DQ_Result_PropertyType with content type ELEMENT_ONLY
class DQ_Result_PropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.isotc211.org/2005/gmd}DQ_Result_PropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gmd, 'DQ_Result_PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 484, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.isotc211.org/2005/gmd}AbstractDQ_Result uses Python identifier AbstractDQ_Result
    __AbstractDQ_Result = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'AbstractDQ_Result'), 'AbstractDQ_Result', '__httpwww_isotc211_org2005gmd_DQ_Result_PropertyType_httpwww_isotc211_org2005gmdAbstractDQ_Result', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 492, 3), )

    
    AbstractDQ_Result = property(__AbstractDQ_Result.value, __AbstractDQ_Result.set, None, None)

    
    # Attribute {http://www.isotc211.org/2005/gco}nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gco, 'nilReason'), 'nilReason', '__httpwww_isotc211_org2005gmd_DQ_Result_PropertyType_httpwww_isotc211_org2005gconilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 54, 3)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 489, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute uuidref uses Python identifier uuidref
    __uuidref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uuidref'), 'uuidref', '__httpwww_isotc211_org2005gmd_DQ_Result_PropertyType_uuidref', pyxb.binding.datatypes.string)
    __uuidref._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    __uuidref._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    
    uuidref = property(__uuidref.value, __uuidref.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_isotc211_org2005gmd_DQ_Result_PropertyType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_isotc211_org2005gmd_DQ_Result_PropertyType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_isotc211_org2005gmd_DQ_Result_PropertyType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_isotc211_org2005gmd_DQ_Result_PropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_isotc211_org2005gmd_DQ_Result_PropertyType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_isotc211_org2005gmd_DQ_Result_PropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_isotc211_org2005gmd_DQ_Result_PropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __AbstractDQ_Result.name() : __AbstractDQ_Result
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __uuidref.name() : __uuidref,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.DQ_Result_PropertyType = DQ_Result_PropertyType
_Namespace_gmd.addCategoryObject('typeBinding', 'DQ_Result_PropertyType', DQ_Result_PropertyType)


# Complex type {http://www.isotc211.org/2005/gsr}SC_CRS_PropertyType with content type ELEMENT_ONLY
class SC_CRS_PropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.isotc211.org/2005/gsr}SC_CRS_PropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gsr, 'SC_CRS_PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gsr/gsr.xsd', 39, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml/3.2}AbstractCRS uses Python identifier AbstractCRS
    __AbstractCRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractCRS'), 'AbstractCRS', '__httpwww_isotc211_org2005gsr_SC_CRS_PropertyType_httpwww_opengis_netgml3_2AbstractCRS', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 351, 3), )

    
    AbstractCRS = property(__AbstractCRS.value, __AbstractCRS.set, None, 'gml:AbstractCRS specifies a coordinate reference system which is usually single but may be compound. This abstract complex type shall not be used, extended, or restricted, in a GML Application Schema, to define a concrete subtype with a meaning equivalent to a concrete subtype specified in this document.')

    
    # Attribute {http://www.isotc211.org/2005/gco}nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gco, 'nilReason'), 'nilReason', '__httpwww_isotc211_org2005gsr_SC_CRS_PropertyType_httpwww_isotc211_org2005gconilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 54, 3)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gsr/gsr.xsd', 44, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute uuidref uses Python identifier uuidref
    __uuidref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uuidref'), 'uuidref', '__httpwww_isotc211_org2005gsr_SC_CRS_PropertyType_uuidref', pyxb.binding.datatypes.string)
    __uuidref._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    __uuidref._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    
    uuidref = property(__uuidref.value, __uuidref.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_isotc211_org2005gsr_SC_CRS_PropertyType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_isotc211_org2005gsr_SC_CRS_PropertyType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_isotc211_org2005gsr_SC_CRS_PropertyType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_isotc211_org2005gsr_SC_CRS_PropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_isotc211_org2005gsr_SC_CRS_PropertyType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_isotc211_org2005gsr_SC_CRS_PropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_isotc211_org2005gsr_SC_CRS_PropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __AbstractCRS.name() : __AbstractCRS
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __uuidref.name() : __uuidref,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.SC_CRS_PropertyType = SC_CRS_PropertyType
_Namespace_gsr.addCategoryObject('typeBinding', 'SC_CRS_PropertyType', SC_CRS_PropertyType)


# Complex type {http://www.isotc211.org/2005/gts}TM_Primitive_PropertyType with content type ELEMENT_ONLY
class TM_Primitive_PropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.isotc211.org/2005/gts}TM_Primitive_PropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gts, 'TM_Primitive_PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gts/gts.xsd', 37, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml/3.2}AbstractTimePrimitive uses Python identifier AbstractTimePrimitive
    __AbstractTimePrimitive = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractTimePrimitive'), 'AbstractTimePrimitive', '__httpwww_isotc211_org2005gts_TM_Primitive_PropertyType_httpwww_opengis_netgml3_2AbstractTimePrimitive', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 270, 3), )

    
    AbstractTimePrimitive = property(__AbstractTimePrimitive.value, __AbstractTimePrimitive.set, None, 'gml:AbstractTimePrimitive acts as the head of a substitution group for geometric and topological temporal primitives.')

    
    # Attribute {http://www.isotc211.org/2005/gco}nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gco, 'nilReason'), 'nilReason', '__httpwww_isotc211_org2005gts_TM_Primitive_PropertyType_httpwww_isotc211_org2005gconilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 54, 3)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gts/gts.xsd', 42, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute uuidref uses Python identifier uuidref
    __uuidref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uuidref'), 'uuidref', '__httpwww_isotc211_org2005gts_TM_Primitive_PropertyType_uuidref', pyxb.binding.datatypes.string)
    __uuidref._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    __uuidref._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 69, 6)
    
    uuidref = property(__uuidref.value, __uuidref.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_isotc211_org2005gts_TM_Primitive_PropertyType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_isotc211_org2005gts_TM_Primitive_PropertyType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_isotc211_org2005gts_TM_Primitive_PropertyType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_isotc211_org2005gts_TM_Primitive_PropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_isotc211_org2005gts_TM_Primitive_PropertyType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_isotc211_org2005gts_TM_Primitive_PropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_isotc211_org2005gts_TM_Primitive_PropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __AbstractTimePrimitive.name() : __AbstractTimePrimitive
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __uuidref.name() : __uuidref,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.TM_Primitive_PropertyType = TM_Primitive_PropertyType
_Namespace_gts.addCategoryObject('typeBinding', 'TM_Primitive_PropertyType', TM_Primitive_PropertyType)


# Complex type {http://www.opengis.net/gml/3.2}DefinitionType with content type ELEMENT_ONLY
class DefinitionType (DefinitionBaseType):
    """Complex type {http://www.opengis.net/gml/3.2}DefinitionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'DefinitionType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 71, 3)
    _ElementMap = DefinitionBaseType._ElementMap.copy()
    _AttributeMap = DefinitionBaseType._AttributeMap.copy()
    # Base type is DefinitionBaseType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element {http://www.opengis.net/gml/3.2}remarks uses Python identifier remarks
    __remarks = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'remarks'), 'remarks', '__httpwww_opengis_netgml3_2_DefinitionType_httpwww_opengis_netgml3_2remarks', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 250, 3), )

    
    remarks = property(__remarks.value, __remarks.set, None, None)

    
    # Attribute id_ inherited from {http://www.opengis.net/gml/3.2}DefinitionBaseType
    _ElementMap.update({
        __remarks.name() : __remarks
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DefinitionType = DefinitionType
_Namespace_gml.addCategoryObject('typeBinding', 'DefinitionType', DefinitionType)


# Complex type {http://www.opengis.net/gml/3.2}StringOrRefType with content type SIMPLE
class StringOrRefType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'StringOrRefType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 179, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netgml3_2_StringOrRefType_nilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_opengis_netgml3_2_StringOrRefType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netgml3_2_StringOrRefType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netgml3_2_StringOrRefType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netgml3_2_StringOrRefType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netgml3_2_StringOrRefType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netgml3_2_StringOrRefType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netgml3_2_StringOrRefType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.StringOrRefType = StringOrRefType
_Namespace_gml.addCategoryObject('typeBinding', 'StringOrRefType', StringOrRefType)


# Complex type {http://www.opengis.net/gml/3.2}ReferenceType with content type EMPTY
class ReferenceType (pyxb.binding.basis.complexTypeDefinition):
    """gml:ReferenceType is intended to be used in application schemas directly, if a property element shall use a "by-reference only" encoding."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'ReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 198, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netgml3_2_ReferenceType_nilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute owns uses Python identifier owns
    __owns = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'owns'), 'owns', '__httpwww_opengis_netgml3_2_ReferenceType_owns', pyxb.binding.datatypes.boolean, unicode_default='false')
    __owns._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 212, 6)
    __owns._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 212, 6)
    
    owns = property(__owns.value, __owns.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_opengis_netgml3_2_ReferenceType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netgml3_2_ReferenceType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netgml3_2_ReferenceType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netgml3_2_ReferenceType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netgml3_2_ReferenceType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netgml3_2_ReferenceType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netgml3_2_ReferenceType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __owns.name() : __owns,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.ReferenceType = ReferenceType
_Namespace_gml.addCategoryObject('typeBinding', 'ReferenceType', ReferenceType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """The gml:domainOfValidity property implements an association role to an EX_Extent object as encoded in ISO/TS 19139, either referencing or containing the definition of that extent."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 256, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.isotc211.org/2005/gmd}EX_Extent uses Python identifier EX_Extent
    __EX_Extent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'EX_Extent'), 'EX_Extent', '__httpwww_opengis_netgml3_2_CTD_ANON_2_httpwww_isotc211_org2005gmdEX_Extent', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 33, 3), )

    
    EX_Extent = property(__EX_Extent.value, __EX_Extent.set, None, None)

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netgml3_2_CTD_ANON_2_nilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_opengis_netgml3_2_CTD_ANON_2_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netgml3_2_CTD_ANON_2_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netgml3_2_CTD_ANON_2_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netgml3_2_CTD_ANON_2_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netgml3_2_CTD_ANON_2_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netgml3_2_CTD_ANON_2_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netgml3_2_CTD_ANON_2_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __EX_Extent.name() : __EX_Extent
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type {http://www.opengis.net/gml/3.2}AbstractTimePrimitiveType with content type ELEMENT_ONLY
class AbstractTimePrimitiveType (AbstractTimeObjectType):
    """Complex type {http://www.opengis.net/gml/3.2}AbstractTimePrimitiveType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractTimePrimitiveType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 278, 3)
    _ElementMap = AbstractTimeObjectType._ElementMap.copy()
    _AttributeMap = AbstractTimeObjectType._AttributeMap.copy()
    # Base type is AbstractTimeObjectType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element {http://www.opengis.net/gml/3.2}relatedTime uses Python identifier relatedTime
    __relatedTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'relatedTime'), 'relatedTime', '__httpwww_opengis_netgml3_2_AbstractTimePrimitiveType_httpwww_opengis_netgml3_2relatedTime', True, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 282, 15), )

    
    relatedTime = property(__relatedTime.value, __relatedTime.set, None, None)

    
    # Attribute id inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    _ElementMap.update({
        __relatedTime.name() : __relatedTime
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AbstractTimePrimitiveType = AbstractTimePrimitiveType
_Namespace_gml.addCategoryObject('typeBinding', 'AbstractTimePrimitiveType', AbstractTimePrimitiveType)


# Complex type {http://www.opengis.net/gml/3.2}TimePrimitivePropertyType with content type ELEMENT_ONLY
class TimePrimitivePropertyType (pyxb.binding.basis.complexTypeDefinition):
    """gml:TimePrimitivePropertyType provides a standard content model for associations between an arbitrary member of the substitution group whose head is gml:AbstractTimePrimitive and another object."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'TimePrimitivePropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 324, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml/3.2}AbstractTimePrimitive uses Python identifier AbstractTimePrimitive
    __AbstractTimePrimitive = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractTimePrimitive'), 'AbstractTimePrimitive', '__httpwww_opengis_netgml3_2_TimePrimitivePropertyType_httpwww_opengis_netgml3_2AbstractTimePrimitive', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 270, 3), )

    
    AbstractTimePrimitive = property(__AbstractTimePrimitive.value, __AbstractTimePrimitive.set, None, 'gml:AbstractTimePrimitive acts as the head of a substitution group for geometric and topological temporal primitives.')

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netgml3_2_TimePrimitivePropertyType_nilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute owns uses Python identifier owns
    __owns = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'owns'), 'owns', '__httpwww_opengis_netgml3_2_TimePrimitivePropertyType_owns', pyxb.binding.datatypes.boolean, unicode_default='false')
    __owns._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 212, 6)
    __owns._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 212, 6)
    
    owns = property(__owns.value, __owns.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_opengis_netgml3_2_TimePrimitivePropertyType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netgml3_2_TimePrimitivePropertyType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netgml3_2_TimePrimitivePropertyType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netgml3_2_TimePrimitivePropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netgml3_2_TimePrimitivePropertyType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netgml3_2_TimePrimitivePropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netgml3_2_TimePrimitivePropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __AbstractTimePrimitive.name() : __AbstractTimePrimitive
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __owns.name() : __owns,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.TimePrimitivePropertyType = TimePrimitivePropertyType
_Namespace_gml.addCategoryObject('typeBinding', 'TimePrimitivePropertyType', TimePrimitivePropertyType)


# Complex type {http://www.opengis.net/gml/3.2}EllipsoidalCSPropertyType with content type ELEMENT_ONLY
class EllipsoidalCSPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """gml:EllipsoidalCSPropertyType is a property type for association roles to an ellipsoidal coordinate system, either referencing or containing the definition of that coordinate system."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'EllipsoidalCSPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 381, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml/3.2}EllipsoidalCS uses Python identifier EllipsoidalCS
    __EllipsoidalCS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'EllipsoidalCS'), 'EllipsoidalCS', '__httpwww_opengis_netgml3_2_EllipsoidalCSPropertyType_httpwww_opengis_netgml3_2EllipsoidalCS', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 391, 3), )

    
    EllipsoidalCS = property(__EllipsoidalCS.value, __EllipsoidalCS.set, None, 'gml:EllipsoidalCS is a two- or three-dimensional coordinate system in which position is specified by geodetic latitude, geodetic longitude, and (in the three-dimensional case) ellipsoidal height. An EllipsoidalCS shall have two or three gml:axis property elements; the number of associations shall equal the dimension of the CS.')

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netgml3_2_EllipsoidalCSPropertyType_nilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_opengis_netgml3_2_EllipsoidalCSPropertyType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netgml3_2_EllipsoidalCSPropertyType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netgml3_2_EllipsoidalCSPropertyType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netgml3_2_EllipsoidalCSPropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netgml3_2_EllipsoidalCSPropertyType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netgml3_2_EllipsoidalCSPropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netgml3_2_EllipsoidalCSPropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __EllipsoidalCS.name() : __EllipsoidalCS
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.EllipsoidalCSPropertyType = EllipsoidalCSPropertyType
_Namespace_gml.addCategoryObject('typeBinding', 'EllipsoidalCSPropertyType', EllipsoidalCSPropertyType)


# Complex type {http://www.opengis.net/gml/3.2}CoordinateSystemAxisPropertyType with content type ELEMENT_ONLY
class CoordinateSystemAxisPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """gml:CoordinateSystemAxisPropertyType is a property type for association roles to a coordinate system axis, either referencing or containing the definition of that axis."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'CoordinateSystemAxisPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 421, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml/3.2}CoordinateSystemAxis uses Python identifier CoordinateSystemAxis
    __CoordinateSystemAxis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'CoordinateSystemAxis'), 'CoordinateSystemAxis', '__httpwww_opengis_netgml3_2_CoordinateSystemAxisPropertyType_httpwww_opengis_netgml3_2CoordinateSystemAxis', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 431, 3), )

    
    CoordinateSystemAxis = property(__CoordinateSystemAxis.value, __CoordinateSystemAxis.set, None, 'gml:CoordinateSystemAxis is a definition of a coordinate system axis.')

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netgml3_2_CoordinateSystemAxisPropertyType_nilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_opengis_netgml3_2_CoordinateSystemAxisPropertyType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netgml3_2_CoordinateSystemAxisPropertyType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netgml3_2_CoordinateSystemAxisPropertyType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netgml3_2_CoordinateSystemAxisPropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netgml3_2_CoordinateSystemAxisPropertyType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netgml3_2_CoordinateSystemAxisPropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netgml3_2_CoordinateSystemAxisPropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __CoordinateSystemAxis.name() : __CoordinateSystemAxis
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.CoordinateSystemAxisPropertyType = CoordinateSystemAxisPropertyType
_Namespace_gml.addCategoryObject('typeBinding', 'CoordinateSystemAxisPropertyType', CoordinateSystemAxisPropertyType)


# Complex type {http://www.opengis.net/gml/3.2}CartesianCSPropertyType with content type ELEMENT_ONLY
class CartesianCSPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """gml:CartesianCSPropertyType is a property type for association roles to a Cartesian coordinate system, either referencing or containing the definition of that coordinate system."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'CartesianCSPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 549, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml/3.2}CartesianCS uses Python identifier CartesianCS
    __CartesianCS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'CartesianCS'), 'CartesianCS', '__httpwww_opengis_netgml3_2_CartesianCSPropertyType_httpwww_opengis_netgml3_2CartesianCS', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 559, 3), )

    
    CartesianCS = property(__CartesianCS.value, __CartesianCS.set, None, 'gml:CartesianCS is a 1-, 2-, or 3-dimensional coordinate system. In the 1-dimensional case, it contains a single straight coordinate axis. In the 2- and 3-dimensional cases gives the position of points relative to orthogonal straight axes. In the multi-dimensional case, all axes shall have the same length unit of measure. A CartesianCS shall have one, two, or three gml:axis property elements.')

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netgml3_2_CartesianCSPropertyType_nilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_opengis_netgml3_2_CartesianCSPropertyType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netgml3_2_CartesianCSPropertyType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netgml3_2_CartesianCSPropertyType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netgml3_2_CartesianCSPropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netgml3_2_CartesianCSPropertyType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netgml3_2_CartesianCSPropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netgml3_2_CartesianCSPropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __CartesianCS.name() : __CartesianCS
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.CartesianCSPropertyType = CartesianCSPropertyType
_Namespace_gml.addCategoryObject('typeBinding', 'CartesianCSPropertyType', CartesianCSPropertyType)


# Complex type {http://www.opengis.net/gml/3.2}SphericalCSPropertyType with content type ELEMENT_ONLY
class SphericalCSPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """gml:SphericalCSPropertyType is property type for association roles to a spherical coordinate system, either referencing or containing the definition of that coordinate system."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'SphericalCSPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 578, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml/3.2}SphericalCS uses Python identifier SphericalCS
    __SphericalCS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'SphericalCS'), 'SphericalCS', '__httpwww_opengis_netgml3_2_SphericalCSPropertyType_httpwww_opengis_netgml3_2SphericalCS', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 588, 3), )

    
    SphericalCS = property(__SphericalCS.value, __SphericalCS.set, None, 'gml:SphericalCS is a three-dimensional coordinate system with one distance measured from the origin and two angular coordinates. A SphericalCS shall have three gml:axis property elements.')

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netgml3_2_SphericalCSPropertyType_nilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_opengis_netgml3_2_SphericalCSPropertyType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netgml3_2_SphericalCSPropertyType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netgml3_2_SphericalCSPropertyType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netgml3_2_SphericalCSPropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netgml3_2_SphericalCSPropertyType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netgml3_2_SphericalCSPropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netgml3_2_SphericalCSPropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __SphericalCS.name() : __SphericalCS
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.SphericalCSPropertyType = SphericalCSPropertyType
_Namespace_gml.addCategoryObject('typeBinding', 'SphericalCSPropertyType', SphericalCSPropertyType)


# Complex type {http://www.opengis.net/gml/3.2}GeodeticDatumPropertyType with content type ELEMENT_ONLY
class GeodeticDatumPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """gml:GeodeticDatumPropertyType is a property type for association roles to a geodetic datum, either referencing or containing the definition of that datum."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'GeodeticDatumPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 608, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml/3.2}GeodeticDatum uses Python identifier GeodeticDatum
    __GeodeticDatum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'GeodeticDatum'), 'GeodeticDatum', '__httpwww_opengis_netgml3_2_GeodeticDatumPropertyType_httpwww_opengis_netgml3_2GeodeticDatum', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 618, 3), )

    
    GeodeticDatum = property(__GeodeticDatum.value, __GeodeticDatum.set, None, 'gml:GeodeticDatum is a geodetic datum defines the precise location and orientation in 3-dimensional space of a defined ellipsoid (or sphere), or of a Cartesian coordinate system centered in this ellipsoid (or sphere).')

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netgml3_2_GeodeticDatumPropertyType_nilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_opengis_netgml3_2_GeodeticDatumPropertyType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netgml3_2_GeodeticDatumPropertyType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netgml3_2_GeodeticDatumPropertyType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netgml3_2_GeodeticDatumPropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netgml3_2_GeodeticDatumPropertyType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netgml3_2_GeodeticDatumPropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netgml3_2_GeodeticDatumPropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __GeodeticDatum.name() : __GeodeticDatum
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.GeodeticDatumPropertyType = GeodeticDatumPropertyType
_Namespace_gml.addCategoryObject('typeBinding', 'GeodeticDatumPropertyType', GeodeticDatumPropertyType)


# Complex type {http://www.opengis.net/gml/3.2}PrimeMeridianPropertyType with content type ELEMENT_ONLY
class PrimeMeridianPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """gml:PrimeMeridianPropertyType is a property type for association roles to a prime meridian, either referencing or containing the definition of that meridian."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'PrimeMeridianPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 671, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml/3.2}PrimeMeridian uses Python identifier PrimeMeridian
    __PrimeMeridian = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'PrimeMeridian'), 'PrimeMeridian', '__httpwww_opengis_netgml3_2_PrimeMeridianPropertyType_httpwww_opengis_netgml3_2PrimeMeridian', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 681, 3), )

    
    PrimeMeridian = property(__PrimeMeridian.value, __PrimeMeridian.set, None, 'A gml:PrimeMeridian defines the origin from which longitude values are determined. The default value for the prime meridian gml:identifier value is "Greenwich".')

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netgml3_2_PrimeMeridianPropertyType_nilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_opengis_netgml3_2_PrimeMeridianPropertyType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netgml3_2_PrimeMeridianPropertyType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netgml3_2_PrimeMeridianPropertyType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netgml3_2_PrimeMeridianPropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netgml3_2_PrimeMeridianPropertyType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netgml3_2_PrimeMeridianPropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netgml3_2_PrimeMeridianPropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __PrimeMeridian.name() : __PrimeMeridian
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.PrimeMeridianPropertyType = PrimeMeridianPropertyType
_Namespace_gml.addCategoryObject('typeBinding', 'PrimeMeridianPropertyType', PrimeMeridianPropertyType)


# Complex type {http://www.opengis.net/gml/3.2}EllipsoidPropertyType with content type ELEMENT_ONLY
class EllipsoidPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """gml:EllipsoidPropertyType is a property type for association roles to an ellipsoid, either referencing or containing the definition of that ellipsoid."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'EllipsoidPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 727, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml/3.2}Ellipsoid uses Python identifier Ellipsoid
    __Ellipsoid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'Ellipsoid'), 'Ellipsoid', '__httpwww_opengis_netgml3_2_EllipsoidPropertyType_httpwww_opengis_netgml3_2Ellipsoid', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 737, 3), )

    
    Ellipsoid = property(__Ellipsoid.value, __Ellipsoid.set, None, 'A gml:Ellipsoid is a geometric figure that may be used to describe the approximate shape of the earth. In mathematical terms, it is a surface formed by the rotation of an ellipse about its minor axis.')

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netgml3_2_EllipsoidPropertyType_nilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_opengis_netgml3_2_EllipsoidPropertyType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netgml3_2_EllipsoidPropertyType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netgml3_2_EllipsoidPropertyType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netgml3_2_EllipsoidPropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netgml3_2_EllipsoidPropertyType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netgml3_2_EllipsoidPropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netgml3_2_EllipsoidPropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __Ellipsoid.name() : __Ellipsoid
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.EllipsoidPropertyType = EllipsoidPropertyType
_Namespace_gml.addCategoryObject('typeBinding', 'EllipsoidPropertyType', EllipsoidPropertyType)


# Complex type {http://www.opengis.net/gml/3.2}GeneralConversionPropertyType with content type ELEMENT_ONLY
class GeneralConversionPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """gml:GeneralConversionPropertyType is a property type for association roles to a general conversion, either referencing or containing the definition of that conversion."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'GeneralConversionPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 843, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml/3.2}AbstractGeneralConversion uses Python identifier AbstractGeneralConversion
    __AbstractGeneralConversion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractGeneralConversion'), 'AbstractGeneralConversion', '__httpwww_opengis_netgml3_2_GeneralConversionPropertyType_httpwww_opengis_netgml3_2AbstractGeneralConversion', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 853, 3), )

    
    AbstractGeneralConversion = property(__AbstractGeneralConversion.value, __AbstractGeneralConversion.set, None, 'gm:AbstractGeneralConversion is an abstract operation on coordinates that does not include any change of datum. The best-known example of a coordinate conversion is a map projection. The parameters describing coordinate conversions are defined rather than empirically derived. Note that some conversions have no parameters. The operationVersion, sourceCRS, and targetCRS elements are omitted in a coordinate conversion.\nThis abstract complex type is expected to be extended for well-known operation methods with many Conversion instances, in GML Application Schemas that define operation-method-specialized element names and contents. This conversion uses an operation method, usually with associated parameter values. However, operation methods and parameter values are directly associated with concrete subtypes, not with this abstract type. All concrete types derived from this type shall extend this type to include a "usesMethod" element that references the "OperationMethod" element. Similarly, all concrete types derived from this type shall extend this type to include zero or more elements each named "uses...Value" that each use the type of an element substitutable for the "AbstractGeneralParameterValue" element.')

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netgml3_2_GeneralConversionPropertyType_nilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_opengis_netgml3_2_GeneralConversionPropertyType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netgml3_2_GeneralConversionPropertyType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netgml3_2_GeneralConversionPropertyType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netgml3_2_GeneralConversionPropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netgml3_2_GeneralConversionPropertyType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netgml3_2_GeneralConversionPropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netgml3_2_GeneralConversionPropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __AbstractGeneralConversion.name() : __AbstractGeneralConversion
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.GeneralConversionPropertyType = GeneralConversionPropertyType
_Namespace_gml.addCategoryObject('typeBinding', 'GeneralConversionPropertyType', GeneralConversionPropertyType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """gml:coordinateOperationAccuracy is an association role to a DQ_PositionalAccuracy object as encoded in ISO/TS 19139, either referencing or containing the definition of that positional accuracy. That object contains an estimate of the impact of this coordinate operation on point accuracy. That is, it gives position error estimates for the target coordinates of this coordinate operation, assuming no errors in the source coordinates."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 906, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.isotc211.org/2005/gmd}AbstractDQ_PositionalAccuracy uses Python identifier AbstractDQ_PositionalAccuracy
    __AbstractDQ_PositionalAccuracy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'AbstractDQ_PositionalAccuracy'), 'AbstractDQ_PositionalAccuracy', '__httpwww_opengis_netgml3_2_CTD_ANON_3_httpwww_isotc211_org2005gmdAbstractDQ_PositionalAccuracy', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 135, 3), )

    
    AbstractDQ_PositionalAccuracy = property(__AbstractDQ_PositionalAccuracy.value, __AbstractDQ_PositionalAccuracy.set, None, None)

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netgml3_2_CTD_ANON_3_nilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_opengis_netgml3_2_CTD_ANON_3_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netgml3_2_CTD_ANON_3_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netgml3_2_CTD_ANON_3_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netgml3_2_CTD_ANON_3_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netgml3_2_CTD_ANON_3_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netgml3_2_CTD_ANON_3_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netgml3_2_CTD_ANON_3_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __AbstractDQ_PositionalAccuracy.name() : __AbstractDQ_PositionalAccuracy
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type {http://www.opengis.net/gml/3.2}CRSPropertyType with content type ELEMENT_ONLY
class CRSPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """gml:CRSPropertyType is a property type for association roles to a CRS abstract coordinate reference system, either referencing or containing the definition of that CRS."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'CRSPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 930, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml/3.2}AbstractCRS uses Python identifier AbstractCRS
    __AbstractCRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractCRS'), 'AbstractCRS', '__httpwww_opengis_netgml3_2_CRSPropertyType_httpwww_opengis_netgml3_2AbstractCRS', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 351, 3), )

    
    AbstractCRS = property(__AbstractCRS.value, __AbstractCRS.set, None, 'gml:AbstractCRS specifies a coordinate reference system which is usually single but may be compound. This abstract complex type shall not be used, extended, or restricted, in a GML Application Schema, to define a concrete subtype with a meaning equivalent to a concrete subtype specified in this document.')

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netgml3_2_CRSPropertyType_nilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_opengis_netgml3_2_CRSPropertyType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netgml3_2_CRSPropertyType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netgml3_2_CRSPropertyType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netgml3_2_CRSPropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netgml3_2_CRSPropertyType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netgml3_2_CRSPropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netgml3_2_CRSPropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __AbstractCRS.name() : __AbstractCRS
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.CRSPropertyType = CRSPropertyType
_Namespace_gml.addCategoryObject('typeBinding', 'CRSPropertyType', CRSPropertyType)


# Complex type {http://www.opengis.net/gml/3.2}GeodeticCRSPropertyType with content type ELEMENT_ONLY
class GeodeticCRSPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """gml:GeodeticCRSPropertyType is a property type for association roles to a geodetic coordinate reference system, either referencing or containing the definition of that reference system."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'GeodeticCRSPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 977, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml/3.2}GeodeticCRS uses Python identifier GeodeticCRS
    __GeodeticCRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'GeodeticCRS'), 'GeodeticCRS', '__httpwww_opengis_netgml3_2_GeodeticCRSPropertyType_httpwww_opengis_netgml3_2GeodeticCRS', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 27, 3), )

    
    GeodeticCRS = property(__GeodeticCRS.value, __GeodeticCRS.set, None, None)

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netgml3_2_GeodeticCRSPropertyType_nilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_opengis_netgml3_2_GeodeticCRSPropertyType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netgml3_2_GeodeticCRSPropertyType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netgml3_2_GeodeticCRSPropertyType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netgml3_2_GeodeticCRSPropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netgml3_2_GeodeticCRSPropertyType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netgml3_2_GeodeticCRSPropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netgml3_2_GeodeticCRSPropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __GeodeticCRS.name() : __GeodeticCRS
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.GeodeticCRSPropertyType = GeodeticCRSPropertyType
_Namespace_gml.addCategoryObject('typeBinding', 'GeodeticCRSPropertyType', GeodeticCRSPropertyType)


# Complex type {http://www.opengis.net/gml/3.2}VerticalCSPropertyType with content type ELEMENT_ONLY
class VerticalCSPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """gml:VerticalCSPropertyType is a property type for association roles to a vertical coordinate system, either referencing or containing the definition of that coordinate system."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'VerticalCSPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 1019, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml/3.2}VerticalCS uses Python identifier VerticalCS
    __VerticalCS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'VerticalCS'), 'VerticalCS', '__httpwww_opengis_netgml3_2_VerticalCSPropertyType_httpwww_opengis_netgml3_2VerticalCS', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 1029, 3), )

    
    VerticalCS = property(__VerticalCS.value, __VerticalCS.set, None, "gml:VerticalCS is a one-dimensional coordinate system used to record the heights or depths of points. Such a coordinate system is usually dependent on the Earth's gravity field, perhaps loosely as when atmospheric pressure is the basis for the vertical coordinate system axis. A VerticalCS shall have one gml:axis property element.")

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netgml3_2_VerticalCSPropertyType_nilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_opengis_netgml3_2_VerticalCSPropertyType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netgml3_2_VerticalCSPropertyType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netgml3_2_VerticalCSPropertyType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netgml3_2_VerticalCSPropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netgml3_2_VerticalCSPropertyType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netgml3_2_VerticalCSPropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netgml3_2_VerticalCSPropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __VerticalCS.name() : __VerticalCS
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.VerticalCSPropertyType = VerticalCSPropertyType
_Namespace_gml.addCategoryObject('typeBinding', 'VerticalCSPropertyType', VerticalCSPropertyType)


# Complex type {http://www.opengis.net/gml/3.2}VerticalDatumPropertyType with content type ELEMENT_ONLY
class VerticalDatumPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """gml:VerticalDatumPropertyType is property type for association roles to a vertical datum, either referencing or containing the definition of that datum."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'VerticalDatumPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 1048, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml/3.2}VerticalDatum uses Python identifier VerticalDatum
    __VerticalDatum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'VerticalDatum'), 'VerticalDatum', '__httpwww_opengis_netgml3_2_VerticalDatumPropertyType_httpwww_opengis_netgml3_2VerticalDatum', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 1058, 3), )

    
    VerticalDatum = property(__VerticalDatum.value, __VerticalDatum.set, None, 'gml:VerticalDatum is a textual description and/or a set of parameters identifying a particular reference level surface used as a zero-height surface, including its position with respect to the Earth for any of the height types recognized by this International Standard.')

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netgml3_2_VerticalDatumPropertyType_nilReason', _module_typeBindings.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    __nilReason._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 130, 6)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_opengis_netgml3_2_VerticalDatumPropertyType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 24, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netgml3_2_VerticalDatumPropertyType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 33, 3)
    __href._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 25, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netgml3_2_VerticalDatumPropertyType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 35, 3)
    __role._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 26, 6)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netgml3_2_VerticalDatumPropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 37, 3)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 27, 6)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netgml3_2_VerticalDatumPropertyType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 39, 3)
    __title._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 28, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netgml3_2_VerticalDatumPropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_bindings_v20__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 41, 3)
    __show._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 29, 6)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netgml3_2_VerticalDatumPropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_bindings_v20__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 69, 3)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/xlink/1.0.0/xlinks.xsd', 30, 6)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    _ElementMap.update({
        __VerticalDatum.name() : __VerticalDatum
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.VerticalDatumPropertyType = VerticalDatumPropertyType
_Namespace_gml.addCategoryObject('typeBinding', 'VerticalDatumPropertyType', VerticalDatumPropertyType)


# Complex type {http://www.opengis.net/gml/3.2}IdentifiedObjectType with content type ELEMENT_ONLY
class IdentifiedObjectType (DefinitionType):
    """gml:IdentifiedObjectType provides identification properties of a CRS-related object. In gml:DefinitionType, the gml:identifier element shall be the primary name by which this object is identified, encoding the "name" attribute in the UML model.
Zero or more of the gml:name elements can be an unordered set of "identifiers", encoding the "identifier" attribute in the UML model. Each of these gml:name elements can reference elsewhere the object's defining information or be an identifier by which this object can be referenced.
Zero or more other gml:name elements can be an unordered set of "alias" alternative names by which this CRS related object is identified, encoding the "alias" attributes in the UML model. An object may have several aliases, typically used in different contexts. The context for an alias is indicated by the value of its (optional) codeSpace attribute.
Any needed version information shall be included in the codeSpace attribute of a gml:identifier and gml:name elements. In this use, the gml:remarks element in the gml:DefinitionType shall contain comments on or information about this object, including data source information."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'IdentifiedObjectType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 59, 3)
    _ElementMap = DefinitionType._ElementMap.copy()
    _AttributeMap = DefinitionType._AttributeMap.copy()
    # Base type is DefinitionType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element remarks ({http://www.opengis.net/gml/3.2}remarks) inherited from {http://www.opengis.net/gml/3.2}DefinitionType
    
    # Attribute id_ inherited from {http://www.opengis.net/gml/3.2}DefinitionBaseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.IdentifiedObjectType = IdentifiedObjectType
_Namespace_gml.addCategoryObject('typeBinding', 'IdentifiedObjectType', IdentifiedObjectType)


# Complex type {http://www.opengis.net/gml/3.2}RelatedTimeType with content type ELEMENT_ONLY
class RelatedTimeType (TimePrimitivePropertyType):
    """gml:RelatedTimeType provides a content model for indicating the relative position of an arbitrary member of the substitution group whose head is gml:AbstractTimePrimitive. It extends the generic gml:TimePrimitivePropertyType with an XML attribute relativePosition, whose value is selected from the set of 13 temporal relationships identified by Allen (1983)"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'RelatedTimeType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 295, 3)
    _ElementMap = TimePrimitivePropertyType._ElementMap.copy()
    _AttributeMap = TimePrimitivePropertyType._AttributeMap.copy()
    # Base type is TimePrimitivePropertyType
    
    # Element AbstractTimePrimitive ({http://www.opengis.net/gml/3.2}AbstractTimePrimitive) inherited from {http://www.opengis.net/gml/3.2}TimePrimitivePropertyType
    
    # Attribute nilReason inherited from {http://www.opengis.net/gml/3.2}TimePrimitivePropertyType
    
    # Attribute owns inherited from {http://www.opengis.net/gml/3.2}TimePrimitivePropertyType
    
    # Attribute relativePosition uses Python identifier relativePosition
    __relativePosition = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'relativePosition'), 'relativePosition', '__httpwww_opengis_netgml3_2_RelatedTimeType_relativePosition', _module_typeBindings.STD_ANON_3)
    __relativePosition._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 301, 12)
    __relativePosition._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 301, 12)
    
    relativePosition = property(__relativePosition.value, __relativePosition.set, None, None)

    
    # Attribute type inherited from {http://www.opengis.net/gml/3.2}TimePrimitivePropertyType
    
    # Attribute href inherited from {http://www.opengis.net/gml/3.2}TimePrimitivePropertyType
    
    # Attribute role inherited from {http://www.opengis.net/gml/3.2}TimePrimitivePropertyType
    
    # Attribute arcrole inherited from {http://www.opengis.net/gml/3.2}TimePrimitivePropertyType
    
    # Attribute title inherited from {http://www.opengis.net/gml/3.2}TimePrimitivePropertyType
    
    # Attribute show inherited from {http://www.opengis.net/gml/3.2}TimePrimitivePropertyType
    
    # Attribute actuate inherited from {http://www.opengis.net/gml/3.2}TimePrimitivePropertyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __relativePosition.name() : __relativePosition
    })
_module_typeBindings.RelatedTimeType = RelatedTimeType
_Namespace_gml.addCategoryObject('typeBinding', 'RelatedTimeType', RelatedTimeType)


# Complex type {http://www.opengis.net/gml/3.2}AbstractCRSType with content type ELEMENT_ONLY
class AbstractCRSType (IdentifiedObjectType):
    """Complex type {http://www.opengis.net/gml/3.2}AbstractCRSType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractCRSType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 48, 3)
    _ElementMap = IdentifiedObjectType._ElementMap.copy()
    _AttributeMap = IdentifiedObjectType._AttributeMap.copy()
    # Base type is IdentifiedObjectType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element remarks ({http://www.opengis.net/gml/3.2}remarks) inherited from {http://www.opengis.net/gml/3.2}DefinitionType
    
    # Element {http://www.opengis.net/gml/3.2}domainOfValidity uses Python identifier domainOfValidity
    __domainOfValidity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'domainOfValidity'), 'domainOfValidity', '__httpwww_opengis_netgml3_2_AbstractCRSType_httpwww_opengis_netgml3_2domainOfValidity', True, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 252, 3), )

    
    domainOfValidity = property(__domainOfValidity.value, __domainOfValidity.set, None, 'The gml:domainOfValidity property implements an association role to an EX_Extent object as encoded in ISO/TS 19139, either referencing or containing the definition of that extent.')

    
    # Element {http://www.opengis.net/gml/3.2}scope uses Python identifier scope
    __scope = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'scope'), 'scope', '__httpwww_opengis_netgml3_2_AbstractCRSType_httpwww_opengis_netgml3_2scope', True, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 369, 3), )

    
    scope = property(__scope.value, __scope.set, None, 'The gml:scope property provides a description of the usage, or limitations of usage, for which this CRS-related object is valid. If unknown, enter "not known".')

    
    # Attribute id_ inherited from {http://www.opengis.net/gml/3.2}DefinitionBaseType
    _ElementMap.update({
        __domainOfValidity.name() : __domainOfValidity,
        __scope.name() : __scope
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AbstractCRSType = AbstractCRSType
_Namespace_gml.addCategoryObject('typeBinding', 'AbstractCRSType', AbstractCRSType)


# Complex type {http://www.opengis.net/gml/3.2}AbstractCoordinateSystemType with content type ELEMENT_ONLY
class AbstractCoordinateSystemType (IdentifiedObjectType):
    """Complex type {http://www.opengis.net/gml/3.2}AbstractCoordinateSystemType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractCoordinateSystemType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 404, 3)
    _ElementMap = IdentifiedObjectType._ElementMap.copy()
    _AttributeMap = IdentifiedObjectType._AttributeMap.copy()
    # Base type is IdentifiedObjectType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element remarks ({http://www.opengis.net/gml/3.2}remarks) inherited from {http://www.opengis.net/gml/3.2}DefinitionType
    
    # Element {http://www.opengis.net/gml/3.2}axis uses Python identifier axis
    __axis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'axis'), 'axis', '__httpwww_opengis_netgml3_2_AbstractCoordinateSystemType_httpwww_opengis_netgml3_2axis', True, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 415, 3), )

    
    axis = property(__axis.value, __axis.set, None, 'The gml:axis property is an association role (ordered sequence) to the coordinate system axes included in this coordinate system. The coordinate values in a coordinate tuple shall be recorded in the order in which the coordinate system axes associations are recorded, whenever those coordinates use a coordinate reference system that uses this coordinate system. The gml:AggregationAttributeGroup should be used to specify that the axis objects are ordered.')

    
    # Attribute id_ inherited from {http://www.opengis.net/gml/3.2}DefinitionBaseType
    
    # Attribute aggregationType uses Python identifier aggregationType
    __aggregationType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'aggregationType'), 'aggregationType', '__httpwww_opengis_netgml3_2_AbstractCoordinateSystemType_aggregationType', _module_typeBindings.AggregationType)
    __aggregationType._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 521, 6)
    __aggregationType._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 521, 6)
    
    aggregationType = property(__aggregationType.value, __aggregationType.set, None, None)

    _ElementMap.update({
        __axis.name() : __axis
    })
    _AttributeMap.update({
        __aggregationType.name() : __aggregationType
    })
_module_typeBindings.AbstractCoordinateSystemType = AbstractCoordinateSystemType
_Namespace_gml.addCategoryObject('typeBinding', 'AbstractCoordinateSystemType', AbstractCoordinateSystemType)


# Complex type {http://www.opengis.net/gml/3.2}CoordinateSystemAxisType with content type ELEMENT_ONLY
class CoordinateSystemAxisType (IdentifiedObjectType):
    """Complex type {http://www.opengis.net/gml/3.2}CoordinateSystemAxisType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'CoordinateSystemAxisType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 438, 3)
    _ElementMap = IdentifiedObjectType._ElementMap.copy()
    _AttributeMap = IdentifiedObjectType._AttributeMap.copy()
    # Base type is IdentifiedObjectType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element remarks ({http://www.opengis.net/gml/3.2}remarks) inherited from {http://www.opengis.net/gml/3.2}DefinitionType
    
    # Element {http://www.opengis.net/gml/3.2}axisAbbrev uses Python identifier axisAbbrev
    __axisAbbrev = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'axisAbbrev'), 'axisAbbrev', '__httpwww_opengis_netgml3_2_CoordinateSystemAxisType_httpwww_opengis_netgml3_2axisAbbrev', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 453, 3), )

    
    axisAbbrev = property(__axisAbbrev.value, __axisAbbrev.set, None, 'gml:axisAbbrev is the abbreviation used for this coordinate system axis; this abbreviation is also used to identify the coordinates in the coordinate tuple. The codeSpace attribute may reference a source of more information on a set of standardized abbreviations, or on this abbreviation.')

    
    # Element {http://www.opengis.net/gml/3.2}axisDirection uses Python identifier axisDirection
    __axisDirection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'axisDirection'), 'axisDirection', '__httpwww_opengis_netgml3_2_CoordinateSystemAxisType_httpwww_opengis_netgml3_2axisDirection', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 459, 3), )

    
    axisDirection = property(__axisDirection.value, __axisDirection.set, None, 'gml:axisDirection is the direction of this coordinate system axis (or in the case of Cartesian projected coordinates, the direction of this coordinate system axis at the origin).\nWithin any set of coordinate system axes, only one of each pair of terms may be used. For earth-fixed CRSs, this direction is often approximate and intended to provide a human interpretable meaning to the axis. When a geodetic datum is used, the precise directions of the axes may therefore vary slightly from this approximate direction.\nThe codeSpace attribute shall reference a source of information specifying the values and meanings of all the allowed string values for this property.')

    
    # Element {http://www.opengis.net/gml/3.2}minimumValue uses Python identifier minimumValue
    __minimumValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'minimumValue'), 'minimumValue', '__httpwww_opengis_netgml3_2_CoordinateSystemAxisType_httpwww_opengis_netgml3_2minimumValue', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 467, 3), )

    
    minimumValue = property(__minimumValue.value, __minimumValue.set, None, 'The gml:minimumValue and gml:maximumValue properties allow the specification of minimum and maximum value normally allowed for this axis, in the unit of measure for the axis. For a continuous angular axis such as longitude, the values wrap-around at this value. Also, values beyond this minimum/maximum can be used for specified purposes, such as in a bounding box. A value of minus infinity shall be allowed for the gml:minimumValue element, a value of plus infiniy for the gml:maximumValue element. If these elements are omitted, the value is unspecified.')

    
    # Element {http://www.opengis.net/gml/3.2}maximumValue uses Python identifier maximumValue
    __maximumValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'maximumValue'), 'maximumValue', '__httpwww_opengis_netgml3_2_CoordinateSystemAxisType_httpwww_opengis_netgml3_2maximumValue', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 473, 3), )

    
    maximumValue = property(__maximumValue.value, __maximumValue.set, None, 'The gml:minimumValue and gml:maximumValue properties allow the specification of minimum and maximum value normally allowed for this axis, in the unit of measure for the axis. For a continuous angular axis such as longitude, the values wrap-around at this value. Also, values beyond this minimum/maximum can be used for specified purposes, such as in a bounding box. A value of minus infinity shall be allowed for the gml:minimumValue element, a value of plus infiniy for the gml:maximumValue element. If these elements are omitted, the value is unspecified.')

    
    # Element {http://www.opengis.net/gml/3.2}rangeMeaning uses Python identifier rangeMeaning
    __rangeMeaning = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'rangeMeaning'), 'rangeMeaning', '__httpwww_opengis_netgml3_2_CoordinateSystemAxisType_httpwww_opengis_netgml3_2rangeMeaning', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 479, 3), )

    
    rangeMeaning = property(__rangeMeaning.value, __rangeMeaning.set, None, 'gml:rangeMeaning describes the meaning of axis value range specified by gml:minimumValue and gml:maximumValue. This element shall be omitted when both gml:minimumValue and gml:maximumValue are omitted. This element should be included when gml:minimumValue and/or gml:maximumValue are included. If this element is omitted when the gml:minimumValue and/or gml:maximumValue are included, the meaning is unspecified. The codeSpace attribute shall reference a source of information specifying the values and meanings of all the allowed string values for this property.')

    
    # Attribute id_ inherited from {http://www.opengis.net/gml/3.2}DefinitionBaseType
    _ElementMap.update({
        __axisAbbrev.name() : __axisAbbrev,
        __axisDirection.name() : __axisDirection,
        __minimumValue.name() : __minimumValue,
        __maximumValue.name() : __maximumValue,
        __rangeMeaning.name() : __rangeMeaning
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CoordinateSystemAxisType = CoordinateSystemAxisType
_Namespace_gml.addCategoryObject('typeBinding', 'CoordinateSystemAxisType', CoordinateSystemAxisType)


# Complex type {http://www.opengis.net/gml/3.2}AbstractDatumType with content type ELEMENT_ONLY
class AbstractDatumType (IdentifiedObjectType):
    """Complex type {http://www.opengis.net/gml/3.2}AbstractDatumType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractDatumType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 636, 3)
    _ElementMap = IdentifiedObjectType._ElementMap.copy()
    _AttributeMap = IdentifiedObjectType._AttributeMap.copy()
    # Base type is IdentifiedObjectType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element remarks ({http://www.opengis.net/gml/3.2}remarks) inherited from {http://www.opengis.net/gml/3.2}DefinitionType
    
    # Element {http://www.opengis.net/gml/3.2}domainOfValidity uses Python identifier domainOfValidity
    __domainOfValidity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'domainOfValidity'), 'domainOfValidity', '__httpwww_opengis_netgml3_2_AbstractDatumType_httpwww_opengis_netgml3_2domainOfValidity', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 252, 3), )

    
    domainOfValidity = property(__domainOfValidity.value, __domainOfValidity.set, None, 'The gml:domainOfValidity property implements an association role to an EX_Extent object as encoded in ISO/TS 19139, either referencing or containing the definition of that extent.')

    
    # Element {http://www.opengis.net/gml/3.2}scope uses Python identifier scope
    __scope = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'scope'), 'scope', '__httpwww_opengis_netgml3_2_AbstractDatumType_httpwww_opengis_netgml3_2scope', True, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 369, 3), )

    
    scope = property(__scope.value, __scope.set, None, 'The gml:scope property provides a description of the usage, or limitations of usage, for which this CRS-related object is valid. If unknown, enter "not known".')

    
    # Element {http://www.opengis.net/gml/3.2}anchorDefinition uses Python identifier anchorDefinition
    __anchorDefinition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'anchorDefinition'), 'anchorDefinition', '__httpwww_opengis_netgml3_2_AbstractDatumType_httpwww_opengis_netgml3_2anchorDefinition', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 649, 3), )

    
    anchorDefinition = property(__anchorDefinition.value, __anchorDefinition.set, None, 'gml:anchorDefinition is a description, possibly including coordinates, of the definition used to anchor the datum to the Earth. Also known as the "origin", especially for engineering and image datums. The codeSpace attribute may be used to reference a source of more detailed on this point or surface, or on a set of such descriptions.\n-\tFor a geodetic datum, this point is also known as the fundamental point, which is traditionally the point where the relationship between geoid and ellipsoid is defined. In some cases, the "fundamental point" may consist of a number of points. In those cases, the parameters defining the geoid/ellipsoid relationship have been averaged for these points, and the averages adopted as the datum definition.\n-\tFor an engineering datum, the anchor definition may be a physical point, or it may be a point with defined coordinates in another CRS.may\n-\tFor an image datum, the anchor definition is usually either the centre of the image or the corner of the image.\n-\tFor a temporal datum, this attribute is not defined. Instead of the anchor definition, a temporal datum carries a separate time origin of type DateTime.')

    
    # Element {http://www.opengis.net/gml/3.2}realizationEpoch uses Python identifier realizationEpoch
    __realizationEpoch = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'realizationEpoch'), 'realizationEpoch', '__httpwww_opengis_netgml3_2_AbstractDatumType_httpwww_opengis_netgml3_2realizationEpoch', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 659, 3), )

    
    realizationEpoch = property(__realizationEpoch.value, __realizationEpoch.set, None, 'gml:realizationEpoch is the time after which this datum definition is valid. See ISO 19111 Table 32 for details.')

    
    # Attribute id_ inherited from {http://www.opengis.net/gml/3.2}DefinitionBaseType
    _ElementMap.update({
        __domainOfValidity.name() : __domainOfValidity,
        __scope.name() : __scope,
        __anchorDefinition.name() : __anchorDefinition,
        __realizationEpoch.name() : __realizationEpoch
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AbstractDatumType = AbstractDatumType
_Namespace_gml.addCategoryObject('typeBinding', 'AbstractDatumType', AbstractDatumType)


# Complex type {http://www.opengis.net/gml/3.2}PrimeMeridianType with content type ELEMENT_ONLY
class PrimeMeridianType (IdentifiedObjectType):
    """Complex type {http://www.opengis.net/gml/3.2}PrimeMeridianType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'PrimeMeridianType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 688, 3)
    _ElementMap = IdentifiedObjectType._ElementMap.copy()
    _AttributeMap = IdentifiedObjectType._AttributeMap.copy()
    # Base type is IdentifiedObjectType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element remarks ({http://www.opengis.net/gml/3.2}remarks) inherited from {http://www.opengis.net/gml/3.2}DefinitionType
    
    # Element {http://www.opengis.net/gml/3.2}greenwichLongitude uses Python identifier greenwichLongitude
    __greenwichLongitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'greenwichLongitude'), 'greenwichLongitude', '__httpwww_opengis_netgml3_2_PrimeMeridianType_httpwww_opengis_netgml3_2greenwichLongitude', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 698, 3), )

    
    greenwichLongitude = property(__greenwichLongitude.value, __greenwichLongitude.set, None, 'gml:greenwichLongitude is the longitude of the prime meridian measured from the Greenwich meridian, positive eastward. If the value of the prime meridian "name" is "Greenwich" then the value of greenwichLongitude shall be 0 degrees.')

    
    # Attribute id_ inherited from {http://www.opengis.net/gml/3.2}DefinitionBaseType
    _ElementMap.update({
        __greenwichLongitude.name() : __greenwichLongitude
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PrimeMeridianType = PrimeMeridianType
_Namespace_gml.addCategoryObject('typeBinding', 'PrimeMeridianType', PrimeMeridianType)


# Complex type {http://www.opengis.net/gml/3.2}EllipsoidType with content type ELEMENT_ONLY
class EllipsoidType (IdentifiedObjectType):
    """Complex type {http://www.opengis.net/gml/3.2}EllipsoidType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'EllipsoidType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 743, 3)
    _ElementMap = IdentifiedObjectType._ElementMap.copy()
    _AttributeMap = IdentifiedObjectType._AttributeMap.copy()
    # Base type is IdentifiedObjectType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element remarks ({http://www.opengis.net/gml/3.2}remarks) inherited from {http://www.opengis.net/gml/3.2}DefinitionType
    
    # Element {http://www.opengis.net/gml/3.2}semiMajorAxis uses Python identifier semiMajorAxis
    __semiMajorAxis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'semiMajorAxis'), 'semiMajorAxis', '__httpwww_opengis_netgml3_2_EllipsoidType_httpwww_opengis_netgml3_2semiMajorAxis', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 754, 3), )

    
    semiMajorAxis = property(__semiMajorAxis.value, __semiMajorAxis.set, None, 'gml:semiMajorAxis specifies the length of the semi-major axis of the ellipsoid, with its units. Uses the MeasureType with the restriction that the unit of measure referenced by uom must be suitable for a length, such as metres or feet.')

    
    # Element {http://www.opengis.net/gml/3.2}secondDefiningParameter uses Python identifier secondDefiningParameter
    __secondDefiningParameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'secondDefiningParameter'), 'secondDefiningParameter', '__httpwww_opengis_netgml3_2_EllipsoidType_httpwww_opengis_netgml3_2secondDefiningParameter', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 760, 3), )

    
    secondDefiningParameter = property(__secondDefiningParameter.value, __secondDefiningParameter.set, None, 'gml:secondDefiningParameter is a property containing the definition of the second parameter that defines the shape of an ellipsoid. An ellipsoid requires two defining parameters: semi-major axis and inverse flattening or semi-major axis and semi-minor axis. When the reference body is a sphere rather than an ellipsoid, only a single defining parameter is required, namely the radius of the sphere; in that case, the semi-major axis "degenerates" into the radius of the sphere.\nThe inverseFlattening element contains the inverse flattening value of the ellipsoid. This value is a scale factor (or ratio). It uses gml:LengthType with the restriction that the unit of measure referenced by the uom attribute must be suitable for a scale factor, such as percent, permil, or parts-per-million.\nThe semiMinorAxis element contains the length of the semi-minor axis of the ellipsoid. When the isSphere element is included, the ellipsoid is degenerate and is actually a sphere. The sphere is completely defined by the semi-major axis, which is the radius of the sphere.')

    
    # Attribute id_ inherited from {http://www.opengis.net/gml/3.2}DefinitionBaseType
    _ElementMap.update({
        __semiMajorAxis.name() : __semiMajorAxis,
        __secondDefiningParameter.name() : __secondDefiningParameter
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.EllipsoidType = EllipsoidType
_Namespace_gml.addCategoryObject('typeBinding', 'EllipsoidType', EllipsoidType)


# Complex type {http://www.opengis.net/gml/3.2}AbstractCoordinateOperationType with content type ELEMENT_ONLY
class AbstractCoordinateOperationType (IdentifiedObjectType):
    """Complex type {http://www.opengis.net/gml/3.2}AbstractCoordinateOperationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractCoordinateOperationType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 881, 3)
    _ElementMap = IdentifiedObjectType._ElementMap.copy()
    _AttributeMap = IdentifiedObjectType._AttributeMap.copy()
    # Base type is IdentifiedObjectType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element remarks ({http://www.opengis.net/gml/3.2}remarks) inherited from {http://www.opengis.net/gml/3.2}DefinitionType
    
    # Element {http://www.opengis.net/gml/3.2}domainOfValidity uses Python identifier domainOfValidity
    __domainOfValidity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'domainOfValidity'), 'domainOfValidity', '__httpwww_opengis_netgml3_2_AbstractCoordinateOperationType_httpwww_opengis_netgml3_2domainOfValidity', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 252, 3), )

    
    domainOfValidity = property(__domainOfValidity.value, __domainOfValidity.set, None, 'The gml:domainOfValidity property implements an association role to an EX_Extent object as encoded in ISO/TS 19139, either referencing or containing the definition of that extent.')

    
    # Element {http://www.opengis.net/gml/3.2}scope uses Python identifier scope
    __scope = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'scope'), 'scope', '__httpwww_opengis_netgml3_2_AbstractCoordinateOperationType_httpwww_opengis_netgml3_2scope', True, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 369, 3), )

    
    scope = property(__scope.value, __scope.set, None, 'The gml:scope property provides a description of the usage, or limitations of usage, for which this CRS-related object is valid. If unknown, enter "not known".')

    
    # Element {http://www.opengis.net/gml/3.2}operationVersion uses Python identifier operationVersion
    __operationVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'operationVersion'), 'operationVersion', '__httpwww_opengis_netgml3_2_AbstractCoordinateOperationType_httpwww_opengis_netgml3_2operationVersion', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 896, 3), )

    
    operationVersion = property(__operationVersion.value, __operationVersion.set, None, 'gml:operationVersion is the version of the coordinate transformation (i.e., instantiation due to the stochastic nature of the parameters). Mandatory when describing a transformation, and should not be supplied for a conversion.')

    
    # Element {http://www.opengis.net/gml/3.2}coordinateOperationAccuracy uses Python identifier coordinateOperationAccuracy
    __coordinateOperationAccuracy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'coordinateOperationAccuracy'), 'coordinateOperationAccuracy', '__httpwww_opengis_netgml3_2_AbstractCoordinateOperationType_httpwww_opengis_netgml3_2coordinateOperationAccuracy', True, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 902, 3), )

    
    coordinateOperationAccuracy = property(__coordinateOperationAccuracy.value, __coordinateOperationAccuracy.set, None, 'gml:coordinateOperationAccuracy is an association role to a DQ_PositionalAccuracy object as encoded in ISO/TS 19139, either referencing or containing the definition of that positional accuracy. That object contains an estimate of the impact of this coordinate operation on point accuracy. That is, it gives position error estimates for the target coordinates of this coordinate operation, assuming no errors in the source coordinates.')

    
    # Element {http://www.opengis.net/gml/3.2}sourceCRS uses Python identifier sourceCRS
    __sourceCRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'sourceCRS'), 'sourceCRS', '__httpwww_opengis_netgml3_2_AbstractCoordinateOperationType_httpwww_opengis_netgml3_2sourceCRS', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 924, 3), )

    
    sourceCRS = property(__sourceCRS.value, __sourceCRS.set, None, 'gml:sourceCRS is an association role to the source CRS (coordinate reference system) of this coordinate operation.')

    
    # Element {http://www.opengis.net/gml/3.2}targetCRS uses Python identifier targetCRS
    __targetCRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'targetCRS'), 'targetCRS', '__httpwww_opengis_netgml3_2_AbstractCoordinateOperationType_httpwww_opengis_netgml3_2targetCRS', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 940, 3), )

    
    targetCRS = property(__targetCRS.value, __targetCRS.set, None, 'gml:targetCRS is an association role to the target CRS (coordinate reference system) of this coordinate operation.')

    
    # Attribute id_ inherited from {http://www.opengis.net/gml/3.2}DefinitionBaseType
    _ElementMap.update({
        __domainOfValidity.name() : __domainOfValidity,
        __scope.name() : __scope,
        __operationVersion.name() : __operationVersion,
        __coordinateOperationAccuracy.name() : __coordinateOperationAccuracy,
        __sourceCRS.name() : __sourceCRS,
        __targetCRS.name() : __targetCRS
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AbstractCoordinateOperationType = AbstractCoordinateOperationType
_Namespace_gml.addCategoryObject('typeBinding', 'AbstractCoordinateOperationType', AbstractCoordinateOperationType)


# Complex type {http://www.opengis.net/gml/3.2}GeodeticCRSType with content type ELEMENT_ONLY
class GeodeticCRSType (AbstractCRSType):
    """gml:GeodeticCRS is a coordinate reference system based on a geodetic datum."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'GeodeticCRSType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 30, 3)
    _ElementMap = AbstractCRSType._ElementMap.copy()
    _AttributeMap = AbstractCRSType._AttributeMap.copy()
    # Base type is AbstractCRSType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element remarks ({http://www.opengis.net/gml/3.2}remarks) inherited from {http://www.opengis.net/gml/3.2}DefinitionType
    
    # Element domainOfValidity ({http://www.opengis.net/gml/3.2}domainOfValidity) inherited from {http://www.opengis.net/gml/3.2}AbstractCRSType
    
    # Element scope ({http://www.opengis.net/gml/3.2}scope) inherited from {http://www.opengis.net/gml/3.2}AbstractCRSType
    
    # Element {http://www.opengis.net/gml/3.2}ellipsoidalCS uses Python identifier ellipsoidalCS
    __ellipsoidalCS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'ellipsoidalCS'), 'ellipsoidalCS', '__httpwww_opengis_netgml3_2_GeodeticCRSType_httpwww_opengis_netgml3_2ellipsoidalCS', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 375, 3), )

    
    ellipsoidalCS = property(__ellipsoidalCS.value, __ellipsoidalCS.set, None, 'gml:ellipsoidalCS is an association role to the ellipsoidal coordinate system used by this CRS.')

    
    # Element {http://www.opengis.net/gml/3.2}cartesianCS uses Python identifier cartesianCS
    __cartesianCS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'cartesianCS'), 'cartesianCS', '__httpwww_opengis_netgml3_2_GeodeticCRSType_httpwww_opengis_netgml3_2cartesianCS', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 543, 3), )

    
    cartesianCS = property(__cartesianCS.value, __cartesianCS.set, None, 'gml:cartesianCS is an association role to the Cartesian coordinate system used by this CRS.')

    
    # Element {http://www.opengis.net/gml/3.2}sphericalCS uses Python identifier sphericalCS
    __sphericalCS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'sphericalCS'), 'sphericalCS', '__httpwww_opengis_netgml3_2_GeodeticCRSType_httpwww_opengis_netgml3_2sphericalCS', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 572, 3), )

    
    sphericalCS = property(__sphericalCS.value, __sphericalCS.set, None, 'gml:sphericalCS is an association role to the spherical coordinate system used by this CRS.')

    
    # Element {http://www.opengis.net/gml/3.2}geodeticDatum uses Python identifier geodeticDatum
    __geodeticDatum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'geodeticDatum'), 'geodeticDatum', '__httpwww_opengis_netgml3_2_GeodeticCRSType_httpwww_opengis_netgml3_2geodeticDatum', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 601, 3), )

    
    geodeticDatum = property(__geodeticDatum.value, __geodeticDatum.set, None, 'gml:geodeticDatum is an association role to the geodetic datum used by this CRS.\n')

    
    # Attribute id_ inherited from {http://www.opengis.net/gml/3.2}DefinitionBaseType
    _ElementMap.update({
        __ellipsoidalCS.name() : __ellipsoidalCS,
        __cartesianCS.name() : __cartesianCS,
        __sphericalCS.name() : __sphericalCS,
        __geodeticDatum.name() : __geodeticDatum
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GeodeticCRSType = GeodeticCRSType
_Namespace_gml.addCategoryObject('typeBinding', 'GeodeticCRSType', GeodeticCRSType)


# Complex type {http://www.opengis.net/gml/3.2}EllipsoidalCSType with content type ELEMENT_ONLY
class EllipsoidalCSType (AbstractCoordinateSystemType):
    """Complex type {http://www.opengis.net/gml/3.2}EllipsoidalCSType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'EllipsoidalCSType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 398, 3)
    _ElementMap = AbstractCoordinateSystemType._ElementMap.copy()
    _AttributeMap = AbstractCoordinateSystemType._AttributeMap.copy()
    # Base type is AbstractCoordinateSystemType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element remarks ({http://www.opengis.net/gml/3.2}remarks) inherited from {http://www.opengis.net/gml/3.2}DefinitionType
    
    # Element axis ({http://www.opengis.net/gml/3.2}axis) inherited from {http://www.opengis.net/gml/3.2}AbstractCoordinateSystemType
    
    # Attribute id_ inherited from {http://www.opengis.net/gml/3.2}DefinitionBaseType
    
    # Attribute aggregationType inherited from {http://www.opengis.net/gml/3.2}AbstractCoordinateSystemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.EllipsoidalCSType = EllipsoidalCSType
_Namespace_gml.addCategoryObject('typeBinding', 'EllipsoidalCSType', EllipsoidalCSType)


# Complex type {http://www.opengis.net/gml/3.2}CartesianCSType with content type ELEMENT_ONLY
class CartesianCSType (AbstractCoordinateSystemType):
    """Complex type {http://www.opengis.net/gml/3.2}CartesianCSType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'CartesianCSType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 566, 3)
    _ElementMap = AbstractCoordinateSystemType._ElementMap.copy()
    _AttributeMap = AbstractCoordinateSystemType._AttributeMap.copy()
    # Base type is AbstractCoordinateSystemType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element remarks ({http://www.opengis.net/gml/3.2}remarks) inherited from {http://www.opengis.net/gml/3.2}DefinitionType
    
    # Element axis ({http://www.opengis.net/gml/3.2}axis) inherited from {http://www.opengis.net/gml/3.2}AbstractCoordinateSystemType
    
    # Attribute id_ inherited from {http://www.opengis.net/gml/3.2}DefinitionBaseType
    
    # Attribute aggregationType inherited from {http://www.opengis.net/gml/3.2}AbstractCoordinateSystemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CartesianCSType = CartesianCSType
_Namespace_gml.addCategoryObject('typeBinding', 'CartesianCSType', CartesianCSType)


# Complex type {http://www.opengis.net/gml/3.2}SphericalCSType with content type ELEMENT_ONLY
class SphericalCSType (AbstractCoordinateSystemType):
    """Complex type {http://www.opengis.net/gml/3.2}SphericalCSType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'SphericalCSType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 595, 3)
    _ElementMap = AbstractCoordinateSystemType._ElementMap.copy()
    _AttributeMap = AbstractCoordinateSystemType._AttributeMap.copy()
    # Base type is AbstractCoordinateSystemType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element remarks ({http://www.opengis.net/gml/3.2}remarks) inherited from {http://www.opengis.net/gml/3.2}DefinitionType
    
    # Element axis ({http://www.opengis.net/gml/3.2}axis) inherited from {http://www.opengis.net/gml/3.2}AbstractCoordinateSystemType
    
    # Attribute id_ inherited from {http://www.opengis.net/gml/3.2}DefinitionBaseType
    
    # Attribute aggregationType inherited from {http://www.opengis.net/gml/3.2}AbstractCoordinateSystemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SphericalCSType = SphericalCSType
_Namespace_gml.addCategoryObject('typeBinding', 'SphericalCSType', SphericalCSType)


# Complex type {http://www.opengis.net/gml/3.2}GeodeticDatumType with content type ELEMENT_ONLY
class GeodeticDatumType (AbstractDatumType):
    """Complex type {http://www.opengis.net/gml/3.2}GeodeticDatumType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'GeodeticDatumType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 625, 3)
    _ElementMap = AbstractDatumType._ElementMap.copy()
    _AttributeMap = AbstractDatumType._AttributeMap.copy()
    # Base type is AbstractDatumType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element remarks ({http://www.opengis.net/gml/3.2}remarks) inherited from {http://www.opengis.net/gml/3.2}DefinitionType
    
    # Element domainOfValidity ({http://www.opengis.net/gml/3.2}domainOfValidity) inherited from {http://www.opengis.net/gml/3.2}AbstractDatumType
    
    # Element scope ({http://www.opengis.net/gml/3.2}scope) inherited from {http://www.opengis.net/gml/3.2}AbstractDatumType
    
    # Element anchorDefinition ({http://www.opengis.net/gml/3.2}anchorDefinition) inherited from {http://www.opengis.net/gml/3.2}AbstractDatumType
    
    # Element realizationEpoch ({http://www.opengis.net/gml/3.2}realizationEpoch) inherited from {http://www.opengis.net/gml/3.2}AbstractDatumType
    
    # Element {http://www.opengis.net/gml/3.2}primeMeridian uses Python identifier primeMeridian
    __primeMeridian = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'primeMeridian'), 'primeMeridian', '__httpwww_opengis_netgml3_2_GeodeticDatumType_httpwww_opengis_netgml3_2primeMeridian', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 665, 3), )

    
    primeMeridian = property(__primeMeridian.value, __primeMeridian.set, None, 'gml:primeMeridian is an association role to the prime meridian used by this geodetic datum.')

    
    # Element {http://www.opengis.net/gml/3.2}ellipsoid uses Python identifier ellipsoid
    __ellipsoid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'ellipsoid'), 'ellipsoid', '__httpwww_opengis_netgml3_2_GeodeticDatumType_httpwww_opengis_netgml3_2ellipsoid', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 721, 3), )

    
    ellipsoid = property(__ellipsoid.value, __ellipsoid.set, None, 'gml:ellipsoid is an association role to the ellipsoid used by this geodetic datum.')

    
    # Attribute id_ inherited from {http://www.opengis.net/gml/3.2}DefinitionBaseType
    _ElementMap.update({
        __primeMeridian.name() : __primeMeridian,
        __ellipsoid.name() : __ellipsoid
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GeodeticDatumType = GeodeticDatumType
_Namespace_gml.addCategoryObject('typeBinding', 'GeodeticDatumType', GeodeticDatumType)


# Complex type {http://www.opengis.net/gml/3.2}AbstractGeneralDerivedCRSType with content type ELEMENT_ONLY
class AbstractGeneralDerivedCRSType (AbstractCRSType):
    """Complex type {http://www.opengis.net/gml/3.2}AbstractGeneralDerivedCRSType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractGeneralDerivedCRSType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 827, 3)
    _ElementMap = AbstractCRSType._ElementMap.copy()
    _AttributeMap = AbstractCRSType._AttributeMap.copy()
    # Base type is AbstractCRSType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element remarks ({http://www.opengis.net/gml/3.2}remarks) inherited from {http://www.opengis.net/gml/3.2}DefinitionType
    
    # Element domainOfValidity ({http://www.opengis.net/gml/3.2}domainOfValidity) inherited from {http://www.opengis.net/gml/3.2}AbstractCRSType
    
    # Element scope ({http://www.opengis.net/gml/3.2}scope) inherited from {http://www.opengis.net/gml/3.2}AbstractCRSType
    
    # Element {http://www.opengis.net/gml/3.2}conversion uses Python identifier conversion
    __conversion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'conversion'), 'conversion', '__httpwww_opengis_netgml3_2_AbstractGeneralDerivedCRSType_httpwww_opengis_netgml3_2conversion', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 837, 3), )

    
    conversion = property(__conversion.value, __conversion.set, None, 'gml:conversion is an association role to the coordinate conversion used to define the derived CRS.')

    
    # Attribute id_ inherited from {http://www.opengis.net/gml/3.2}DefinitionBaseType
    _ElementMap.update({
        __conversion.name() : __conversion
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AbstractGeneralDerivedCRSType = AbstractGeneralDerivedCRSType
_Namespace_gml.addCategoryObject('typeBinding', 'AbstractGeneralDerivedCRSType', AbstractGeneralDerivedCRSType)


# Complex type {http://www.opengis.net/gml/3.2}AbstractGeneralConversionType with content type ELEMENT_ONLY
class AbstractGeneralConversionType (AbstractCoordinateOperationType):
    """Complex type {http://www.opengis.net/gml/3.2}AbstractGeneralConversionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractGeneralConversionType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 862, 3)
    _ElementMap = AbstractCoordinateOperationType._ElementMap.copy()
    _AttributeMap = AbstractCoordinateOperationType._AttributeMap.copy()
    # Base type is AbstractCoordinateOperationType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element remarks ({http://www.opengis.net/gml/3.2}remarks) inherited from {http://www.opengis.net/gml/3.2}DefinitionType
    
    # Element domainOfValidity ({http://www.opengis.net/gml/3.2}domainOfValidity) inherited from {http://www.opengis.net/gml/3.2}AbstractCoordinateOperationType
    
    # Element scope ({http://www.opengis.net/gml/3.2}scope) inherited from {http://www.opengis.net/gml/3.2}AbstractCoordinateOperationType
    
    # Element coordinateOperationAccuracy ({http://www.opengis.net/gml/3.2}coordinateOperationAccuracy) inherited from {http://www.opengis.net/gml/3.2}AbstractCoordinateOperationType
    
    # Attribute id is restricted from parent
    
    # Attribute {http://www.opengis.net/gml/3.2}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'id'), 'id', '__httpwww_opengis_netgml3_2_AbstractGMLType_httpwww_opengis_netgml3_2id', pyxb.binding.datatypes.ID, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 113, 3)
    __id._UseLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 876, 12)
    
    id = property(__id.value, __id.set, None, 'The attribute gml:id supports provision of a handle for the XML element representing a GML Object. Its use is mandatory for all GML objects. It is of XML type ID, so is constrained to be unique in the XML document within which it occurs.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.AbstractGeneralConversionType = AbstractGeneralConversionType
_Namespace_gml.addCategoryObject('typeBinding', 'AbstractGeneralConversionType', AbstractGeneralConversionType)


# Complex type {http://www.opengis.net/gml/3.2}VerticalCRSType with content type ELEMENT_ONLY
class VerticalCRSType (AbstractCRSType):
    """Complex type {http://www.opengis.net/gml/3.2}VerticalCRSType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'VerticalCRSType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 1002, 3)
    _ElementMap = AbstractCRSType._ElementMap.copy()
    _AttributeMap = AbstractCRSType._AttributeMap.copy()
    # Base type is AbstractCRSType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element remarks ({http://www.opengis.net/gml/3.2}remarks) inherited from {http://www.opengis.net/gml/3.2}DefinitionType
    
    # Element domainOfValidity ({http://www.opengis.net/gml/3.2}domainOfValidity) inherited from {http://www.opengis.net/gml/3.2}AbstractCRSType
    
    # Element scope ({http://www.opengis.net/gml/3.2}scope) inherited from {http://www.opengis.net/gml/3.2}AbstractCRSType
    
    # Element {http://www.opengis.net/gml/3.2}verticalCS uses Python identifier verticalCS
    __verticalCS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'verticalCS'), 'verticalCS', '__httpwww_opengis_netgml3_2_VerticalCRSType_httpwww_opengis_netgml3_2verticalCS', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 1013, 3), )

    
    verticalCS = property(__verticalCS.value, __verticalCS.set, None, 'gml:verticalCS is an association role to the vertical coordinate system used by this CRS.')

    
    # Element {http://www.opengis.net/gml/3.2}verticalDatum uses Python identifier verticalDatum
    __verticalDatum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'verticalDatum'), 'verticalDatum', '__httpwww_opengis_netgml3_2_VerticalCRSType_httpwww_opengis_netgml3_2verticalDatum', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 1042, 3), )

    
    verticalDatum = property(__verticalDatum.value, __verticalDatum.set, None, 'gml:verticalDatum is an association role to the vertical datum used by this CRS.')

    
    # Attribute id_ inherited from {http://www.opengis.net/gml/3.2}DefinitionBaseType
    _ElementMap.update({
        __verticalCS.name() : __verticalCS,
        __verticalDatum.name() : __verticalDatum
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.VerticalCRSType = VerticalCRSType
_Namespace_gml.addCategoryObject('typeBinding', 'VerticalCRSType', VerticalCRSType)


# Complex type {http://www.opengis.net/gml/3.2}VerticalCSType with content type ELEMENT_ONLY
class VerticalCSType (AbstractCoordinateSystemType):
    """Complex type {http://www.opengis.net/gml/3.2}VerticalCSType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'VerticalCSType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 1036, 3)
    _ElementMap = AbstractCoordinateSystemType._ElementMap.copy()
    _AttributeMap = AbstractCoordinateSystemType._AttributeMap.copy()
    # Base type is AbstractCoordinateSystemType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element remarks ({http://www.opengis.net/gml/3.2}remarks) inherited from {http://www.opengis.net/gml/3.2}DefinitionType
    
    # Element axis ({http://www.opengis.net/gml/3.2}axis) inherited from {http://www.opengis.net/gml/3.2}AbstractCoordinateSystemType
    
    # Attribute id_ inherited from {http://www.opengis.net/gml/3.2}DefinitionBaseType
    
    # Attribute aggregationType inherited from {http://www.opengis.net/gml/3.2}AbstractCoordinateSystemType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.VerticalCSType = VerticalCSType
_Namespace_gml.addCategoryObject('typeBinding', 'VerticalCSType', VerticalCSType)


# Complex type {http://www.opengis.net/gml/3.2}VerticalDatumType with content type ELEMENT_ONLY
class VerticalDatumType (AbstractDatumType):
    """Complex type {http://www.opengis.net/gml/3.2}VerticalDatumType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'VerticalDatumType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 1065, 3)
    _ElementMap = AbstractDatumType._ElementMap.copy()
    _AttributeMap = AbstractDatumType._AttributeMap.copy()
    # Base type is AbstractDatumType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element remarks ({http://www.opengis.net/gml/3.2}remarks) inherited from {http://www.opengis.net/gml/3.2}DefinitionType
    
    # Element domainOfValidity ({http://www.opengis.net/gml/3.2}domainOfValidity) inherited from {http://www.opengis.net/gml/3.2}AbstractDatumType
    
    # Element scope ({http://www.opengis.net/gml/3.2}scope) inherited from {http://www.opengis.net/gml/3.2}AbstractDatumType
    
    # Element anchorDefinition ({http://www.opengis.net/gml/3.2}anchorDefinition) inherited from {http://www.opengis.net/gml/3.2}AbstractDatumType
    
    # Element realizationEpoch ({http://www.opengis.net/gml/3.2}realizationEpoch) inherited from {http://www.opengis.net/gml/3.2}AbstractDatumType
    
    # Attribute id_ inherited from {http://www.opengis.net/gml/3.2}DefinitionBaseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.VerticalDatumType = VerticalDatumType
_Namespace_gml.addCategoryObject('typeBinding', 'VerticalDatumType', VerticalDatumType)


# Complex type {http://www.opengis.net/gml/3.2}ProjectedCRSType with content type ELEMENT_ONLY
class ProjectedCRSType (AbstractGeneralDerivedCRSType):
    """Complex type {http://www.opengis.net/gml/3.2}ProjectedCRSType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_gml, 'ProjectedCRSType')
    _XSDLocation = pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 813, 3)
    _ElementMap = AbstractGeneralDerivedCRSType._ElementMap.copy()
    _AttributeMap = AbstractGeneralDerivedCRSType._AttributeMap.copy()
    # Base type is AbstractGeneralDerivedCRSType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element remarks ({http://www.opengis.net/gml/3.2}remarks) inherited from {http://www.opengis.net/gml/3.2}DefinitionType
    
    # Element domainOfValidity ({http://www.opengis.net/gml/3.2}domainOfValidity) inherited from {http://www.opengis.net/gml/3.2}AbstractCRSType
    
    # Element scope ({http://www.opengis.net/gml/3.2}scope) inherited from {http://www.opengis.net/gml/3.2}AbstractCRSType
    
    # Element {http://www.opengis.net/gml/3.2}cartesianCS uses Python identifier cartesianCS
    __cartesianCS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'cartesianCS'), 'cartesianCS', '__httpwww_opengis_netgml3_2_ProjectedCRSType_httpwww_opengis_netgml3_2cartesianCS', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 543, 3), )

    
    cartesianCS = property(__cartesianCS.value, __cartesianCS.set, None, 'gml:cartesianCS is an association role to the Cartesian coordinate system used by this CRS.')

    
    # Element conversion ({http://www.opengis.net/gml/3.2}conversion) inherited from {http://www.opengis.net/gml/3.2}AbstractGeneralDerivedCRSType
    
    # Element {http://www.opengis.net/gml/3.2}baseGeodeticCRS uses Python identifier baseGeodeticCRS
    __baseGeodeticCRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'baseGeodeticCRS'), 'baseGeodeticCRS', '__httpwww_opengis_netgml3_2_ProjectedCRSType_httpwww_opengis_netgml3_2baseGeodeticCRS', False, pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 971, 3), )

    
    baseGeodeticCRS = property(__baseGeodeticCRS.value, __baseGeodeticCRS.set, None, 'gml:baseGeodeticCRS is an association role to the geodetic coordinate reference system used by this projected CRS.')

    
    # Attribute id_ inherited from {http://www.opengis.net/gml/3.2}DefinitionBaseType
    _ElementMap.update({
        __cartesianCS.name() : __cartesianCS,
        __baseGeodeticCRS.name() : __baseGeodeticCRS
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ProjectedCRSType = ProjectedCRSType
_Namespace_gml.addCategoryObject('typeBinding', 'ProjectedCRSType', ProjectedCRSType)


CharacterString = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gco, 'CharacterString'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 52, 3))
_Namespace_gco.addCategoryObject('elementBinding', CharacterString.name().localName(), CharacterString)

Boolean = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gco, 'Boolean'), pyxb.binding.datatypes.boolean, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 63, 3))
_Namespace_gco.addCategoryObject('elementBinding', Boolean.name().localName(), Boolean)

Real = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gco, 'Real'), pyxb.binding.datatypes.double, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 79, 3))
_Namespace_gco.addCategoryObject('elementBinding', Real.name().localName(), Real)

DateTime = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gco, 'DateTime'), pyxb.binding.datatypes.dateTime, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 103, 3))
_Namespace_gco.addCategoryObject('elementBinding', DateTime.name().localName(), DateTime)

URL = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'URL'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 419, 3))
_Namespace_gmd.addCategoryObject('elementBinding', URL.name().localName(), URL)

AbstractObject = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractObject'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), documentation='This element has no type defined, and is therefore implicitly (according to the rules of W3C XML Schema) an XML Schema anyType. It is used as the head of an XML Schema substitution group which unifies complex content and certain simple content elements used for datatypes in GML, including the gml:AbstractGML substitution group.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 119, 3))
_Namespace_gml.addCategoryObject('elementBinding', AbstractObject.name().localName(), AbstractObject)

remarks = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'remarks'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 250, 3))
_Namespace_gml.addCategoryObject('elementBinding', remarks.name().localName(), remarks)

scope = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'scope'), pyxb.binding.datatypes.string, documentation='The gml:scope property provides a description of the usage, or limitations of usage, for which this CRS-related object is valid. If unknown, enter "not known".', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 369, 3))
_Namespace_gml.addCategoryObject('elementBinding', scope.name().localName(), scope)

minimumValue = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'minimumValue'), pyxb.binding.datatypes.double, documentation='The gml:minimumValue and gml:maximumValue properties allow the specification of minimum and maximum value normally allowed for this axis, in the unit of measure for the axis. For a continuous angular axis such as longitude, the values wrap-around at this value. Also, values beyond this minimum/maximum can be used for specified purposes, such as in a bounding box. A value of minus infinity shall be allowed for the gml:minimumValue element, a value of plus infiniy for the gml:maximumValue element. If these elements are omitted, the value is unspecified.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 467, 3))
_Namespace_gml.addCategoryObject('elementBinding', minimumValue.name().localName(), minimumValue)

maximumValue = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'maximumValue'), pyxb.binding.datatypes.double, documentation='The gml:minimumValue and gml:maximumValue properties allow the specification of minimum and maximum value normally allowed for this axis, in the unit of measure for the axis. For a continuous angular axis such as longitude, the values wrap-around at this value. Also, values beyond this minimum/maximum can be used for specified purposes, such as in a bounding box. A value of minus infinity shall be allowed for the gml:minimumValue element, a value of plus infiniy for the gml:maximumValue element. If these elements are omitted, the value is unspecified.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 473, 3))
_Namespace_gml.addCategoryObject('elementBinding', maximumValue.name().localName(), maximumValue)

realizationEpoch = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'realizationEpoch'), pyxb.binding.datatypes.date, documentation='gml:realizationEpoch is the time after which this datum definition is valid. See ISO 19111 Table 32 for details.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 659, 3))
_Namespace_gml.addCategoryObject('elementBinding', realizationEpoch.name().localName(), realizationEpoch)

operationVersion = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'operationVersion'), pyxb.binding.datatypes.string, documentation='gml:operationVersion is the version of the coordinate transformation (i.e., instantiation due to the stochastic nature of the parameters). Mandatory when describing a transformation, and should not be supplied for a conversion.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 896, 3))
_Namespace_gml.addCategoryObject('elementBinding', operationVersion.name().localName(), operationVersion)

Date = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gco, 'Date'), Date_Type, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 91, 3))
_Namespace_gco.addCategoryObject('elementBinding', Date.name().localName(), Date)

CI_DateTypeCode = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_DateTypeCode'), CodeListValue_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 267, 3))
_Namespace_gmd.addCategoryObject('elementBinding', CI_DateTypeCode.name().localName(), CI_DateTypeCode)

CI_OnLineFunctionCode = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_OnLineFunctionCode'), CodeListValue_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 428, 3))
_Namespace_gmd.addCategoryObject('elementBinding', CI_OnLineFunctionCode.name().localName(), CI_OnLineFunctionCode)

CI_RoleCode = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_RoleCode'), CodeListValue_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 438, 3))
_Namespace_gmd.addCategoryObject('elementBinding', CI_RoleCode.name().localName(), CI_RoleCode)

CI_PresentationFormCode = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_PresentationFormCode'), CodeListValue_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 448, 3))
_Namespace_gmd.addCategoryObject('elementBinding', CI_PresentationFormCode.name().localName(), CI_PresentationFormCode)

DQ_EvaluationMethodTypeCode = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'DQ_EvaluationMethodTypeCode'), CodeListValue_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 481, 3))
_Namespace_gmd.addCategoryObject('elementBinding', DQ_EvaluationMethodTypeCode.name().localName(), DQ_EvaluationMethodTypeCode)

name = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'name'), CodeType, documentation='The gml:name property provides a label or identifier for the object, commonly a descriptive name. An object may have several names, typically assigned by different authorities. gml:name uses the gml:CodeType content model.  The authority for a name is indicated by the value of its (optional) codeSpace attribute.  The name may or may not be unique, as determined by the rules of the organization responsible for the codeSpace.  In common usage there will be one name per authority, so a processing application may select the name from its preferred codeSpace.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 244, 3))
_Namespace_gml.addCategoryObject('elementBinding', name.name().localName(), name)

AbstractGML = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractGML'), AbstractGMLType, abstract=pyxb.binding.datatypes.boolean(1), documentation='The abstract element gml:AbstractGML is "any GML object having identity".   It acts as the head of an XML Schema substitution group, which may include any element which is a GML feature, or other object, with identity.  This is used as a variable in content models in GML core and application schemas.  It is effectively an abstract superclass for all GML objects.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 342, 3))
_Namespace_gml.addCategoryObject('elementBinding', AbstractGML.name().localName(), AbstractGML)

axisAbbrev = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'axisAbbrev'), CodeType, documentation='gml:axisAbbrev is the abbreviation used for this coordinate system axis; this abbreviation is also used to identify the coordinates in the coordinate tuple. The codeSpace attribute may reference a source of more information on a set of standardized abbreviations, or on this abbreviation.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 453, 3))
_Namespace_gml.addCategoryObject('elementBinding', axisAbbrev.name().localName(), axisAbbrev)

anchorDefinition = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'anchorDefinition'), CodeType, documentation='gml:anchorDefinition is a description, possibly including coordinates, of the definition used to anchor the datum to the Earth. Also known as the "origin", especially for engineering and image datums. The codeSpace attribute may be used to reference a source of more detailed on this point or surface, or on a set of such descriptions.\n-\tFor a geodetic datum, this point is also known as the fundamental point, which is traditionally the point where the relationship between geoid and ellipsoid is defined. In some cases, the "fundamental point" may consist of a number of points. In those cases, the parameters defining the geoid/ellipsoid relationship have been averaged for these points, and the averages adopted as the datum definition.\n-\tFor an engineering datum, the anchor definition may be a physical point, or it may be a point with defined coordinates in another CRS.may\n-\tFor an image datum, the anchor definition is usually either the centre of the image or the corner of the image.\n-\tFor a temporal datum, this attribute is not defined. Instead of the anchor definition, a temporal datum carries a separate time origin of type DateTime.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 649, 3))
_Namespace_gml.addCategoryObject('elementBinding', anchorDefinition.name().localName(), anchorDefinition)

semiMajorAxis = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'semiMajorAxis'), MeasureType, documentation='gml:semiMajorAxis specifies the length of the semi-major axis of the ellipsoid, with its units. Uses the MeasureType with the restriction that the unit of measure referenced by uom must be suitable for a length, such as metres or feet.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 754, 3))
_Namespace_gml.addCategoryObject('elementBinding', semiMajorAxis.name().localName(), semiMajorAxis)

secondDefiningParameter = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'secondDefiningParameter'), CTD_ANON, documentation='gml:secondDefiningParameter is a property containing the definition of the second parameter that defines the shape of an ellipsoid. An ellipsoid requires two defining parameters: semi-major axis and inverse flattening or semi-major axis and semi-minor axis. When the reference body is a sphere rather than an ellipsoid, only a single defining parameter is required, namely the radius of the sphere; in that case, the semi-major axis "degenerates" into the radius of the sphere.\nThe inverseFlattening element contains the inverse flattening value of the ellipsoid. This value is a scale factor (or ratio). It uses gml:LengthType with the restriction that the unit of measure referenced by the uom attribute must be suitable for a scale factor, such as percent, permil, or parts-per-million.\nThe semiMinorAxis element contains the length of the semi-minor axis of the ellipsoid. When the isSphere element is included, the ellipsoid is degenerate and is actually a sphere. The sphere is completely defined by the semi-major axis, which is the radius of the sphere.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 760, 3))
_Namespace_gml.addCategoryObject('elementBinding', secondDefiningParameter.name().localName(), secondDefiningParameter)

SecondDefiningParameter = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'SecondDefiningParameter'), CTD_ANON_, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 773, 3))
_Namespace_gml.addCategoryObject('elementBinding', SecondDefiningParameter.name().localName(), SecondDefiningParameter)

EX_Extent = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'EX_Extent'), EX_Extent_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 33, 3))
_Namespace_gmd.addCategoryObject('elementBinding', EX_Extent.name().localName(), EX_Extent)

AbstractEX_GeographicExtent = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'AbstractEX_GeographicExtent'), AbstractEX_GeographicExtent_Type, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 67, 3))
_Namespace_gmd.addCategoryObject('elementBinding', AbstractEX_GeographicExtent.name().localName(), AbstractEX_GeographicExtent)

EX_TemporalExtent = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'EX_TemporalExtent'), EX_TemporalExtent_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 93, 3))
_Namespace_gmd.addCategoryObject('elementBinding', EX_TemporalExtent.name().localName(), EX_TemporalExtent)

EX_VerticalExtent = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'EX_VerticalExtent'), EX_VerticalExtent_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 116, 3))
_Namespace_gmd.addCategoryObject('elementBinding', EX_VerticalExtent.name().localName(), EX_VerticalExtent)

MD_Identifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'MD_Identifier'), MD_Identifier_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 176, 3))
_Namespace_gmd.addCategoryObject('elementBinding', MD_Identifier.name().localName(), MD_Identifier)

CI_Citation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Citation'), CI_Citation_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 197, 3))
_Namespace_gmd.addCategoryObject('elementBinding', CI_Citation.name().localName(), CI_Citation)

CI_Date = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Date'), CI_Date_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 239, 3))
_Namespace_gmd.addCategoryObject('elementBinding', CI_Date.name().localName(), CI_Date)

CI_ResponsibleParty = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_ResponsibleParty'), CI_ResponsibleParty_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 280, 3))
_Namespace_gmd.addCategoryObject('elementBinding', CI_ResponsibleParty.name().localName(), CI_ResponsibleParty)

CI_Contact = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Contact'), CI_Contact_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 307, 3))
_Namespace_gmd.addCategoryObject('elementBinding', CI_Contact.name().localName(), CI_Contact)

CI_Telephone = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Telephone'), CI_Telephone_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 335, 3))
_Namespace_gmd.addCategoryObject('elementBinding', CI_Telephone.name().localName(), CI_Telephone)

CI_Address = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Address'), CI_Address_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 361, 3))
_Namespace_gmd.addCategoryObject('elementBinding', CI_Address.name().localName(), CI_Address)

CI_OnlineResource = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_OnlineResource'), CI_OnlineResource_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 392, 3))
_Namespace_gmd.addCategoryObject('elementBinding', CI_OnlineResource.name().localName(), CI_OnlineResource)

CI_Series = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Series'), CI_Series_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 459, 3))
_Namespace_gmd.addCategoryObject('elementBinding', CI_Series.name().localName(), CI_Series)

AbstractDQ_Result = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'AbstractDQ_Result'), AbstractDQ_Result_Type, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 492, 3))
_Namespace_gmd.addCategoryObject('elementBinding', AbstractDQ_Result.name().localName(), AbstractDQ_Result)

AbstractDQ_Element = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'AbstractDQ_Element'), AbstractDQ_Element_Type, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 502, 3))
_Namespace_gmd.addCategoryObject('elementBinding', AbstractDQ_Element.name().localName(), AbstractDQ_Element)

identifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier'), CodeWithAuthorityType, documentation='Often, a special identifier is assigned to an object by the maintaining authority with the intention that it is used in references to the object For such cases, the codeSpace shall be provided. That identifier is usually unique either globally or within an application domain. gml:identifier is a pre-defined property for such identifiers.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 215, 3))
_Namespace_gml.addCategoryObject('elementBinding', identifier.name().localName(), identifier)

AbstractTimeObject = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractTimeObject'), AbstractTimeObjectType, abstract=pyxb.binding.datatypes.boolean(1), documentation='gml:AbstractTimeObject acts as the head of a substitution group for all temporal primitives and complexes.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 335, 3))
_Namespace_gml.addCategoryObject('elementBinding', AbstractTimeObject.name().localName(), AbstractTimeObject)

axisDirection = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'axisDirection'), CodeWithAuthorityType, documentation='gml:axisDirection is the direction of this coordinate system axis (or in the case of Cartesian projected coordinates, the direction of this coordinate system axis at the origin).\nWithin any set of coordinate system axes, only one of each pair of terms may be used. For earth-fixed CRSs, this direction is often approximate and intended to provide a human interpretable meaning to the axis. When a geodetic datum is used, the precise directions of the axes may therefore vary slightly from this approximate direction.\nThe codeSpace attribute shall reference a source of information specifying the values and meanings of all the allowed string values for this property.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 459, 3))
_Namespace_gml.addCategoryObject('elementBinding', axisDirection.name().localName(), axisDirection)

rangeMeaning = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'rangeMeaning'), CodeWithAuthorityType, documentation='gml:rangeMeaning describes the meaning of axis value range specified by gml:minimumValue and gml:maximumValue. This element shall be omitted when both gml:minimumValue and gml:maximumValue are omitted. This element should be included when gml:minimumValue and/or gml:maximumValue are included. If this element is omitted when the gml:minimumValue and/or gml:maximumValue are included, the meaning is unspecified. The codeSpace attribute shall reference a source of information specifying the values and meanings of all the allowed string values for this property.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 479, 3))
_Namespace_gml.addCategoryObject('elementBinding', rangeMeaning.name().localName(), rangeMeaning)

greenwichLongitude = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'greenwichLongitude'), AngleType, documentation='gml:greenwichLongitude is the longitude of the prime meridian measured from the Greenwich meridian, positive eastward. If the value of the prime meridian "name" is "Greenwich" then the value of greenwichLongitude shall be 0 degrees.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 698, 3))
_Namespace_gml.addCategoryObject('elementBinding', greenwichLongitude.name().localName(), greenwichLongitude)

AbstractDQ_PositionalAccuracy = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'AbstractDQ_PositionalAccuracy'), AbstractDQ_PositionalAccuracy_Type, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 135, 3))
_Namespace_gmd.addCategoryObject('elementBinding', AbstractDQ_PositionalAccuracy.name().localName(), AbstractDQ_PositionalAccuracy)

description = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'description'), StringOrRefType, documentation='The value of this property is a text description of the object. gml:description uses gml:StringOrRefType as its content model, so it may contain a simple text string content, or carry a reference to an external description. The use of gml:description to reference an external description has been deprecated and replaced by the gml:descriptionReference property.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 173, 3))
_Namespace_gml.addCategoryObject('elementBinding', description.name().localName(), description)

descriptionReference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference'), ReferenceType, documentation='The value of this property is a remote text description of the object. The xlink:href attribute of the gml:descriptionReference property references the external description.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 192, 3))
_Namespace_gml.addCategoryObject('elementBinding', descriptionReference.name().localName(), descriptionReference)

domainOfValidity = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'domainOfValidity'), CTD_ANON_2, documentation='The gml:domainOfValidity property implements an association role to an EX_Extent object as encoded in ISO/TS 19139, either referencing or containing the definition of that extent.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 252, 3))
_Namespace_gml.addCategoryObject('elementBinding', domainOfValidity.name().localName(), domainOfValidity)

AbstractTimePrimitive = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractTimePrimitive'), AbstractTimePrimitiveType, abstract=pyxb.binding.datatypes.boolean(1), documentation='gml:AbstractTimePrimitive acts as the head of a substitution group for geometric and topological temporal primitives.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 270, 3))
_Namespace_gml.addCategoryObject('elementBinding', AbstractTimePrimitive.name().localName(), AbstractTimePrimitive)

Definition = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'Definition'), DefinitionType, documentation='The basic gml:Definition element specifies a definition, which can be included in or referenced by a dictionary. \nThe content model for a generic definition is a derivation from gml:AbstractGMLType.  \nThe gml:description property element shall hold the definition if this can be captured in a simple text string, or the gml:descriptionReference property element may carry a link to a description elsewhere.\nThe gml:identifier element shall provide one identifier identifying this definition. The identifier shall be unique within the dictionaries using this definition. \nThe gml:name elements shall provide zero or more terms and synonyms for which this is the definition.\nThe gml:remarks element shall be used to hold additional textual information that is not conceptually part of the definition but is useful in understanding the definition.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 358, 3))
_Namespace_gml.addCategoryObject('elementBinding', Definition.name().localName(), Definition)

ellipsoidalCS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'ellipsoidalCS'), EllipsoidalCSPropertyType, documentation='gml:ellipsoidalCS is an association role to the ellipsoidal coordinate system used by this CRS.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 375, 3))
_Namespace_gml.addCategoryObject('elementBinding', ellipsoidalCS.name().localName(), ellipsoidalCS)

axis = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'axis'), CoordinateSystemAxisPropertyType, documentation='The gml:axis property is an association role (ordered sequence) to the coordinate system axes included in this coordinate system. The coordinate values in a coordinate tuple shall be recorded in the order in which the coordinate system axes associations are recorded, whenever those coordinates use a coordinate reference system that uses this coordinate system. The gml:AggregationAttributeGroup should be used to specify that the axis objects are ordered.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 415, 3))
_Namespace_gml.addCategoryObject('elementBinding', axis.name().localName(), axis)

cartesianCS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'cartesianCS'), CartesianCSPropertyType, documentation='gml:cartesianCS is an association role to the Cartesian coordinate system used by this CRS.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 543, 3))
_Namespace_gml.addCategoryObject('elementBinding', cartesianCS.name().localName(), cartesianCS)

sphericalCS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'sphericalCS'), SphericalCSPropertyType, documentation='gml:sphericalCS is an association role to the spherical coordinate system used by this CRS.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 572, 3))
_Namespace_gml.addCategoryObject('elementBinding', sphericalCS.name().localName(), sphericalCS)

geodeticDatum = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'geodeticDatum'), GeodeticDatumPropertyType, documentation='gml:geodeticDatum is an association role to the geodetic datum used by this CRS.\n', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 601, 3))
_Namespace_gml.addCategoryObject('elementBinding', geodeticDatum.name().localName(), geodeticDatum)

primeMeridian = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'primeMeridian'), PrimeMeridianPropertyType, documentation='gml:primeMeridian is an association role to the prime meridian used by this geodetic datum.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 665, 3))
_Namespace_gml.addCategoryObject('elementBinding', primeMeridian.name().localName(), primeMeridian)

ellipsoid = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'ellipsoid'), EllipsoidPropertyType, documentation='gml:ellipsoid is an association role to the ellipsoid used by this geodetic datum.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 721, 3))
_Namespace_gml.addCategoryObject('elementBinding', ellipsoid.name().localName(), ellipsoid)

conversion = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'conversion'), GeneralConversionPropertyType, documentation='gml:conversion is an association role to the coordinate conversion used to define the derived CRS.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 837, 3))
_Namespace_gml.addCategoryObject('elementBinding', conversion.name().localName(), conversion)

coordinateOperationAccuracy = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'coordinateOperationAccuracy'), CTD_ANON_3, documentation='gml:coordinateOperationAccuracy is an association role to a DQ_PositionalAccuracy object as encoded in ISO/TS 19139, either referencing or containing the definition of that positional accuracy. That object contains an estimate of the impact of this coordinate operation on point accuracy. That is, it gives position error estimates for the target coordinates of this coordinate operation, assuming no errors in the source coordinates.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 902, 3))
_Namespace_gml.addCategoryObject('elementBinding', coordinateOperationAccuracy.name().localName(), coordinateOperationAccuracy)

sourceCRS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'sourceCRS'), CRSPropertyType, documentation='gml:sourceCRS is an association role to the source CRS (coordinate reference system) of this coordinate operation.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 924, 3))
_Namespace_gml.addCategoryObject('elementBinding', sourceCRS.name().localName(), sourceCRS)

targetCRS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'targetCRS'), CRSPropertyType, documentation='gml:targetCRS is an association role to the target CRS (coordinate reference system) of this coordinate operation.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 940, 3))
_Namespace_gml.addCategoryObject('elementBinding', targetCRS.name().localName(), targetCRS)

baseGeodeticCRS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'baseGeodeticCRS'), GeodeticCRSPropertyType, documentation='gml:baseGeodeticCRS is an association role to the geodetic coordinate reference system used by this projected CRS.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 971, 3))
_Namespace_gml.addCategoryObject('elementBinding', baseGeodeticCRS.name().localName(), baseGeodeticCRS)

verticalCS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'verticalCS'), VerticalCSPropertyType, documentation='gml:verticalCS is an association role to the vertical coordinate system used by this CRS.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 1013, 3))
_Namespace_gml.addCategoryObject('elementBinding', verticalCS.name().localName(), verticalCS)

verticalDatum = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'verticalDatum'), VerticalDatumPropertyType, documentation='gml:verticalDatum is an association role to the vertical datum used by this CRS.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 1042, 3))
_Namespace_gml.addCategoryObject('elementBinding', verticalDatum.name().localName(), verticalDatum)

AbstractCRS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractCRS'), AbstractCRSType, abstract=pyxb.binding.datatypes.boolean(1), documentation='gml:AbstractCRS specifies a coordinate reference system which is usually single but may be compound. This abstract complex type shall not be used, extended, or restricted, in a GML Application Schema, to define a concrete subtype with a meaning equivalent to a concrete subtype specified in this document.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 351, 3))
_Namespace_gml.addCategoryObject('elementBinding', AbstractCRS.name().localName(), AbstractCRS)

CoordinateSystemAxis = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'CoordinateSystemAxis'), CoordinateSystemAxisType, documentation='gml:CoordinateSystemAxis is a definition of a coordinate system axis.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 431, 3))
_Namespace_gml.addCategoryObject('elementBinding', CoordinateSystemAxis.name().localName(), CoordinateSystemAxis)

AbstractCoordinateSystem = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractCoordinateSystem'), AbstractCoordinateSystemType, abstract=pyxb.binding.datatypes.boolean(1), documentation='gml:AbstractCoordinateSystem is a coordinate system (CS) is the non-repeating sequence of coordinate system axes that spans a given coordinate space. A CS is derived from a set of mathematical rules for specifying how coordinates in a given space are to be assigned to points. The coordinate values in a coordinate tuple shall be recorded in the order in which the coordinate system axes associations are recorded. This abstract complex type shall not be used, extended, or restricted, in an Application Schema, to define a concrete subtype with a meaning equivalent to a concrete subtype specified in this document.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 535, 3))
_Namespace_gml.addCategoryObject('elementBinding', AbstractCoordinateSystem.name().localName(), AbstractCoordinateSystem)

PrimeMeridian = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'PrimeMeridian'), PrimeMeridianType, documentation='A gml:PrimeMeridian defines the origin from which longitude values are determined. The default value for the prime meridian gml:identifier value is "Greenwich".', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 681, 3))
_Namespace_gml.addCategoryObject('elementBinding', PrimeMeridian.name().localName(), PrimeMeridian)

Ellipsoid = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'Ellipsoid'), EllipsoidType, documentation='A gml:Ellipsoid is a geometric figure that may be used to describe the approximate shape of the earth. In mathematical terms, it is a surface formed by the rotation of an ellipse about its minor axis.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 737, 3))
_Namespace_gml.addCategoryObject('elementBinding', Ellipsoid.name().localName(), Ellipsoid)

AbstractDatum = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractDatum'), AbstractDatumType, abstract=pyxb.binding.datatypes.boolean(1), documentation='A gml:AbstractDatum specifies the relationship of a coordinate system to the earth, thus creating a coordinate reference system. A datum uses a parameter or set of parameters that determine the location of the origin of the coordinate reference system. Each datum subtype may be associated with only specific types of coordinate systems. This abstract complex type shall not be used, extended, or restricted, in a GML Application Schema, to define a concrete subtype with a meaning equivalent to a concrete subtype specified in this document.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 792, 3))
_Namespace_gml.addCategoryObject('elementBinding', AbstractDatum.name().localName(), AbstractDatum)

AbstractSingleCRS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractSingleCRS'), AbstractCRSType, abstract=pyxb.binding.datatypes.boolean(1), documentation='gml:AbstractSingleCRS implements a coordinate reference system consisting of one coordinate system and one datum (as opposed to a Compound CRS).', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 799, 3))
_Namespace_gml.addCategoryObject('elementBinding', AbstractSingleCRS.name().localName(), AbstractSingleCRS)

AbstractOperation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractOperation'), AbstractCoordinateOperationType, abstract=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 946, 3))
_Namespace_gml.addCategoryObject('elementBinding', AbstractOperation.name().localName(), AbstractOperation)

AbstractSingleOperation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractSingleOperation'), AbstractCoordinateOperationType, abstract=pyxb.binding.datatypes.boolean(1), documentation='gml:AbstractSingleOperation is a single (not concatenated) coordinate operation.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 954, 3))
_Namespace_gml.addCategoryObject('elementBinding', AbstractSingleOperation.name().localName(), AbstractSingleOperation)

AbstractCoordinateOperation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractCoordinateOperation'), AbstractCoordinateOperationType, abstract=pyxb.binding.datatypes.boolean(1), documentation='gml:AbstractCoordinateOperation is a mathematical operation on coordinates that transforms or converts coordinates to another coordinate reference system. Many but not all coordinate operations (from CRS A to CRS B) also uniquely define the inverse operation (from CRS B to CRS A). In some cases, the operation method algorithm for the inverse operation is the same as for the forward algorithm, but the signs of some operation parameter values shall be reversed. In other cases, different algorithms are required for the forward and inverse operations, but the same operation parameter values are used. If (some) entirely different parameter values are needed, a different coordinate operation shall be defined.\nThe optional coordinateOperationAccuracy property elements provide estimates of the impact of this coordinate operation on point position accuracy.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 962, 3))
_Namespace_gml.addCategoryObject('elementBinding', AbstractCoordinateOperation.name().localName(), AbstractCoordinateOperation)

GeodeticCRS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'GeodeticCRS'), GeodeticCRSType, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 27, 3))
_Namespace_gml.addCategoryObject('elementBinding', GeodeticCRS.name().localName(), GeodeticCRS)

EllipsoidalCS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'EllipsoidalCS'), EllipsoidalCSType, documentation='gml:EllipsoidalCS is a two- or three-dimensional coordinate system in which position is specified by geodetic latitude, geodetic longitude, and (in the three-dimensional case) ellipsoidal height. An EllipsoidalCS shall have two or three gml:axis property elements; the number of associations shall equal the dimension of the CS.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 391, 3))
_Namespace_gml.addCategoryObject('elementBinding', EllipsoidalCS.name().localName(), EllipsoidalCS)

CartesianCS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'CartesianCS'), CartesianCSType, documentation='gml:CartesianCS is a 1-, 2-, or 3-dimensional coordinate system. In the 1-dimensional case, it contains a single straight coordinate axis. In the 2- and 3-dimensional cases gives the position of points relative to orthogonal straight axes. In the multi-dimensional case, all axes shall have the same length unit of measure. A CartesianCS shall have one, two, or three gml:axis property elements.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 559, 3))
_Namespace_gml.addCategoryObject('elementBinding', CartesianCS.name().localName(), CartesianCS)

SphericalCS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'SphericalCS'), SphericalCSType, documentation='gml:SphericalCS is a three-dimensional coordinate system with one distance measured from the origin and two angular coordinates. A SphericalCS shall have three gml:axis property elements.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 588, 3))
_Namespace_gml.addCategoryObject('elementBinding', SphericalCS.name().localName(), SphericalCS)

GeodeticDatum = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'GeodeticDatum'), GeodeticDatumType, documentation='gml:GeodeticDatum is a geodetic datum defines the precise location and orientation in 3-dimensional space of a defined ellipsoid (or sphere), or of a Cartesian coordinate system centered in this ellipsoid (or sphere).', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 618, 3))
_Namespace_gml.addCategoryObject('elementBinding', GeodeticDatum.name().localName(), GeodeticDatum)

AbstractGeneralConversion = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractGeneralConversion'), AbstractGeneralConversionType, abstract=pyxb.binding.datatypes.boolean(1), documentation='gm:AbstractGeneralConversion is an abstract operation on coordinates that does not include any change of datum. The best-known example of a coordinate conversion is a map projection. The parameters describing coordinate conversions are defined rather than empirically derived. Note that some conversions have no parameters. The operationVersion, sourceCRS, and targetCRS elements are omitted in a coordinate conversion.\nThis abstract complex type is expected to be extended for well-known operation methods with many Conversion instances, in GML Application Schemas that define operation-method-specialized element names and contents. This conversion uses an operation method, usually with associated parameter values. However, operation methods and parameter values are directly associated with concrete subtypes, not with this abstract type. All concrete types derived from this type shall extend this type to include a "usesMethod" element that references the "OperationMethod" element. Similarly, all concrete types derived from this type shall extend this type to include zero or more elements each named "uses...Value" that each use the type of an element substitutable for the "AbstractGeneralParameterValue" element.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 853, 3))
_Namespace_gml.addCategoryObject('elementBinding', AbstractGeneralConversion.name().localName(), AbstractGeneralConversion)

AbstractGeneralDerivedCRS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractGeneralDerivedCRS'), AbstractGeneralDerivedCRSType, abstract=pyxb.binding.datatypes.boolean(1), documentation='gml:AbstractGeneralDerivedCRS is a coordinate reference system that is defined by its coordinate conversion from another coordinate reference system. This abstract complex type shall not be used, extended, or restricted, in a GML Application Schema, to define a concrete subtype with a meaning equivalent to a concrete subtype specified in this document.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 987, 3))
_Namespace_gml.addCategoryObject('elementBinding', AbstractGeneralDerivedCRS.name().localName(), AbstractGeneralDerivedCRS)

VerticalCRS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'VerticalCRS'), VerticalCRSType, documentation='gml:VerticalCRS is a 1D coordinate reference system used for recording heights or depths. Vertical CRSs make use of the direction of gravity to define the concept of height or depth, but the relationship with gravity may not be straightforward. By implication, ellipsoidal heights (h) cannot be captured in a vertical coordinate reference system. Ellipsoidal heights cannot exist independently, but only as an inseparable part of a 3D coordinate tuple defined in a geographic 3D coordinate reference system.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 995, 3))
_Namespace_gml.addCategoryObject('elementBinding', VerticalCRS.name().localName(), VerticalCRS)

VerticalCS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'VerticalCS'), VerticalCSType, documentation="gml:VerticalCS is a one-dimensional coordinate system used to record the heights or depths of points. Such a coordinate system is usually dependent on the Earth's gravity field, perhaps loosely as when atmospheric pressure is the basis for the vertical coordinate system axis. A VerticalCS shall have one gml:axis property element.", location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 1029, 3))
_Namespace_gml.addCategoryObject('elementBinding', VerticalCS.name().localName(), VerticalCS)

VerticalDatum = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'VerticalDatum'), VerticalDatumType, documentation='gml:VerticalDatum is a textual description and/or a set of parameters identifying a particular reference level surface used as a zero-height surface, including its position with respect to the Earth for any of the height types recognized by this International Standard.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 1058, 3))
_Namespace_gml.addCategoryObject('elementBinding', VerticalDatum.name().localName(), VerticalDatum)

ProjectedCRS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'ProjectedCRS'), ProjectedCRSType, documentation='gml:ProjectedCRS is a 2D coordinate reference system used to approximate the shape of the earth on a planar surface, but in such a way that the distortion that is inherent to the approximation is carefully controlled and known. Distortion correction is commonly applied to calculated bearings and distances to produce values that are a close match to actual field values.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 806, 3))
_Namespace_gml.addCategoryObject('elementBinding', ProjectedCRS.name().localName(), ProjectedCRS)



AbstractGMLType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'description'), StringOrRefType, scope=AbstractGMLType, documentation='The value of this property is a text description of the object. gml:description uses gml:StringOrRefType as its content model, so it may contain a simple text string content, or carry a reference to an external description. The use of gml:description to reference an external description has been deprecated and replaced by the gml:descriptionReference property.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 173, 3)))

AbstractGMLType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference'), ReferenceType, scope=AbstractGMLType, documentation='The value of this property is a remote text description of the object. The xlink:href attribute of the gml:descriptionReference property references the external description.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 192, 3)))

AbstractGMLType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier'), CodeWithAuthorityType, scope=AbstractGMLType, documentation='Often, a special identifier is assigned to an object by the maintaining authority with the intention that it is used in references to the object For such cases, the codeSpace shall be provided. That identifier is usually unique either globally or within an application domain. gml:identifier is a pre-defined property for such identifiers.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 215, 3)))

AbstractGMLType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'name'), CodeType, scope=AbstractGMLType, documentation='The gml:name property provides a label or identifier for the object, commonly a descriptive name. An object may have several names, typically assigned by different authorities. gml:name uses the gml:CodeType content model.  The authority for a name is indicated by the value of its (optional) codeSpace attribute.  The name may or may not be unique, as determined by the rules of the organization responsible for the codeSpace.  In common usage there will be one name per authority, so a processing application may select the name from its preferred codeSpace.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 244, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 106, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 107, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 108, 9))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 109, 9))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AbstractGMLType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 106, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AbstractGMLType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 107, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AbstractGMLType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 108, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AbstractGMLType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 109, 9))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AbstractGMLType._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'SecondDefiningParameter'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 773, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'SecondDefiningParameter')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 768, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'inverseFlattening'), MeasureType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 776, 12)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'semiMinorAxis'), LengthType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 777, 12)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'isSphere'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 778, 12), unicode_default='true'))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'inverseFlattening')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 776, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'semiMinorAxis')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 777, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'isSphere')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 778, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_2()




EX_Extent_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'description'), CharacterString_PropertyType, scope=EX_Extent_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 42, 15)))

EX_Extent_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'geographicElement'), EX_GeographicExtent_PropertyType, scope=EX_Extent_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 43, 15)))

EX_Extent_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'temporalElement'), EX_TemporalExtent_PropertyType, scope=EX_Extent_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 46, 15)))

EX_Extent_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'verticalElement'), EX_VerticalExtent_PropertyType, scope=EX_Extent_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 48, 15)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 42, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 43, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 46, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 48, 15))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(EX_Extent_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'description')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 42, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(EX_Extent_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'geographicElement')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 43, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(EX_Extent_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'temporalElement')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 46, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(EX_Extent_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'verticalElement')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 48, 15))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
EX_Extent_Type._Automaton = _BuildAutomaton_3()




AbstractEX_GeographicExtent_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'extentTypeCode'), Boolean_PropertyType, scope=AbstractEX_GeographicExtent_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 77, 15)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 77, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AbstractEX_GeographicExtent_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'extentTypeCode')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 77, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AbstractEX_GeographicExtent_Type._Automaton = _BuildAutomaton_4()




EX_TemporalExtent_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'extent'), TM_Primitive_PropertyType, scope=EX_TemporalExtent_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 102, 15)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EX_TemporalExtent_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'extent')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 102, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
EX_TemporalExtent_Type._Automaton = _BuildAutomaton_5()




EX_VerticalExtent_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'minimumValue'), Real_PropertyType, scope=EX_VerticalExtent_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 125, 15)))

EX_VerticalExtent_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'maximumValue'), Real_PropertyType, scope=EX_VerticalExtent_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 126, 15)))

EX_VerticalExtent_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'verticalCRS'), SC_CRS_PropertyType, scope=EX_VerticalExtent_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 127, 15)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EX_VerticalExtent_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'minimumValue')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 125, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EX_VerticalExtent_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'maximumValue')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 126, 15))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EX_VerticalExtent_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'verticalCRS')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 127, 15))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
EX_VerticalExtent_Type._Automaton = _BuildAutomaton_6()




AbstractDQ_Element_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'nameOfMeasure'), CharacterString_PropertyType, scope=AbstractDQ_Element_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 150, 15)))

AbstractDQ_Element_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'measureIdentification'), MD_Identifier_PropertyType, scope=AbstractDQ_Element_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 152, 15)))

AbstractDQ_Element_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'measureDescription'), CharacterString_PropertyType, scope=AbstractDQ_Element_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 154, 15)))

AbstractDQ_Element_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'evaluationMethodType'), DQ_EvaluationMethodTypeCode_PropertyType, scope=AbstractDQ_Element_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 155, 15)))

AbstractDQ_Element_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'evaluationMethodDescription'), CharacterString_PropertyType, scope=AbstractDQ_Element_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 157, 15)))

AbstractDQ_Element_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'evaluationProcedure'), CI_Citation_PropertyType, scope=AbstractDQ_Element_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 159, 15)))

AbstractDQ_Element_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'dateTime'), DateTime_PropertyType, scope=AbstractDQ_Element_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 160, 15)))

AbstractDQ_Element_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'result'), DQ_Result_PropertyType, scope=AbstractDQ_Element_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 162, 15)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 150, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 152, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 154, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 155, 15))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 157, 15))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 159, 15))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 160, 15))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=1, max=2, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 162, 15))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractDQ_Element_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'nameOfMeasure')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 150, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractDQ_Element_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'measureIdentification')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 152, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractDQ_Element_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'measureDescription')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 154, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractDQ_Element_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'evaluationMethodType')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 155, 15))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractDQ_Element_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'evaluationMethodDescription')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 157, 15))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractDQ_Element_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'evaluationProcedure')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 159, 15))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractDQ_Element_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'dateTime')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 160, 15))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(AbstractDQ_Element_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'result')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 162, 15))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AbstractDQ_Element_Type._Automaton = _BuildAutomaton_7()




MD_Identifier_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'authority'), CI_Citation_PropertyType, scope=MD_Identifier_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 182, 15)))

MD_Identifier_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'code'), CharacterString_PropertyType, scope=MD_Identifier_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 183, 15)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 182, 15))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MD_Identifier_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'authority')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 182, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MD_Identifier_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'code')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 183, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MD_Identifier_Type._Automaton = _BuildAutomaton_8()




CI_Citation_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'title'), CharacterString_PropertyType, scope=CI_Citation_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 206, 15)))

CI_Citation_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'alternateTitle'), CharacterString_PropertyType, scope=CI_Citation_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 207, 15)))

CI_Citation_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'date'), CI_Date_PropertyType, scope=CI_Citation_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 209, 15)))

CI_Citation_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'edition'), CharacterString_PropertyType, scope=CI_Citation_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 210, 15)))

CI_Citation_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'editionDate'), Date_PropertyType, scope=CI_Citation_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 211, 15)))

CI_Citation_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'identifier'), MD_Identifier_PropertyType, scope=CI_Citation_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 212, 15)))

CI_Citation_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'citedResponsibleParty'), CI_ResponsibleParty_PropertyType, scope=CI_Citation_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 214, 15)))

CI_Citation_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'presentationForm'), CI_PresentationFormCode_PropertyType, scope=CI_Citation_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 217, 15)))

CI_Citation_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'series'), CI_Series_PropertyType, scope=CI_Citation_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 220, 15)))

CI_Citation_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'otherCitationDetails'), CharacterString_PropertyType, scope=CI_Citation_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 221, 15)))

CI_Citation_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'collectiveTitle'), CharacterString_PropertyType, scope=CI_Citation_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 223, 15)))

CI_Citation_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'ISBN'), CharacterString_PropertyType, scope=CI_Citation_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 224, 15)))

CI_Citation_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'ISSN'), CharacterString_PropertyType, scope=CI_Citation_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 225, 15)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 207, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 210, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 211, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 212, 15))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 214, 15))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 217, 15))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 220, 15))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 221, 15))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 223, 15))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 224, 15))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 225, 15))
    counters.add(cc_10)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CI_Citation_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'title')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 206, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CI_Citation_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'alternateTitle')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 207, 15))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CI_Citation_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'date')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 209, 15))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CI_Citation_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'edition')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 210, 15))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CI_Citation_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'editionDate')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 211, 15))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CI_Citation_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'identifier')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 212, 15))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CI_Citation_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'citedResponsibleParty')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 214, 15))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CI_Citation_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'presentationForm')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 217, 15))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CI_Citation_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'series')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 220, 15))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CI_Citation_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'otherCitationDetails')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 221, 15))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CI_Citation_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'collectiveTitle')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 223, 15))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CI_Citation_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'ISBN')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 224, 15))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CI_Citation_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'ISSN')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 225, 15))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CI_Citation_Type._Automaton = _BuildAutomaton_9()




CI_Date_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'date'), Date_PropertyType, scope=CI_Date_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 245, 15)))

CI_Date_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'dateType'), CI_DateTypeCode_PropertyType, scope=CI_Date_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 246, 15)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CI_Date_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'date')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 245, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CI_Date_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'dateType')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 246, 15))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CI_Date_Type._Automaton = _BuildAutomaton_10()




CI_ResponsibleParty_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'individualName'), CharacterString_PropertyType, scope=CI_ResponsibleParty_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 289, 15)))

CI_ResponsibleParty_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'organisationName'), CharacterString_PropertyType, scope=CI_ResponsibleParty_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 290, 15)))

CI_ResponsibleParty_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'positionName'), CharacterString_PropertyType, scope=CI_ResponsibleParty_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 291, 15)))

CI_ResponsibleParty_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'contactInfo'), CI_Contact_PropertyType, scope=CI_ResponsibleParty_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 292, 15)))

CI_ResponsibleParty_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'role'), CI_RoleCode_PropertyType, scope=CI_ResponsibleParty_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 293, 15)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 289, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 290, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 291, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 292, 15))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CI_ResponsibleParty_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'individualName')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 289, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CI_ResponsibleParty_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'organisationName')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 290, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CI_ResponsibleParty_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'positionName')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 291, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CI_ResponsibleParty_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'contactInfo')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 292, 15))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CI_ResponsibleParty_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'role')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 293, 15))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CI_ResponsibleParty_Type._Automaton = _BuildAutomaton_11()




CI_Contact_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'phone'), CI_Telephone_PropertyType, scope=CI_Contact_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 316, 15)))

CI_Contact_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'address'), CI_Address_PropertyType, scope=CI_Contact_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 317, 15)))

CI_Contact_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'onlineResource'), CI_OnlineResource_PropertyType, scope=CI_Contact_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 318, 15)))

CI_Contact_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'hoursOfService'), CharacterString_PropertyType, scope=CI_Contact_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 319, 15)))

CI_Contact_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'contactInstructions'), CharacterString_PropertyType, scope=CI_Contact_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 320, 15)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 316, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 317, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 318, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 319, 15))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 320, 15))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CI_Contact_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'phone')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 316, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CI_Contact_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'address')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 317, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CI_Contact_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'onlineResource')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 318, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CI_Contact_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'hoursOfService')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 319, 15))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CI_Contact_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'contactInstructions')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 320, 15))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CI_Contact_Type._Automaton = _BuildAutomaton_12()




CI_Telephone_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'voice'), CharacterString_PropertyType, scope=CI_Telephone_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 344, 15)))

CI_Telephone_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'facsimile'), CharacterString_PropertyType, scope=CI_Telephone_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 346, 15)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 344, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 346, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CI_Telephone_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'voice')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 344, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CI_Telephone_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'facsimile')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 346, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CI_Telephone_Type._Automaton = _BuildAutomaton_13()




CI_Address_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'deliveryPoint'), CharacterString_PropertyType, scope=CI_Address_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 370, 15)))

CI_Address_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'city'), CharacterString_PropertyType, scope=CI_Address_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 372, 15)))

CI_Address_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'administrativeArea'), CharacterString_PropertyType, scope=CI_Address_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 373, 15)))

CI_Address_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'postalCode'), CharacterString_PropertyType, scope=CI_Address_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 374, 15)))

CI_Address_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'country'), CharacterString_PropertyType, scope=CI_Address_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 375, 15)))

CI_Address_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'electronicMailAddress'), CharacterString_PropertyType, scope=CI_Address_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 376, 15)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 370, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 372, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 373, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 374, 15))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 375, 15))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 376, 15))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CI_Address_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'deliveryPoint')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 370, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CI_Address_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'city')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 372, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CI_Address_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'administrativeArea')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 373, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CI_Address_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'postalCode')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 374, 15))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CI_Address_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'country')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 375, 15))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CI_Address_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'electronicMailAddress')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 376, 15))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CI_Address_Type._Automaton = _BuildAutomaton_14()




CI_OnlineResource_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'linkage'), URL_PropertyType, scope=CI_OnlineResource_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 401, 15)))

CI_OnlineResource_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'protocol'), CharacterString_PropertyType, scope=CI_OnlineResource_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 402, 15)))

CI_OnlineResource_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'applicationProfile'), CharacterString_PropertyType, scope=CI_OnlineResource_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 403, 15)))

CI_OnlineResource_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'name'), CharacterString_PropertyType, scope=CI_OnlineResource_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 404, 15)))

CI_OnlineResource_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'description'), CharacterString_PropertyType, scope=CI_OnlineResource_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 405, 15)))

CI_OnlineResource_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'function'), CI_OnLineFunctionCode_PropertyType, scope=CI_OnlineResource_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 406, 15)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 402, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 403, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 404, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 405, 15))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 406, 15))
    counters.add(cc_4)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CI_OnlineResource_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'linkage')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 401, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CI_OnlineResource_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'protocol')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 402, 15))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CI_OnlineResource_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'applicationProfile')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 403, 15))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CI_OnlineResource_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'name')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 404, 15))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CI_OnlineResource_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'description')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 405, 15))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CI_OnlineResource_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'function')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 406, 15))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CI_OnlineResource_Type._Automaton = _BuildAutomaton_15()




CI_Series_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'name'), CharacterString_PropertyType, scope=CI_Series_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 465, 15)))

CI_Series_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'issueIdentification'), CharacterString_PropertyType, scope=CI_Series_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 466, 15)))

CI_Series_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'page'), CharacterString_PropertyType, scope=CI_Series_Type, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 468, 15)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 465, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 466, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 468, 15))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CI_Series_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'name')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 465, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CI_Series_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'issueIdentification')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 466, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CI_Series_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'page')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 468, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CI_Series_Type._Automaton = _BuildAutomaton_16()




def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DefinitionBaseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DefinitionBaseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DefinitionBaseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 88, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DefinitionBaseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DefinitionBaseType._Automaton = _BuildAutomaton_17()




def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 106, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 107, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 108, 9))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 109, 9))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AbstractTimeObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 106, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AbstractTimeObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 107, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AbstractTimeObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 108, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AbstractTimeObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 109, 9))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AbstractTimeObjectType._Automaton = _BuildAutomaton_18()




CharacterString_PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gco, 'CharacterString'), pyxb.binding.datatypes.string, scope=CharacterString_PropertyType, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 52, 3)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 46, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CharacterString_PropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gco, 'CharacterString')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 47, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CharacterString_PropertyType._Automaton = _BuildAutomaton_19()




Boolean_PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gco, 'Boolean'), pyxb.binding.datatypes.boolean, scope=Boolean_PropertyType, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 63, 3)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 57, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Boolean_PropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gco, 'Boolean')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 58, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Boolean_PropertyType._Automaton = _BuildAutomaton_20()




Real_PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gco, 'Real'), pyxb.binding.datatypes.double, scope=Real_PropertyType, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 79, 3)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 73, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Real_PropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gco, 'Real')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 74, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Real_PropertyType._Automaton = _BuildAutomaton_21()




Date_PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gco, 'Date'), Date_Type, nillable=pyxb.binding.datatypes.boolean(1), scope=Date_PropertyType, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 91, 3)))

Date_PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gco, 'DateTime'), pyxb.binding.datatypes.dateTime, scope=Date_PropertyType, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 103, 3)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 84, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Date_PropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gco, 'Date')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 85, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Date_PropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gco, 'DateTime')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 86, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Date_PropertyType._Automaton = _BuildAutomaton_22()




DateTime_PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gco, 'DateTime'), pyxb.binding.datatypes.dateTime, scope=DateTime_PropertyType, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 103, 3)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 120, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DateTime_PropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gco, 'DateTime')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gco/gco.xsd', 121, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DateTime_PropertyType._Automaton = _BuildAutomaton_23()




EX_GeographicExtent_PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'AbstractEX_GeographicExtent'), AbstractEX_GeographicExtent_Type, abstract=pyxb.binding.datatypes.boolean(1), scope=EX_GeographicExtent_PropertyType, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 67, 3)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 60, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(EX_GeographicExtent_PropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'AbstractEX_GeographicExtent')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 61, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
EX_GeographicExtent_PropertyType._Automaton = _BuildAutomaton_24()




EX_TemporalExtent_PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'EX_TemporalExtent'), EX_TemporalExtent_Type, scope=EX_TemporalExtent_PropertyType, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 93, 3)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 86, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(EX_TemporalExtent_PropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'EX_TemporalExtent')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 87, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
EX_TemporalExtent_PropertyType._Automaton = _BuildAutomaton_25()




EX_VerticalExtent_PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'EX_VerticalExtent'), EX_VerticalExtent_Type, scope=EX_VerticalExtent_PropertyType, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 116, 3)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 109, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(EX_VerticalExtent_PropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'EX_VerticalExtent')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 110, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
EX_VerticalExtent_PropertyType._Automaton = _BuildAutomaton_26()




def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 150, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 152, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 154, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 155, 15))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 157, 15))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 159, 15))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 160, 15))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=1, max=2, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 162, 15))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractDQ_PositionalAccuracy_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'nameOfMeasure')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 150, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractDQ_PositionalAccuracy_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'measureIdentification')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 152, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractDQ_PositionalAccuracy_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'measureDescription')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 154, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractDQ_PositionalAccuracy_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'evaluationMethodType')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 155, 15))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractDQ_PositionalAccuracy_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'evaluationMethodDescription')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 157, 15))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractDQ_PositionalAccuracy_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'evaluationProcedure')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 159, 15))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractDQ_PositionalAccuracy_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'dateTime')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 160, 15))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(AbstractDQ_PositionalAccuracy_Type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'result')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 162, 15))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AbstractDQ_PositionalAccuracy_Type._Automaton = _BuildAutomaton_27()




MD_Identifier_PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'MD_Identifier'), MD_Identifier_Type, scope=MD_Identifier_PropertyType, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 176, 3)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 169, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MD_Identifier_PropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'MD_Identifier')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 170, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MD_Identifier_PropertyType._Automaton = _BuildAutomaton_28()




CI_Citation_PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Citation'), CI_Citation_Type, scope=CI_Citation_PropertyType, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 197, 3)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 190, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CI_Citation_PropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Citation')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 191, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CI_Citation_PropertyType._Automaton = _BuildAutomaton_29()




CI_Date_PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Date'), CI_Date_Type, scope=CI_Date_PropertyType, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 239, 3)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 232, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CI_Date_PropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Date')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 233, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CI_Date_PropertyType._Automaton = _BuildAutomaton_30()




CI_DateTypeCode_PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_DateTypeCode'), CodeListValue_Type, scope=CI_DateTypeCode_PropertyType, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 267, 3)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 261, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CI_DateTypeCode_PropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_DateTypeCode')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 262, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CI_DateTypeCode_PropertyType._Automaton = _BuildAutomaton_31()




CI_ResponsibleParty_PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_ResponsibleParty'), CI_ResponsibleParty_Type, scope=CI_ResponsibleParty_PropertyType, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 280, 3)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 273, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CI_ResponsibleParty_PropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_ResponsibleParty')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 274, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CI_ResponsibleParty_PropertyType._Automaton = _BuildAutomaton_32()




CI_Contact_PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Contact'), CI_Contact_Type, scope=CI_Contact_PropertyType, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 307, 3)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 300, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CI_Contact_PropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Contact')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 301, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CI_Contact_PropertyType._Automaton = _BuildAutomaton_33()




CI_Telephone_PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Telephone'), CI_Telephone_Type, scope=CI_Telephone_PropertyType, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 335, 3)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 328, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CI_Telephone_PropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Telephone')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 329, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CI_Telephone_PropertyType._Automaton = _BuildAutomaton_34()




CI_Address_PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Address'), CI_Address_Type, scope=CI_Address_PropertyType, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 361, 3)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 354, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CI_Address_PropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Address')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 355, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CI_Address_PropertyType._Automaton = _BuildAutomaton_35()




CI_OnlineResource_PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_OnlineResource'), CI_OnlineResource_Type, scope=CI_OnlineResource_PropertyType, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 392, 3)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 385, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CI_OnlineResource_PropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_OnlineResource')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 386, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CI_OnlineResource_PropertyType._Automaton = _BuildAutomaton_36()




URL_PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'URL'), pyxb.binding.datatypes.anyURI, scope=URL_PropertyType, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 419, 3)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 413, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(URL_PropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'URL')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 414, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
URL_PropertyType._Automaton = _BuildAutomaton_37()




CI_OnLineFunctionCode_PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_OnLineFunctionCode'), CodeListValue_Type, scope=CI_OnLineFunctionCode_PropertyType, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 428, 3)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 422, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CI_OnLineFunctionCode_PropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_OnLineFunctionCode')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 423, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CI_OnLineFunctionCode_PropertyType._Automaton = _BuildAutomaton_38()




CI_RoleCode_PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_RoleCode'), CodeListValue_Type, scope=CI_RoleCode_PropertyType, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 438, 3)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 432, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CI_RoleCode_PropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_RoleCode')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 433, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CI_RoleCode_PropertyType._Automaton = _BuildAutomaton_39()




CI_PresentationFormCode_PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_PresentationFormCode'), CodeListValue_Type, scope=CI_PresentationFormCode_PropertyType, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 448, 3)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 442, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CI_PresentationFormCode_PropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_PresentationFormCode')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 443, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CI_PresentationFormCode_PropertyType._Automaton = _BuildAutomaton_40()




CI_Series_PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Series'), CI_Series_Type, scope=CI_Series_PropertyType, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 459, 3)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 452, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CI_Series_PropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'CI_Series')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 453, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CI_Series_PropertyType._Automaton = _BuildAutomaton_41()




DQ_EvaluationMethodTypeCode_PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'DQ_EvaluationMethodTypeCode'), CodeListValue_Type, scope=DQ_EvaluationMethodTypeCode_PropertyType, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 481, 3)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 475, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DQ_EvaluationMethodTypeCode_PropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'DQ_EvaluationMethodTypeCode')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 476, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DQ_EvaluationMethodTypeCode_PropertyType._Automaton = _BuildAutomaton_42()




DQ_Result_PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'AbstractDQ_Result'), AbstractDQ_Result_Type, abstract=pyxb.binding.datatypes.boolean(1), scope=DQ_Result_PropertyType, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 492, 3)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 485, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DQ_Result_PropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'AbstractDQ_Result')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 486, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DQ_Result_PropertyType._Automaton = _BuildAutomaton_43()




SC_CRS_PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractCRS'), AbstractCRSType, abstract=pyxb.binding.datatypes.boolean(1), scope=SC_CRS_PropertyType, documentation='gml:AbstractCRS specifies a coordinate reference system which is usually single but may be compound. This abstract complex type shall not be used, extended, or restricted, in a GML Application Schema, to define a concrete subtype with a meaning equivalent to a concrete subtype specified in this document.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 351, 3)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gsr/gsr.xsd', 40, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SC_CRS_PropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractCRS')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gsr/gsr.xsd', 41, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SC_CRS_PropertyType._Automaton = _BuildAutomaton_44()




TM_Primitive_PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractTimePrimitive'), AbstractTimePrimitiveType, abstract=pyxb.binding.datatypes.boolean(1), scope=TM_Primitive_PropertyType, documentation='gml:AbstractTimePrimitive acts as the head of a substitution group for geometric and topological temporal primitives.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 270, 3)))

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gts/gts.xsd', 38, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TM_Primitive_PropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractTimePrimitive')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gts/gts.xsd', 39, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TM_Primitive_PropertyType._Automaton = _BuildAutomaton_45()




DefinitionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'remarks'), pyxb.binding.datatypes.string, scope=DefinitionType, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 250, 3)))

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DefinitionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DefinitionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DefinitionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 88, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DefinitionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(DefinitionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'remarks')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DefinitionType._Automaton = _BuildAutomaton_46()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'EX_Extent'), EX_Extent_Type, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 33, 3)))

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 257, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'EX_Extent')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 258, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_47()




AbstractTimePrimitiveType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'relatedTime'), RelatedTimeType, scope=AbstractTimePrimitiveType, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 282, 15)))

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 106, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 107, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 108, 9))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 109, 9))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 282, 15))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AbstractTimePrimitiveType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 106, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AbstractTimePrimitiveType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 107, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AbstractTimePrimitiveType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 108, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AbstractTimePrimitiveType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 109, 9))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(AbstractTimePrimitiveType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'relatedTime')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 282, 15))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AbstractTimePrimitiveType._Automaton = _BuildAutomaton_48()




TimePrimitivePropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractTimePrimitive'), AbstractTimePrimitiveType, abstract=pyxb.binding.datatypes.boolean(1), scope=TimePrimitivePropertyType, documentation='gml:AbstractTimePrimitive acts as the head of a substitution group for geometric and topological temporal primitives.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 270, 3)))

def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 328, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TimePrimitivePropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractTimePrimitive')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 329, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TimePrimitivePropertyType._Automaton = _BuildAutomaton_49()




EllipsoidalCSPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'EllipsoidalCS'), EllipsoidalCSType, scope=EllipsoidalCSPropertyType, documentation='gml:EllipsoidalCS is a two- or three-dimensional coordinate system in which position is specified by geodetic latitude, geodetic longitude, and (in the three-dimensional case) ellipsoidal height. An EllipsoidalCS shall have two or three gml:axis property elements; the number of associations shall equal the dimension of the CS.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 391, 3)))

def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 385, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(EllipsoidalCSPropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'EllipsoidalCS')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 386, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
EllipsoidalCSPropertyType._Automaton = _BuildAutomaton_50()




CoordinateSystemAxisPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'CoordinateSystemAxis'), CoordinateSystemAxisType, scope=CoordinateSystemAxisPropertyType, documentation='gml:CoordinateSystemAxis is a definition of a coordinate system axis.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 431, 3)))

def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 425, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CoordinateSystemAxisPropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'CoordinateSystemAxis')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 426, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CoordinateSystemAxisPropertyType._Automaton = _BuildAutomaton_51()




CartesianCSPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'CartesianCS'), CartesianCSType, scope=CartesianCSPropertyType, documentation='gml:CartesianCS is a 1-, 2-, or 3-dimensional coordinate system. In the 1-dimensional case, it contains a single straight coordinate axis. In the 2- and 3-dimensional cases gives the position of points relative to orthogonal straight axes. In the multi-dimensional case, all axes shall have the same length unit of measure. A CartesianCS shall have one, two, or three gml:axis property elements.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 559, 3)))

def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 553, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CartesianCSPropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'CartesianCS')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 554, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CartesianCSPropertyType._Automaton = _BuildAutomaton_52()




SphericalCSPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'SphericalCS'), SphericalCSType, scope=SphericalCSPropertyType, documentation='gml:SphericalCS is a three-dimensional coordinate system with one distance measured from the origin and two angular coordinates. A SphericalCS shall have three gml:axis property elements.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 588, 3)))

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 582, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SphericalCSPropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'SphericalCS')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 583, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SphericalCSPropertyType._Automaton = _BuildAutomaton_53()




GeodeticDatumPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'GeodeticDatum'), GeodeticDatumType, scope=GeodeticDatumPropertyType, documentation='gml:GeodeticDatum is a geodetic datum defines the precise location and orientation in 3-dimensional space of a defined ellipsoid (or sphere), or of a Cartesian coordinate system centered in this ellipsoid (or sphere).', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 618, 3)))

def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 612, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GeodeticDatumPropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'GeodeticDatum')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 613, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
GeodeticDatumPropertyType._Automaton = _BuildAutomaton_54()




PrimeMeridianPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'PrimeMeridian'), PrimeMeridianType, scope=PrimeMeridianPropertyType, documentation='A gml:PrimeMeridian defines the origin from which longitude values are determined. The default value for the prime meridian gml:identifier value is "Greenwich".', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 681, 3)))

def _BuildAutomaton_55 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 675, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PrimeMeridianPropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'PrimeMeridian')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 676, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PrimeMeridianPropertyType._Automaton = _BuildAutomaton_55()




EllipsoidPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'Ellipsoid'), EllipsoidType, scope=EllipsoidPropertyType, documentation='A gml:Ellipsoid is a geometric figure that may be used to describe the approximate shape of the earth. In mathematical terms, it is a surface formed by the rotation of an ellipse about its minor axis.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 737, 3)))

def _BuildAutomaton_56 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 731, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(EllipsoidPropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'Ellipsoid')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 732, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
EllipsoidPropertyType._Automaton = _BuildAutomaton_56()




GeneralConversionPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractGeneralConversion'), AbstractGeneralConversionType, abstract=pyxb.binding.datatypes.boolean(1), scope=GeneralConversionPropertyType, documentation='gm:AbstractGeneralConversion is an abstract operation on coordinates that does not include any change of datum. The best-known example of a coordinate conversion is a map projection. The parameters describing coordinate conversions are defined rather than empirically derived. Note that some conversions have no parameters. The operationVersion, sourceCRS, and targetCRS elements are omitted in a coordinate conversion.\nThis abstract complex type is expected to be extended for well-known operation methods with many Conversion instances, in GML Application Schemas that define operation-method-specialized element names and contents. This conversion uses an operation method, usually with associated parameter values. However, operation methods and parameter values are directly associated with concrete subtypes, not with this abstract type. All concrete types derived from this type shall extend this type to include a "usesMethod" element that references the "OperationMethod" element. Similarly, all concrete types derived from this type shall extend this type to include zero or more elements each named "uses...Value" that each use the type of an element substitutable for the "AbstractGeneralParameterValue" element.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 853, 3)))

def _BuildAutomaton_57 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_57
    del _BuildAutomaton_57
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 847, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GeneralConversionPropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractGeneralConversion')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 848, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
GeneralConversionPropertyType._Automaton = _BuildAutomaton_57()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'AbstractDQ_PositionalAccuracy'), AbstractDQ_PositionalAccuracy_Type, abstract=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_3, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/iso/19139/20070417/gmd/gmd.xsd', 135, 3)))

def _BuildAutomaton_58 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_58
    del _BuildAutomaton_58
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 907, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'AbstractDQ_PositionalAccuracy')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 908, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_58()




CRSPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractCRS'), AbstractCRSType, abstract=pyxb.binding.datatypes.boolean(1), scope=CRSPropertyType, documentation='gml:AbstractCRS specifies a coordinate reference system which is usually single but may be compound. This abstract complex type shall not be used, extended, or restricted, in a GML Application Schema, to define a concrete subtype with a meaning equivalent to a concrete subtype specified in this document.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 351, 3)))

def _BuildAutomaton_59 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_59
    del _BuildAutomaton_59
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 934, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CRSPropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractCRS')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 935, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CRSPropertyType._Automaton = _BuildAutomaton_59()




GeodeticCRSPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'GeodeticCRS'), GeodeticCRSType, scope=GeodeticCRSPropertyType, location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 27, 3)))

def _BuildAutomaton_60 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_60
    del _BuildAutomaton_60
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 981, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GeodeticCRSPropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'GeodeticCRS')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 982, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
GeodeticCRSPropertyType._Automaton = _BuildAutomaton_60()




VerticalCSPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'VerticalCS'), VerticalCSType, scope=VerticalCSPropertyType, documentation="gml:VerticalCS is a one-dimensional coordinate system used to record the heights or depths of points. Such a coordinate system is usually dependent on the Earth's gravity field, perhaps loosely as when atmospheric pressure is the basis for the vertical coordinate system axis. A VerticalCS shall have one gml:axis property element.", location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 1029, 3)))

def _BuildAutomaton_61 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_61
    del _BuildAutomaton_61
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 1023, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(VerticalCSPropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'VerticalCS')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 1024, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
VerticalCSPropertyType._Automaton = _BuildAutomaton_61()




VerticalDatumPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'VerticalDatum'), VerticalDatumType, scope=VerticalDatumPropertyType, documentation='gml:VerticalDatum is a textual description and/or a set of parameters identifying a particular reference level surface used as a zero-height surface, including its position with respect to the Earth for any of the height types recognized by this International Standard.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 1058, 3)))

def _BuildAutomaton_62 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_62
    del _BuildAutomaton_62
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 1052, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(VerticalDatumPropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'VerticalDatum')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 1053, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
VerticalDatumPropertyType._Automaton = _BuildAutomaton_62()




def _BuildAutomaton_63 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_63
    del _BuildAutomaton_63
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(IdentifiedObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(IdentifiedObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(IdentifiedObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 88, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(IdentifiedObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(IdentifiedObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'remarks')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
IdentifiedObjectType._Automaton = _BuildAutomaton_63()




def _BuildAutomaton_64 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_64
    del _BuildAutomaton_64
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 328, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RelatedTimeType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractTimePrimitive')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 329, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RelatedTimeType._Automaton = _BuildAutomaton_64()




AbstractCRSType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'domainOfValidity'), CTD_ANON_2, scope=AbstractCRSType, documentation='The gml:domainOfValidity property implements an association role to an EX_Extent object as encoded in ISO/TS 19139, either referencing or containing the definition of that extent.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 252, 3)))

AbstractCRSType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'scope'), pyxb.binding.datatypes.string, scope=AbstractCRSType, documentation='The gml:scope property provides a description of the usage, or limitations of usage, for which this CRS-related object is valid. If unknown, enter "not known".', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 369, 3)))

def _BuildAutomaton_65 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_65
    del _BuildAutomaton_65
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 52, 15))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 88, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'remarks')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'domainOfValidity')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 52, 15))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AbstractCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'scope')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 53, 15))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AbstractCRSType._Automaton = _BuildAutomaton_65()




AbstractCoordinateSystemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'axis'), CoordinateSystemAxisPropertyType, scope=AbstractCoordinateSystemType, documentation='The gml:axis property is an association role (ordered sequence) to the coordinate system axes included in this coordinate system. The coordinate values in a coordinate tuple shall be recorded in the order in which the coordinate system axes associations are recorded, whenever those coordinates use a coordinate reference system that uses this coordinate system. The gml:AggregationAttributeGroup should be used to specify that the axis objects are ordered.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 415, 3)))

def _BuildAutomaton_66 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_66
    del _BuildAutomaton_66
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractCoordinateSystemType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractCoordinateSystemType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractCoordinateSystemType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 88, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractCoordinateSystemType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractCoordinateSystemType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'remarks')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AbstractCoordinateSystemType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'axis')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 408, 15))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AbstractCoordinateSystemType._Automaton = _BuildAutomaton_66()




CoordinateSystemAxisType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'axisAbbrev'), CodeType, scope=CoordinateSystemAxisType, documentation='gml:axisAbbrev is the abbreviation used for this coordinate system axis; this abbreviation is also used to identify the coordinates in the coordinate tuple. The codeSpace attribute may reference a source of more information on a set of standardized abbreviations, or on this abbreviation.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 453, 3)))

CoordinateSystemAxisType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'axisDirection'), CodeWithAuthorityType, scope=CoordinateSystemAxisType, documentation='gml:axisDirection is the direction of this coordinate system axis (or in the case of Cartesian projected coordinates, the direction of this coordinate system axis at the origin).\nWithin any set of coordinate system axes, only one of each pair of terms may be used. For earth-fixed CRSs, this direction is often approximate and intended to provide a human interpretable meaning to the axis. When a geodetic datum is used, the precise directions of the axes may therefore vary slightly from this approximate direction.\nThe codeSpace attribute shall reference a source of information specifying the values and meanings of all the allowed string values for this property.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 459, 3)))

CoordinateSystemAxisType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'minimumValue'), pyxb.binding.datatypes.double, scope=CoordinateSystemAxisType, documentation='The gml:minimumValue and gml:maximumValue properties allow the specification of minimum and maximum value normally allowed for this axis, in the unit of measure for the axis. For a continuous angular axis such as longitude, the values wrap-around at this value. Also, values beyond this minimum/maximum can be used for specified purposes, such as in a bounding box. A value of minus infinity shall be allowed for the gml:minimumValue element, a value of plus infiniy for the gml:maximumValue element. If these elements are omitted, the value is unspecified.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 467, 3)))

CoordinateSystemAxisType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'maximumValue'), pyxb.binding.datatypes.double, scope=CoordinateSystemAxisType, documentation='The gml:minimumValue and gml:maximumValue properties allow the specification of minimum and maximum value normally allowed for this axis, in the unit of measure for the axis. For a continuous angular axis such as longitude, the values wrap-around at this value. Also, values beyond this minimum/maximum can be used for specified purposes, such as in a bounding box. A value of minus infinity shall be allowed for the gml:minimumValue element, a value of plus infiniy for the gml:maximumValue element. If these elements are omitted, the value is unspecified.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 473, 3)))

CoordinateSystemAxisType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'rangeMeaning'), CodeWithAuthorityType, scope=CoordinateSystemAxisType, documentation='gml:rangeMeaning describes the meaning of axis value range specified by gml:minimumValue and gml:maximumValue. This element shall be omitted when both gml:minimumValue and gml:maximumValue are omitted. This element should be included when gml:minimumValue and/or gml:maximumValue are included. If this element is omitted when the gml:minimumValue and/or gml:maximumValue are included, the meaning is unspecified. The codeSpace attribute shall reference a source of information specifying the values and meanings of all the allowed string values for this property.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 479, 3)))

def _BuildAutomaton_67 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_67
    del _BuildAutomaton_67
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 444, 15))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 445, 15))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 446, 15))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CoordinateSystemAxisType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CoordinateSystemAxisType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CoordinateSystemAxisType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 88, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CoordinateSystemAxisType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CoordinateSystemAxisType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'remarks')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CoordinateSystemAxisType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'axisAbbrev')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 442, 15))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CoordinateSystemAxisType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'axisDirection')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 443, 15))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CoordinateSystemAxisType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'minimumValue')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 444, 15))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CoordinateSystemAxisType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'maximumValue')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 445, 15))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CoordinateSystemAxisType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'rangeMeaning')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 446, 15))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CoordinateSystemAxisType._Automaton = _BuildAutomaton_67()




AbstractDatumType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'domainOfValidity'), CTD_ANON_2, scope=AbstractDatumType, documentation='The gml:domainOfValidity property implements an association role to an EX_Extent object as encoded in ISO/TS 19139, either referencing or containing the definition of that extent.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 252, 3)))

AbstractDatumType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'scope'), pyxb.binding.datatypes.string, scope=AbstractDatumType, documentation='The gml:scope property provides a description of the usage, or limitations of usage, for which this CRS-related object is valid. If unknown, enter "not known".', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 369, 3)))

AbstractDatumType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'anchorDefinition'), CodeType, scope=AbstractDatumType, documentation='gml:anchorDefinition is a description, possibly including coordinates, of the definition used to anchor the datum to the Earth. Also known as the "origin", especially for engineering and image datums. The codeSpace attribute may be used to reference a source of more detailed on this point or surface, or on a set of such descriptions.\n-\tFor a geodetic datum, this point is also known as the fundamental point, which is traditionally the point where the relationship between geoid and ellipsoid is defined. In some cases, the "fundamental point" may consist of a number of points. In those cases, the parameters defining the geoid/ellipsoid relationship have been averaged for these points, and the averages adopted as the datum definition.\n-\tFor an engineering datum, the anchor definition may be a physical point, or it may be a point with defined coordinates in another CRS.may\n-\tFor an image datum, the anchor definition is usually either the centre of the image or the corner of the image.\n-\tFor a temporal datum, this attribute is not defined. Instead of the anchor definition, a temporal datum carries a separate time origin of type DateTime.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 649, 3)))

AbstractDatumType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'realizationEpoch'), pyxb.binding.datatypes.date, scope=AbstractDatumType, documentation='gml:realizationEpoch is the time after which this datum definition is valid. See ISO 19111 Table 32 for details.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 659, 3)))

def _BuildAutomaton_68 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_68
    del _BuildAutomaton_68
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 640, 15))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 642, 15))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 643, 15))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractDatumType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractDatumType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractDatumType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 88, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractDatumType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractDatumType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'remarks')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractDatumType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'domainOfValidity')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 640, 15))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AbstractDatumType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'scope')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 641, 15))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AbstractDatumType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'anchorDefinition')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 642, 15))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(AbstractDatumType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'realizationEpoch')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 643, 15))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AbstractDatumType._Automaton = _BuildAutomaton_68()




PrimeMeridianType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'greenwichLongitude'), AngleType, scope=PrimeMeridianType, documentation='gml:greenwichLongitude is the longitude of the prime meridian measured from the Greenwich meridian, positive eastward. If the value of the prime meridian "name" is "Greenwich" then the value of greenwichLongitude shall be 0 degrees.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 698, 3)))

def _BuildAutomaton_69 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_69
    del _BuildAutomaton_69
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PrimeMeridianType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PrimeMeridianType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PrimeMeridianType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 88, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PrimeMeridianType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PrimeMeridianType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'remarks')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PrimeMeridianType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'greenwichLongitude')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 692, 15))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PrimeMeridianType._Automaton = _BuildAutomaton_69()




EllipsoidType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'semiMajorAxis'), MeasureType, scope=EllipsoidType, documentation='gml:semiMajorAxis specifies the length of the semi-major axis of the ellipsoid, with its units. Uses the MeasureType with the restriction that the unit of measure referenced by uom must be suitable for a length, such as metres or feet.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 754, 3)))

EllipsoidType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'secondDefiningParameter'), CTD_ANON, scope=EllipsoidType, documentation='gml:secondDefiningParameter is a property containing the definition of the second parameter that defines the shape of an ellipsoid. An ellipsoid requires two defining parameters: semi-major axis and inverse flattening or semi-major axis and semi-minor axis. When the reference body is a sphere rather than an ellipsoid, only a single defining parameter is required, namely the radius of the sphere; in that case, the semi-major axis "degenerates" into the radius of the sphere.\nThe inverseFlattening element contains the inverse flattening value of the ellipsoid. This value is a scale factor (or ratio). It uses gml:LengthType with the restriction that the unit of measure referenced by the uom attribute must be suitable for a scale factor, such as percent, permil, or parts-per-million.\nThe semiMinorAxis element contains the length of the semi-minor axis of the ellipsoid. When the isSphere element is included, the ellipsoid is degenerate and is actually a sphere. The sphere is completely defined by the semi-major axis, which is the radius of the sphere.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 760, 3)))

def _BuildAutomaton_70 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_70
    del _BuildAutomaton_70
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EllipsoidType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EllipsoidType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EllipsoidType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 88, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EllipsoidType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EllipsoidType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'remarks')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EllipsoidType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'semiMajorAxis')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 747, 15))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EllipsoidType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'secondDefiningParameter')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 748, 15))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
EllipsoidType._Automaton = _BuildAutomaton_70()




AbstractCoordinateOperationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'domainOfValidity'), CTD_ANON_2, scope=AbstractCoordinateOperationType, documentation='The gml:domainOfValidity property implements an association role to an EX_Extent object as encoded in ISO/TS 19139, either referencing or containing the definition of that extent.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 252, 3)))

AbstractCoordinateOperationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'scope'), pyxb.binding.datatypes.string, scope=AbstractCoordinateOperationType, documentation='The gml:scope property provides a description of the usage, or limitations of usage, for which this CRS-related object is valid. If unknown, enter "not known".', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 369, 3)))

AbstractCoordinateOperationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'operationVersion'), pyxb.binding.datatypes.string, scope=AbstractCoordinateOperationType, documentation='gml:operationVersion is the version of the coordinate transformation (i.e., instantiation due to the stochastic nature of the parameters). Mandatory when describing a transformation, and should not be supplied for a conversion.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 896, 3)))

AbstractCoordinateOperationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'coordinateOperationAccuracy'), CTD_ANON_3, scope=AbstractCoordinateOperationType, documentation='gml:coordinateOperationAccuracy is an association role to a DQ_PositionalAccuracy object as encoded in ISO/TS 19139, either referencing or containing the definition of that positional accuracy. That object contains an estimate of the impact of this coordinate operation on point accuracy. That is, it gives position error estimates for the target coordinates of this coordinate operation, assuming no errors in the source coordinates.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 902, 3)))

AbstractCoordinateOperationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'sourceCRS'), CRSPropertyType, scope=AbstractCoordinateOperationType, documentation='gml:sourceCRS is an association role to the source CRS (coordinate reference system) of this coordinate operation.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 924, 3)))

AbstractCoordinateOperationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'targetCRS'), CRSPropertyType, scope=AbstractCoordinateOperationType, documentation='gml:targetCRS is an association role to the target CRS (coordinate reference system) of this coordinate operation.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 940, 3)))

def _BuildAutomaton_71 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_71
    del _BuildAutomaton_71
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 885, 15))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 887, 15))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 888, 15))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 889, 15))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 890, 15))
    counters.add(cc_8)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractCoordinateOperationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractCoordinateOperationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractCoordinateOperationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 88, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractCoordinateOperationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractCoordinateOperationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'remarks')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractCoordinateOperationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'domainOfValidity')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 885, 15))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AbstractCoordinateOperationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'scope')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 886, 15))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AbstractCoordinateOperationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'operationVersion')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 887, 15))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(AbstractCoordinateOperationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'coordinateOperationAccuracy')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 888, 15))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(AbstractCoordinateOperationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'sourceCRS')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 889, 15))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(AbstractCoordinateOperationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'targetCRS')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 890, 15))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AbstractCoordinateOperationType._Automaton = _BuildAutomaton_71()




GeodeticCRSType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'ellipsoidalCS'), EllipsoidalCSPropertyType, scope=GeodeticCRSType, documentation='gml:ellipsoidalCS is an association role to the ellipsoidal coordinate system used by this CRS.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 375, 3)))

GeodeticCRSType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'cartesianCS'), CartesianCSPropertyType, scope=GeodeticCRSType, documentation='gml:cartesianCS is an association role to the Cartesian coordinate system used by this CRS.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 543, 3)))

GeodeticCRSType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'sphericalCS'), SphericalCSPropertyType, scope=GeodeticCRSType, documentation='gml:sphericalCS is an association role to the spherical coordinate system used by this CRS.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 572, 3)))

GeodeticCRSType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'geodeticDatum'), GeodeticDatumPropertyType, scope=GeodeticCRSType, documentation='gml:geodeticDatum is an association role to the geodetic datum used by this CRS.\n', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 601, 3)))

def _BuildAutomaton_72 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_72
    del _BuildAutomaton_72
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 52, 15))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GeodeticCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GeodeticCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GeodeticCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 88, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GeodeticCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GeodeticCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'remarks')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GeodeticCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'domainOfValidity')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 52, 15))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GeodeticCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'scope')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 53, 15))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GeodeticCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'ellipsoidalCS')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 38, 18))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GeodeticCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'cartesianCS')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 39, 18))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GeodeticCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'sphericalCS')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 40, 18))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GeodeticCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'geodeticDatum')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 42, 15))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GeodeticCRSType._Automaton = _BuildAutomaton_72()




def _BuildAutomaton_73 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_73
    del _BuildAutomaton_73
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EllipsoidalCSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EllipsoidalCSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EllipsoidalCSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 88, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EllipsoidalCSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EllipsoidalCSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'remarks')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EllipsoidalCSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'axis')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 408, 15))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
EllipsoidalCSType._Automaton = _BuildAutomaton_73()




def _BuildAutomaton_74 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_74
    del _BuildAutomaton_74
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CartesianCSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CartesianCSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CartesianCSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 88, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CartesianCSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CartesianCSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'remarks')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CartesianCSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'axis')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 408, 15))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CartesianCSType._Automaton = _BuildAutomaton_74()




def _BuildAutomaton_75 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_75
    del _BuildAutomaton_75
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SphericalCSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SphericalCSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SphericalCSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 88, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SphericalCSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SphericalCSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'remarks')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SphericalCSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'axis')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 408, 15))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SphericalCSType._Automaton = _BuildAutomaton_75()




GeodeticDatumType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'primeMeridian'), PrimeMeridianPropertyType, scope=GeodeticDatumType, documentation='gml:primeMeridian is an association role to the prime meridian used by this geodetic datum.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 665, 3)))

GeodeticDatumType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'ellipsoid'), EllipsoidPropertyType, scope=GeodeticDatumType, documentation='gml:ellipsoid is an association role to the ellipsoid used by this geodetic datum.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 721, 3)))

def _BuildAutomaton_76 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_76
    del _BuildAutomaton_76
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 640, 15))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 642, 15))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 643, 15))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GeodeticDatumType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GeodeticDatumType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GeodeticDatumType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 88, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GeodeticDatumType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GeodeticDatumType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'remarks')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GeodeticDatumType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'domainOfValidity')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 640, 15))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GeodeticDatumType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'scope')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 641, 15))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GeodeticDatumType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'anchorDefinition')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 642, 15))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GeodeticDatumType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'realizationEpoch')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 643, 15))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GeodeticDatumType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'primeMeridian')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 629, 15))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GeodeticDatumType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'ellipsoid')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 630, 15))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GeodeticDatumType._Automaton = _BuildAutomaton_76()




AbstractGeneralDerivedCRSType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'conversion'), GeneralConversionPropertyType, scope=AbstractGeneralDerivedCRSType, documentation='gml:conversion is an association role to the coordinate conversion used to define the derived CRS.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 837, 3)))

def _BuildAutomaton_77 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_77
    del _BuildAutomaton_77
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 52, 15))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractGeneralDerivedCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractGeneralDerivedCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractGeneralDerivedCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 88, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractGeneralDerivedCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractGeneralDerivedCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'remarks')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractGeneralDerivedCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'domainOfValidity')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 52, 15))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractGeneralDerivedCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'scope')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 53, 15))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AbstractGeneralDerivedCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'conversion')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 831, 15))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AbstractGeneralDerivedCRSType._Automaton = _BuildAutomaton_77()




def _BuildAutomaton_78 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_78
    del _BuildAutomaton_78
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 867, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 868, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 870, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 871, 15))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 872, 15))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 874, 15))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractGeneralConversionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 867, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractGeneralConversionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 868, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractGeneralConversionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 869, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractGeneralConversionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 870, 15))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractGeneralConversionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'remarks')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 871, 15))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractGeneralConversionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'domainOfValidity')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 872, 15))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AbstractGeneralConversionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'scope')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 873, 15))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AbstractGeneralConversionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'coordinateOperationAccuracy')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 874, 15))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AbstractGeneralConversionType._Automaton = _BuildAutomaton_78()




VerticalCRSType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'verticalCS'), VerticalCSPropertyType, scope=VerticalCRSType, documentation='gml:verticalCS is an association role to the vertical coordinate system used by this CRS.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 1013, 3)))

VerticalCRSType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'verticalDatum'), VerticalDatumPropertyType, scope=VerticalCRSType, documentation='gml:verticalDatum is an association role to the vertical datum used by this CRS.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 1042, 3)))

def _BuildAutomaton_79 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_79
    del _BuildAutomaton_79
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 52, 15))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(VerticalCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(VerticalCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(VerticalCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 88, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(VerticalCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(VerticalCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'remarks')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(VerticalCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'domainOfValidity')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 52, 15))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(VerticalCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'scope')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 53, 15))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(VerticalCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'verticalCS')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 1006, 15))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(VerticalCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'verticalDatum')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 1007, 15))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
VerticalCRSType._Automaton = _BuildAutomaton_79()




def _BuildAutomaton_80 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_80
    del _BuildAutomaton_80
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(VerticalCSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(VerticalCSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(VerticalCSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 88, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(VerticalCSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(VerticalCSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'remarks')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(VerticalCSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'axis')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 408, 15))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
VerticalCSType._Automaton = _BuildAutomaton_80()




def _BuildAutomaton_81 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_81
    del _BuildAutomaton_81
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 640, 15))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 642, 15))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 643, 15))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(VerticalDatumType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(VerticalDatumType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(VerticalDatumType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 88, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(VerticalDatumType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(VerticalDatumType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'remarks')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(VerticalDatumType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'domainOfValidity')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 640, 15))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(VerticalDatumType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'scope')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 641, 15))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(VerticalDatumType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'anchorDefinition')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 642, 15))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(VerticalDatumType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'realizationEpoch')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 643, 15))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
VerticalDatumType._Automaton = _BuildAutomaton_81()




ProjectedCRSType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'cartesianCS'), CartesianCSPropertyType, scope=ProjectedCRSType, documentation='gml:cartesianCS is an association role to the Cartesian coordinate system used by this CRS.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 543, 3)))

ProjectedCRSType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'baseGeodeticCRS'), GeodeticCRSPropertyType, scope=ProjectedCRSType, documentation='gml:baseGeodeticCRS is an association role to the geodetic coordinate reference system used by this projected CRS.', location=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 971, 3)))

def _BuildAutomaton_82 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_82
    del _BuildAutomaton_82
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 52, 15))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProjectedCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 86, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProjectedCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 87, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProjectedCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 88, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProjectedCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 89, 15))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProjectedCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'remarks')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 75, 15))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProjectedCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'domainOfValidity')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 52, 15))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProjectedCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'scope')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 53, 15))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProjectedCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'conversion')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 831, 15))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProjectedCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'baseGeodeticCRS')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 818, 18))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ProjectedCRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'cartesianCS')), pyxb.utils.utility.Location('http://w3.energistics.org/energyML/data/common/v2.1/xsd_schemas/gml/3.2.1/gml.xsd', 821, 15))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ProjectedCRSType._Automaton = _BuildAutomaton_82()


CI_DateTypeCode._setSubstitutionGroup(CharacterString)

CI_OnLineFunctionCode._setSubstitutionGroup(CharacterString)

CI_RoleCode._setSubstitutionGroup(CharacterString)

CI_PresentationFormCode._setSubstitutionGroup(CharacterString)

DQ_EvaluationMethodTypeCode._setSubstitutionGroup(CharacterString)

AbstractGML._setSubstitutionGroup(AbstractObject)

AbstractTimeObject._setSubstitutionGroup(AbstractGML)

AbstractDQ_PositionalAccuracy._setSubstitutionGroup(AbstractDQ_Element)

AbstractTimePrimitive._setSubstitutionGroup(AbstractTimeObject)

Definition._setSubstitutionGroup(AbstractGML)

AbstractCRS._setSubstitutionGroup(Definition)

CoordinateSystemAxis._setSubstitutionGroup(Definition)

AbstractCoordinateSystem._setSubstitutionGroup(Definition)

PrimeMeridian._setSubstitutionGroup(Definition)

Ellipsoid._setSubstitutionGroup(Definition)

AbstractDatum._setSubstitutionGroup(Definition)

AbstractSingleCRS._setSubstitutionGroup(AbstractCRS)

AbstractOperation._setSubstitutionGroup(AbstractSingleOperation)

AbstractSingleOperation._setSubstitutionGroup(AbstractCoordinateOperation)

AbstractCoordinateOperation._setSubstitutionGroup(Definition)

GeodeticCRS._setSubstitutionGroup(AbstractSingleCRS)

EllipsoidalCS._setSubstitutionGroup(AbstractCoordinateSystem)

CartesianCS._setSubstitutionGroup(AbstractCoordinateSystem)

SphericalCS._setSubstitutionGroup(AbstractCoordinateSystem)

GeodeticDatum._setSubstitutionGroup(AbstractDatum)

AbstractGeneralConversion._setSubstitutionGroup(AbstractOperation)

AbstractGeneralDerivedCRS._setSubstitutionGroup(AbstractSingleCRS)

VerticalCRS._setSubstitutionGroup(AbstractSingleCRS)

VerticalCS._setSubstitutionGroup(AbstractCoordinateSystem)

VerticalDatum._setSubstitutionGroup(AbstractDatum)

ProjectedCRS._setSubstitutionGroup(AbstractGeneralDerivedCRS)
