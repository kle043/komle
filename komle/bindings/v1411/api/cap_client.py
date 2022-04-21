# komle/bindings/v1411/api/cap_client.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:3b7fbd5f64431e9d44183d2bca44c1a87b88e242
# Generated 2022-04-21 03:30:51.721219 by PyXB version 1.2.6 using Python 3.10.4.final.0
# Namespace http://www.witsml.org/api/141

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
    "urn:uuid:b2b75c57-60e7-4e4a-b724-b7c3176ee7bf"
)

# Version of PyXB used to generate the bindings
_PyXBVersion = "1.2.6"

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(
    "http://www.witsml.org/api/141", create_if_missing=True
)
Namespace.configureCategories(["typeBinding", "elementBinding"])


def CreateFromDocument(
    xml_text,
    fallback_namespace=None,
    location_base=None,
    default_namespace=None,
):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword fallback_namespace An absent L{pyxb.Namespace} instance
    to use for unqualified names when there is no default namespace in
    scope.  If unspecified or C{None}, the namespace of the module
    containing this function will be used, if it is an absent
    namespace.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.

    @keyword default_namespace An alias for @c fallback_namespace used
    in PyXB 1.1.4 through 1.2.6.  It behaved like a default namespace
    only for absent namespaces.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(
        fallback_namespace=fallback_namespace, location_base=location_base
    )
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance


def CreateFromDOM(node, fallback_namespace=None, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, fallback_namespace)


# Atomic simple type: {http://www.witsml.org/api/141}timestamp
class timestamp(pyxb.binding.datatypes.dateTime):

    """A date with the time of day and a mandatory time zone."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "timestamp")
    _XSDLocation = pyxb.utils.utility.Location(
        "../../../public/typ_dataTypes.xsd", 45, 1
    )
    _Documentation = "A date with the time of day and a mandatory time zone."


timestamp._CF_pattern = pyxb.binding.facets.CF_pattern()
timestamp._CF_pattern.addPattern(pattern=".+T.+[Z+\\-].*")
timestamp._InitializeFacetMap(timestamp._CF_pattern)
Namespace.addCategoryObject("typeBinding", "timestamp", timestamp)
_module_typeBindings.timestamp = timestamp

# Atomic simple type: {http://www.witsml.org/api/141}nonNegativeCount
class nonNegativeCount(pyxb.binding.datatypes.int):

    """A non-negative integer (zero based count or index)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "nonNegativeCount")
    _XSDLocation = pyxb.utils.utility.Location(
        "../../../public/typ_dataTypes.xsd", 61, 1
    )
    _Documentation = "A non-negative integer (zero based count or index)."


nonNegativeCount._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(
    value=pyxb.binding.datatypes.int(0), value_datatype=nonNegativeCount
)
nonNegativeCount._InitializeFacetMap(nonNegativeCount._CF_minInclusive)
Namespace.addCategoryObject("typeBinding", "nonNegativeCount", nonNegativeCount)
_module_typeBindings.nonNegativeCount = nonNegativeCount

# Atomic simple type: {http://www.witsml.org/api/141}abstractString
class abstractString(pyxb.binding.datatypes.string):

    """The intended abstract supertype of all strings.
    This abstract type allows the control over whitespace for all strings to be defined at a high level.
    This type should not be used directly except to derive another type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "abstractString")
    _XSDLocation = pyxb.utils.utility.Location(
        "../../../public/typ_dataTypes.xsd", 105, 1
    )
    _Documentation = "The intended abstract supertype of all strings.\n\t\t\tThis abstract type allows the control over whitespace for all strings to be defined at a high level. \n\t\t\tThis type should not be used directly except to derive another type."


abstractString._CF_minLength = pyxb.binding.facets.CF_minLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(1)
)
abstractString._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(
    value=pyxb.binding.facets._WhiteSpace_enum.collapse
)
abstractString._InitializeFacetMap(
    abstractString._CF_minLength, abstractString._CF_whiteSpace
)
Namespace.addCategoryObject("typeBinding", "abstractString", abstractString)
_module_typeBindings.abstractString = abstractString

# Atomic simple type: {http://www.witsml.org/api/141}abstractPositiveCount
class abstractPositiveCount(pyxb.binding.datatypes.int):

    """The intended abstract supertype of all xsd:int types which must be positive.
    This type should not be used directly except to derive another type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "abstractPositiveCount")
    _XSDLocation = pyxb.utils.utility.Location(
        "../../../public/typ_dataTypes.xsd", 129, 1
    )
    _Documentation = "The intended abstract supertype of all xsd:int types which must be positive.\n\t\t\tThis type should not be used directly except to derive another type."


