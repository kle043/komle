# komle/bindings/v1411/api/cap_client.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:3b7fbd5f64431e9d44183d2bca44c1a87b88e242
# Generated 2022-04-21 03:35:58.111104 by PyXB version 1.2.6 using Python 3.10.4.final.0
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
    "urn:uuid:75c7df19-662d-440b-9358-945826e9f2fa"
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


# Complex type {http://www.witsml.org/api/141}obj_capServers with content type ELEMENT_ONLY
class obj_capServers(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.witsml.org/api/141}obj_capServers with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "obj_capServers")
    _XSDLocation = pyxb.utils.utility.Location(
        "../../../public/obj_capServer.xsd", 40, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.witsml.org/api/141}capServer uses Python identifier capServer
    __capServer = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "capServer"),
        "capServer",
        "__httpwww_witsml_orgapi141_obj_capServers_httpwww_witsml_orgapi141capServer",
        False,
        pyxb.utils.utility.Location("../../../public/obj_capServer.xsd", 47, 3),
    )

    capServer = property(__capServer.value, __capServer.set, None, None)

    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "version"),
        "version",
        "__httpwww_witsml_orgapi141_obj_capServers_version",
        _module_typeBindings.str16,
        fixed=True,
        unicode_default="1.4.1",
    )
    __version._DeclarationLocation = pyxb.utils.utility.Location(
        "../../../public/obj_capServer.xsd", 49, 2
    )
    __version._UseLocation = pyxb.utils.utility.Location(
        "../../../public/obj_capServer.xsd", 49, 2
    )

    version = property(
        __version.value,
        __version.set,
        None,
        "API schema version.  It is optional.\n\t\t\t\tIf the version is specified, its value must be set equal to the value specified by the \n\t\t\t\tversion's fixed attribute. Note that this is different from the data schema version.\n\t\t\t\t",
    )

    _ElementMap.update({__capServer.name(): __capServer})
    _AttributeMap.update({__version.name(): __version})


_module_typeBindings.obj_capServers = obj_capServers
Namespace.addCategoryObject("typeBinding", "obj_capServers", obj_capServers)


