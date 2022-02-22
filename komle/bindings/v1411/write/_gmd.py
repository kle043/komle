# komle/bindings/v1411/write/_gmd.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:410705b36885cae3fa86a581e054e9b962463ed8
# Generated 2020-05-05 12:37:19.643594 by PyXB version 1.2.6 using Python 3.8.2.final.0
# Namespace http://www.isotc211.org/2005/gmd [xmlns:gmd]

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
    'http://www.isotc211.org/2005/gmd', create_if_missing=True
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


from komle.bindings.v1411.write._nsgroup import (  # {http://www.isotc211.org/2005/gmd}URL; {http://www.isotc211.org/2005/gmd}CI_RoleCode; {http://www.isotc211.org/2005/gmd}CI_PresentationFormCode; {http://www.isotc211.org/2005/gmd}CI_OnLineFunctionCode; {http://www.isotc211.org/2005/gmd}CI_DateTypeCode; {http://www.isotc211.org/2005/gmd}MD_ClassificationCode; {http://www.isotc211.org/2005/gmd}MD_RestrictionCode; {http://www.isotc211.org/2005/gmd}MD_CoverageContentTypeCode; {http://www.isotc211.org/2005/gmd}MD_ImagingConditionCode; {http://www.isotc211.org/2005/gmd}DQ_EvaluationMethodTypeCode; {http://www.isotc211.org/2005/gmd}MD_DistributionUnits; {http://www.isotc211.org/2005/gmd}MD_MediumFormatCode; {http://www.isotc211.org/2005/gmd}MD_MediumNameCode; {http://www.isotc211.org/2005/gmd}LocalisedCharacterString; {http://www.isotc211.org/2005/gmd}PT_LocaleContainer; {http://www.isotc211.org/2005/gmd}LanguageCode; {http://www.isotc211.org/2005/gmd}Country; {http://www.isotc211.org/2005/gmd}MD_Resolution; {http://www.isotc211.org/2005/gmd}MD_TopicCategoryCode; {http://www.isotc211.org/2005/gmd}MD_CharacterSetCode; {http://www.isotc211.org/2005/gmd}MD_SpatialRepresentationTypeCode; {http://www.isotc211.org/2005/gmd}MD_ProgressCode; {http://www.isotc211.org/2005/gmd}MD_KeywordTypeCode; {http://www.isotc211.org/2005/gmd}DS_AssociationTypeCode; {http://www.isotc211.org/2005/gmd}DS_InitiativeTypeCode; {http://www.isotc211.org/2005/gmd}MD_ScopeDescription; {http://www.isotc211.org/2005/gmd}MD_MaintenanceFrequencyCode; {http://www.isotc211.org/2005/gmd}MD_ScopeCode; {http://www.isotc211.org/2005/gmd}MD_ObligationCode; {http://www.isotc211.org/2005/gmd}MD_DatatypeCode; {http://www.isotc211.org/2005/gmd}MD_PixelOrientationCode; {http://www.isotc211.org/2005/gmd}MD_TopologyLevelCode; {http://www.isotc211.org/2005/gmd}MD_GeometricObjectTypeCode; {http://www.isotc211.org/2005/gmd}MD_CellGeometryCode; {http://www.isotc211.org/2005/gmd}MD_DimensionNameTypeCode; {http://www.isotc211.org/2005/gmd}MD_ApplicationSchemaInformation; {http://www.isotc211.org/2005/gmd}CI_ResponsibleParty; {http://www.isotc211.org/2005/gmd}CI_Citation; {http://www.isotc211.org/2005/gmd}CI_Address; {http://www.isotc211.org/2005/gmd}CI_OnlineResource; {http://www.isotc211.org/2005/gmd}CI_Contact; {http://www.isotc211.org/2005/gmd}CI_Telephone; {http://www.isotc211.org/2005/gmd}CI_Date; {http://www.isotc211.org/2005/gmd}CI_Series; {http://www.isotc211.org/2005/gmd}MD_Constraints; {http://www.isotc211.org/2005/gmd}AbstractMD_ContentInformation; {http://www.isotc211.org/2005/gmd}MD_RangeDimension; {http://www.isotc211.org/2005/gmd}LI_ProcessStep; {http://www.isotc211.org/2005/gmd}LI_Source; {http://www.isotc211.org/2005/gmd}LI_Lineage; {http://www.isotc211.org/2005/gmd}AbstractDQ_Result; {http://www.isotc211.org/2005/gmd}AbstractDQ_Element; {http://www.isotc211.org/2005/gmd}DQ_DataQuality; {http://www.isotc211.org/2005/gmd}DQ_Scope; {http://www.isotc211.org/2005/gmd}MD_Medium; {http://www.isotc211.org/2005/gmd}MD_DigitalTransferOptions; {http://www.isotc211.org/2005/gmd}MD_StandardOrderProcess; {http://www.isotc211.org/2005/gmd}MD_Distributor; {http://www.isotc211.org/2005/gmd}MD_Distribution; {http://www.isotc211.org/2005/gmd}MD_Format; {http://www.isotc211.org/2005/gmd}EX_TemporalExtent; {http://www.isotc211.org/2005/gmd}EX_VerticalExtent; {http://www.isotc211.org/2005/gmd}EX_Extent; {http://www.isotc211.org/2005/gmd}AbstractEX_GeographicExtent; {http://www.isotc211.org/2005/gmd}PT_FreeText; {http://www.isotc211.org/2005/gmd}PT_Locale; {http://www.isotc211.org/2005/gmd}AbstractMD_Identification; {http://www.isotc211.org/2005/gmd}MD_BrowseGraphic; {http://www.isotc211.org/2005/gmd}MD_RepresentativeFraction; {http://www.isotc211.org/2005/gmd}MD_Usage; {http://www.isotc211.org/2005/gmd}MD_Keywords; {http://www.isotc211.org/2005/gmd}DS_Association; {http://www.isotc211.org/2005/gmd}MD_AggregateInformation; {http://www.isotc211.org/2005/gmd}MD_MaintenanceInformation; {http://www.isotc211.org/2005/gmd}AbstractDS_Aggregate; {http://www.isotc211.org/2005/gmd}DS_DataSet; {http://www.isotc211.org/2005/gmd}MD_Metadata; {http://www.isotc211.org/2005/gmd}MD_ExtendedElementInformation; {http://www.isotc211.org/2005/gmd}MD_MetadataExtensionInformation; {http://www.isotc211.org/2005/gmd}MD_PortrayalCatalogueReference; {http://www.isotc211.org/2005/gmd}MD_ReferenceSystem; {http://www.isotc211.org/2005/gmd}MD_Identifier; {http://www.isotc211.org/2005/gmd}AbstractRS_ReferenceSystem; {http://www.isotc211.org/2005/gmd}AbstractMD_SpatialRepresentation; {http://www.isotc211.org/2005/gmd}MD_Dimension; {http://www.isotc211.org/2005/gmd}MD_GeometricObjects; {http://www.isotc211.org/2005/gmd}MD_LegalConstraints; {http://www.isotc211.org/2005/gmd}MD_SecurityConstraints; {http://www.isotc211.org/2005/gmd}MD_FeatureCatalogueDescription; {http://www.isotc211.org/2005/gmd}MD_CoverageDescription; {http://www.isotc211.org/2005/gmd}MD_Band; {http://www.isotc211.org/2005/gmd}DQ_ConformanceResult; {http://www.isotc211.org/2005/gmd}DQ_QuantitativeResult; {http://www.isotc211.org/2005/gmd}AbstractDQ_TemporalAccuracy; {http://www.isotc211.org/2005/gmd}AbstractDQ_ThematicAccuracy; {http://www.isotc211.org/2005/gmd}AbstractDQ_PositionalAccuracy; {http://www.isotc211.org/2005/gmd}AbstractDQ_LogicalConsistency; {http://www.isotc211.org/2005/gmd}AbstractDQ_Completeness; {http://www.isotc211.org/2005/gmd}EX_BoundingPolygon; {http://www.isotc211.org/2005/gmd}EX_GeographicBoundingBox; {http://www.isotc211.org/2005/gmd}EX_SpatialTemporalExtent; {http://www.isotc211.org/2005/gmd}EX_GeographicDescription; {http://www.isotc211.org/2005/gmd}MD_DataIdentification; {http://www.isotc211.org/2005/gmd}MD_ServiceIdentification; {http://www.isotc211.org/2005/gmd}DS_OtherAggregate; {http://www.isotc211.org/2005/gmd}DS_Series; {http://www.isotc211.org/2005/gmd}DS_Initiative; {http://www.isotc211.org/2005/gmd}RS_Identifier; {http://www.isotc211.org/2005/gmd}MD_GridSpatialRepresentation; {http://www.isotc211.org/2005/gmd}MD_VectorSpatialRepresentation; {http://www.isotc211.org/2005/gmd}MD_ImageDescription; {http://www.isotc211.org/2005/gmd}DQ_TemporalValidity; {http://www.isotc211.org/2005/gmd}DQ_TemporalConsistency; {http://www.isotc211.org/2005/gmd}DQ_AccuracyOfATimeMeasurement; {http://www.isotc211.org/2005/gmd}DQ_QuantitativeAttributeAccuracy; {http://www.isotc211.org/2005/gmd}DQ_NonQuantitativeAttributeAccuracy; {http://www.isotc211.org/2005/gmd}DQ_ThematicClassificationCorrectness; {http://www.isotc211.org/2005/gmd}DQ_RelativeInternalPositionalAccuracy; {http://www.isotc211.org/2005/gmd}DQ_GriddedDataPositionalAccuracy; {http://www.isotc211.org/2005/gmd}DQ_AbsoluteExternalPositionalAccuracy; {http://www.isotc211.org/2005/gmd}DQ_TopologicalConsistency; {http://www.isotc211.org/2005/gmd}DQ_FormatConsistency; {http://www.isotc211.org/2005/gmd}DQ_DomainConsistency; {http://www.isotc211.org/2005/gmd}DQ_ConceptualConsistency; {http://www.isotc211.org/2005/gmd}DQ_CompletenessOmission; {http://www.isotc211.org/2005/gmd}DQ_CompletenessCommission; {http://www.isotc211.org/2005/gmd}DS_Platform; {http://www.isotc211.org/2005/gmd}DS_Sensor; {http://www.isotc211.org/2005/gmd}DS_ProductionSeries; {http://www.isotc211.org/2005/gmd}DS_StereoMate; {http://www.isotc211.org/2005/gmd}MD_Georeferenceable; {http://www.isotc211.org/2005/gmd}MD_Georectified; {http://www.isotc211.org/2005/gmd}LocalisedCharacterString_Type; {http://www.isotc211.org/2005/gmd}PT_LocaleContainer_Type; {http://www.isotc211.org/2005/gmd}MD_Resolution_Type; {http://www.isotc211.org/2005/gmd}MD_TopicCategoryCode_Type; {http://www.isotc211.org/2005/gmd}MD_ScopeDescription_Type; {http://www.isotc211.org/2005/gmd}MD_ObligationCode_Type; {http://www.isotc211.org/2005/gmd}MD_PixelOrientationCode_Type; {http://www.isotc211.org/2005/gmd}MD_ApplicationSchemaInformation_Type; {http://www.isotc211.org/2005/gmd}CI_ResponsibleParty_Type; {http://www.isotc211.org/2005/gmd}CI_Citation_Type; {http://www.isotc211.org/2005/gmd}CI_Address_Type; {http://www.isotc211.org/2005/gmd}CI_OnlineResource_Type; {http://www.isotc211.org/2005/gmd}CI_Contact_Type; {http://www.isotc211.org/2005/gmd}CI_Telephone_Type; {http://www.isotc211.org/2005/gmd}CI_Date_Type; {http://www.isotc211.org/2005/gmd}CI_Series_Type; {http://www.isotc211.org/2005/gmd}MD_Constraints_Type; {http://www.isotc211.org/2005/gmd}AbstractMD_ContentInformation_Type; {http://www.isotc211.org/2005/gmd}MD_RangeDimension_Type; {http://www.isotc211.org/2005/gmd}LI_ProcessStep_Type; {http://www.isotc211.org/2005/gmd}LI_Source_Type; {http://www.isotc211.org/2005/gmd}LI_Lineage_Type; {http://www.isotc211.org/2005/gmd}AbstractDQ_Result_Type; {http://www.isotc211.org/2005/gmd}AbstractDQ_Element_Type; {http://www.isotc211.org/2005/gmd}DQ_DataQuality_Type; {http://www.isotc211.org/2005/gmd}DQ_Scope_Type; {http://www.isotc211.org/2005/gmd}MD_Medium_Type; {http://www.isotc211.org/2005/gmd}MD_DigitalTransferOptions_Type; {http://www.isotc211.org/2005/gmd}MD_StandardOrderProcess_Type; {http://www.isotc211.org/2005/gmd}MD_Distributor_Type; {http://www.isotc211.org/2005/gmd}MD_Distribution_Type; {http://www.isotc211.org/2005/gmd}MD_Format_Type; {http://www.isotc211.org/2005/gmd}EX_TemporalExtent_Type; {http://www.isotc211.org/2005/gmd}EX_VerticalExtent_Type; {http://www.isotc211.org/2005/gmd}EX_Extent_Type; {http://www.isotc211.org/2005/gmd}AbstractEX_GeographicExtent_Type; {http://www.isotc211.org/2005/gmd}PT_FreeText_Type; {http://www.isotc211.org/2005/gmd}PT_Locale_Type; {http://www.isotc211.org/2005/gmd}AbstractMD_Identification_Type; {http://www.isotc211.org/2005/gmd}MD_BrowseGraphic_Type; {http://www.isotc211.org/2005/gmd}MD_RepresentativeFraction_Type; {http://www.isotc211.org/2005/gmd}MD_Usage_Type; {http://www.isotc211.org/2005/gmd}MD_Keywords_Type; {http://www.isotc211.org/2005/gmd}DS_Association_Type; {http://www.isotc211.org/2005/gmd}MD_AggregateInformation_Type; {http://www.isotc211.org/2005/gmd}MD_MaintenanceInformation_Type; {http://www.isotc211.org/2005/gmd}AbstractDS_Aggregate_Type; {http://www.isotc211.org/2005/gmd}DS_DataSet_Type; {http://www.isotc211.org/2005/gmd}MD_Metadata_Type; {http://www.isotc211.org/2005/gmd}MD_ExtendedElementInformation_Type; {http://www.isotc211.org/2005/gmd}MD_MetadataExtensionInformation_Type; {http://www.isotc211.org/2005/gmd}MD_PortrayalCatalogueReference_Type; {http://www.isotc211.org/2005/gmd}MD_ReferenceSystem_Type; {http://www.isotc211.org/2005/gmd}MD_Identifier_Type; {http://www.isotc211.org/2005/gmd}AbstractRS_ReferenceSystem_Type; {http://www.isotc211.org/2005/gmd}AbstractMD_SpatialRepresentation_Type; {http://www.isotc211.org/2005/gmd}MD_Dimension_Type; {http://www.isotc211.org/2005/gmd}MD_GeometricObjects_Type; {http://www.isotc211.org/2005/gmd}MD_ApplicationSchemaInformation_PropertyType; {http://www.isotc211.org/2005/gmd}CI_ResponsibleParty_PropertyType; {http://www.isotc211.org/2005/gmd}CI_Citation_PropertyType; {http://www.isotc211.org/2005/gmd}CI_Address_PropertyType; {http://www.isotc211.org/2005/gmd}CI_OnlineResource_PropertyType; {http://www.isotc211.org/2005/gmd}CI_Contact_PropertyType; {http://www.isotc211.org/2005/gmd}CI_Telephone_PropertyType; {http://www.isotc211.org/2005/gmd}CI_Date_PropertyType; {http://www.isotc211.org/2005/gmd}CI_Series_PropertyType; {http://www.isotc211.org/2005/gmd}URL_PropertyType; {http://www.isotc211.org/2005/gmd}CI_RoleCode_PropertyType; {http://www.isotc211.org/2005/gmd}CI_PresentationFormCode_PropertyType; {http://www.isotc211.org/2005/gmd}CI_OnLineFunctionCode_PropertyType; {http://www.isotc211.org/2005/gmd}CI_DateTypeCode_PropertyType; {http://www.isotc211.org/2005/gmd}MD_Constraints_PropertyType; {http://www.isotc211.org/2005/gmd}MD_LegalConstraints_Type; {http://www.isotc211.org/2005/gmd}MD_LegalConstraints_PropertyType; {http://www.isotc211.org/2005/gmd}MD_SecurityConstraints_Type; {http://www.isotc211.org/2005/gmd}MD_SecurityConstraints_PropertyType; {http://www.isotc211.org/2005/gmd}MD_ClassificationCode_PropertyType; {http://www.isotc211.org/2005/gmd}MD_RestrictionCode_PropertyType; {http://www.isotc211.org/2005/gmd}MD_FeatureCatalogueDescription_Type; {http://www.isotc211.org/2005/gmd}MD_FeatureCatalogueDescription_PropertyType; {http://www.isotc211.org/2005/gmd}MD_CoverageDescription_Type; {http://www.isotc211.org/2005/gmd}MD_CoverageDescription_PropertyType; {http://www.isotc211.org/2005/gmd}MD_ImageDescription_PropertyType; {http://www.isotc211.org/2005/gmd}MD_ContentInformation_PropertyType; {http://www.isotc211.org/2005/gmd}MD_RangeDimension_PropertyType; {http://www.isotc211.org/2005/gmd}MD_Band_Type; {http://www.isotc211.org/2005/gmd}MD_Band_PropertyType; {http://www.isotc211.org/2005/gmd}MD_CoverageContentTypeCode_PropertyType; {http://www.isotc211.org/2005/gmd}MD_ImagingConditionCode_PropertyType; {http://www.isotc211.org/2005/gmd}LI_ProcessStep_PropertyType; {http://www.isotc211.org/2005/gmd}LI_Source_PropertyType; {http://www.isotc211.org/2005/gmd}LI_Lineage_PropertyType; {http://www.isotc211.org/2005/gmd}DQ_ConformanceResult_Type; {http://www.isotc211.org/2005/gmd}DQ_ConformanceResult_PropertyType; {http://www.isotc211.org/2005/gmd}DQ_QuantitativeResult_Type; {http://www.isotc211.org/2005/gmd}DQ_QuantitativeResult_PropertyType; {http://www.isotc211.org/2005/gmd}DQ_Result_PropertyType; {http://www.isotc211.org/2005/gmd}DQ_TemporalValidity_PropertyType; {http://www.isotc211.org/2005/gmd}DQ_TemporalConsistency_PropertyType; {http://www.isotc211.org/2005/gmd}DQ_AccuracyOfATimeMeasurement_PropertyType; {http://www.isotc211.org/2005/gmd}DQ_QuantitativeAttributeAccuracy_PropertyType; {http://www.isotc211.org/2005/gmd}DQ_NonQuantitativeAttributeAccuracy_PropertyType; {http://www.isotc211.org/2005/gmd}DQ_ThematicClassificationCorrectness_PropertyType; {http://www.isotc211.org/2005/gmd}DQ_RelativeInternalPositionalAccuracy_PropertyType; {http://www.isotc211.org/2005/gmd}DQ_GriddedDataPositionalAccuracy_PropertyType; {http://www.isotc211.org/2005/gmd}DQ_AbsoluteExternalPositionalAccuracy_PropertyType; {http://www.isotc211.org/2005/gmd}DQ_TopologicalConsistency_PropertyType; {http://www.isotc211.org/2005/gmd}DQ_FormatConsistency_PropertyType; {http://www.isotc211.org/2005/gmd}DQ_DomainConsistency_PropertyType; {http://www.isotc211.org/2005/gmd}DQ_ConceptualConsistency_PropertyType; {http://www.isotc211.org/2005/gmd}DQ_CompletenessOmission_PropertyType; {http://www.isotc211.org/2005/gmd}DQ_CompletenessCommission_PropertyType; {http://www.isotc211.org/2005/gmd}AbstractDQ_TemporalAccuracy_Type; {http://www.isotc211.org/2005/gmd}DQ_TemporalAccuracy_PropertyType; {http://www.isotc211.org/2005/gmd}AbstractDQ_ThematicAccuracy_Type; {http://www.isotc211.org/2005/gmd}DQ_ThematicAccuracy_PropertyType; {http://www.isotc211.org/2005/gmd}AbstractDQ_PositionalAccuracy_Type; {http://www.isotc211.org/2005/gmd}DQ_PositionalAccuracy_PropertyType; {http://www.isotc211.org/2005/gmd}AbstractDQ_LogicalConsistency_Type; {http://www.isotc211.org/2005/gmd}DQ_LogicalConsistency_PropertyType; {http://www.isotc211.org/2005/gmd}AbstractDQ_Completeness_Type; {http://www.isotc211.org/2005/gmd}DQ_Completeness_PropertyType; {http://www.isotc211.org/2005/gmd}DQ_Element_PropertyType; {http://www.isotc211.org/2005/gmd}DQ_DataQuality_PropertyType; {http://www.isotc211.org/2005/gmd}DQ_Scope_PropertyType; {http://www.isotc211.org/2005/gmd}DQ_EvaluationMethodTypeCode_PropertyType; {http://www.isotc211.org/2005/gmd}MD_Medium_PropertyType; {http://www.isotc211.org/2005/gmd}MD_DigitalTransferOptions_PropertyType; {http://www.isotc211.org/2005/gmd}MD_StandardOrderProcess_PropertyType; {http://www.isotc211.org/2005/gmd}MD_Distributor_PropertyType; {http://www.isotc211.org/2005/gmd}MD_Distribution_PropertyType; {http://www.isotc211.org/2005/gmd}MD_Format_PropertyType; {http://www.isotc211.org/2005/gmd}MD_DistributionUnits_PropertyType; {http://www.isotc211.org/2005/gmd}MD_MediumFormatCode_PropertyType; {http://www.isotc211.org/2005/gmd}MD_MediumNameCode_PropertyType; {http://www.isotc211.org/2005/gmd}EX_TemporalExtent_PropertyType; {http://www.isotc211.org/2005/gmd}EX_VerticalExtent_PropertyType; {http://www.isotc211.org/2005/gmd}EX_BoundingPolygon_Type; {http://www.isotc211.org/2005/gmd}EX_BoundingPolygon_PropertyType; {http://www.isotc211.org/2005/gmd}EX_Extent_PropertyType; {http://www.isotc211.org/2005/gmd}EX_GeographicExtent_PropertyType; {http://www.isotc211.org/2005/gmd}EX_GeographicBoundingBox_Type; {http://www.isotc211.org/2005/gmd}EX_GeographicBoundingBox_PropertyType; {http://www.isotc211.org/2005/gmd}EX_SpatialTemporalExtent_Type; {http://www.isotc211.org/2005/gmd}EX_SpatialTemporalExtent_PropertyType; {http://www.isotc211.org/2005/gmd}EX_GeographicDescription_Type; {http://www.isotc211.org/2005/gmd}EX_GeographicDescription_PropertyType; {http://www.isotc211.org/2005/gmd}PT_Locale_PropertyType; {http://www.isotc211.org/2005/gmd}PT_LocaleContainer_PropertyType; {http://www.isotc211.org/2005/gmd}LanguageCode_PropertyType; {http://www.isotc211.org/2005/gmd}Country_PropertyType; {http://www.isotc211.org/2005/gmd}MD_Identification_PropertyType; {http://www.isotc211.org/2005/gmd}MD_BrowseGraphic_PropertyType; {http://www.isotc211.org/2005/gmd}MD_DataIdentification_Type; {http://www.isotc211.org/2005/gmd}MD_DataIdentification_PropertyType; {http://www.isotc211.org/2005/gmd}MD_ServiceIdentification_Type; {http://www.isotc211.org/2005/gmd}MD_ServiceIdentification_PropertyType; {http://www.isotc211.org/2005/gmd}MD_RepresentativeFraction_PropertyType; {http://www.isotc211.org/2005/gmd}MD_Usage_PropertyType; {http://www.isotc211.org/2005/gmd}MD_Keywords_PropertyType; {http://www.isotc211.org/2005/gmd}DS_Association_PropertyType; {http://www.isotc211.org/2005/gmd}MD_AggregateInformation_PropertyType; {http://www.isotc211.org/2005/gmd}MD_Resolution_PropertyType; {http://www.isotc211.org/2005/gmd}MD_TopicCategoryCode_PropertyType; {http://www.isotc211.org/2005/gmd}MD_CharacterSetCode_PropertyType; {http://www.isotc211.org/2005/gmd}MD_SpatialRepresentationTypeCode_PropertyType; {http://www.isotc211.org/2005/gmd}MD_ProgressCode_PropertyType; {http://www.isotc211.org/2005/gmd}MD_KeywordTypeCode_PropertyType; {http://www.isotc211.org/2005/gmd}DS_AssociationTypeCode_PropertyType; {http://www.isotc211.org/2005/gmd}DS_InitiativeTypeCode_PropertyType; {http://www.isotc211.org/2005/gmd}MD_MaintenanceInformation_PropertyType; {http://www.isotc211.org/2005/gmd}MD_ScopeDescription_PropertyType; {http://www.isotc211.org/2005/gmd}MD_MaintenanceFrequencyCode_PropertyType; {http://www.isotc211.org/2005/gmd}MD_ScopeCode_PropertyType; {http://www.isotc211.org/2005/gmd}DS_Aggregate_PropertyType; {http://www.isotc211.org/2005/gmd}DS_DataSet_PropertyType; {http://www.isotc211.org/2005/gmd}DS_OtherAggregate_Type; {http://www.isotc211.org/2005/gmd}DS_OtherAggregate_PropertyType; {http://www.isotc211.org/2005/gmd}DS_Series_Type; {http://www.isotc211.org/2005/gmd}DS_Series_PropertyType; {http://www.isotc211.org/2005/gmd}DS_Initiative_Type; {http://www.isotc211.org/2005/gmd}DS_Initiative_PropertyType; {http://www.isotc211.org/2005/gmd}DS_Platform_PropertyType; {http://www.isotc211.org/2005/gmd}DS_Sensor_PropertyType; {http://www.isotc211.org/2005/gmd}DS_ProductionSeries_PropertyType; {http://www.isotc211.org/2005/gmd}DS_StereoMate_PropertyType; {http://www.isotc211.org/2005/gmd}MD_Metadata_PropertyType; {http://www.isotc211.org/2005/gmd}MD_ExtendedElementInformation_PropertyType; {http://www.isotc211.org/2005/gmd}MD_MetadataExtensionInformation_PropertyType; {http://www.isotc211.org/2005/gmd}MD_ObligationCode_PropertyType; {http://www.isotc211.org/2005/gmd}MD_DatatypeCode_PropertyType; {http://www.isotc211.org/2005/gmd}MD_PortrayalCatalogueReference_PropertyType; {http://www.isotc211.org/2005/gmd}RS_Identifier_Type; {http://www.isotc211.org/2005/gmd}RS_Identifier_PropertyType; {http://www.isotc211.org/2005/gmd}MD_ReferenceSystem_PropertyType; {http://www.isotc211.org/2005/gmd}MD_Identifier_PropertyType; {http://www.isotc211.org/2005/gmd}RS_ReferenceSystem_PropertyType; {http://www.isotc211.org/2005/gmd}MD_GridSpatialRepresentation_Type; {http://www.isotc211.org/2005/gmd}MD_GridSpatialRepresentation_PropertyType; {http://www.isotc211.org/2005/gmd}MD_VectorSpatialRepresentation_Type; {http://www.isotc211.org/2005/gmd}MD_VectorSpatialRepresentation_PropertyType; {http://www.isotc211.org/2005/gmd}MD_SpatialRepresentation_PropertyType; {http://www.isotc211.org/2005/gmd}MD_Georeferenceable_PropertyType; {http://www.isotc211.org/2005/gmd}MD_Dimension_PropertyType; {http://www.isotc211.org/2005/gmd}MD_Georectified_PropertyType; {http://www.isotc211.org/2005/gmd}MD_GeometricObjects_PropertyType; {http://www.isotc211.org/2005/gmd}MD_PixelOrientationCode_PropertyType; {http://www.isotc211.org/2005/gmd}MD_TopologyLevelCode_PropertyType; {http://www.isotc211.org/2005/gmd}MD_GeometricObjectTypeCode_PropertyType; {http://www.isotc211.org/2005/gmd}MD_CellGeometryCode_PropertyType; {http://www.isotc211.org/2005/gmd}MD_DimensionNameTypeCode_PropertyType; {http://www.isotc211.org/2005/gmd}MD_ImageDescription_Type; {http://www.isotc211.org/2005/gmd}DQ_TemporalValidity_Type; {http://www.isotc211.org/2005/gmd}DQ_TemporalConsistency_Type; {http://www.isotc211.org/2005/gmd}DQ_AccuracyOfATimeMeasurement_Type; {http://www.isotc211.org/2005/gmd}DQ_QuantitativeAttributeAccuracy_Type; {http://www.isotc211.org/2005/gmd}DQ_NonQuantitativeAttributeAccuracy_Type; {http://www.isotc211.org/2005/gmd}DQ_ThematicClassificationCorrectness_Type; {http://www.isotc211.org/2005/gmd}DQ_RelativeInternalPositionalAccuracy_Type; {http://www.isotc211.org/2005/gmd}DQ_GriddedDataPositionalAccuracy_Type; {http://www.isotc211.org/2005/gmd}DQ_AbsoluteExternalPositionalAccuracy_Type; {http://www.isotc211.org/2005/gmd}DQ_TopologicalConsistency_Type; {http://www.isotc211.org/2005/gmd}DQ_FormatConsistency_Type; {http://www.isotc211.org/2005/gmd}DQ_DomainConsistency_Type; {http://www.isotc211.org/2005/gmd}DQ_ConceptualConsistency_Type; {http://www.isotc211.org/2005/gmd}DQ_CompletenessOmission_Type; {http://www.isotc211.org/2005/gmd}DQ_CompletenessCommission_Type; {http://www.isotc211.org/2005/gmd}PT_FreeText_PropertyType; {http://www.isotc211.org/2005/gmd}LocalisedCharacterString_PropertyType; {http://www.isotc211.org/2005/gmd}DS_Platform_Type; {http://www.isotc211.org/2005/gmd}DS_Sensor_Type; {http://www.isotc211.org/2005/gmd}DS_ProductionSeries_Type; {http://www.isotc211.org/2005/gmd}DS_StereoMate_Type; {http://www.isotc211.org/2005/gmd}MD_Georeferenceable_Type; {http://www.isotc211.org/2005/gmd}MD_Georectified_Type
    URL, AbstractDQ_Completeness, AbstractDQ_Completeness_Type,
    AbstractDQ_Element, AbstractDQ_Element_Type, AbstractDQ_LogicalConsistency,
    AbstractDQ_LogicalConsistency_Type, AbstractDQ_PositionalAccuracy,
    AbstractDQ_PositionalAccuracy_Type, AbstractDQ_Result,
    AbstractDQ_Result_Type, AbstractDQ_TemporalAccuracy,
    AbstractDQ_TemporalAccuracy_Type, AbstractDQ_ThematicAccuracy,
    AbstractDQ_ThematicAccuracy_Type, AbstractDS_Aggregate,
    AbstractDS_Aggregate_Type, AbstractEX_GeographicExtent,
    AbstractEX_GeographicExtent_Type, AbstractMD_ContentInformation,
    AbstractMD_ContentInformation_Type, AbstractMD_Identification,
    AbstractMD_Identification_Type, AbstractMD_SpatialRepresentation,
    AbstractMD_SpatialRepresentation_Type, AbstractRS_ReferenceSystem,
    AbstractRS_ReferenceSystem_Type, CI_Address, CI_Address_PropertyType,
    CI_Address_Type, CI_Citation, CI_Citation_PropertyType, CI_Citation_Type,
    CI_Contact, CI_Contact_PropertyType, CI_Contact_Type, CI_Date,
    CI_Date_PropertyType, CI_Date_Type, CI_DateTypeCode,
    CI_DateTypeCode_PropertyType, CI_OnLineFunctionCode,
    CI_OnLineFunctionCode_PropertyType, CI_OnlineResource,
    CI_OnlineResource_PropertyType, CI_OnlineResource_Type,
    CI_PresentationFormCode, CI_PresentationFormCode_PropertyType,
    CI_ResponsibleParty, CI_ResponsibleParty_PropertyType,
    CI_ResponsibleParty_Type, CI_RoleCode, CI_RoleCode_PropertyType, CI_Series,
    CI_Series_PropertyType, CI_Series_Type, CI_Telephone,
    CI_Telephone_PropertyType, CI_Telephone_Type, Country,
    Country_PropertyType, DQ_AbsoluteExternalPositionalAccuracy,
    DQ_AbsoluteExternalPositionalAccuracy_PropertyType,
    DQ_AbsoluteExternalPositionalAccuracy_Type, DQ_AccuracyOfATimeMeasurement,
    DQ_AccuracyOfATimeMeasurement_PropertyType,
    DQ_AccuracyOfATimeMeasurement_Type, DQ_Completeness_PropertyType,
    DQ_CompletenessCommission, DQ_CompletenessCommission_PropertyType,
    DQ_CompletenessCommission_Type, DQ_CompletenessOmission,
    DQ_CompletenessOmission_PropertyType, DQ_CompletenessOmission_Type,
    DQ_ConceptualConsistency, DQ_ConceptualConsistency_PropertyType,
    DQ_ConceptualConsistency_Type, DQ_ConformanceResult,
    DQ_ConformanceResult_PropertyType, DQ_ConformanceResult_Type,
    DQ_DataQuality, DQ_DataQuality_PropertyType, DQ_DataQuality_Type,
    DQ_DomainConsistency, DQ_DomainConsistency_PropertyType,
    DQ_DomainConsistency_Type, DQ_Element_PropertyType,
    DQ_EvaluationMethodTypeCode, DQ_EvaluationMethodTypeCode_PropertyType,
    DQ_FormatConsistency, DQ_FormatConsistency_PropertyType,
    DQ_FormatConsistency_Type, DQ_GriddedDataPositionalAccuracy,
    DQ_GriddedDataPositionalAccuracy_PropertyType,
    DQ_GriddedDataPositionalAccuracy_Type, DQ_LogicalConsistency_PropertyType,
    DQ_NonQuantitativeAttributeAccuracy,
    DQ_NonQuantitativeAttributeAccuracy_PropertyType,
    DQ_NonQuantitativeAttributeAccuracy_Type,
    DQ_PositionalAccuracy_PropertyType, DQ_QuantitativeAttributeAccuracy,
    DQ_QuantitativeAttributeAccuracy_PropertyType,
    DQ_QuantitativeAttributeAccuracy_Type, DQ_QuantitativeResult,
    DQ_QuantitativeResult_PropertyType, DQ_QuantitativeResult_Type,
    DQ_RelativeInternalPositionalAccuracy,
    DQ_RelativeInternalPositionalAccuracy_PropertyType,
    DQ_RelativeInternalPositionalAccuracy_Type, DQ_Result_PropertyType,
    DQ_Scope, DQ_Scope_PropertyType, DQ_Scope_Type,
    DQ_TemporalAccuracy_PropertyType, DQ_TemporalConsistency,
    DQ_TemporalConsistency_PropertyType, DQ_TemporalConsistency_Type,
    DQ_TemporalValidity, DQ_TemporalValidity_PropertyType,
    DQ_TemporalValidity_Type, DQ_ThematicAccuracy_PropertyType,
    DQ_ThematicClassificationCorrectness,
    DQ_ThematicClassificationCorrectness_PropertyType,
    DQ_ThematicClassificationCorrectness_Type, DQ_TopologicalConsistency,
    DQ_TopologicalConsistency_PropertyType, DQ_TopologicalConsistency_Type,
    DS_Aggregate_PropertyType, DS_Association, DS_Association_PropertyType,
    DS_Association_Type, DS_AssociationTypeCode,
    DS_AssociationTypeCode_PropertyType, DS_DataSet, DS_DataSet_PropertyType,
    DS_DataSet_Type, DS_Initiative, DS_Initiative_PropertyType,
    DS_Initiative_Type, DS_InitiativeTypeCode,
    DS_InitiativeTypeCode_PropertyType, DS_OtherAggregate,
    DS_OtherAggregate_PropertyType, DS_OtherAggregate_Type, DS_Platform,
    DS_Platform_PropertyType, DS_Platform_Type, DS_ProductionSeries,
    DS_ProductionSeries_PropertyType, DS_ProductionSeries_Type, DS_Sensor,
    DS_Sensor_PropertyType, DS_Sensor_Type, DS_Series, DS_Series_PropertyType,
    DS_Series_Type, DS_StereoMate, DS_StereoMate_PropertyType,
    DS_StereoMate_Type, EX_BoundingPolygon, EX_BoundingPolygon_PropertyType,
    EX_BoundingPolygon_Type, EX_Extent, EX_Extent_PropertyType, EX_Extent_Type,
    EX_GeographicBoundingBox, EX_GeographicBoundingBox_PropertyType,
    EX_GeographicBoundingBox_Type, EX_GeographicDescription,
    EX_GeographicDescription_PropertyType, EX_GeographicDescription_Type,
    EX_GeographicExtent_PropertyType, EX_SpatialTemporalExtent,
    EX_SpatialTemporalExtent_PropertyType, EX_SpatialTemporalExtent_Type,
    EX_TemporalExtent, EX_TemporalExtent_PropertyType, EX_TemporalExtent_Type,
    EX_VerticalExtent, EX_VerticalExtent_PropertyType, EX_VerticalExtent_Type,
    LanguageCode, LanguageCode_PropertyType, LI_Lineage,
    LI_Lineage_PropertyType, LI_Lineage_Type, LI_ProcessStep,
    LI_ProcessStep_PropertyType, LI_ProcessStep_Type, LI_Source,
    LI_Source_PropertyType, LI_Source_Type, LocalisedCharacterString,
    LocalisedCharacterString_PropertyType, LocalisedCharacterString_Type,
    MD_AggregateInformation, MD_AggregateInformation_PropertyType,
    MD_AggregateInformation_Type, MD_ApplicationSchemaInformation,
    MD_ApplicationSchemaInformation_PropertyType,
    MD_ApplicationSchemaInformation_Type, MD_Band, MD_Band_PropertyType,
    MD_Band_Type, MD_BrowseGraphic, MD_BrowseGraphic_PropertyType,
    MD_BrowseGraphic_Type, MD_CellGeometryCode,
    MD_CellGeometryCode_PropertyType, MD_CharacterSetCode,
    MD_CharacterSetCode_PropertyType, MD_ClassificationCode,
    MD_ClassificationCode_PropertyType, MD_Constraints,
    MD_Constraints_PropertyType, MD_Constraints_Type,
    MD_ContentInformation_PropertyType, MD_CoverageContentTypeCode,
    MD_CoverageContentTypeCode_PropertyType, MD_CoverageDescription,
    MD_CoverageDescription_PropertyType, MD_CoverageDescription_Type,
    MD_DataIdentification, MD_DataIdentification_PropertyType,
    MD_DataIdentification_Type, MD_DatatypeCode, MD_DatatypeCode_PropertyType,
    MD_DigitalTransferOptions, MD_DigitalTransferOptions_PropertyType,
    MD_DigitalTransferOptions_Type, MD_Dimension, MD_Dimension_PropertyType,
    MD_Dimension_Type, MD_DimensionNameTypeCode,
    MD_DimensionNameTypeCode_PropertyType, MD_Distribution,
    MD_Distribution_PropertyType, MD_Distribution_Type, MD_DistributionUnits,
    MD_DistributionUnits_PropertyType, MD_Distributor,
    MD_Distributor_PropertyType, MD_Distributor_Type,
    MD_ExtendedElementInformation, MD_ExtendedElementInformation_PropertyType,
    MD_ExtendedElementInformation_Type, MD_FeatureCatalogueDescription,
    MD_FeatureCatalogueDescription_PropertyType,
    MD_FeatureCatalogueDescription_Type, MD_Format, MD_Format_PropertyType,
    MD_Format_Type, MD_GeometricObjects, MD_GeometricObjects_PropertyType,
    MD_GeometricObjects_Type, MD_GeometricObjectTypeCode,
    MD_GeometricObjectTypeCode_PropertyType, MD_Georectified,
    MD_Georectified_PropertyType, MD_Georectified_Type, MD_Georeferenceable,
    MD_Georeferenceable_PropertyType, MD_Georeferenceable_Type,
    MD_GridSpatialRepresentation, MD_GridSpatialRepresentation_PropertyType,
    MD_GridSpatialRepresentation_Type, MD_Identification_PropertyType,
    MD_Identifier, MD_Identifier_PropertyType, MD_Identifier_Type,
    MD_ImageDescription, MD_ImageDescription_PropertyType,
    MD_ImageDescription_Type, MD_ImagingConditionCode,
    MD_ImagingConditionCode_PropertyType, MD_Keywords,
    MD_Keywords_PropertyType, MD_Keywords_Type, MD_KeywordTypeCode,
    MD_KeywordTypeCode_PropertyType, MD_LegalConstraints,
    MD_LegalConstraints_PropertyType, MD_LegalConstraints_Type,
    MD_MaintenanceFrequencyCode, MD_MaintenanceFrequencyCode_PropertyType,
    MD_MaintenanceInformation, MD_MaintenanceInformation_PropertyType,
    MD_MaintenanceInformation_Type, MD_Medium, MD_Medium_PropertyType,
    MD_Medium_Type, MD_MediumFormatCode, MD_MediumFormatCode_PropertyType,
    MD_MediumNameCode, MD_MediumNameCode_PropertyType, MD_Metadata,
    MD_Metadata_PropertyType, MD_Metadata_Type,
    MD_MetadataExtensionInformation,
    MD_MetadataExtensionInformation_PropertyType,
    MD_MetadataExtensionInformation_Type, MD_ObligationCode,
    MD_ObligationCode_PropertyType, MD_ObligationCode_Type,
    MD_PixelOrientationCode, MD_PixelOrientationCode_PropertyType,
    MD_PixelOrientationCode_Type, MD_PortrayalCatalogueReference,
    MD_PortrayalCatalogueReference_PropertyType,
    MD_PortrayalCatalogueReference_Type, MD_ProgressCode,
    MD_ProgressCode_PropertyType, MD_RangeDimension,
    MD_RangeDimension_PropertyType, MD_RangeDimension_Type, MD_ReferenceSystem,
    MD_ReferenceSystem_PropertyType, MD_ReferenceSystem_Type,
    MD_RepresentativeFraction, MD_RepresentativeFraction_PropertyType,
    MD_RepresentativeFraction_Type, MD_Resolution, MD_Resolution_PropertyType,
    MD_Resolution_Type, MD_RestrictionCode, MD_RestrictionCode_PropertyType,
    MD_ScopeCode, MD_ScopeCode_PropertyType, MD_ScopeDescription,
    MD_ScopeDescription_PropertyType, MD_ScopeDescription_Type,
    MD_SecurityConstraints, MD_SecurityConstraints_PropertyType,
    MD_SecurityConstraints_Type, MD_ServiceIdentification,
    MD_ServiceIdentification_PropertyType, MD_ServiceIdentification_Type,
    MD_SpatialRepresentation_PropertyType, MD_SpatialRepresentationTypeCode,
    MD_SpatialRepresentationTypeCode_PropertyType, MD_StandardOrderProcess,
    MD_StandardOrderProcess_PropertyType, MD_StandardOrderProcess_Type,
    MD_TopicCategoryCode, MD_TopicCategoryCode_PropertyType,
    MD_TopicCategoryCode_Type, MD_TopologyLevelCode,
    MD_TopologyLevelCode_PropertyType, MD_Usage, MD_Usage_PropertyType,
    MD_Usage_Type, MD_VectorSpatialRepresentation,
    MD_VectorSpatialRepresentation_PropertyType,
    MD_VectorSpatialRepresentation_Type, PT_FreeText, PT_FreeText_PropertyType,
    PT_FreeText_Type, PT_Locale, PT_Locale_PropertyType, PT_Locale_Type,
    PT_LocaleContainer, PT_LocaleContainer_PropertyType,
    PT_LocaleContainer_Type, RS_Identifier, RS_Identifier_PropertyType,
    RS_Identifier_Type, RS_ReferenceSystem_PropertyType, URL_PropertyType)
