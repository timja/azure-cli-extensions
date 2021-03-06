# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .arecord import ARecord
from .aaaa_record import AaaaRecord
from .mx_record import MxRecord
from .ns_record import NsRecord
from .ptr_record import PtrRecord
from .srv_record import SrvRecord
from .txt_record import TxtRecord
from .cname_record import CnameRecord
from .soa_record import SoaRecord
from .caa_record import CaaRecord
from .record_set import RecordSet
from .record_set_update_parameters import RecordSetUpdateParameters
from .sub_resource import SubResource
from .zone import Zone
from .zone_update import ZoneUpdate
from .resource import Resource
from .record_set_paged import RecordSetPaged
from .zone_paged import ZonePaged
from .dns_management_client_enums import (
    ZoneType,
    RecordType,
)

__all__ = [
    'ARecord',
    'AaaaRecord',
    'MxRecord',
    'NsRecord',
    'PtrRecord',
    'SrvRecord',
    'TxtRecord',
    'CnameRecord',
    'SoaRecord',
    'CaaRecord',
    'RecordSet',
    'RecordSetUpdateParameters',
    'SubResource',
    'Zone',
    'ZoneUpdate',
    'Resource',
    'RecordSetPaged',
    'ZonePaged',
    'ZoneType',
    'RecordType',
]