abstractPositiveCount._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(
    value=pyxb.binding.datatypes.int(1), value_datatype=abstractPositiveCount
)
abstractPositiveCount._InitializeFacetMap(abstractPositiveCount._CF_minInclusive)
Namespace.addCategoryObject(
    "typeBinding", "abstractPositiveCount", abstractPositiveCount
)
_module_typeBindings.abstractPositiveCount = abstractPositiveCount

# Atomic simple type: {http://www.witsml.org/api/141}str16
class str16(abstractString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "str16")
    _XSDLocation = pyxb.utils.utility.Location(
        "../../../public/typ_dataTypes.xsd", 23, 1
    )
    _Documentation = None


str16._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(16)
)
str16._InitializeFacetMap(str16._CF_maxLength)
Namespace.addCategoryObject("typeBinding", "str16", str16)
_module_typeBindings.str16 = str16

# Atomic simple type: {http://www.witsml.org/api/141}str256
class str256(abstractString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "str256")
    _XSDLocation = pyxb.utils.utility.Location(
        "../../../public/typ_dataTypes.xsd", 33, 1
    )
    _Documentation = None


str256._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(256)
)
str256._InitializeFacetMap(str256._CF_maxLength)
Namespace.addCategoryObject("typeBinding", "str256", str256)
_module_typeBindings.str256 = str256

# Atomic simple type: {http://www.witsml.org/api/141}str4096
class str4096(abstractString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "str4096")
    _XSDLocation = pyxb.utils.utility.Location(
        "../../../public/typ_dataTypes.xsd", 39, 1
    )
    _Documentation = None


str4096._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(4096)
)
str4096._InitializeFacetMap(str4096._CF_maxLength)
Namespace.addCategoryObject("typeBinding", "str4096", str4096)
_module_typeBindings.str4096 = str4096

# Atomic simple type: {http://www.witsml.org/api/141}positiveCount
class positiveCount(abstractPositiveCount):

    """A positive integer (one based count or index)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "positiveCount")
    _XSDLocation = pyxb.utils.utility.Location(
        "../../../public/typ_dataTypes.xsd", 54, 1
    )
    _Documentation = "A positive integer (one based count or index)."


positiveCount._InitializeFacetMap()
Namespace.addCategoryObject("typeBinding", "positiveCount", positiveCount)
_module_typeBindings.positiveCount = positiveCount

# Atomic simple type: {http://www.witsml.org/api/141}abstractString64
class abstractString64(abstractString):

    """The intended abstract supertype of all 64 character string types.
    This type should not be used directly except to derive another type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "abstractString64")
    _XSDLocation = pyxb.utils.utility.Location(
        "../../../public/typ_dataTypes.xsd", 145, 1
    )
    _Documentation = "The intended abstract supertype of all 64 character string types.\n\t\t\tThis type should not be used directly except to derive another type."


abstractString64._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(64)
)
abstractString64._InitializeFacetMap(abstractString64._CF_maxLength)
Namespace.addCategoryObject("typeBinding", "abstractString64", abstractString64)
_module_typeBindings.abstractString64 = abstractString64

# Atomic simple type: {http://www.witsml.org/api/141}str64
class str64(abstractString64):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "str64")
    _XSDLocation = pyxb.utils.utility.Location(
        "../../../public/typ_dataTypes.xsd", 29, 1
    )
    _Documentation = None


str64._InitializeFacetMap()
Namespace.addCategoryObject("typeBinding", "str64", str64)
_module_typeBindings.str64 = str64