# Complex type {http://www.witsml.org/api/141}obj_capServer with content type ELEMENT_ONLY
class obj_capServer(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.witsml.org/api/141}obj_capServer with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "obj_capServer")
    _XSDLocation = pyxb.utils.utility.Location(
        "../../../public/obj_capServer.xsd", 59, 1
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.witsml.org/api/141}contact uses Python identifier contact
    __contact = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "contact"),
        "contact",
        "__httpwww_witsml_orgapi141_obj_capServer_httpwww_witsml_orgapi141contact",
        False,
        pyxb.utils.utility.Location("../../../public/obj_capServer.xsd", 61, 3),
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
        "__httpwww_witsml_orgapi141_obj_capServer_httpwww_witsml_orgapi141description",
        False,
        pyxb.utils.utility.Location("../../../public/obj_capServer.xsd", 66, 3),
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
        "__httpwww_witsml_orgapi141_obj_capServer_httpwww_witsml_orgapi141name",
        False,
        pyxb.utils.utility.Location("../../../public/obj_capServer.xsd", 71, 3),
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
        "__httpwww_witsml_orgapi141_obj_capServer_httpwww_witsml_orgapi141vendor",
        False,
        pyxb.utils.utility.Location("../../../public/obj_capServer.xsd", 76, 3),
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
        "__httpwww_witsml_orgapi141_obj_capServer_httpwww_witsml_orgapi141version",
        False,
        pyxb.utils.utility.Location("../../../public/obj_capServer.xsd", 81, 3),
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
        "__httpwww_witsml_orgapi141_obj_capServer_httpwww_witsml_orgapi141schemaVersion",
        False,
        pyxb.utils.utility.Location("../../../public/obj_capServer.xsd", 86, 3),
    )

    schemaVersion = property(
        __schemaVersion.value,
        __schemaVersion.set,
        None,
        "See the API specification for a description of the use of this data.",
    )

    # Element {http://www.witsml.org/api/141}changeDetectionPeriod uses Python identifier changeDetectionPeriod
    __changeDetectionPeriod = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "changeDetectionPeriod"),
        "changeDetectionPeriod",
        "__httpwww_witsml_orgapi141_obj_capServer_httpwww_witsml_orgapi141changeDetectionPeriod",
        False,
        pyxb.utils.utility.Location("../../../public/obj_capServer.xsd", 91, 3),
    )

    changeDetectionPeriod = property(
        __changeDetectionPeriod.value,
        __changeDetectionPeriod.set,
        None,
        "See the API specification for a description of the use of this data.",
    )

    # Element {http://www.witsml.org/api/141}growingTimeoutPeriod uses Python identifier growingTimeoutPeriod
    __growingTimeoutPeriod = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "growingTimeoutPeriod"),
        "growingTimeoutPeriod",
        "__httpwww_witsml_orgapi141_obj_capServer_httpwww_witsml_orgapi141growingTimeoutPeriod",
        True,
        pyxb.utils.utility.Location("../../../public/obj_capServer.xsd", 96, 3),
    )

    growingTimeoutPeriod = property(
        __growingTimeoutPeriod.value,
        __growingTimeoutPeriod.set,
        None,
        "See the API specification for a description of the use of this data.",
    )

    # Element {http://www.witsml.org/api/141}maxRequestLatestValues uses Python identifier maxRequestLatestValues
    __maxRequestLatestValues = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "maxRequestLatestValues"),
        "maxRequestLatestValues",
        "__httpwww_witsml_orgapi141_obj_capServer_httpwww_witsml_orgapi141maxRequestLatestValues",
        False,
        pyxb.utils.utility.Location("../../../public/obj_capServer.xsd", 101, 3),
    )

    maxRequestLatestValues = property(
        __maxRequestLatestValues.value,
        __maxRequestLatestValues.set,
        None,
        "See the API specification for a description of the use of this data.",
    )

    # Element {http://www.witsml.org/api/141}cascadedDelete uses Python identifier cascadedDelete
    __cascadedDelete = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "cascadedDelete"),
        "cascadedDelete",
        "__httpwww_witsml_orgapi141_obj_capServer_httpwww_witsml_orgapi141cascadedDelete",
        False,
        pyxb.utils.utility.Location("../../../public/obj_capServer.xsd", 106, 3),
    )

    cascadedDelete = property(
        __cascadedDelete.value,
        __cascadedDelete.set,
        None,
        "See the API specification for a description of the use of this data.",
    )

    # Element {http://www.witsml.org/api/141}supportUomConversion uses Python identifier supportUomConversion
    __supportUomConversion = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "supportUomConversion"),
        "supportUomConversion",
        "__httpwww_witsml_orgapi141_obj_capServer_httpwww_witsml_orgapi141supportUomConversion",
        False,
        pyxb.utils.utility.Location("../../../public/obj_capServer.xsd", 111, 3),
    )

    supportUomConversion = property(
        __supportUomConversion.value,
        __supportUomConversion.set,
        None,
        "See the API specification for a description of the use of this data.",
    )

    # Element {http://www.witsml.org/api/141}compressionMethod uses Python identifier compressionMethod
    __compressionMethod = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "compressionMethod"),
        "compressionMethod",
        "__httpwww_witsml_orgapi141_obj_capServer_httpwww_witsml_orgapi141compressionMethod",
        False,
        pyxb.utils.utility.Location("../../../public/obj_capServer.xsd", 116, 3),
    )

    compressionMethod = property(
        __compressionMethod.value,
        __compressionMethod.set,
        None,
        "See the API specification for a description of the use of this data.",
    )

    # Element {http://www.witsml.org/api/141}function uses Python identifier function
    __function = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "function"),
        "function",
        "__httpwww_witsml_orgapi141_obj_capServer_httpwww_witsml_orgapi141function",
        True,
        pyxb.utils.utility.Location("../../../public/obj_capServer.xsd", 121, 3),
    )

    function = property(
        __function.value,
        __function.set,
        None,
        "See the API specification for a description of the use of this data.",
    )

    # Attribute apiVers uses Python identifier apiVers
    __apiVers = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "apiVers"),
        "apiVers",
        "__httpwww_witsml_orgapi141_obj_capServer_apiVers",
        _module_typeBindings.str16,
        required=True,
    )
    __apiVers._DeclarationLocation = pyxb.utils.utility.Location(
        "../../../public/obj_capServer.xsd", 127, 2
    )
    __apiVers._UseLocation = pyxb.utils.utility.Location(
        "../../../public/obj_capServer.xsd", 127, 2
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
            __changeDetectionPeriod.name(): __changeDetectionPeriod,
            __growingTimeoutPeriod.name(): __growingTimeoutPeriod,
            __maxRequestLatestValues.name(): __maxRequestLatestValues,
            __cascadedDelete.name(): __cascadedDelete,
            __supportUomConversion.name(): __supportUomConversion,
            __compressionMethod.name(): __compressionMethod,
            __function.name(): __function,
        }
    )
    _AttributeMap.update({__apiVers.name(): __apiVers})


