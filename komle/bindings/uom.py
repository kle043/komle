# komle/uom_bindings/uom.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:de5669d245f178776916647737ebc73cda75213c
# Generated 2020-04-19 10:21:50.429390 by PyXB version 1.2.6 using Python 3.7.5.final.0
# Namespace http://www.posc.org/schemas

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
    "urn:uuid:d0c8f168-8216-11ea-8441-f1a2c51e3802"
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
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(
    "http://www.posc.org/schemas", create_if_missing=True
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
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
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


# Union simple type: {http://www.posc.org/schemas}expandedDateTime
# superclasses pyxb.binding.datatypes.anySimpleType
class expandedDateTime(pyxb.binding.basis.STD_union):

    """Expand possibilities of dateTime format to include date, dateTime, gYearMonth, and gYear"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'expandedDateTime')
    _XSDLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 337, 0
    )
    _Documentation = 'Expand possibilities of dateTime format to include date, dateTime, gYearMonth, and gYear'

    _MemberTypes = (
        pyxb.binding.datatypes.dateTime,
        pyxb.binding.datatypes.date,
        pyxb.binding.datatypes.gYearMonth,
        pyxb.binding.datatypes.gYear,
    )


expandedDateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
expandedDateTime._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=expandedDateTime
)
expandedDateTime._InitializeFacetMap(
    expandedDateTime._CF_pattern, expandedDateTime._CF_enumeration
)
Namespace.addCategoryObject("typeBinding", "expandedDateTime", expandedDateTime)
_module_typeBindings.expandedDateTime = expandedDateTime

# Atomic simple type: {http://www.posc.org/schemas}keyid
class keyid(pyxb.binding.datatypes.string):

    """
    The keyid type is intended to be a replacement for the DTD, ID type, which is being deprecated. This type is intended to carry the same semantics as the ID type.
    """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'keyid')
    _XSDLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 456, 0
    )
    _Documentation = '\nThe keyid type is intended to be a replacement for the DTD, ID type, which is being deprecated. This type is intended to carry the same semantics as the ID type.\n    '


keyid._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'keyid', keyid)
_module_typeBindings.keyid = keyid

# Complex type {http://www.posc.org/schemas}documentInfoType with content type ELEMENT_ONLY
class documentInfoType(pyxb.binding.basis.complexTypeDefinition):
    """
    A convenience schema to capture a set of data that is relevant for many
    exchange documents. It includes information about the file that was created,
    and high-level information about the data that is being exchanged within the
    file.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'documentInfoType')
    _XSDLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 46, 0
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.posc.org/schemas}_DocClasses uses Python identifier DocClasses
    __DocClasses = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "_DocClasses"),
        "DocClasses",
        "__httpwww_posc_orgschemas_documentInfoType_httpwww_posc_orgschemas_DocClasses",
        True,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 35, 0
        ),
    )

    DocClasses = property(
        __DocClasses.value,
        __DocClasses.set,
        None,
        "\nAn abstract element, to serve as a head for a substitution group. The \n_DocClasses is intended to handle any classification systems that a group\nwould model. It may be a simple substitution, or a container with many\nclasses contained in it.\n                ",
    )

    # Element {http://www.posc.org/schemas}DocumentName uses Python identifier DocumentName
    __DocumentName = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "DocumentName"),
        "DocumentName",
        "__httpwww_posc_orgschemas_documentInfoType_httpwww_posc_orgschemasDocumentName",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 56, 2
        ),
    )

    DocumentName = property(
        __DocumentName.value,
        __DocumentName.set,
        None,
        "\nAn identifier for the document. This is intended to be unique within the \ncontext of the NamingSystem.\n                ",
    )

    # Element {http://www.posc.org/schemas}DocumentAlias uses Python identifier DocumentAlias
    __DocumentAlias = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "DocumentAlias"),
        "DocumentAlias",
        "__httpwww_posc_orgschemas_documentInfoType_httpwww_posc_orgschemasDocumentAlias",
        True,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 64, 2
        ),
    )

    DocumentAlias = property(
        __DocumentAlias.value,
        __DocumentAlias.set,
        None,
        "\nZero or more alternate names for the document. These names do not need to be\nunique within the naming system.\n                ",
    )

    # Element {http://www.posc.org/schemas}DocumentDate uses Python identifier DocumentDate
    __DocumentDate = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "DocumentDate"),
        "DocumentDate",
        "__httpwww_posc_orgschemas_documentInfoType_httpwww_posc_orgschemasDocumentDate",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 72, 2
        ),
    )

    DocumentDate = property(
        __DocumentDate.value,
        __DocumentDate.set,
        None,
        "\nThe date of the creation of the document. This is not the same as the date\nthat the file was created. For this date, the document is considered to be\nthe set of information associated with this document information.\nFor example, the document may be a seismic binset. This represents the date\nthat the binset was created. The FileCreation information would capture the\ndate that the XML file was created to send or exchange the binset.\n                ",
    )

    # Element {http://www.posc.org/schemas}FileCreationInformation uses Python identifier FileCreationInformation
    __FileCreationInformation = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "FileCreationInformation"),
        "FileCreationInformation",
        "__httpwww_posc_orgschemas_documentInfoType_httpwww_posc_orgschemasFileCreationInformation",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 93, 2
        ),
    )

    FileCreationInformation = property(
        __FileCreationInformation.value,
        __FileCreationInformation.set,
        None,
        "\nThe information about the creation of the exchange file. This is not about\nthe creation of the data within the file, but the creation of the file itself.\n                ",
    )

    # Element {http://www.posc.org/schemas}SecurityInformation uses Python identifier SecurityInformation
    __SecurityInformation = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "SecurityInformation"),
        "SecurityInformation",
        "__httpwww_posc_orgschemas_documentInfoType_httpwww_posc_orgschemasSecurityInformation",
        True,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 101, 2
        ),
    )

    SecurityInformation = property(
        __SecurityInformation.value,
        __SecurityInformation.set,
        None,
        "\nInformation about the security to be applied to this file. More than one\nclassification can be given.\n                ",
    )

    # Element {http://www.posc.org/schemas}Disclaimer uses Python identifier Disclaimer
    __Disclaimer = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Disclaimer"),
        "Disclaimer",
        "__httpwww_posc_orgschemas_documentInfoType_httpwww_posc_orgschemasDisclaimer",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 109, 2
        ),
    )

    Disclaimer = property(
        __Disclaimer.value,
        __Disclaimer.set,
        None,
        "\nA free-form string that allows a disclaimer to accompany the information.\n                ",
    )

    # Element {http://www.posc.org/schemas}AuditTrail uses Python identifier AuditTrail
    __AuditTrail = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "AuditTrail"),
        "AuditTrail",
        "__httpwww_posc_orgschemas_documentInfoType_httpwww_posc_orgschemasAuditTrail",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 116, 2
        ),
    )

    AuditTrail = property(
        __AuditTrail.value,
        __AuditTrail.set,
        None,
        "\nA collection of events that can document the history of the data.\n                ",
    )

    # Element {http://www.posc.org/schemas}DataOwnerRef uses Python identifier DataOwnerRef
    __DataOwnerRef = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "DataOwnerRef"),
        "DataOwnerRef",
        "__httpwww_posc_orgschemas_documentInfoType_httpwww_posc_orgschemasDataOwnerRef",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 131, 4
        ),
    )

    DataOwnerRef = property(__DataOwnerRef.value, __DataOwnerRef.set, None, None)

    # Element {http://www.posc.org/schemas}DataOwnerID uses Python identifier DataOwnerID
    __DataOwnerID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "DataOwnerID"),
        "DataOwnerID",
        "__httpwww_posc_orgschemas_documentInfoType_httpwww_posc_orgschemasDataOwnerID",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 132, 4
        ),
    )

    DataOwnerID = property(__DataOwnerID.value, __DataOwnerID.set, None, None)

    # Element {http://www.posc.org/schemas}Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Comment"),
        "Comment",
        "__httpwww_posc_orgschemas_documentInfoType_httpwww_posc_orgschemasComment",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 134, 2
        ),
    )

    Comment = property(
        __Comment.value,
        __Comment.set,
        None,
        "\nAn optional comment about the document.\n                ",
    )

    # Attribute modver uses Python identifier modver
    __modver = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "modver"),
        "modver",
        "__httpwww_posc_orgschemas_documentInfoType_modver",
        pyxb.binding.datatypes.string,
        fixed=True,
        unicode_default="1.1",
    )
    __modver._DeclarationLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 142, 1
    )
    __modver._UseLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 142, 1
    )

    modver = property(__modver.value, __modver.set, None, None)

    _ElementMap.update(
        {
            __DocClasses.name(): __DocClasses,
            __DocumentName.name(): __DocumentName,
            __DocumentAlias.name(): __DocumentAlias,
            __DocumentDate.name(): __DocumentDate,
            __FileCreationInformation.name(): __FileCreationInformation,
            __SecurityInformation.name(): __SecurityInformation,
            __Disclaimer.name(): __Disclaimer,
            __AuditTrail.name(): __AuditTrail,
            __DataOwnerRef.name(): __DataOwnerRef,
            __DataOwnerID.name(): __DataOwnerID,
            __Comment.name(): __Comment,
        }
    )
    _AttributeMap.update({__modver.name(): __modver})


_module_typeBindings.documentInfoType = documentInfoType
Namespace.addCategoryObject("typeBinding", "documentInfoType", documentInfoType)