# Complex type {http://www.witsml.org/api/141}cs_contact with content type ELEMENT_ONLY
class cs_contact(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.witsml.org/api/141}cs_contact with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "cs_contact")
    _XSDLocation = pyxb.utils.utility.Location("../../../public/cs_contact.xsd", 21, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.witsml.org/api/141}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "name"),
        "name",
        "__httpwww_witsml_orgapi141_cs_contact_httpwww_witsml_orgapi141name",
        False,
        pyxb.utils.utility.Location("../../../public/cs_contact.xsd", 23, 3),
    )

    name = property(
        __name.value,
        __name.set,
        None,
        "See the API specification for a description of the use of this data.",
    )

    # Element {http://www.witsml.org/api/141}email uses Python identifier email
    __email = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "email"),
        "email",
        "__httpwww_witsml_orgapi141_cs_contact_httpwww_witsml_orgapi141email",
        False,
        pyxb.utils.utility.Location("../../../public/cs_contact.xsd", 28, 3),
    )

    email = property(
        __email.value,
        __email.set,
        None,
        "See the API specification for a description of the use of this data.",
    )

    # Element {http://www.witsml.org/api/141}phone uses Python identifier phone
    __phone = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "phone"),
        "phone",
        "__httpwww_witsml_orgapi141_cs_contact_httpwww_witsml_orgapi141phone",
        False,
        pyxb.utils.utility.Location("../../../public/cs_contact.xsd", 33, 3),
    )

    phone = property(
        __phone.value,
        __phone.set,
        None,
        "See the API specification for a description of the use of this data.",
    )

    _ElementMap.update(
        {
            __name.name(): __name,
            __email.name(): __email,
            __phone.name(): __phone,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.cs_contact = cs_contact
Namespace.addCategoryObject("typeBinding", "cs_contact", cs_contact)


# Complex type {http://www.witsml.org/api/141}obj_capClients with content type ELEMENT_ONLY
class obj_capClients(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.witsml.org/api/141}obj_capClients with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "obj_capClients")
    _XSDLocation = pyxb.utils.utility.Location(
        "../../../public/obj_capClient.xsd", 41, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.witsml.org/api/141}capClient uses Python identifier capClient
    __capClient = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "capClient"),
        "capClient",
        "__httpwww_witsml_orgapi141_obj_capClients_httpwww_witsml_orgapi141capClient",
        False,
        pyxb.utils.utility.Location("../../../public/obj_capClient.xsd", 43, 3),
    )

    capClient = property(
        __capClient.value,
        __capClient.set,
        None,
        "Defines the singular Client Capabilities (capClient) element; only one can be specified. \n\t\t\t\t\t",
    )

    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "version"),
        "version",
        "__httpwww_witsml_orgapi141_obj_capClients_version",
        _module_typeBindings.str16,
        fixed=True,
        unicode_default="1.4.1",
    )
    __version._DeclarationLocation = pyxb.utils.utility.Location(
        "../../../public/obj_capClient.xsd", 50, 2
    )
    __version._UseLocation = pyxb.utils.utility.Location(
        "../../../public/obj_capClient.xsd", 50, 2
    )

    version = property(
        __version.value,
        __version.set,
        None,
        "API schema version.  It is optional.\n\t\t\t\tIf the version is specified, its value must be set equal to the value specified by the \n\t\t\t\tversion's fixed attribute. Note that this is different from the data schema version.\n\t\t\t\t",
    )

    _ElementMap.update({__capClient.name(): __capClient})
    _AttributeMap.update({__version.name(): __version})


_module_typeBindings.obj_capClients = obj_capClients
Namespace.addCategoryObject("typeBinding", "obj_capClients", obj_capClients)