_module_typeBindings.obj_capServer = obj_capServer
Namespace.addCategoryObject("typeBinding", "obj_capServer", obj_capServer)


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


# Complex type {http://www.witsml.org/api/141}cs_function with content type ELEMENT_ONLY
class cs_function(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.witsml.org/api/141}cs_function with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "cs_function")
    _XSDLocation = pyxb.utils.utility.Location("../../../public/cs_function.xsd", 21, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.witsml.org/api/141}dataObject uses Python identifier dataObject
    __dataObject = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "dataObject"),
        "dataObject",
        "__httpwww_witsml_orgapi141_cs_function_httpwww_witsml_orgapi141dataObject",
        True,
        pyxb.utils.utility.Location("../../../public/cs_function.xsd", 23, 3),
    )

    dataObject = property(
        __dataObject.value,
        __dataObject.set,
        None,
        "See the API specification for a description of the use of this data.",
    )

    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "name"),
        "name",
        "__httpwww_witsml_orgapi141_cs_function_name",
        _module_typeBindings.str64,
        required=True,
    )
    __name._DeclarationLocation = pyxb.utils.utility.Location(
        "../../../public/cs_function.xsd", 29, 2
    )
    __name._UseLocation = pyxb.utils.utility.Location(
        "../../../public/cs_function.xsd", 29, 2
    )

    name = property(
        __name.value,
        __name.set,
        None,
        "See the API specification for a description of the use of this data.",
    )

    _ElementMap.update({__dataObject.name(): __dataObject})
    _AttributeMap.update({__name.name(): __name})


_module_typeBindings.cs_function = cs_function
Namespace.addCategoryObject("typeBinding", "cs_function", cs_function)


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


capServers = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "capServers"),
    obj_capServers,
    location=pyxb.utils.utility.Location("../../../public/obj_capServer.xsd", 30, 1),
)
Namespace.addCategoryObject("elementBinding", capServers.name().localName(), capServers)


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


obj_capServers._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "capServer"),
        obj_capServer,
        scope=obj_capServers,
        location=pyxb.utils.utility.Location(
            "../../../public/obj_capServer.xsd", 47, 3
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
            "../../../public/obj_capServer.xsd", 47, 3
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        obj_capServers._UseForTag(pyxb.namespace.ExpandedName(Namespace, "capServer")),
        pyxb.utils.utility.Location("../../../public/obj_capServer.xsd", 47, 3),
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


obj_capServers._Automaton = _BuildAutomaton_()


obj_capServer._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "contact"),
        cs_contact,
        scope=obj_capServer,
        documentation="See the API specification for a description of the use of this data.",
        location=pyxb.utils.utility.Location(
            "../../../public/obj_capServer.xsd", 61, 3
        ),
    )
)