# Complex type {http://www.posc.org/schemas}fileCrType with content type ELEMENT_ONLY
class fileCrType(pyxb.binding.basis.complexTypeDefinition):
    """
    A block of information about the creation of the XML file. This is different
    than the creation of the data that is included within the file.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'fileCrType')
    _XSDLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 145, 0
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.posc.org/schemas}FileCreationDate uses Python identifier FileCreationDate
    __FileCreationDate = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "FileCreationDate"),
        "FileCreationDate",
        "__httpwww_posc_orgschemas_fileCrType_httpwww_posc_orgschemasFileCreationDate",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 153, 2
        ),
    )

    FileCreationDate = property(
        __FileCreationDate.value,
        __FileCreationDate.set,
        None,
        "\nThe date and/or time that the file was created.\n                ",
    )

    # Element {http://www.posc.org/schemas}SoftwareName uses Python identifier SoftwareName
    __SoftwareName = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "SoftwareName"),
        "SoftwareName",
        "__httpwww_posc_orgschemas_fileCrType_httpwww_posc_orgschemasSoftwareName",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 160, 2
        ),
    )

    SoftwareName = property(
        __SoftwareName.value,
        __SoftwareName.set,
        None,
        "\nIf appropriate, the software that created the file. This is a free form\nstring, and may include whatever information is deemed relevant.\n                ",
    )

    # Element {http://www.posc.org/schemas}FileCreator uses Python identifier FileCreator
    __FileCreator = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "FileCreator"),
        "FileCreator",
        "__httpwww_posc_orgschemas_fileCrType_httpwww_posc_orgschemasFileCreator",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 168, 2
        ),
    )

    FileCreator = property(
        __FileCreator.value,
        __FileCreator.set,
        None,
        "\nThe person or business associate that created the file. This is a free\nform string.\n                ",
    )

    # Element {http://www.posc.org/schemas}Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Comment"),
        "Comment",
        "__httpwww_posc_orgschemas_fileCrType_httpwww_posc_orgschemasComment",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 176, 2
        ),
    )

    Comment = property(
        __Comment.value,
        __Comment.set,
        None,
        "\nAny comment that would be useful to further explain the creation of this\ninstance document.\n                ",
    )

    _ElementMap.update(
        {
            __FileCreationDate.name(): __FileCreationDate,
            __SoftwareName.name(): __SoftwareName,
            __FileCreator.name(): __FileCreator,
            __Comment.name(): __Comment,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.fileCrType = fileCrType
Namespace.addCategoryObject('typeBinding', 'fileCrType', fileCrType)


# Complex type {http://www.posc.org/schemas}securityInfoType with content type ELEMENT_ONLY
class securityInfoType(pyxb.binding.basis.complexTypeDefinition):
    """
    Information about the security classification of the document. This is
    intended as a documentation of the security so that the file will not
    inadvertently be sent to someone who is not allowed access to the data.
    This block also carries a date that the security classification expires.
    For example, a well log is confidential for a period of time, and then
    becomes open.
    All security classes are characterized by their classification systems.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'securityInfoType')
    _XSDLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 187, 0
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.posc.org/schemas}Class uses Python identifier Class
    __Class = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Class"),
        "Class",
        "__httpwww_posc_orgschemas_securityInfoType_httpwww_posc_orgschemasClass",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 200, 2
        ),
    )

    Class = property(
        __Class.value,
        __Class.set,
        None,
        "\nThe security class in which this document is classified. Examples would \nbe confidential, partner confidential, tight. The meaning of the class is\ndetermined by the System in which it is defined.\n                ",
    )

    # Element {http://www.posc.org/schemas}System uses Python identifier System
    __System = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "System"),
        "System",
        "__httpwww_posc_orgschemas_securityInfoType_httpwww_posc_orgschemasSystem",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 209, 2
        ),
    )

    System = property(
        __System.value,
        __System.set,
        None,
        "\nThe security classification system. This gives context to the meaning of the\nClass value.\n                ",
    )

    # Element {http://www.posc.org/schemas}EndDate uses Python identifier EndDate
    __EndDate = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "EndDate"),
        "EndDate",
        "__httpwww_posc_orgschemas_securityInfoType_httpwww_posc_orgschemasEndDate",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 217, 2
        ),
    )

    EndDate = property(
        __EndDate.value,
        __EndDate.set,
        None,
        "\nThe date on which this security class is no longer applicable.\n                ",
    )

    # Element {http://www.posc.org/schemas}Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Comment"),
        "Comment",
        "__httpwww_posc_orgschemas_securityInfoType_httpwww_posc_orgschemasComment",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 224, 2
        ),
    )

    Comment = property(
        __Comment.value,
        __Comment.set,
        None,
        "\nA general comment to further define the security class.\n                ",
    )

    _ElementMap.update(
        {
            __Class.name(): __Class,
            __System.name(): __System,
            __EndDate.name(): __EndDate,
            __Comment.name(): __Comment,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.securityInfoType = securityInfoType
Namespace.addCategoryObject("typeBinding", "securityInfoType", securityInfoType)


# Complex type {http://www.posc.org/schemas}auditType with content type ELEMENT_ONLY
class auditType(pyxb.binding.basis.complexTypeDefinition):
    """
    The audit records what happened to the data, to produce the data that is in
    this file. It consists of one or more events.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'auditType')
    _XSDLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 234, 0
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.posc.org/schemas}Event uses Python identifier Event
    __Event = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Event"),
        "Event",
        "__httpwww_posc_orgschemas_auditType_httpwww_posc_orgschemasEvent",
        True,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 242, 2
        ),
    )

    Event = property(__Event.value, __Event.set, None, None)

    _ElementMap.update({__Event.name(): __Event})
    _AttributeMap.update({})


_module_typeBindings.auditType = auditType
Namespace.addCategoryObject('typeBinding', 'auditType', auditType)


# Complex type {http://www.posc.org/schemas}eventType with content type ELEMENT_ONLY
class eventType(pyxb.binding.basis.complexTypeDefinition):
    """
    An event type captures the basic information about an event that has
    affected the data.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'eventType')
    _XSDLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 246, 0
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.posc.org/schemas}EventDate uses Python identifier EventDate
    __EventDate = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "EventDate"),
        "EventDate",
        "__httpwww_posc_orgschemas_eventType_httpwww_posc_orgschemasEventDate",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 254, 2
        ),
    )

    EventDate = property(
        __EventDate.value,
        __EventDate.set,
        None,
        "\nThe date on which the event took place.\n                ",
    )

    # Element {http://www.posc.org/schemas}ResponsiblePartyRef uses Python identifier ResponsiblePartyRef
    __ResponsiblePartyRef = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ResponsiblePartyRef"),
        "ResponsiblePartyRef",
        "__httpwww_posc_orgschemas_eventType_httpwww_posc_orgschemasResponsiblePartyRef",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 269, 3
        ),
    )

    ResponsiblePartyRef = property(
        __ResponsiblePartyRef.value, __ResponsiblePartyRef.set, None, None
    )

    # Element {http://www.posc.org/schemas}ResponsiblePartyID uses Python identifier ResponsiblePartyID
    __ResponsiblePartyID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ResponsiblePartyID"),
        "ResponsiblePartyID",
        "__httpwww_posc_orgschemas_eventType_httpwww_posc_orgschemasResponsiblePartyID",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 270, 3
        ),
    )

    ResponsiblePartyID = property(
        __ResponsiblePartyID.value, __ResponsiblePartyID.set, None, None
    )

    # Element {http://www.posc.org/schemas}Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Comment"),
        "Comment",
        "__httpwww_posc_orgschemas_eventType_httpwww_posc_orgschemasComment",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 272, 2
        ),
    )

    Comment = property(
        __Comment.value,
        __Comment.set,
        None,
        "\nA free form comment that can further define the event that occurred.\n                ",
    )

    _ElementMap.update(
        {
            __EventDate.name(): __EventDate,
            __ResponsiblePartyRef.name(): __ResponsiblePartyRef,
            __ResponsiblePartyID.name(): __ResponsiblePartyID,
            __Comment.name(): __Comment,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.eventType = eventType
Namespace.addCategoryObject('typeBinding', 'eventType', eventType)


# Complex type {http://www.posc.org/schemas}abstractFeatureType with content type ELEMENT_ONLY
class abstractFeatureType(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.posc.org/schemas}abstractFeatureType with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "abstractFeatureType")
    _XSDLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 282, 0
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.posc.org/schemas}Text uses Python identifier Text
    __Text = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Text"),
        "Text",
        "__httpwww_posc_orgschemas_abstractFeatureType_httpwww_posc_orgschemasText",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 284, 4
        ),
    )

    Text = property(__Text.value, __Text.set, None, None)

    _ElementMap.update({__Text.name(): __Text})
    _AttributeMap.update({})


_module_typeBindings.abstractFeatureType = abstractFeatureType
Namespace.addCategoryObject("typeBinding", "abstractFeatureType", abstractFeatureType)


# Complex type {http://www.posc.org/schemas}identifierType with content type ELEMENT_ONLY
class identifierType(pyxb.binding.basis.complexTypeDefinition):
    """
    A common way for handling names of objects. An identifier type must include a Name. It
    may also include a NamingSystem, which gives meaning to the name. Since Names and
    NamingSystems may change with time, it may also include a Version, to further refine the
    meaning of the name.
    Note that this three-part structure is based on the ISO Identifier type.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'identifierType')
    _XSDLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 288, 0
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.posc.org/schemas}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Name"),
        "Name",
        "__httpwww_posc_orgschemas_identifierType_httpwww_posc_orgschemasName",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 299, 4
        ),
    )

    Name = property(
        __Name.value,
        __Name.set,
        None,
        '\nThe name of the object being identified. It may or may not be a unique name, depending on the use of this type. When used as an "identifier," it should be a unique name, within the naming system. When used as an "alias," the name is not required to be unique.\n    ',
    )

    # Element {http://www.posc.org/schemas}NamingSystem uses Python identifier NamingSystem
    __NamingSystem = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "NamingSystem"),
        "NamingSystem",
        "__httpwww_posc_orgschemas_identifierType_httpwww_posc_orgschemasNamingSystem",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 307, 6
        ),
    )

    NamingSystem = property(
        __NamingSystem.value,
        __NamingSystem.set,
        None,
        "\nThe naming system under which the name is defined. For example, if the name is a person's social security number, the naming system would be SSN, or some equivalent code which represents that the name is a social security number. Since naming system may be a code, there are two attributes (nameRef and systemList), which may be used to lead an application to a registry, where meaning can be obtained for the code. \n    ",
    )

    # Element {http://www.posc.org/schemas}Version uses Python identifier Version
    __Version = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Version"),
        "Version",
        "__httpwww_posc_orgschemas_identifierType_httpwww_posc_orgschemasVersion",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 314, 6
        ),
    )

    Version = property(
        __Version.value,
        __Version.set,
        None,
        "\nWhen a naming system is declared, it may be further qualified by giving a version of the\nnaming system. This is needed only when a group puts out a new set of names that are not\nbackward compatible with a previous list.\n    ",
    )

    # Element {http://www.posc.org/schemas}Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Comment"),
        "Comment",
        "__httpwww_posc_orgschemas_identifierType_httpwww_posc_orgschemasComment",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 324, 4
        ),
    )

    Comment = property(__Comment.value, __Comment.set, None, None)

    _ElementMap.update(
        {
            __Name.name(): __Name,
            __NamingSystem.name(): __NamingSystem,
            __Version.name(): __Version,
            __Comment.name(): __Comment,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.identifierType = identifierType
Namespace.addCategoryObject('typeBinding', 'identifierType', identifierType)


# Complex type {http://www.posc.org/schemas}referenceToType with content type EMPTY
class referenceToType(pyxb.binding.basis.complexTypeDefinition):
    """
    A reference, with no content. The only attribute is href, which is a reference to another instance.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'referenceToType')
    _XSDLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 328, 0
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Attribute href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "href"),
        "href",
        "__httpwww_posc_orgschemas_referenceToType_href",
        pyxb.binding.datatypes.string,
        required=True,
    )
    __href._DeclarationLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 334, 1
    )
    __href._UseLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 334, 1
    )

    href = property(__href.value, __href.set, None, None)

    _ElementMap.update({})
    _AttributeMap.update({__href.name(): __href})


