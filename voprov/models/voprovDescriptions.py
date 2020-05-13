# -*- coding: ISO-8859-1 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from prov.model import (ProvElement)
from voprov.models.constants import *


class VOProvDescription(ProvElement):
    """Base class for VOProvDescription classes"""
    FORMAL_ATTRIBUTES = None
    _prov_type = None


class VOProvActivityDescription(VOProvDescription):
    """Class for VOProv activity description"""

    FORMAL_ATTRIBUTES = (VOPROV_ATTR_NAME,)
    _prov_type = VOPROV_ACTIVITY_DESCRIPTION

    def set_name(self, name):
        """Set the name of this activity description.

        :param name:                    A human-readable name for the agent.
        """
        self._attributes[VOPROV_ATTR_NAME] = {name}

    def set_version(self, version):
        """Set a version for this activity description.

        :param version:                 A version number, if applicable (e.g., for the code used).
        """
        self._attributes["voprov:version"] = {version}

    def set_description(self, description):
        """Set a description for this activity description.

        :param description:             Additional free text describing how the activity works internally.
        """
        self._attributes["voprov:description"] = {description}

    def set_docurl(self, docurl):
        """Set a docurl for this activity description.

        :param docurl:                  Link to further documentation on this activity, e.g., a paper, the source code
                                        in a version control system etc.
        """
        self._attributes["voprov:docurl"] = {docurl}

    def set_type(self, type):
        """Set the type of this activity description.

        :param type:                    Type of the activity.
        """
        self._attributes["voprov:type"] = {type}

    def set_subtype(self, subtype):
        """Set a subtype for this activity description.

        :param subtype:                 More specific subtype of the activity.
        """
        self._attributes["voprov:subtype"] = {subtype}

    def isDescriptorOf_activity(self, activity, identifier=None):
        """
        Creates a new relation between an activity and this activity description.

        :param activity:                Identifier or object of the activity described by this activity description.
        :param identifier:              Identifier for the relation between this activity description and the activity
                                        (default: None).
        """
        return self._bundle.description(activity, self, identifier)

    def usageDescription(self, identifier, role, description=None, type=None,
                         multiplicity=None, other_attributes=None):
        """
        Creates a new usage description.

        :param identifier:              Identifier for new usage description.
        :param role:                    Function of the entity with respect to the activity.
        :param description:             A descriptive text for this kind of usage (default: None).
        :param type:                    Type of relation (default: None).
        :param multiplicity:            Number of expected input entities to be used with the given role
                                        (default: None).
        :param other_attributes:        Optional other attributes as a dictionary or list
                                        of tuples to be added to the record optionally (default: None).
        """
        return self._bundle.usageDescription(identifier, self, role, description, type, multiplicity, other_attributes)

    def generationDescription(self, identifier, role, description=None, type=None,
                              multiplicity=None, other_attributes=None):
        """
        Creates a new generation description.

        :param identifier:              Identifier for new generation description.
        :param role:                    Function of the entity with respect to the activity.
        :param description:             A descriptive text for this kind of generation (default: None).
        :param type:                    Type of relation (default: None).
        :param multiplicity:            Number of expected input entities to be generated with the given role
                                        (default: None).
        :param other_attributes:        Optional other attributes as a dictionary or list
                                        of tuples to be added to the record optionally (default: None).
        """
        return self._bundle.generationDescription(identifier, self, role, description, type,
                                                  multiplicity, other_attributes)


class VOProvGenerationDescription(VOProvDescription):
    """Class for VOProv generation description"""

    FORMAL_ATTRIBUTES = (VOPROV_ATTR_ROLE,)
    _prov_type = VOPROV_GENERATION_DESCRIPTION

    def set_role(self, role):
        """Set the role of this generation description.

        :param role:                    Function of the entity with respect to the activity.
        """
        self._attributes[VOPROV_ATTR_ROLE] = {role}

    def set_description(self, description):
        """Set a description for this generation description.

        :param description:             A descriptive text for this kind of generation.
        """
        self._attributes["voprov:description"] = {description}

    def set_type(self, type):
        """Set the type of this generation description.

        :param type:                    Type of relation.
        """
        self._attributes["voprov:type"] = {type}

    def set_multiplicity(self, multiplicity):
        """Set a multiplicity for this generation description.

        :param multiplicity:            Number of expected input entities to be generated with the given role.
        """
        self._attributes["voprov:multiplicity"] = {multiplicity}

    def isRelatedTo_entityDescription(self, entity_description, identifier=None):
        """
        Creates a new relation between this generation description and a entity description.

        :param entity_description:      The entity description related to this generation description.
        :param identifier:              Identifier for new isRelatedTo relation record (default: None).
        """
        return self._bundle.relate(entity_description, self, identifier)

    def isDescriptorOf_generation(self, wasGeneratedBy, identifier=None):
        """
        Creates a new relation between an usage and this usage description.

        :param wasGeneratedBy:          The generated relation described by this generation description.
        :param identifier:              Identifier for new isDescribedBy relation record (default: None).
        """
        return self._bundle.description(wasGeneratedBy, self, identifier)