# Complex type {http://www.witsml.org/api/141}obj_capClient with content type ELEMENT_ONLY
class obj_capClient(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.witsml.org/api/141}obj_capClient with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "obj_capClient")
    _XSDLocation = pyxb.utils.utility.Location(
        "../../../public/obj_capClient.xsd", 60, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.witsml.org/api/141}contact uses Python identifier contact
    __contact = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "contact"),
        "contact",
        "__httpwww_witsml_orgapi141_obj_capClient_httpwww_witsml_orgapi141contact",
        False,
        pyxb.utils.utility.Location("../../../public/obj_capClient.xsd", 62, 3),
    )

    contact = property(
        __contact.value,
        __contact.set,
        None,
        "See the API specification for a description of the use of this data.",
    )

    # Element {http://www.witsml.org/api/141}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "description"),
        "description",
        "__httpwww_witsml_orgapi141_obj_capClient_httpwww_witsml_orgapi141description",
        False,
        pyxb.utils.utility.Location("../../../public/obj_capClient.xsd", 67, 3),
    )

    description = property(
        __description.value,
        __description.set,
        None,
        "See the API specification for a description of the use of this data.",
    )

    # Element {http://www.witsml.org/api/141}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "name"),
        "name",
        "__httpwww_witsml_orgapi141_obj_capClient_httpwww_witsml_orgapi141name",
        False,
        pyxb.utils.utility.Location("../../../public/obj_capClient.xsd", 72, 3),
    )

    name = property(
        __name.value,
        __name.set,
        None,
        "See the API specification for a description of the use of this data.",
    )

    # Element {http://www.witsml.org/api/141}vendor uses Python identifier vendor
    __vendor = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "vendor"),
        "vendor",
        "__httpwww_witsml_orgapi141_obj_capClient_httpwww_witsml_orgapi141vendor",
        False,
        pyxb.utils.utility.Location("../../../public/obj_capClient.xsd", 77, 3),
    )

    vendor = property(
        __vendor.value,
        __vendor.set,
        None,
        "See the API specification for a description of the use of this data.",
    )

    # Element {http://www.witsml.org/api/141}version uses Python identifier version
    __version = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "version"),
        "version",
        "__httpwww_witsml_orgapi141_obj_capClient_httpwww_witsml_orgapi141version",
        False,
        pyxb.utils.utility.Location("../../../public/obj_capClient.xsd", 82, 3),
    )

    version = property(
        __version.value,
        __version.set,
        None,
        "See the API specification for a description of the use of this data.",
    )

    # Element {http://www.witsml.org/api/141}schemaVersion uses Python identifier schemaVersion
    __schemaVersion = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "schemaVersion"),
        "schemaVersion",
        "__httpwww_witsml_orgapi141_obj_capClient_httpwww_witsml_orgapi141schemaVersion",
        False,
        pyxb.utils.utility.Location("../../../public/obj_capClient.xsd", 87, 3),
    )

    schemaVersion = property(
        __schemaVersion.value,
        __schemaVersion.set,
        None,
        "See the API specification for a description of the use of this data.",
    )

    # Attribute apiVers uses Python identifier apiVers
    __apiVers = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "apiVers"),
        "apiVers",
        "__httpwww_witsml_orgapi141_obj_capClient_apiVers",
        _module_typeBindings.str16,
        required=True,
    )
    __apiVers._DeclarationLocation = pyxb.utils.utility.Location(
        "../../../public/obj_capClient.xsd", 93, 2
    )
    __apiVers._UseLocation = pyxb.utils.utility.Location(
        "../../../public/obj_capClient.xsd", 93, 2
    )

    apiVers = property(
        __apiVers.value,
        __apiVers.set,
        None,
        "See the API specification for a description of the use of this data.",
    )

    _ElementMap.update(
        {
            __contact.name(): __contact,
            __description.name(): __description,
            __name.name(): __name,
            __vendor.name(): __vendor,
            __version.name(): __version,
            __schemaVersion.name(): __schemaVersion,
        }
    )
    _AttributeMap.update({__apiVers.name(): __apiVers})


_module_typeBindings.obj_capClient = obj_capClient
Namespace.addCategoryObject("typeBinding", "obj_capClient", obj_capClient)