_module_typeBindings.referenceToType = referenceToType
Namespace.addCategoryObject('typeBinding', 'referenceToType', referenceToType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 25, 2
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.posc.org/schemas}DocumentInformation uses Python identifier DocumentInformation
    __DocumentInformation = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "DocumentInformation"),
        "DocumentInformation",
        "__httpwww_posc_orgschemas_CTD_ANON_httpwww_posc_orgschemasDocumentInformation",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 24, 0
        ),
    )

    DocumentInformation = property(
        __DocumentInformation.value,
        __DocumentInformation.set,
        None,
        "\nA standard name for an element of type documentInfoType. Other names may be \nused at the discretion of the developer.\n                  ",
    )

    # Element {http://www.posc.org/schemas}UnitsDefinition uses Python identifier UnitsDefinition
    __UnitsDefinition = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "UnitsDefinition"),
        "UnitsDefinition",
        "__httpwww_posc_orgschemas_CTD_ANON_httpwww_posc_orgschemasUnitsDefinition",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 28, 6
        ),
    )

    UnitsDefinition = property(
        __UnitsDefinition.value, __UnitsDefinition.set, None, None
    )

    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "version"),
        "version",
        "__httpwww_posc_orgschemas_CTD_ANON_version",
        pyxb.binding.datatypes.string,
    )
    __version._DeclarationLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 36, 4
    )
    __version._UseLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 36, 4
    )

    version = property(
        __version.value,
        __version.set,
        None,
        "The version of the dictionary. Optional.",
    )

    _ElementMap.update(
        {
            __DocumentInformation.name(): __DocumentInformation,
            __UnitsDefinition.name(): __UnitsDefinition,
        }
    )
    _AttributeMap.update({__version.name(): __version})


_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 29, 8
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.posc.org/schemas}UnitOfMeasure uses Python identifier UnitOfMeasure
    __UnitOfMeasure = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "UnitOfMeasure"),
        "UnitOfMeasure",
        "__httpwww_posc_orgschemas_CTD_ANON__httpwww_posc_orgschemasUnitOfMeasure",
        True,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 31, 12
        ),
    )

    UnitOfMeasure = property(__UnitOfMeasure.value, __UnitOfMeasure.set, None, None)

    _ElementMap.update({__UnitOfMeasure.name(): __UnitOfMeasure})
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type {http://www.posc.org/schemas}explicitType with content type SIMPLE
class explicitType(pyxb.binding.basis.complexTypeDefinition):
    """
    If isExplicit is true, the uom is explicitly contained in and defined in
    the referenced catalog. If isExplicity is false, the uom is implicitly
    present. For example, a catalog may contain a metre (m), and a second (s),
     and allow a units algebra. Thus, the unit of velocity, metre/second (m/s),
    may not explicitly be in the catalog. But it is implied by the algebra
    which allows units division.
    """

    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'explicitType')
    _XSDLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 297, 0
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string

    # Attribute isExplicit uses Python identifier isExplicit
    __isExplicit = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "isExplicit"),
        "isExplicit",
        "__httpwww_posc_orgschemas_explicitType_isExplicit",
        pyxb.binding.datatypes.boolean,
    )
    __isExplicit._DeclarationLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 310, 6
    )
    __isExplicit._UseLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 310, 6
    )

    isExplicit = property(__isExplicit.value, __isExplicit.set, None, None)

    _ElementMap.update({})
    _AttributeMap.update({__isExplicit.name(): __isExplicit})


_module_typeBindings.explicitType = explicitType
Namespace.addCategoryObject('typeBinding', 'explicitType', explicitType)


# Complex type {http://www.posc.org/schemas}baseUnitType with content type ELEMENT_ONLY
class baseUnitType(pyxb.binding.basis.complexTypeDefinition):
    """
    A base unit, by our defintion, is one which represents a type of quantity,
    and therefore has no conversion. It is the unit to which all others of the
    quantity type are referenced. Base units may be among the basic types
    defined by ISO (m, s, K, etc), or they may be units derived from these using
    units algebra (m/s, Newtons, Pascals, etc). The definition (description) of
    the unit may be given, along with the Basic Authority which defines it.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'baseUnitType')
    _XSDLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 315, 0
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.posc.org/schemas}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Description"),
        "Description",
        "__httpwww_posc_orgschemas_baseUnitType_httpwww_posc_orgschemasDescription",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 327, 2
        ),
    )

    Description = property(__Description.value, __Description.set, None, None)

    # Element {http://www.posc.org/schemas}BasicAuthority uses Python identifier BasicAuthority
    __BasicAuthority = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "BasicAuthority"),
        "BasicAuthority",
        "__httpwww_posc_orgschemas_baseUnitType_httpwww_posc_orgschemasBasicAuthority",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 328, 2
        ),
    )

    BasicAuthority = property(__BasicAuthority.value, __BasicAuthority.set, None, None)

    _ElementMap.update(
        {
            __Description.name(): __Description,
            __BasicAuthority.name(): __BasicAuthority,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.baseUnitType = baseUnitType
Namespace.addCategoryObject('typeBinding', 'baseUnitType', baseUnitType)


# Complex type {http://www.posc.org/schemas}sameUnitType with content type EMPTY
class sameUnitType(pyxb.binding.basis.complexTypeDefinition):
    """
    Information from several catalogs may be recorded by stating that uoms from
    different catalogs are the same. This is generally given by the uom "symbol"
    in another catalog, along with the naming system. The uom may alternatively
    be resolved as an actual reference to another XML registry, although this
    interpretation is not required.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'sameUnitType')
    _XSDLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 332, 0
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "uom"),
        "uom",
        "__httpwww_posc_orgschemas_sameUnitType_uom",
        pyxb.binding.datatypes.string,
        required=True,
    )
    __uom._DeclarationLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 342, 2
    )
    __uom._UseLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 342, 2
    )

    uom = property(__uom.value, __uom.set, None, None)

    # Attribute namingSystem uses Python identifier namingSystem
    __namingSystem = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "namingSystem"),
        "namingSystem",
        "__httpwww_posc_orgschemas_sameUnitType_namingSystem",
        pyxb.binding.datatypes.string,
    )
    __namingSystem._DeclarationLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 343, 2
    )
    __namingSystem._UseLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 343, 2
    )

    namingSystem = property(__namingSystem.value, __namingSystem.set, None, None)

    _ElementMap.update({})
    _AttributeMap.update({__uom.name(): __uom, __namingSystem.name(): __namingSystem})


_module_typeBindings.sameUnitType = sameUnitType
Namespace.addCategoryObject('typeBinding', 'sameUnitType', sameUnitType)


# Complex type {http://www.posc.org/schemas}compositeUnitType with content type ELEMENT_ONLY
class compositeUnitType(pyxb.binding.basis.complexTypeDefinition):
    """
    A composite unit may be defined by giving the units and the exponents needed
    to form the composite. For example, a square foot would be a single UnitTerm,
    with uom attribute = 'ft', and exponent attriube = '2'. A Newton (kg.m/s2)
    would be three terms, with the kg (kilogram) unit having an exponent = '1',
    a m (metre) unit with exponent = '1', and a s (second) unit having
    exponent = '-2'.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'compositeUnitType')
    _XSDLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 346, 0
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.posc.org/schemas}UnitTerm uses Python identifier UnitTerm
    __UnitTerm = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "UnitTerm"),
        "UnitTerm",
        "__httpwww_posc_orgschemas_compositeUnitType_httpwww_posc_orgschemasUnitTerm",
        True,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 358, 4
        ),
    )

    UnitTerm = property(__UnitTerm.value, __UnitTerm.set, None, None)

    _ElementMap.update({__UnitTerm.name(): __UnitTerm})
    _AttributeMap.update({})


_module_typeBindings.compositeUnitType = compositeUnitType
Namespace.addCategoryObject("typeBinding", "compositeUnitType", compositeUnitType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_2(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 359, 6
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "uom"),
        "uom",
        "__httpwww_posc_orgschemas_CTD_ANON_2_uom",
        pyxb.binding.datatypes.anyURI,
        required=True,
    )
    __uom._DeclarationLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 360, 8
    )
    __uom._UseLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 360, 8
    )

    uom = property(__uom.value, __uom.set, None, None)

    # Attribute exponent uses Python identifier exponent
    __exponent = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "exponent"),
        "exponent",
        "__httpwww_posc_orgschemas_CTD_ANON_2_exponent",
        pyxb.binding.datatypes.integer,
        required=True,
    )
    __exponent._DeclarationLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 361, 8
    )
    __exponent._UseLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 361, 8
    )

    exponent = property(__exponent.value, __exponent.set, None, None)

    _ElementMap.update({})
    _AttributeMap.update({__uom.name(): __uom, __exponent.name(): __exponent})


_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type {http://www.posc.org/schemas}conversionType with content type ELEMENT_ONLY
class conversionType(pyxb.binding.basis.complexTypeDefinition):
    """
    A conversion to a base unit is defined as (A + BX)/(C + DX), where X is the
    unit to be converted. The A, B, C, D are contained in the Formula choice.
    Special cases are a single factor and a fraction. Examples are given with
    the different elements. One of the three choices is mandatory.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'conversionType')
    _XSDLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 367, 0
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.posc.org/schemas}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Description"),
        "Description",
        "__httpwww_posc_orgschemas_conversionType_httpwww_posc_orgschemasDescription",
        True,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 377, 2
        ),
    )

    Description = property(
        __Description.value,
        __Description.set,
        None,
        "\nA definition, description, or other comment about the unit of measure.\n              ",
    )

    # Element {http://www.posc.org/schemas}Factor uses Python identifier Factor
    __Factor = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Factor"),
        "Factor",
        "__httpwww_posc_orgschemas_conversionType_httpwww_posc_orgschemasFactor",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 385, 4
        ),
    )

    Factor = property(
        __Factor.value,
        __Factor.set,
        None,
        '\nIf A = D = 0, and C = 1, the value of B becomes a factor. For example, \nthe conversion of an international foot to a metre is with Factor=".3048"\n              ',
    )

    # Element {http://www.posc.org/schemas}Fraction uses Python identifier Fraction
    __Fraction = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Fraction"),
        "Fraction",
        "__httpwww_posc_orgschemas_conversionType_httpwww_posc_orgschemasFraction",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 393, 4
        ),
    )

    Fraction = property(
        __Fraction.value,
        __Fraction.set,
        None,
        "\nIf A = D = 0, B and C represent a fraction. For example, the conversion of a \nUS Survey foot to a metre is given with the fraction of 12 / 39.37. Hence,\n Numerator = '12', Denominator = '39.37'\n              ",
    )

    # Element {http://www.posc.org/schemas}Formula uses Python identifier Formula
    __Formula = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Formula"),
        "Formula",
        "__httpwww_posc_orgschemas_conversionType_httpwww_posc_orgschemasFormula",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 408, 4
        ),
    )

    Formula = property(
        __Formula.value,
        __Formula.set,
        None,
        '\nA few units of measure do not have a factor or fraction. For example the \nconversion from degrees Celcius to Kelvin is given as degK = 273.15 + degC. \nHence, A = "273.15", B = "1.", C = "1.", D = "0."\n              ',
    )

    # Attribute baseUnit uses Python identifier baseUnit
    __baseUnit = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "baseUnit"),
        "baseUnit",
        "__httpwww_posc_orgschemas_conversionType_baseUnit",
        pyxb.binding.datatypes.anyURI,
        required=True,
    )
    __baseUnit._DeclarationLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 428, 1
    )
    __baseUnit._UseLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 428, 1
    )

    baseUnit = property(
        __baseUnit.value,
        __baseUnit.set,
        None,
        "\nThe conversion is to a base unit. This attribute is a reference to the base \nunit. The base unit is generally defined within the same document, although \nthis does not need to be the case.\n              ",
    )

    # Attribute modver uses Python identifier modver
    __modver = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "modver"),
        "modver",
        "__httpwww_posc_orgschemas_conversionType_modver",
        pyxb.binding.datatypes.string,
        fixed=True,
        unicode_default="2.0",
    )
    __modver._DeclarationLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 437, 1
    )
    __modver._UseLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 437, 1
    )

    modver = property(__modver.value, __modver.set, None, None)

    _ElementMap.update(
        {
            __Description.name(): __Description,
            __Factor.name(): __Factor,
            __Fraction.name(): __Fraction,
            __Formula.name(): __Formula,
        }
    )
    _AttributeMap.update({__baseUnit.name(): __baseUnit, __modver.name(): __modver})