class VOProvUsageDescription(VOProvDescription):
    """Class for VOProv usage description"""

    FORMAL_ATTRIBUTES = (VOPROV_ATTR_ROLE,)
    _prov_type = VOPROV_USAGE_DESCRIPTION

    def set_role(self, role):
        """Set the role of this usage description.

        :param role:                    Function of the entity with respect to the activity.
        """
        self._attributes[VOPROV_ATTR_ROLE] = {role}

    def set_description(self, description):
        """Set a description for this usage description.

        :param description:             A descriptive text for this kind of usage.
        """
        self._attributes["voprov:description"] = {description}

    def set_type(self, type):
        """Set the type of this usage description.

        :param type:                    Type of relation.
        """
        self._attributes["voprov:type"] = {type}

    def set_multiplicity(self, multiplicity):
        """Set a multiplicity for this usage description.

        :param multiplicity:            Number of expected input entities to be used with the given role.
        """
        self._attributes["voprov:multiplicity"] = {multiplicity}

    def isRelatedTo_entityDescription(self, entity_description, identifier=None):
        """
        Creates a new relation between this usage description and an entity description.

        :param entity_description:      The entity description related to this usage description.
        :param identifier:              Identifier for new isRelatedTo relation record (default: None).
        """
        return self._bundle.relate(entity_description, self, identifier)

    def isDescriptorOf_usage(self, used, identifier=None):
        """
        Creates a new relation between an usage and this usage description.

        :param used:                    The used relation described by this usage description.
        :param identifier:              Identifier for new isDescribedBy relation record (default: None).
        """
        return self._bundle.description(used, self, identifier)


class VOProvEntityDescription(VOProvDescription):
    """Base class for VOProv entity description classes"""

    FORMAL_ATTRIBUTES = (VOPROV_ATTR_NAME,)
    _prov_type = VOPROV_ENTITY_DESCRIPTION

    def set_name(self, name):
        """Set the role of this usage description.

        :param name:                    A human-readable name for the entity description.
        """
        self._attributes[VOPROV_ATTR_NAME] = {name}

    def set_description(self, description):
        """Set a description for this entity description.

        :param description:             A descriptive text for this kind of entity.
        """
        self._attributes["voprov:description"] = {description}

    def set_docurl(self, docurl):
        """Set a docurl for this entity description.

        :param docurl:                  Link to more documentation.
        """
        self._attributes["voprov:docurl"] = {docurl}

    def set_type(self, type):
        """Set the type of this entity description.

        :param type:                    Type of the entity.
        """
        self._attributes["voprov:type"] = {type}

    def isDescriptorOf_entity(self, entity, identifier=None):
        """
        Creates a new relation between an entity and this entity description.

        :param entity:                  The entity described by this entity description.
        :param identifier:              Identifier for new isDescribedBy relation record (default: None).
        """
        return self._bundle.description(entity, self, identifier)

    def isRelatedTo_usageDescription(self, usage_description, identifier=None):
        """
        Creates a new relation between an usage description and this entity description.

        :param usage_description:       The usage description related to this entity description.
        :param identifier:              Identifier for new isRelatedTo relation record (default: None).
        """
        return self._bundle.relate(usage_description, self, identifier)

    def isRelatedTo_generationDescription(self, generation_description, identifier=None):
        """
        Creates a new relation between a generation description and this entity description.

        :param generation_description:  The generation description related to this entity description.
        :param identifier:              Identifier for new isRelatedTo relation record (default: None).
        """
        return self._bundle.relate(generation_description, self, identifier)


class VOProvValueDescription(VOProvEntityDescription):
    """Class for VOProv value entity description"""

    FORMAL_ATTRIBUTES = None
    _prov_type = None


class VOProvDataSetDescription(VOProvEntityDescription):
    """Class for VOProv data set entity description"""

    FORMAL_ATTRIBUTES = None
    _prov_type = None


class VOProvConfigFileDescription(VOProvEntityDescription):
    """Class for VOProv configuration file description"""

    FORMAL_ATTRIBUTES = None
    _prov_type = None


class VOProvParameterDescription(VOProvDescription):
    """Class for VOProv parameter description"""

    FORMAL_ATTRIBUTES = None
    _prov_type = None