# Complex type {http://www.witsml.org/api/141}objectWithConstraint with content type SIMPLE
class objectWithConstraint(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.witsml.org/api/141}objectWithConstraint with content type SIMPLE"""

    _TypeDefinition = abstractString64
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "objectWithConstraint")
    _XSDLocation = pyxb.utils.utility.Location(
        "../../../public/typ_dataTypes.xsd", 86, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is abstractString64

    # Attribute maxDataNodes uses Python identifier maxDataNodes
    __maxDataNodes = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "maxDataNodes"),
        "maxDataNodes",
        "__httpwww_witsml_orgapi141_objectWithConstraint_maxDataNodes",
        _module_typeBindings.positiveCount,
    )
    __maxDataNodes._DeclarationLocation = pyxb.utils.utility.Location(
        "../../../public/typ_dataTypes.xsd", 89, 4
    )
    __maxDataNodes._UseLocation = pyxb.utils.utility.Location(
        "../../../public/typ_dataTypes.xsd", 89, 4
    )

    maxDataNodes = property(
        __maxDataNodes.value,
        __maxDataNodes.set,
        None,
        "See the API specification for a description of the use of this data.",
    )

    # Attribute maxDataPoints uses Python identifier maxDataPoints
    __maxDataPoints = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "maxDataPoints"),
        "maxDataPoints",
        "__httpwww_witsml_orgapi141_objectWithConstraint_maxDataPoints",
        _module_typeBindings.positiveCount,
    )
    __maxDataPoints._DeclarationLocation = pyxb.utils.utility.Location(
        "../../../public/typ_dataTypes.xsd", 94, 4
    )
    __maxDataPoints._UseLocation = pyxb.utils.utility.Location(
        "../../../public/typ_dataTypes.xsd", 94, 4
    )

    maxDataPoints = property(
        __maxDataPoints.value,
        __maxDataPoints.set,
        None,
        "See the API specification for a description of the use of this data.",
    )

    _ElementMap.update({})
    _AttributeMap.update(
        {
            __maxDataNodes.name(): __maxDataNodes,
            __maxDataPoints.name(): __maxDataPoints,
        }
    )


_module_typeBindings.objectWithConstraint = objectWithConstraint
Namespace.addCategoryObject("typeBinding", "objectWithConstraint", objectWithConstraint)


# Complex type {http://www.witsml.org/api/141}growingTimeoutPeriod with content type SIMPLE
class growingTimeoutPeriod(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.witsml.org/api/141}growingTimeoutPeriod with content type SIMPLE"""

    _TypeDefinition = abstractPositiveCount
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "growingTimeoutPeriod")
    _XSDLocation = pyxb.utils.utility.Location(
        "../../../public/typ_dataTypes.xsd", 74, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is abstractPositiveCount

    # Attribute dataObject uses Python identifier dataObject
    __dataObject = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "dataObject"),
        "dataObject",
        "__httpwww_witsml_orgapi141_growingTimeoutPeriod_dataObject",
        _module_typeBindings.str64,
        required=True,
    )
    __dataObject._DeclarationLocation = pyxb.utils.utility.Location(
        "../../../public/typ_dataTypes.xsd", 77, 4
    )
    __dataObject._UseLocation = pyxb.utils.utility.Location(
        "../../../public/typ_dataTypes.xsd", 77, 4
    )

    dataObject = property(
        __dataObject.value,
        __dataObject.set,
        None,
        "See the API specification for a description of the use of this data.",
    )

    _ElementMap.update({})
    _AttributeMap.update({__dataObject.name(): __dataObject})


_module_typeBindings.growingTimeoutPeriod = growingTimeoutPeriod
Namespace.addCategoryObject("typeBinding", "growingTimeoutPeriod", growingTimeoutPeriod)


capClients = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "capClients"),
    obj_capClients,
    documentation='The WITSML API mandated plural root element which allows \n\t\t\tmultiple singular objects to be sent. The plural name is formed by adding\n\t\t\tan "s" to the singular name.\n\t\t\tPresent only for consistency with other WITSML data objects (multiple \n\t\t\tcapClient elements are not allowed). \n\t\t\t',
    location=pyxb.utils.utility.Location("../../../public/obj_capClient.xsd", 30, 1),
)
Namespace.addCategoryObject("elementBinding", capClients.name().localName(), capClients)


cs_contact._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "name"),
        str256,
        scope=cs_contact,
        documentation="See the API specification for a description of the use of this data.",
        location=pyxb.utils.utility.Location("../../../public/cs_contact.xsd", 23, 3),
    )
)

cs_contact._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "email"),
        str256,
        scope=cs_contact,
        documentation="See the API specification for a description of the use of this data.",
        location=pyxb.utils.utility.Location("../../../public/cs_contact.xsd", 28, 3),
    )
)

cs_contact._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "phone"),
        str256,
        scope=cs_contact,
        documentation="See the API specification for a description of the use of this data.",
        location=pyxb.utils.utility.Location("../../../public/cs_contact.xsd", 33, 3),
    )
)


def _BuildAutomaton():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location("../../../public/cs_contact.xsd", 23, 3),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location("../../../public/cs_contact.xsd", 28, 3),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location("../../../public/cs_contact.xsd", 33, 3),
    )
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        cs_contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, "name")),
        pyxb.utils.utility.Location("../../../public/cs_contact.xsd", 23, 3),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        cs_contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, "email")),
        pyxb.utils.utility.Location("../../../public/cs_contact.xsd", 28, 3),
    )
    st_1 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(
        cs_contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, "phone")),
        pyxb.utils.utility.Location("../../../public/cs_contact.xsd", 33, 3),
    )
    st_2 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_2, True)]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