_module_typeBindings.conversionType = conversionType
Namespace.addCategoryObject('typeBinding', 'conversionType', conversionType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3(pyxb.binding.basis.complexTypeDefinition):
    """
    If A = D = 0, B and C represent a fraction. For example, the conversion of a
    US Survey foot to a metre is given with the fraction of 12 / 39.37. Hence,
     Numerator = '12', Denominator = '39.37'
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 401, 5
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.posc.org/schemas}Numerator uses Python identifier Numerator
    __Numerator = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Numerator"),
        "Numerator",
        "__httpwww_posc_orgschemas_CTD_ANON_3_httpwww_posc_orgschemasNumerator",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 403, 8
        ),
    )

    Numerator = property(__Numerator.value, __Numerator.set, None, None)

    # Element {http://www.posc.org/schemas}Denominator uses Python identifier Denominator
    __Denominator = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Denominator"),
        "Denominator",
        "__httpwww_posc_orgschemas_CTD_ANON_3_httpwww_posc_orgschemasDenominator",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 404, 8
        ),
    )

    Denominator = property(__Denominator.value, __Denominator.set, None, None)

    _ElementMap.update(
        {__Numerator.name(): __Numerator, __Denominator.name(): __Denominator}
    )
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4(pyxb.binding.basis.complexTypeDefinition):
    """
    A few units of measure do not have a factor or fraction. For example the
    conversion from degrees Celcius to Kelvin is given as degK = 273.15 + degC.
    Hence, A = "273.15", B = "1.", C = "1.", D = "0."
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 416, 5
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.posc.org/schemas}A uses Python identifier A
    __A = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "A"),
        "A",
        "__httpwww_posc_orgschemas_CTD_ANON_4_httpwww_posc_orgschemasA",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 418, 8
        ),
    )

    A = property(__A.value, __A.set, None, None)

    # Element {http://www.posc.org/schemas}B uses Python identifier B
    __B = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "B"),
        "B",
        "__httpwww_posc_orgschemas_CTD_ANON_4_httpwww_posc_orgschemasB",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 419, 8
        ),
    )

    B = property(__B.value, __B.set, None, None)

    # Element {http://www.posc.org/schemas}C uses Python identifier C
    __C = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "C"),
        "C",
        "__httpwww_posc_orgschemas_CTD_ANON_4_httpwww_posc_orgschemasC",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 420, 8
        ),
    )

    C = property(__C.value, __C.set, None, None)

    # Element {http://www.posc.org/schemas}D uses Python identifier D
    __D = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "D"),
        "D",
        "__httpwww_posc_orgschemas_CTD_ANON_4_httpwww_posc_orgschemasD",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 421, 8
        ),
    )

    D = property(__D.value, __D.set, None, None)

    _ElementMap.update(
        {__A.name(): __A, __B.name(): __B, __C.name(): __C, __D.name(): __D}
    )
    _AttributeMap.update({})