obj_capServer._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "description"),
        str4096,
        scope=obj_capServer,
        documentation="See the API specification for a description of the use of this data.",
        location=pyxb.utils.utility.Location(
            "../../../public/obj_capServer.xsd", 66, 3
        ),
    )
)

obj_capServer._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "name"),
        str64,
        scope=obj_capServer,
        documentation="See the API specification for a description of the use of this data.",
        location=pyxb.utils.utility.Location(
            "../../../public/obj_capServer.xsd", 71, 3
        ),
    )
)

obj_capServer._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "vendor"),
        str64,
        scope=obj_capServer,
        documentation="See the API specification for a description of the use of this data.",
        location=pyxb.utils.utility.Location(
            "../../../public/obj_capServer.xsd", 76, 3
        ),
    )
)

obj_capServer._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "version"),
        str64,
        scope=obj_capServer,
        documentation="See the API specification for a description of the use of this data.",
        location=pyxb.utils.utility.Location(
            "../../../public/obj_capServer.xsd", 81, 3
        ),
    )
)

obj_capServer._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "schemaVersion"),
        str64,
        scope=obj_capServer,
        documentation="See the API specification for a description of the use of this data.",
        location=pyxb.utils.utility.Location(
            "../../../public/obj_capServer.xsd", 86, 3
        ),
    )
)

obj_capServer._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "changeDetectionPeriod"),
        nonNegativeCount,
        scope=obj_capServer,
        documentation="See the API specification for a description of the use of this data.",
        location=pyxb.utils.utility.Location(
            "../../../public/obj_capServer.xsd", 91, 3
        ),
    )
)

obj_capServer._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "growingTimeoutPeriod"),
        growingTimeoutPeriod,
        scope=obj_capServer,
        documentation="See the API specification for a description of the use of this data.",
        location=pyxb.utils.utility.Location(
            "../../../public/obj_capServer.xsd", 96, 3
        ),
    )
)

obj_capServer._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "maxRequestLatestValues"),
        positiveCount,
        scope=obj_capServer,
        documentation="See the API specification for a description of the use of this data.",
        location=pyxb.utils.utility.Location(
            "../../../public/obj_capServer.xsd", 101, 3
        ),
    )
)

obj_capServer._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "cascadedDelete"),
        pyxb.binding.datatypes.boolean,
        scope=obj_capServer,
        documentation="See the API specification for a description of the use of this data.",
        location=pyxb.utils.utility.Location(
            "../../../public/obj_capServer.xsd", 106, 3
        ),
    )
)

obj_capServer._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "supportUomConversion"),
        pyxb.binding.datatypes.boolean,
        scope=obj_capServer,
        documentation="See the API specification for a description of the use of this data.",
        location=pyxb.utils.utility.Location(
            "../../../public/obj_capServer.xsd", 111, 3
        ),
    )
)

obj_capServer._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "compressionMethod"),
        str64,
        scope=obj_capServer,
        documentation="See the API specification for a description of the use of this data.",
        location=pyxb.utils.utility.Location(
            "../../../public/obj_capServer.xsd", 116, 3
        ),
    )
)

