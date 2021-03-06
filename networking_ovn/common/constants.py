#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from neutron_lib.api.definitions import portbindings
from neutron_lib import constants as const
import six

# TODO(lucasagomes): Remove OVN_SG_NAME_EXT_ID_KEY in the Rocky release
OVN_SG_NAME_EXT_ID_KEY = 'neutron:security_group_name'
OVN_SG_EXT_ID_KEY = 'neutron:security_group_id'
OVN_ML2_MECH_DRIVER_NAME = 'ovn'
OVN_NETWORK_NAME_EXT_ID_KEY = 'neutron:network_name'
OVN_PORT_NAME_EXT_ID_KEY = 'neutron:port_name'
OVN_ROUTER_NAME_EXT_ID_KEY = 'neutron:router_name'
OVN_PHYSNET_EXT_ID_KEY = 'neutron:provnet-physical-network'
OVN_NETTYPE_EXT_ID_KEY = 'neutron:provnet-network-type'
OVN_SEGID_EXT_ID_KEY = 'neutron:provnet-segmentation-id'
OVN_PROJID_EXT_ID_KEY = 'neutron:project_id'
OVN_DEVID_EXT_ID_KEY = 'neutron:device_id'
OVN_CIDRS_EXT_ID_KEY = 'neutron:cidrs'
OVN_FIP_EXT_ID_KEY = 'neutron:fip_id'
OVN_FIP_PORT_EXT_ID_KEY = 'neutron:fip_port_id'
OVN_REV_NUM_EXT_ID_KEY = 'neutron:revision_number'
OVN_QOS_POLICY_EXT_ID_KEY = 'neutron:qos_policy_id'
OVN_PORT_BINDING_PROFILE = portbindings.PROFILE
OVN_PORT_BINDING_PROFILE_PARAMS = [{'parent_name': six.string_types,
                                    'tag': six.integer_types},
                                   {'vtep-physical-switch': six.string_types,
                                    'vtep-logical-switch': six.string_types}]
OVN_ROUTER_PORT_OPTION_KEYS = ['router-port', 'nat-addresses']
OVN_GATEWAY_CHASSIS_KEY = 'redirect-chassis'
OVN_GATEWAY_NAT_ADDRESSES_KEY = 'nat-addresses'

OVN_PROVNET_PORT_NAME_PREFIX = 'provnet-'

OVN_NEUTRON_OWNER_TO_PORT_TYPE = {const.DEVICE_OWNER_DHCP: 'localport'}

# OVN ACLs have priorities.  The highest priority ACL that matches is the one
# that takes effect.  Our choice of priority numbers is arbitrary, but it
# leaves room above and below the ACLs we create.  We only need two priorities.
# The first is for all the things we allow.  The second is for dropping traffic
# by default.
ACL_PRIORITY_ALLOW = 1002
ACL_PRIORITY_DROP = 1001

ACL_ACTION_DROP = 'drop'
ACL_ACTION_ALLOW_RELATED = 'allow-related'
ACL_ACTION_ALLOW = 'allow'

# When a OVN L3 gateway is created, it needs to be bound to a chassis. In
# case a chassis is not found OVN_GATEWAY_INVALID_CHASSIS will be set in
# the options column of the Logical Router. This value is used to detect
# unhosted router gateways to schedule.
OVN_GATEWAY_INVALID_CHASSIS = 'neutron-ovn-invalid-chassis'

SUPPORTED_DHCP_OPTS = {
    4: ['netmask', 'router', 'dns-server', 'log-server',
        'lpr-server', 'swap-server', 'ip-forward-enable',
        'policy-filter', 'default-ttl', 'mtu', 'router-discovery',
        'router-solicitation', 'arp-timeout', 'ethernet-encap',
        'tcp-ttl', 'tcp-keepalive', 'nis-server', 'ntp-server',
        'tftp-server'],
    6: ['server-id', 'dns-server', 'domain-search']}
DHCPV6_STATELESS_OPT = 'dhcpv6_stateless'

CHASSIS_DATAPATH_NETDEV = 'netdev'
CHASSIS_IFACE_DPDKVHOSTUSER = 'dpdkvhostuser'

OVN_IPV6_ADDRESS_MODES = {
    const.IPV6_SLAAC: const.IPV6_SLAAC,
    const.DHCPV6_STATEFUL: const.DHCPV6_STATEFUL.replace('-', '_'),
    const.DHCPV6_STATELESS: const.DHCPV6_STATELESS.replace('-', '_')
}

DB_MAX_RETRIES = 60
DB_INITIAL_RETRY_INTERVAL = 0.5
DB_MAX_RETRY_INTERVAL = 1

TXN_COMMITTED = 'committed'
INITIAL_REV_NUM = -1

# Resource types
TYPE_NETWORKS = 'networks'