_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type {http://www.posc.org/schemas}displayType with content type MIXED
class displayType(pyxb.binding.basis.complexTypeDefinition):
    """
    This implementation of displayType allows a mixed type. It allows the
    inclusion of a sub element (for subscript), sup element (for superscript),
    and gr element (for greek). The greek symbol is given as a Unicode hex value.
    For example, the mu would be X03BC.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'displayType')
    _XSDLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 440, 0
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.posc.org/schemas}sup uses Python identifier sup
    __sup = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "sup"),
        "sup",
        "__httpwww_posc_orgschemas_displayType_httpwww_posc_orgschemassup",
        True,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 450, 4
        ),
    )

    sup = property(__sup.value, __sup.set, None, None)

    # Element {http://www.posc.org/schemas}sub uses Python identifier sub
    __sub = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "sub"),
        "sub",
        "__httpwww_posc_orgschemas_displayType_httpwww_posc_orgschemassub",
        True,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 451, 4
        ),
    )

    sub = property(__sub.value, __sub.set, None, None)

    # Element {http://www.posc.org/schemas}gr uses Python identifier gr
    __gr = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "gr"),
        "gr",
        "__httpwww_posc_orgschemas_displayType_httpwww_posc_orgschemasgr",
        True,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 452, 4
        ),
    )

    gr = property(__gr.value, __gr.set, None, None)

    _ElementMap.update({__sup.name(): __sup, __sub.name(): __sub, __gr.name(): __gr})
    _AttributeMap.update({})


_module_typeBindings.displayType = displayType
Namespace.addCategoryObject('typeBinding', 'displayType', displayType)


# Complex type {http://www.posc.org/schemas}unitDictionaryType with content type ELEMENT_ONLY
class unitDictionaryType(pyxb.binding.basis.complexTypeDefinition):
    """
    A standard form for a units dictionary. This allows the developer of the
    dictionary to record the basic information about a unit of measure (namely,
    is it a base unit or a customary unit, convertible to a base unit. And what
    is the conversion). It also allows some additional information, such as a
    mapping to other unit dictionaries (using the Same Unit element). It also
    allows a choice of unit symbols.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "unitDictionaryType")
    _XSDLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 44, 0
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.posc.org/schemas}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Name"),
        "Name",
        "__httpwww_posc_orgschemas_unitDictionaryType_httpwww_posc_orgschemasName",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 56, 4
        ),
    )

    Name = property(
        __Name.value,
        __Name.set,
        None,
        "\nThe name of the unit. This does not necessarily need to be unique within \nthe catalog, but it probably should be. For example, there are several types \nof feet, all with different conversions. It is based on the converstions \nthat we should find the uniqueness.\n              ",
    )

    # Element {http://www.posc.org/schemas}QuantityType uses Python identifier QuantityType
    __QuantityType = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "QuantityType"),
        "QuantityType",
        "__httpwww_posc_orgschemas_unitDictionaryType_httpwww_posc_orgschemasQuantityType",
        True,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 66, 4
        ),
    )

    QuantityType = property(
        __QuantityType.value,
        __QuantityType.set,
        None,
        "\nThis is an uncontrolled list to specify the quantity type that this uom is \nused for. Examples would be length, temperature, pressure, density.\n              ",
    )

    # Element {http://www.posc.org/schemas}DimensionalClass uses Python identifier DimensionalClass
    __DimensionalClass = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "DimensionalClass"),
        "DimensionalClass",
        "__httpwww_posc_orgschemas_unitDictionaryType_httpwww_posc_orgschemasDimensionalClass",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 74, 4
        ),
    )

    DimensionalClass = property(
        __DimensionalClass.value,
        __DimensionalClass.set,
        None,
        "\nThe dimensional analysis of the unit. For example, a metre (m) would be of class [L], which represents length. A foot (ft) would also be in this class. Abbreviations used are L = length, M = mass, T = time, 1 = dimensionless, K = temperature, C = current, N = amount (mole), A = angle (radian), S = solid angle (sr), B = light amount (cd). For consistency, the values are broken into numerator and denominator, separated by a slash (/), in alphabetical order (LM, not ML). \n              ",
    )

    # Element {http://www.posc.org/schemas}SameUnit uses Python identifier SameUnit
    __SameUnit = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "SameUnit"),
        "SameUnit",
        "__httpwww_posc_orgschemas_unitDictionaryType_httpwww_posc_orgschemasSameUnit",
        True,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 81, 4
        ),
    )

    SameUnit = property(
        __SameUnit.value,
        __SameUnit.set,
        None,
        "\nA unit of measure may have different expressions in different registries. \nThis allows zero or more of these mappings to be recorded. The SameUnit \nallows a uom and a naming system to be given. The uom is presumably the \nunique symbol in the other system.\n              ",
    )

    # Element {http://www.posc.org/schemas}CatalogName uses Python identifier CatalogName
    __CatalogName = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CatalogName"),
        "CatalogName",
        "__httpwww_posc_orgschemas_unitDictionaryType_httpwww_posc_orgschemasCatalogName",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 91, 4
        ),
    )

    CatalogName = property(
        __CatalogName.value,
        __CatalogName.set,
        None,
        "\nA uom is generally defined in a standard catalog of units somewhere. \nThis is the name of that catalog. The combination of CatalogName and \nCatalogSymbol should be unique.\n              ",
    )

    # Element {http://www.posc.org/schemas}CatalogSymbol uses Python identifier CatalogSymbol
    __CatalogSymbol = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CatalogSymbol"),
        "CatalogSymbol",
        "__httpwww_posc_orgschemas_unitDictionaryType_httpwww_posc_orgschemasCatalogSymbol",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 100, 4
        ),
    )

    CatalogSymbol = property(
        __CatalogSymbol.value,
        __CatalogSymbol.set,
        None,
        "\nThe symbol taken from the catalog. Within the catalog, defined by \nCatalogName, the CatalogSymbol should be unique. This element has an \nattribute, isExplicit, which states whether a uom symbol is explicitly \nin the catalog, or only implicitly defined.\n              ",
    )

    # Element {http://www.posc.org/schemas}Display uses Python identifier Display
    __Display = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Display"),
        "Display",
        "__httpwww_posc_orgschemas_unitDictionaryType_httpwww_posc_orgschemasDisplay",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 110, 4
        ),
    )

    Display = property(
        __Display.value,
        __Display.set,
        None,
        "\nThis allows a unit to have tags that define a display. For example, a sub \nelement may be used to indicate a subscript. The displayType allows one more \nstandard choice for displaying a uom, depending on the medium that the \ninformation is being displayed on.\n              ",
    )

    # Element {http://www.posc.org/schemas}Deprecated uses Python identifier Deprecated
    __Deprecated = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Deprecated"),
        "Deprecated",
        "__httpwww_posc_orgschemas_unitDictionaryType_httpwww_posc_orgschemasDeprecated",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 120, 4
        ),
    )

    Deprecated = property(
        __Deprecated.value,
        __Deprecated.set,
        None,
        "\nThis element is used to indicate that a unit is being deprecated. Normally, this means that the symbol representing the unit is no longer to be used (CatalogSymbol). It is generally replaced by another instance of the unit, which has a different symbol. For example, a cubic foot, with symbol, cu ft, would be deprecated, but there would be another instance of cubic foot, with symbol, ft3. The value of the instance repesents the version of the dictionary for which the value is first deprecated. A deprecated unit (symbol) is carried for backward compatibility, but will, at some point, be removed.\n              ",
    )

    # Element {http://www.posc.org/schemas}BaseUnit uses Python identifier BaseUnit
    __BaseUnit = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "BaseUnit"),
        "BaseUnit",
        "__httpwww_posc_orgschemas_unitDictionaryType_httpwww_posc_orgschemasBaseUnit",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 138, 6
        ),
    )

    BaseUnit = property(__BaseUnit.value, __BaseUnit.set, None, None)

    # Element {http://www.posc.org/schemas}ConversionToBaseUnit uses Python identifier ConversionToBaseUnit
    __ConversionToBaseUnit = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ConversionToBaseUnit"),
        "ConversionToBaseUnit",
        "__httpwww_posc_orgschemas_unitDictionaryType_httpwww_posc_orgschemasConversionToBaseUnit",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 139, 6
        ),
    )

    ConversionToBaseUnit = property(
        __ConversionToBaseUnit.value, __ConversionToBaseUnit.set, None, None
    )

    # Element {http://www.posc.org/schemas}CompositeUnit uses Python identifier CompositeUnit
    __CompositeUnit = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CompositeUnit"),
        "CompositeUnit",
        "__httpwww_posc_orgschemas_unitDictionaryType_httpwww_posc_orgschemasCompositeUnit",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 141, 4
        ),
    )

    CompositeUnit = property(
        __CompositeUnit.value,
        __CompositeUnit.set,
        None,
        "\nA composite unit can be formed by an algebra of units. For example, a foot \nper second (quantity type of velocity) can be formed by a foot divided by \na second. This element allows the registry to identify composite units. \nNote that a composite unit is chosen to represent a quantity type.\nExample: metre per second. This uom is the base unit for the quantity type \nof velocity. A foot per second is also a composite unit, and can be converted \nto the base unit by defining a conversion formula.\n              ",
    )

    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "id"),
        "id",
        "__httpwww_posc_orgschemas_unitDictionaryType_id",
        _module_typeBindings.keyid,
        required=True,
    )
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 155, 2
    )
    __id._UseLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 155, 2
    )

    id = property(
        __id.value,
        __id.set,
        None,
        '\nThis is a key for referencing the unit in the dictionary. The id value \nshould be unique within the dictionary document. The value should carry \nno semantic meaning. However, it is common to use a simple unit symbol for \nthe id. Because of the requirements of DTD\'s, it was necessary to separate \nout the id, which was originally of type ID. The DTD ID type did not allow \nslashes "/" or spaces or astericks (*).\n              ',
    )

    # Attribute annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "annotation"),
        "annotation",
        "__httpwww_posc_orgschemas_unitDictionaryType_annotation",
        pyxb.binding.datatypes.string,
    )
    __annotation._DeclarationLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 167, 2
    )
    __annotation._UseLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 167, 2
    )

    annotation = property(
        __annotation.value,
        __annotation.set,
        None,
        '\nFor backward compatibility, the id value was selected to be a value of type \nID. Hence, a value, such as ft/s, could not be used for the ID value. The \nannotation attribute was introduced as a schema attribute that could allow \nthe "/". Hence, ft/s is possible. This is intended to be a simple annotation,\n based on the 7 bit ascii character set. A more complex display symbol can \nbe built using the Display element.\n              ',
    )

    # Attribute modver uses Python identifier modver
    __modver = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "modver"),
        "modver",
        "__httpwww_posc_orgschemas_unitDictionaryType_modver",
        pyxb.binding.datatypes.string,
        fixed=True,
        unicode_default="2.0",
    )
    __modver._DeclarationLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 179, 2
    )
    __modver._UseLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 179, 2
    )

    modver = property(__modver.value, __modver.set, None, None)

    _ElementMap.update(
        {
            __Name.name(): __Name,
            __QuantityType.name(): __QuantityType,
            __DimensionalClass.name(): __DimensionalClass,
            __SameUnit.name(): __SameUnit,
            __CatalogName.name(): __CatalogName,
            __CatalogSymbol.name(): __CatalogSymbol,
            __Display.name(): __Display,
            __Deprecated.name(): __Deprecated,
            __BaseUnit.name(): __BaseUnit,
            __ConversionToBaseUnit.name(): __ConversionToBaseUnit,
            __CompositeUnit.name(): __CompositeUnit,
        }
    )
    _AttributeMap.update(
        {
            __id.name(): __id,
            __annotation.name(): __annotation,
            __modver.name(): __modver,
        }
    )


_module_typeBindings.unitDictionaryType = unitDictionaryType
Namespace.addCategoryObject("typeBinding", "unitDictionaryType", unitDictionaryType)


