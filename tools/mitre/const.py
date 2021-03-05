#!/usr/bin/env python
#
# Copyright (C) 2015-2021, Wazuh Inc.
# Created by Wazuh, Inc. <info@wazuh.com>.
# This program is a free software; you can redistribute it and/or modify it under the terms of GPLv2

####### Constants #######

TIME_FORMAT= '%Y-%m-%dT%H:%M:%S.%fZ'

### Table

ID_t= 'id'
KEY_t= 'key'
VALUE_t= 'value'
NAME_t= 'name'
DESCRIPTION_t= 'description'
CREATED_t= 'created_time'
MODIFIED_t= 'modified_time'
MITRE_VERSION_t= 'mitre_version'
REVOKED_BY_t= 'revoked_by'
DEPRECATED_t='deprecated'
SHORT_NAME_t='short_name'
MITRE_DETECTION_t= 'mitre_detection'
NETWORK_REQ_t= 'network_requirements'
REMOTE_SUPPORT_t= 'remote_support'
SUBTECHNIQUE_OF_t= 'subtechnique_of'
SOURCE_t= 'source'
DEFENSE_t= 'defense'
PERMISSION_t= 'permission'
IMPACT_t= 'impact'
REQUIREMENT_t= 'requirement'
SOURCE_ID_t= 'source_id'
TARGET_ID_t= 'target_id'
TACTIC_ID_t= 'tactic_id'
TECH_ID_t= 'tech_id'

DB_VERSION_t = 'db_version'
DB_VERSION_N_t = '1'
MITRE_VERSION_t = 'mitre_version'

### Relationships
DATASOURCE_r= 'DataSource'
DEFENSEBYPASSES_r='DefenseByPasses'
EFFECTIVEPERMISSON_r= 'EffectivePermission'
IMPACT_r= 'Impact'
PERMISSION_r= 'Permission'
SYSTEMREQ_r= 'SystemRequirement'
TECHNIQUES_r= 'techniques'
MITIGATE_r= 'Mitigate'

TECHNIQUE_ID_fk= 'techniques.id'
MITIGATION_ID_fk= 'mitigations.id'
TACTICS_ID_fk= 'tactics.id'

### Json index

# Global
TYPE_j= 'type'
OBJECT_j= 'objects'
# Groups
INTRUSION_SET_j= 'intrusion-set'
# Mitigations
COURSE_OF_ACTION_j= 'course-of-action'
# Software
MALWARE_j= 'malware'
TOOL_j= 'tool'
# Tactics
TACTIC_j= 'x-mitre-tactic'
# Techniques
ATTACK_PATTERN_j= 'attack-pattern'

ID_j= 'id'
VERSION_j= 'spec_version'
MARKING_DEFINITION_j= 'marking-definition'
DEFINITION_j= 'definition'
STATEMENT_j= 'statement'
NAME_j= 'name'
DESCRIPTION_j= 'description'
CREATED_j= 'created'
MODIFIED_j= 'modified'
MITRE_VERSION_j= 'x_mitre_version'
DEPRECATED_j='x_mitre_deprecated'
MITRE_DETECTION_j= 'x_mitre_detection'
MITRE_NETWOR_REQ_j= 'x_mitre_network_requirements'
MITRE_REMOTE_SUPP_j= 'x_mitre_remote_support'
DATASOURCE_j= 'x_mitre_data_sources'
DEFENSE_BYPASSED_j= 'x_mitre_defense_bypassed'
EFFECTIVE_PERMISSION_j= 'x_mitre_effective_permissions'
IMPACT_TYPE_j= 'x_mitre_impact_type'
PERMISSIONS_REQ_j= 'x_mitre_permissions_required'
SYSTEM_REQ_j= 'x_mitre_system_requirements'
PHASES_j= 'kill_chain_phases'
PHASE_NAME_j= 'phase_name'
SHORT_NAME_j='x_mitre_shortname'

# Relationship type
RELATIONSHIP_j= 'relationship'
RELATIONSHIP_TYPE_j= 'relationship_type'
REVOKED_BY_j= 'revoked-by'
SOURCE_REF_j='source_ref'
TARGET_REF_j= 'target_ref'
SUBTECHNIQUE_OF_j= 'subtechnique-of'
MITIGATES_j= 'mitigates'
USES_j= 'uses'