cs_contact._Automaton = _BuildAutomaton()


obj_capClients._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "capClient"),
        obj_capClient,
        scope=obj_capClients,
        documentation="Defines the singular Client Capabilities (capClient) element; only one can be specified. \n\t\t\t\t\t",
        location=pyxb.utils.utility.Location(
            "../../../public/obj_capClient.xsd", 43, 3
        ),
    )
)


def _BuildAutomaton_():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "../../../public/obj_capClient.xsd", 43, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        obj_capClients._UseForTag(pyxb.namespace.ExpandedName(Namespace, "capClient")),
        pyxb.utils.utility.Location("../../../public/obj_capClient.xsd", 43, 3),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


obj_capClients._Automaton = _BuildAutomaton_()


obj_capClient._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "contact"),
        cs_contact,
        scope=obj_capClient,
        documentation="See the API specification for a description of the use of this data.",
        location=pyxb.utils.utility.Location(
            "../../../public/obj_capClient.xsd", 62, 3
        ),
    )
)

obj_capClient._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "description"),
        str4096,
        scope=obj_capClient,
        documentation="See the API specification for a description of the use of this data.",
        location=pyxb.utils.utility.Location(
            "../../../public/obj_capClient.xsd", 67, 3
        ),
    )
)

obj_capClient._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "name"),
        str64,
        scope=obj_capClient,
        documentation="See the API specification for a description of the use of this data.",
        location=pyxb.utils.utility.Location(
            "../../../public/obj_capClient.xsd", 72, 3
        ),
    )
)

obj_capClient._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "vendor"),
        str64,
        scope=obj_capClient,
        documentation="See the API specification for a description of the use of this data.",
        location=pyxb.utils.utility.Location(
            "../../../public/obj_capClient.xsd", 77, 3
        ),
    )
)

obj_capClient._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "version"),
        str64,
        scope=obj_capClient,
        documentation="See the API specification for a description of the use of this data.",
        location=pyxb.utils.utility.Location(
            "../../../public/obj_capClient.xsd", 82, 3
        ),
    )
)

obj_capClient._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "schemaVersion"),
        str64,
        scope=obj_capClient,
        documentation="See the API specification for a description of the use of this data.",
        location=pyxb.utils.utility.Location(
            "../../../public/obj_capClient.xsd", 87, 3
        ),
    )
)


def _BuildAutomaton_2():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "../../../public/obj_capClient.xsd", 62, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "../../../public/obj_capClient.xsd", 67, 3
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "../../../public/obj_capClient.xsd", 72, 3
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "../../../public/obj_capClient.xsd", 77, 3
        ),
    )
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "../../../public/obj_capClient.xsd", 82, 3
        ),
    )
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "../../../public/obj_capClient.xsd", 87, 3
        ),
    )
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        obj_capClient._UseForTag(pyxb.namespace.ExpandedName(Namespace, "contact")),
        pyxb.utils.utility.Location("../../../public/obj_capClient.xsd", 62, 3),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        obj_capClient._UseForTag(pyxb.namespace.ExpandedName(Namespace, "description")),
        pyxb.utils.utility.Location("../../../public/obj_capClient.xsd", 67, 3),
    )
    st_1 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(
        obj_capClient._UseForTag(pyxb.namespace.ExpandedName(Namespace, "name")),
        pyxb.utils.utility.Location("../../../public/obj_capClient.xsd", 72, 3),
    )
    st_2 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(
        obj_capClient._UseForTag(pyxb.namespace.ExpandedName(Namespace, "vendor")),
        pyxb.utils.utility.Location("../../../public/obj_capClient.xsd", 77, 3),
    )
    st_3 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(
        obj_capClient._UseForTag(pyxb.namespace.ExpandedName(Namespace, "version")),
        pyxb.utils.utility.Location("../../../public/obj_capClient.xsd", 82, 3),
    )
    st_4 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(
        obj_capClient._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "schemaVersion")
        ),
        pyxb.utils.utility.Location("../../../public/obj_capClient.xsd", 87, 3),
    )
    st_5 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_5, True)]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


obj_capClient._Automaton = _BuildAutomaton_2()