# Complex type {http://www.posc.org/schemas}unitDefinitionType with content type ELEMENT_ONLY
class unitDefinitionType(pyxb.binding.basis.complexTypeDefinition):
    """
    The unitDefinitionType is the same as the unitDictionaryType, with two
    exceptions. It contains a possible IsUnknown element. It does not contain a
    SameUnit. A unitDictionaryType is intended as a type for a registry, in which
    all units are known and are being declared with their defintions. However,
    when exchanging data, the sender may be passing through a value and uom, and
    is not sure what the appropriate definition is for the uom. For example it
    may read a file with FT as a uom, and the sender is not sure which type of
    foot this is. When defining the uom in the resolution section, he may state
    that the uom is unknown, but is probably ... an international foot.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "unitDefinitionType")
    _XSDLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 182, 0
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.posc.org/schemas}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Name"),
        "Name",
        "__httpwww_posc_orgschemas_unitDefinitionType_httpwww_posc_orgschemasName",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 197, 4
        ),
    )

    Name = property(
        __Name.value,
        __Name.set,
        None,
        "\nThe name of the unit. This does not necessarily need to be unique within \nthe catalog, but it probably should be. For example, there are several types \nof feet, all with different conversions. It is based on the converstions \nthat we should find the uniqueness.\n              ",
    )

    # Element {http://www.posc.org/schemas}QuantityType uses Python identifier QuantityType
    __QuantityType = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "QuantityType"),
        "QuantityType",
        "__httpwww_posc_orgschemas_unitDefinitionType_httpwww_posc_orgschemasQuantityType",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 207, 4
        ),
    )

    QuantityType = property(
        __QuantityType.value,
        __QuantityType.set,
        None,
        "\nThis is an uncontrolled list to specify the quantity type that this uom is \nused for. Examples would be length, temperature, pressure, density.\n              ",
    )

    # Element {http://www.posc.org/schemas}CatalogName uses Python identifier CatalogName
    __CatalogName = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CatalogName"),
        "CatalogName",
        "__httpwww_posc_orgschemas_unitDefinitionType_httpwww_posc_orgschemasCatalogName",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 215, 4
        ),
    )

    CatalogName = property(
        __CatalogName.value,
        __CatalogName.set,
        None,
        "\nA uom is generally defined in a standard catalog of units somewhere. \nThis is the name of that catalog. The combination of CatalogName and \nCatalogSymbol should be unique.\n              ",
    )

    # Element {http://www.posc.org/schemas}CatalogSymbol uses Python identifier CatalogSymbol
    __CatalogSymbol = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CatalogSymbol"),
        "CatalogSymbol",
        "__httpwww_posc_orgschemas_unitDefinitionType_httpwww_posc_orgschemasCatalogSymbol",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 224, 4
        ),
    )

    CatalogSymbol = property(
        __CatalogSymbol.value,
        __CatalogSymbol.set,
        None,
        "\nThe symbol taken from the catalog. Within the catalog, defined by \nCatalogName, the CatalogSymbol should be unique. This element has an \nattribute, isExplicit, which states whether a uom symbol is explicitly \nin the catalog, or only implicitly defined.\n              ",
    )

    # Element {http://www.posc.org/schemas}Display uses Python identifier Display
    __Display = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "Display"),
        "Display",
        "__httpwww_posc_orgschemas_unitDefinitionType_httpwww_posc_orgschemasDisplay",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 234, 4
        ),
    )

    Display = property(
        __Display.value,
        __Display.set,
        None,
        "\nThis allows a unit to have tags that define a display. For example, a sub \nelement may be used to indicate a subscript. The displayType allows one more \nstandard choice for displaying a uom, depending on the medium that the \ninformation is being displayed on.\n              ",
    )

    # Element {http://www.posc.org/schemas}BaseUnit uses Python identifier BaseUnit
    __BaseUnit = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "BaseUnit"),
        "BaseUnit",
        "__httpwww_posc_orgschemas_unitDefinitionType_httpwww_posc_orgschemasBaseUnit",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 262, 6
        ),
    )

    BaseUnit = property(__BaseUnit.value, __BaseUnit.set, None, None)

    # Element {http://www.posc.org/schemas}IsUnknown uses Python identifier IsUnknown
    __IsUnknown = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "IsUnknown"),
        "IsUnknown",
        "__httpwww_posc_orgschemas_unitDefinitionType_httpwww_posc_orgschemasIsUnknown",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 264, 8
        ),
    )

    IsUnknown = property(__IsUnknown.value, __IsUnknown.set, None, None)

    # Element {http://www.posc.org/schemas}ConversionToBaseUnit uses Python identifier ConversionToBaseUnit
    __ConversionToBaseUnit = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "ConversionToBaseUnit"),
        "ConversionToBaseUnit",
        "__httpwww_posc_orgschemas_unitDefinitionType_httpwww_posc_orgschemasConversionToBaseUnit",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 265, 8
        ),
    )

    ConversionToBaseUnit = property(
        __ConversionToBaseUnit.value, __ConversionToBaseUnit.set, None, None
    )

    # Element {http://www.posc.org/schemas}CompositeUnit uses Python identifier CompositeUnit
    __CompositeUnit = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "CompositeUnit"),
        "CompositeUnit",
        "__httpwww_posc_orgschemas_unitDefinitionType_httpwww_posc_orgschemasCompositeUnit",
        False,
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 268, 4
        ),
    )

    CompositeUnit = property(__CompositeUnit.value, __CompositeUnit.set, None, None)

    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "id"),
        "id",
        "__httpwww_posc_orgschemas_unitDefinitionType_id",
        _module_typeBindings.keyid,
        required=True,
    )
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 270, 2
    )
    __id._UseLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 270, 2
    )

    id = property(
        __id.value,
        __id.set,
        None,
        '\nThis is a key for referencing the unit in the dictionary. The id value \nshould be unique within the dictionary document. The value should carry \nno semantic meaning. However, it is common to use a simple unit symbol for \nthe id. Because of the requirements of DTD\'s, it was necessary to separate \nout the id, which was originally of type ID. The DTD ID type did not allow \nslashes "/" or spaces or astericks (*).\n              ',
    )

    # Attribute annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "annotation"),
        "annotation",
        "__httpwww_posc_orgschemas_unitDefinitionType_annotation",
        pyxb.binding.datatypes.string,
    )
    __annotation._DeclarationLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 282, 2
    )
    __annotation._UseLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 282, 2
    )

    annotation = property(
        __annotation.value,
        __annotation.set,
        None,
        '\nFor backward compatibility, the id value was selected to be a value of type \nID. Hence, a value, such as ft/s, could not be used for the ID value. The \nannotation attribute was introduced as a schema attribute that could allow \nthe "/". Hence, ft/s is possible. This is intended to be a simple annotation,\n based on the 7 bit ascii character set. A more complex display symbol can \nbe built using the Display element.\n              ',
    )

    # Attribute modver uses Python identifier modver
    __modver = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "modver"),
        "modver",
        "__httpwww_posc_orgschemas_unitDefinitionType_modver",
        pyxb.binding.datatypes.string,
        fixed=True,
        unicode_default="1.0",
    )
    __modver._DeclarationLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 294, 2
    )
    __modver._UseLocation = pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 294, 2
    )

    modver = property(__modver.value, __modver.set, None, None)

    _ElementMap.update(
        {
            __Name.name(): __Name,
            __QuantityType.name(): __QuantityType,
            __CatalogName.name(): __CatalogName,
            __CatalogSymbol.name(): __CatalogSymbol,
            __Display.name(): __Display,
            __BaseUnit.name(): __BaseUnit,
            __IsUnknown.name(): __IsUnknown,
            __ConversionToBaseUnit.name(): __ConversionToBaseUnit,
            __CompositeUnit.name(): __CompositeUnit,
        }
    )
    _AttributeMap.update(
        {
            __id.name(): __id,
            __annotation.name(): __annotation,
            __modver.name(): __modver,
        }
    )


_module_typeBindings.unitDefinitionType = unitDefinitionType
Namespace.addCategoryObject("typeBinding", "unitDefinitionType", unitDefinitionType)


DocumentInformation = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "DocumentInformation"),
    documentInfoType,
    documentation="\nA standard name for an element of type documentInfoType. Other names may be \nused at the discretion of the developer.\n                  ",
    location=pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 24, 0
    ),
)
Namespace.addCategoryObject(
    "elementBinding",
    DocumentInformation.name().localName(),
    DocumentInformation,
)

DocClasses = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "_DocClasses"),
    abstractFeatureType,
    abstract=pyxb.binding.datatypes.boolean(1),
    documentation="\nAn abstract element, to serve as a head for a substitution group. The \n_DocClasses is intended to handle any classification systems that a group\nwould model. It may be a simple substitution, or a container with many\nclasses contained in it.\n                ",
    location=pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 35, 0
    ),
)
Namespace.addCategoryObject("elementBinding", DocClasses.name().localName(), DocClasses)

UnitOfMeasureDictionary = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "UnitOfMeasureDictionary"),
    CTD_ANON,
    location=pyxb.utils.utility.Location(
        "http://w3.energistics.org/uom/units20/Units.xsd", 24, 0
    ),
)
Namespace.addCategoryObject(
    "elementBinding",
    UnitOfMeasureDictionary.name().localName(),
    UnitOfMeasureDictionary,
)


documentInfoType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "_DocClasses"),
        abstractFeatureType,
        abstract=pyxb.binding.datatypes.boolean(1),
        scope=documentInfoType,
        documentation="\nAn abstract element, to serve as a head for a substitution group. The \n_DocClasses is intended to handle any classification systems that a group\nwould model. It may be a simple substitution, or a container with many\nclasses contained in it.\n                ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 35, 0
        ),
    )
)

documentInfoType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "DocumentName"),
        identifierType,
        scope=documentInfoType,
        documentation="\nAn identifier for the document. This is intended to be unique within the \ncontext of the NamingSystem.\n                ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 56, 2
        ),
    )
)

documentInfoType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "DocumentAlias"),
        identifierType,
        scope=documentInfoType,
        documentation="\nZero or more alternate names for the document. These names do not need to be\nunique within the naming system.\n                ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 64, 2
        ),
    )
)

documentInfoType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "DocumentDate"),
        pyxb.binding.datatypes.date,
        scope=documentInfoType,
        documentation="\nThe date of the creation of the document. This is not the same as the date\nthat the file was created. For this date, the document is considered to be\nthe set of information associated with this document information.\nFor example, the document may be a seismic binset. This represents the date\nthat the binset was created. The FileCreation information would capture the\ndate that the XML file was created to send or exchange the binset.\n                ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 72, 2
        ),
    )
)

documentInfoType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "FileCreationInformation"),
        fileCrType,
        scope=documentInfoType,
        documentation="\nThe information about the creation of the exchange file. This is not about\nthe creation of the data within the file, but the creation of the file itself.\n                ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 93, 2
        ),
    )
)

documentInfoType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "SecurityInformation"),
        securityInfoType,
        scope=documentInfoType,
        documentation="\nInformation about the security to be applied to this file. More than one\nclassification can be given.\n                ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 101, 2
        ),
    )
)

documentInfoType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Disclaimer"),
        pyxb.binding.datatypes.string,
        scope=documentInfoType,
        documentation="\nA free-form string that allows a disclaimer to accompany the information.\n                ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 109, 2
        ),
    )
)

documentInfoType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "AuditTrail"),
        auditType,
        scope=documentInfoType,
        documentation="\nA collection of events that can document the history of the data.\n                ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 116, 2
        ),
    )
)

documentInfoType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "DataOwnerRef"),
        referenceToType,
        scope=documentInfoType,
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 131, 4
        ),
    )
)

documentInfoType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "DataOwnerID"),
        pyxb.binding.datatypes.string,
        scope=documentInfoType,
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 132, 4
        ),
    )
)

documentInfoType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Comment"),
        pyxb.binding.datatypes.string,
        scope=documentInfoType,
        documentation="\nAn optional comment about the document.\n                ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 134, 2
        ),
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
        max=None,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 64, 2
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 72, 2
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 84, 2
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 93, 2
        ),
    )
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(
        min=0,
        max=5,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 101, 2
        ),
    )
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 109, 2
        ),
    )
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 116, 2
        ),
    )
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 123, 2
        ),
    )
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 134, 2
        ),
    )
    counters.add(cc_8)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        documentInfoType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "DocumentName")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 56, 2
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        documentInfoType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "DocumentAlias")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 64, 2
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        documentInfoType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "DocumentDate")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 72, 2
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(
        documentInfoType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "_DocClasses")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 84, 2
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(
        documentInfoType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "FileCreationInformation")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 93, 2
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(
        documentInfoType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "SecurityInformation")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 101, 2
        ),
    )
    st_5 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(
        documentInfoType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "Disclaimer")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 109, 2
        ),
    )
    st_6 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(
        documentInfoType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "AuditTrail")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 116, 2
        ),
    )
    st_7 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(
        documentInfoType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "DataOwnerRef")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 131, 4
        ),
    )
    st_8 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(
        documentInfoType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "DataOwnerID")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 132, 4
        ),
    )
    st_9 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(
        documentInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Comment")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 134, 2
        ),
    )
    st_10 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    transitions.append(fac.Transition(st_2, []))
    transitions.append(fac.Transition(st_3, []))
    transitions.append(fac.Transition(st_4, []))
    transitions.append(fac.Transition(st_5, []))
    transitions.append(fac.Transition(st_6, []))
    transitions.append(fac.Transition(st_7, []))
    transitions.append(fac.Transition(st_8, []))
    transitions.append(fac.Transition(st_9, []))
    transitions.append(fac.Transition(st_10, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_0, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_1, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_2, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_3, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_4, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_5, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_6, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_7, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_7, False)]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_8, True)]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


documentInfoType._Automaton = _BuildAutomaton()


fileCrType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "FileCreationDate"),
        expandedDateTime,
        scope=fileCrType,
        documentation="\nThe date and/or time that the file was created.\n                ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 153, 2
        ),
    )
)

fileCrType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "SoftwareName"),
        pyxb.binding.datatypes.string,
        scope=fileCrType,
        documentation="\nIf appropriate, the software that created the file. This is a free form\nstring, and may include whatever information is deemed relevant.\n                ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 160, 2
        ),
    )
)

fileCrType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "FileCreator"),
        pyxb.binding.datatypes.string,
        scope=fileCrType,
        documentation="\nThe person or business associate that created the file. This is a free\nform string.\n                ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 168, 2
        ),
    )
)

fileCrType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Comment"),
        pyxb.binding.datatypes.string,
        scope=fileCrType,
        documentation="\nAny comment that would be useful to further explain the creation of this\ninstance document.\n                ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 176, 2
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
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 160, 2
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 168, 2
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 176, 2
        ),
    )
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        fileCrType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "FileCreationDate")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 153, 2
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        fileCrType._UseForTag(pyxb.namespace.ExpandedName(Namespace, "SoftwareName")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 160, 2
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        fileCrType._UseForTag(pyxb.namespace.ExpandedName(Namespace, "FileCreator")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 168, 2
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(
        fileCrType._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Comment")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 176, 2
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    transitions.append(fac.Transition(st_2, []))
    transitions.append(fac.Transition(st_3, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_2, True)]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


fileCrType._Automaton = _BuildAutomaton_()


securityInfoType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Class"),
        pyxb.binding.datatypes.string,
        scope=securityInfoType,
        documentation="\nThe security class in which this document is classified. Examples would \nbe confidential, partner confidential, tight. The meaning of the class is\ndetermined by the System in which it is defined.\n                ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 200, 2
        ),
    )
)

securityInfoType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "System"),
        pyxb.binding.datatypes.string,
        scope=securityInfoType,
        documentation="\nThe security classification system. This gives context to the meaning of the\nClass value.\n                ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 209, 2
        ),
    )
)

securityInfoType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "EndDate"),
        expandedDateTime,
        scope=securityInfoType,
        documentation="\nThe date on which this security class is no longer applicable.\n                ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 217, 2
        ),
    )
)

securityInfoType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Comment"),
        pyxb.binding.datatypes.string,
        scope=securityInfoType,
        documentation="\nA general comment to further define the security class.\n                ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 224, 2
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
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 209, 2
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 217, 2
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 224, 2
        ),
    )
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        securityInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Class")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 200, 2
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        securityInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, "System")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 209, 2
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        securityInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, "EndDate")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 217, 2
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(
        securityInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Comment")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 224, 2
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    transitions.append(fac.Transition(st_2, []))
    transitions.append(fac.Transition(st_3, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_2, True)]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


securityInfoType._Automaton = _BuildAutomaton_2()


auditType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Event"),
        eventType,
        scope=auditType,
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 242, 2
        ),
    )
)


def _BuildAutomaton_3():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        auditType._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Event")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 242, 2
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, []))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


auditType._Automaton = _BuildAutomaton_3()


eventType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "EventDate"),
        expandedDateTime,
        scope=eventType,
        documentation="\nThe date on which the event took place.\n                ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 254, 2
        ),
    )
)

eventType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ResponsiblePartyRef"),
        referenceToType,
        scope=eventType,
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 269, 3
        ),
    )
)

eventType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ResponsiblePartyID"),
        pyxb.binding.datatypes.string,
        scope=eventType,
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 270, 3
        ),
    )
)

eventType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Comment"),
        pyxb.binding.datatypes.string,
        scope=eventType,
        documentation="\nA free form comment that can further define the event that occurred.\n                ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 272, 2
        ),
    )
)


def _BuildAutomaton_4():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 261, 2
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        eventType._UseForTag(pyxb.namespace.ExpandedName(Namespace, "EventDate")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 254, 2
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        eventType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "ResponsiblePartyRef")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 269, 3
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        eventType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "ResponsiblePartyID")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 270, 3
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        eventType._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Comment")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 272, 2
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    transitions.append(fac.Transition(st_2, []))
    transitions.append(fac.Transition(st_3, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


eventType._Automaton = _BuildAutomaton_4()


abstractFeatureType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Text"),
        pyxb.binding.datatypes.string,
        scope=abstractFeatureType,
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 284, 4
        ),
    )
)


def _BuildAutomaton_5():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 284, 4
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        abstractFeatureType._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Text")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 284, 4
        ),
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


abstractFeatureType._Automaton = _BuildAutomaton_5()


identifierType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Name"),
        pyxb.binding.datatypes.string,
        scope=identifierType,
        documentation='\nThe name of the object being identified. It may or may not be a unique name, depending on the use of this type. When used as an "identifier," it should be a unique name, within the naming system. When used as an "alias," the name is not required to be unique.\n    ',
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 299, 4
        ),
    )
)

identifierType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "NamingSystem"),
        pyxb.binding.datatypes.string,
        scope=identifierType,
        documentation="\nThe naming system under which the name is defined. For example, if the name is a person's social security number, the naming system would be SSN, or some equivalent code which represents that the name is a social security number. Since naming system may be a code, there are two attributes (nameRef and systemList), which may be used to lead an application to a registry, where meaning can be obtained for the code. \n    ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 307, 6
        ),
    )
)

identifierType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Version"),
        pyxb.binding.datatypes.string,
        scope=identifierType,
        documentation="\nWhen a naming system is declared, it may be further qualified by giving a version of the\nnaming system. This is needed only when a group puts out a new set of names that are not\nbackward compatible with a previous list.\n    ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 314, 6
        ),
    )
)

identifierType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Comment"),
        pyxb.binding.datatypes.string,
        scope=identifierType,
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 324, 4
        ),
    )
)


def _BuildAutomaton_6():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 306, 4
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 314, 6
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 324, 4
        ),
    )
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        identifierType._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Name")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 299, 4
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        identifierType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "NamingSystem")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 307, 6
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        identifierType._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Version")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 314, 6
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(
        identifierType._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Comment")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 324, 4
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    transitions.append(fac.Transition(st_3, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, []))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(
        fac.Transition(
            st_1,
            [
                fac.UpdateInstruction(cc_0, True),
                fac.UpdateInstruction(cc_1, False),
            ],
        )
    )
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(
        fac.Transition(
            st_3,
            [
                fac.UpdateInstruction(cc_0, False),
                fac.UpdateInstruction(cc_1, False),
            ],
        )
    )
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_2, True)]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


identifierType._Automaton = _BuildAutomaton_6()


CTD_ANON._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "DocumentInformation"),
        documentInfoType,
        scope=CTD_ANON,
        documentation="\nA standard name for an element of type documentInfoType. Other names may be \nused at the discretion of the developer.\n                  ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/DocumentInfo.xsd", 24, 0
        ),
    )
)

CTD_ANON._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "UnitsDefinition"),
        CTD_ANON_,
        scope=CTD_ANON,
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 28, 6
        ),
    )
)


def _BuildAutomaton_7():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "DocumentInformation")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 27, 6
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, "UnitsDefinition")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 28, 6
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON._Automaton = _BuildAutomaton_7()


CTD_ANON_._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "UnitOfMeasure"),
        unitDictionaryType,
        scope=CTD_ANON_,
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 31, 12
        ),
    )
)


def _BuildAutomaton_8():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, "UnitOfMeasure")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 31, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, []))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_._Automaton = _BuildAutomaton_8()


baseUnitType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Description"),
        pyxb.binding.datatypes.string,
        scope=baseUnitType,
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 327, 2
        ),
    )
)

baseUnitType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "BasicAuthority"),
        pyxb.binding.datatypes.string,
        scope=baseUnitType,
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 328, 2
        ),
    )
)


def _BuildAutomaton_9():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 327, 2
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 328, 2
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        baseUnitType._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Description")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 327, 2
        ),
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
        baseUnitType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "BasicAuthority")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 328, 2
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_1, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


baseUnitType._Automaton = _BuildAutomaton_9()


compositeUnitType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "UnitTerm"),
        CTD_ANON_2,
        scope=compositeUnitType,
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 358, 4
        ),
    )
)


def _BuildAutomaton_10():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        compositeUnitType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "UnitTerm")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 358, 4
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, []))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


compositeUnitType._Automaton = _BuildAutomaton_10()


conversionType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Description"),
        pyxb.binding.datatypes.string,
        scope=conversionType,
        documentation="\nA definition, description, or other comment about the unit of measure.\n              ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 377, 2
        ),
    )
)

conversionType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Factor"),
        pyxb.binding.datatypes.double,
        scope=conversionType,
        documentation='\nIf A = D = 0, and C = 1, the value of B becomes a factor. For example, \nthe conversion of an international foot to a metre is with Factor=".3048"\n              ',
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 385, 4
        ),
    )
)

conversionType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Fraction"),
        CTD_ANON_3,
        scope=conversionType,
        documentation="\nIf A = D = 0, B and C represent a fraction. For example, the conversion of a \nUS Survey foot to a metre is given with the fraction of 12 / 39.37. Hence,\n Numerator = '12', Denominator = '39.37'\n              ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 393, 4
        ),
    )
)

conversionType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Formula"),
        CTD_ANON_4,
        scope=conversionType,
        documentation='\nA few units of measure do not have a factor or fraction. For example the \nconversion from degrees Celcius to Kelvin is given as degK = 273.15 + degC. \nHence, A = "273.15", B = "1.", C = "1.", D = "0."\n              ',
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 408, 4
        ),
    )
)


def _BuildAutomaton_11():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 377, 2
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 426, 2
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        conversionType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "Description")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 377, 2
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        conversionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Factor")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 385, 4
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        conversionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Fraction")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 393, 4
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        conversionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Formula")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 408, 4
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        conversionType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "Description")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 426, 2
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, []))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, []))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_1, True)]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


conversionType._Automaton = _BuildAutomaton_11()


CTD_ANON_3._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Numerator"),
        pyxb.binding.datatypes.double,
        scope=CTD_ANON_3,
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 403, 8
        ),
    )
)

CTD_ANON_3._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Denominator"),
        pyxb.binding.datatypes.double,
        scope=CTD_ANON_3,
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 404, 8
        ),
    )
)


def _BuildAutomaton_12():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Numerator")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 403, 8
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Denominator")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 404, 8
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_3._Automaton = _BuildAutomaton_12()


CTD_ANON_4._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "A"),
        pyxb.binding.datatypes.double,
        scope=CTD_ANON_4,
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 418, 8
        ),
    )
)

CTD_ANON_4._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "B"),
        pyxb.binding.datatypes.double,
        scope=CTD_ANON_4,
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 419, 8
        ),
    )
)

CTD_ANON_4._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "C"),
        pyxb.binding.datatypes.double,
        scope=CTD_ANON_4,
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 420, 8
        ),
    )
)

CTD_ANON_4._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "D"),
        pyxb.binding.datatypes.double,
        scope=CTD_ANON_4,
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 421, 8
        ),
    )
)


def _BuildAutomaton_13():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 418, 8
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 421, 8
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, "A")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 418, 8
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, "B")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 419, 8
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, "C")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 420, 8
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, "D")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 421, 8
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, []))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, True)]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_4._Automaton = _BuildAutomaton_13()


displayType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "sup"),
        pyxb.binding.datatypes.string,
        scope=displayType,
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 450, 4
        ),
    )
)

displayType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "sub"),
        pyxb.binding.datatypes.string,
        scope=displayType,
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 451, 4
        ),
    )
)

displayType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "gr"),
        pyxb.binding.datatypes.string,
        scope=displayType,
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 452, 4
        ),
    )
)


def _BuildAutomaton_14():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 449, 2
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        displayType._UseForTag(pyxb.namespace.ExpandedName(Namespace, "sup")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 450, 4
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        displayType._UseForTag(pyxb.namespace.ExpandedName(Namespace, "sub")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 451, 4
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        displayType._UseForTag(pyxb.namespace.ExpandedName(Namespace, "gr")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 452, 4
        ),
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
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, True)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, True)]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


displayType._Automaton = _BuildAutomaton_14()


unitDictionaryType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Name"),
        pyxb.binding.datatypes.string,
        scope=unitDictionaryType,
        documentation="\nThe name of the unit. This does not necessarily need to be unique within \nthe catalog, but it probably should be. For example, there are several types \nof feet, all with different conversions. It is based on the converstions \nthat we should find the uniqueness.\n              ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 56, 4
        ),
    )
)

unitDictionaryType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "QuantityType"),
        pyxb.binding.datatypes.string,
        scope=unitDictionaryType,
        documentation="\nThis is an uncontrolled list to specify the quantity type that this uom is \nused for. Examples would be length, temperature, pressure, density.\n              ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 66, 4
        ),
    )
)

unitDictionaryType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "DimensionalClass"),
        pyxb.binding.datatypes.string,
        scope=unitDictionaryType,
        documentation="\nThe dimensional analysis of the unit. For example, a metre (m) would be of class [L], which represents length. A foot (ft) would also be in this class. Abbreviations used are L = length, M = mass, T = time, 1 = dimensionless, K = temperature, C = current, N = amount (mole), A = angle (radian), S = solid angle (sr), B = light amount (cd). For consistency, the values are broken into numerator and denominator, separated by a slash (/), in alphabetical order (LM, not ML). \n              ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 74, 4
        ),
    )
)

unitDictionaryType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "SameUnit"),
        sameUnitType,
        scope=unitDictionaryType,
        documentation="\nA unit of measure may have different expressions in different registries. \nThis allows zero or more of these mappings to be recorded. The SameUnit \nallows a uom and a naming system to be given. The uom is presumably the \nunique symbol in the other system.\n              ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 81, 4
        ),
    )
)

unitDictionaryType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CatalogName"),
        pyxb.binding.datatypes.string,
        scope=unitDictionaryType,
        documentation="\nA uom is generally defined in a standard catalog of units somewhere. \nThis is the name of that catalog. The combination of CatalogName and \nCatalogSymbol should be unique.\n              ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 91, 4
        ),
    )
)

unitDictionaryType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CatalogSymbol"),
        explicitType,
        scope=unitDictionaryType,
        documentation="\nThe symbol taken from the catalog. Within the catalog, defined by \nCatalogName, the CatalogSymbol should be unique. This element has an \nattribute, isExplicit, which states whether a uom symbol is explicitly \nin the catalog, or only implicitly defined.\n              ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 100, 4
        ),
    )
)

unitDictionaryType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Display"),
        displayType,
        scope=unitDictionaryType,
        documentation="\nThis allows a unit to have tags that define a display. For example, a sub \nelement may be used to indicate a subscript. The displayType allows one more \nstandard choice for displaying a uom, depending on the medium that the \ninformation is being displayed on.\n              ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 110, 4
        ),
    )
)

unitDictionaryType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Deprecated"),
        pyxb.binding.datatypes.string,
        scope=unitDictionaryType,
        documentation="\nThis element is used to indicate that a unit is being deprecated. Normally, this means that the symbol representing the unit is no longer to be used (CatalogSymbol). It is generally replaced by another instance of the unit, which has a different symbol. For example, a cubic foot, with symbol, cu ft, would be deprecated, but there would be another instance of cubic foot, with symbol, ft3. The value of the instance repesents the version of the dictionary for which the value is first deprecated. A deprecated unit (symbol) is carried for backward compatibility, but will, at some point, be removed.\n              ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 120, 4
        ),
    )
)

unitDictionaryType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "BaseUnit"),
        baseUnitType,
        scope=unitDictionaryType,
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 138, 6
        ),
    )
)

unitDictionaryType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ConversionToBaseUnit"),
        conversionType,
        scope=unitDictionaryType,
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 139, 6
        ),
    )
)

unitDictionaryType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CompositeUnit"),
        compositeUnitType,
        scope=unitDictionaryType,
        documentation="\nA composite unit can be formed by an algebra of units. For example, a foot \nper second (quantity type of velocity) can be formed by a foot divided by \na second. This element allows the registry to identify composite units. \nNote that a composite unit is chosen to represent a quantity type.\nExample: metre per second. This uom is the base unit for the quantity type \nof velocity. A foot per second is also a composite unit, and can be converted \nto the base unit by defining a conversion formula.\n              ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 141, 4
        ),
    )
)


def _BuildAutomaton_15():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 66, 4
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 74, 4
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 81, 4
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 91, 4
        ),
    )
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 100, 4
        ),
    )
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 110, 4
        ),
    )
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 120, 4
        ),
    )
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 141, 4
        ),
    )
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        unitDictionaryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Name")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 56, 4
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        unitDictionaryType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "QuantityType")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 66, 4
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        unitDictionaryType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "DimensionalClass")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 74, 4
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        unitDictionaryType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "SameUnit")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 81, 4
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        unitDictionaryType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "CatalogName")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 91, 4
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        unitDictionaryType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "CatalogSymbol")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 100, 4
        ),
    )
    st_5 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        unitDictionaryType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "Display")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 110, 4
        ),
    )
    st_6 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        unitDictionaryType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "Deprecated")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 120, 4
        ),
    )
    st_7 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        unitDictionaryType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "BaseUnit")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 138, 6
        ),
    )
    st_8 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        unitDictionaryType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "ConversionToBaseUnit")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 139, 6
        ),
    )
    st_9 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(
        unitDictionaryType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "CompositeUnit")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 141, 4
        ),
    )
    st_10 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    transitions.append(fac.Transition(st_2, []))
    transitions.append(fac.Transition(st_3, []))
    transitions.append(fac.Transition(st_4, []))
    transitions.append(fac.Transition(st_5, []))
    transitions.append(fac.Transition(st_6, []))
    transitions.append(fac.Transition(st_7, []))
    transitions.append(fac.Transition(st_8, []))
    transitions.append(fac.Transition(st_9, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_0, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_1, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_2, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_3, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_4, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_5, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [fac.UpdateInstruction(cc_6, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, []))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, []))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [fac.UpdateInstruction(cc_7, True)]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


unitDictionaryType._Automaton = _BuildAutomaton_15()


unitDefinitionType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Name"),
        pyxb.binding.datatypes.string,
        scope=unitDefinitionType,
        documentation="\nThe name of the unit. This does not necessarily need to be unique within \nthe catalog, but it probably should be. For example, there are several types \nof feet, all with different conversions. It is based on the converstions \nthat we should find the uniqueness.\n              ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 197, 4
        ),
    )
)

unitDefinitionType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "QuantityType"),
        pyxb.binding.datatypes.string,
        scope=unitDefinitionType,
        documentation="\nThis is an uncontrolled list to specify the quantity type that this uom is \nused for. Examples would be length, temperature, pressure, density.\n              ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 207, 4
        ),
    )
)

unitDefinitionType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CatalogName"),
        pyxb.binding.datatypes.string,
        scope=unitDefinitionType,
        documentation="\nA uom is generally defined in a standard catalog of units somewhere. \nThis is the name of that catalog. The combination of CatalogName and \nCatalogSymbol should be unique.\n              ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 215, 4
        ),
    )
)

unitDefinitionType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CatalogSymbol"),
        explicitType,
        scope=unitDefinitionType,
        documentation="\nThe symbol taken from the catalog. Within the catalog, defined by \nCatalogName, the CatalogSymbol should be unique. This element has an \nattribute, isExplicit, which states whether a uom symbol is explicitly \nin the catalog, or only implicitly defined.\n              ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 224, 4
        ),
    )
)

unitDefinitionType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "Display"),
        displayType,
        scope=unitDefinitionType,
        documentation="\nThis allows a unit to have tags that define a display. For example, a sub \nelement may be used to indicate a subscript. The displayType allows one more \nstandard choice for displaying a uom, depending on the medium that the \ninformation is being displayed on.\n              ",
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 234, 4
        ),
    )
)

unitDefinitionType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "BaseUnit"),
        baseUnitType,
        scope=unitDefinitionType,
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 262, 6
        ),
    )
)

unitDefinitionType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "IsUnknown"),
        pyxb.binding.datatypes.boolean,
        scope=unitDefinitionType,
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 264, 8
        ),
    )
)

unitDefinitionType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "ConversionToBaseUnit"),
        conversionType,
        scope=unitDefinitionType,
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 265, 8
        ),
    )
)

unitDefinitionType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "CompositeUnit"),
        compositeUnitType,
        scope=unitDefinitionType,
        location=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 268, 4
        ),
    )
)


def _BuildAutomaton_16():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 207, 4
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 215, 4
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 224, 4
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 234, 4
        ),
    )
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 264, 8
        ),
    )
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 265, 8
        ),
    )
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 268, 4
        ),
    )
    counters.add(cc_6)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        unitDefinitionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, "Name")),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 197, 4
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        unitDefinitionType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "QuantityType")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 207, 4
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        unitDefinitionType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "CatalogName")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 215, 4
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(
        unitDefinitionType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "CatalogSymbol")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 224, 4
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(
        unitDefinitionType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "Display")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 234, 4
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        unitDefinitionType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "BaseUnit")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 262, 6
        ),
    )
    st_5 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(
        unitDefinitionType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "IsUnknown")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 264, 8
        ),
    )
    st_6 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(
        unitDefinitionType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "ConversionToBaseUnit")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 265, 8
        ),
    )
    st_7 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(
        unitDefinitionType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "CompositeUnit")
        ),
        pyxb.utils.utility.Location(
            "http://w3.energistics.org/uom/units20/Units.xsd", 268, 4
        ),
    )
    st_8 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    transitions.append(fac.Transition(st_2, []))
    transitions.append(fac.Transition(st_3, []))
    transitions.append(fac.Transition(st_4, []))
    transitions.append(fac.Transition(st_5, []))
    transitions.append(fac.Transition(st_6, []))
    transitions.append(fac.Transition(st_7, []))
    transitions.append(fac.Transition(st_8, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_0, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_1, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_2, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_3, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, []))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_4, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_5, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_6, True)]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


unitDefinitionType._Automaton = _BuildAutomaton_16()