obj_capServer._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "function"),
        cs_function,
        scope=obj_capServer,
        documentation="See the API specification for a description of the use of this data.",
        location=pyxb.utils.utility.Location(
            "../../../public/obj_capServer.xsd", 121, 3
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
            "../../../public/obj_capServer.xsd", 61, 3
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "../../../public/obj_capServer.xsd", 66, 3
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "../../../public/obj_capServer.xsd", 71, 3
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "../../../public/obj_capServer.xsd", 76, 3
        ),
    )
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "../../../public/obj_capServer.xsd", 81, 3
        ),
    )
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "../../../public/obj_capServer.xsd", 86, 3
        ),
    )
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "../../../public/obj_capServer.xsd", 91, 3
        ),
    )
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "../../../public/obj_capServer.xsd", 96, 3
        ),
    )
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "../../../public/obj_capServer.xsd", 101, 3
        ),
    )
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "../../../public/obj_capServer.xsd", 106, 3
        ),
    )
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "../../../public/obj_capServer.xsd", 111, 3
        ),
    )
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "../../../public/obj_capServer.xsd", 116, 3
        ),
    )
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "../../../public/obj_capServer.xsd", 121, 3
        ),
    )
    counters.add(cc_12)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        obj_capServer._UseForTag(pyxb.namespace.ExpandedName(Namespace, "contact")),
        pyxb.utils.utility.Location("../../../public/obj_capServer.xsd", 61, 3),
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
        obj_capServer._UseForTag(pyxb.namespace.ExpandedName(Namespace, "description")),
        pyxb.utils.utility.Location("../../../public/obj_capServer.xsd", 66, 3),
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
        obj_capServer._UseForTag(pyxb.namespace.ExpandedName(Namespace, "name")),
        pyxb.utils.utility.Location("../../../public/obj_capServer.xsd", 71, 3),
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
        obj_capServer._UseForTag(pyxb.namespace.ExpandedName(Namespace, "vendor")),
        pyxb.utils.utility.Location("../../../public/obj_capServer.xsd", 76, 3),
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
        obj_capServer._UseForTag(pyxb.namespace.ExpandedName(Namespace, "version")),
        pyxb.utils.utility.Location("../../../public/obj_capServer.xsd", 81, 3),
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
        obj_capServer._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "schemaVersion")
        ),
        pyxb.utils.utility.Location("../../../public/obj_capServer.xsd", 86, 3),
    )
    st_5 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(
        obj_capServer._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "changeDetectionPeriod")
        ),
        pyxb.utils.utility.Location("../../../public/obj_capServer.xsd", 91, 3),
    )
    st_6 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(
        obj_capServer._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "growingTimeoutPeriod")
        ),
        pyxb.utils.utility.Location("../../../public/obj_capServer.xsd", 96, 3),
    )
    st_7 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(
        obj_capServer._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "maxRequestLatestValues")
        ),
        pyxb.utils.utility.Location("../../../public/obj_capServer.xsd", 101, 3),
    )
    st_8 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(
        obj_capServer._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "cascadedDelete")
        ),
        pyxb.utils.utility.Location("../../../public/obj_capServer.xsd", 106, 3),
    )
    st_9 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(
        obj_capServer._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "supportUomConversion")
        ),
        pyxb.utils.utility.Location("../../../public/obj_capServer.xsd", 111, 3),
    )
    st_10 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(
        obj_capServer._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "compressionMethod")
        ),
        pyxb.utils.utility.Location("../../../public/obj_capServer.xsd", 116, 3),
    )
    st_11 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(
        obj_capServer._UseForTag(pyxb.namespace.ExpandedName(Namespace, "function")),
        pyxb.utils.utility.Location("../../../public/obj_capServer.xsd", 121, 3),
    )
    st_12 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_9, False)]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_10, True)]))
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_10, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_11, True)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_11, False)]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_12, True)]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


obj_capServer._Automaton = _BuildAutomaton_2()


cs_function._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "dataObject"),
        objectWithConstraint,
        scope=cs_function,
        documentation="See the API specification for a description of the use of this data.",
        location=pyxb.utils.utility.Location("../../../public/cs_function.xsd", 23, 3),
    )
)


def _BuildAutomaton_3():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location("../../../public/cs_function.xsd", 23, 3),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        cs_function._UseForTag(pyxb.namespace.ExpandedName(Namespace, "dataObject")),
        pyxb.utils.utility.Location("../../../public/cs_function.xsd", 23, 3),
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


cs_function._Automaton = _BuildAutomaton_3()

__version__ = "1.4.1.1"
