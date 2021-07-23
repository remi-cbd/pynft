#!/usr/bin/env python3

from enum import Enum
from typing import List, Union

class ADDR_FAMILY(Enum):
	IP		= "ip"
	IP6		= "ip6"
	INET	= "inet"
	ARP		= "arp"
	BRIDGE	= "bridge"
	NETDEV	= "netdev"

class CHAIN_TYPE(Enum):
	FILTER	= "filter"
	ROUTE	= "route"
	NAT		= "nat"

class CHAIN_HOOK(Enum):
	PREROUTING	= "prerouting"
	INPUT		= "input"
	FORWARD		= "forward"
	OUTPUT		= "output"
	POSTROUTING	= "postrouting"
	INGRESS		= "ingress"

class CHAIN_PRIORITY(Enum):
	NF_IP_PRI_CONNTRACK_DEFRAG	= -400
	NF_IP_PRI_RAW				= -300
	NF_IP_PRI_SELINUX_FIRST		= -225
	NF_IP_PRI_CONNTRACK			= -200
	NF_IP_PRI_MANGLE			= -150
	NF_IP_PRI_NAT_DST			= -100
	NF_IP_PRI_FILTER			= 0
	NF_IP_PRI_SECURITY			= 50
	NF_IP_PRI_NAT_SRC			= 100
	NF_IP_PRI_SELINUX_LAST		= 225
	NF_IP_PRI_CONNTRACK_HELPER	= 300

class CHAIN_POLICY(Enum):
	ACCEPT		= "accept"
	DROP		= "drop"
	QUEUE		= "queue"
	CONTINUE	= "continue"
	RETURN		= "return"

class SET_TYPE(Enum):
	IPV4_ADDR		= "ipv4_addr"
	IPV6_ADDR		= "ipv6_addr"
	ETHER_ADDR		= "ether_addr"
	INET_PROTO		= "inet_proto"
	INET_SERVICE	= "inet_service"
	MARK			= "mark"
	IFNAME			= "ifname"
SET_TYPE_ARRAY = List[SET_TYPE]
SET_TYPES = Union[SET_TYPE, SET_TYPE_ARRAY]

class SET_POLICY(Enum):
	PERFORMANCE	= "performance"
	MEMORY		= "memory"

class SET_FLAG(Enum):
	CONSTANT	= "constant"
	INTERVAL	= "interval"
	TIMEOUT		= "timeout"
SET_FLAG_ARRAY = List[SET_FLAG]

class CT_HELPER_PROTO(Enum):
	TCP	= "tcp"
	UDP	= "udp"

class TIME_UNIT(Enum):
	SECOND	= "second"
	MINUTE	= "minute"
	HOUR	= "hour"
	DAY		= "day"
	WEEK	= "week"

class LIMIT_UNIT(Enum):
	PACKETS	= "packets"
	BYTES	= "bytes"

class CT_TIMEOUT_PROTO(Enum):
	TCP		= "tcp"
	UDP		= "udp"
	DCCP	= "dccp"
	SCTP	= "sctp"
	GRE		= "gre"
	ICMPV6	= "icmpv6"
	ICMP	= "icmp"
	GENERIC	= "generic"

class CT_EXPECTATION_PROTO(Enum):
	TCP		= "tcp"
	UDP		= "udp"
	DCCP	= "dccp"
	SCTP	= "sctp"
	GRE		= "gre"
	ICMPV6	= "icmpv6"
	ICMP	= "icmp"
	GENERIC	= "generic"

class OPERATOR(Enum):
	AND					= "&"
	OR					= "|"
	XOR					= "^"
	LEFT_SHIFT			= "<<"
	RIGHT_SHIFT			= ">>"
	EQUAL				= "=="
	NEQUAL				= "!="
	LESS_THAN			= "<"
	GREATER_THAN		= ">"
	LESS_OR_EQUAL		= "<="
	GREATER_OR_EQUAL	= ">="
	LOOKUP				= "in"


class FWD_FAMILY(Enum):
	IP	= "ip"
	IP6	= "ip6"

class NAT_REDIRECT_FLAG(Enum):
	RANDOM		= "random"
	FULLY		= "fully-random"
	PERSISTENT	= "persistent"
NAT_REDIRECT_FLAG_ARRAY = List[NAT_REDIRECT_FLAG]
NAT_REDIRECT_FLAGS = Union[NAT_REDIRECT_FLAG, NAT_REDIRECT_FLAG_ARRAY]

class SET_OPERATOR(Enum):
	ADD		= "add"
	UPDATE	= "update"

class LEVEL(Enum):
	EMERG	= "emerg"
	ALERT	= "alert"
	CRIT	= "crit"
	ERR		= "err"
	WARN	= "warn"
	NOTICE	= "notice"
	INFO	=  "info"
	DEBUG	= "debug"
	AUDIT	= "audit"

class LOG_FLAG(Enum):
	TCP_SEQUENCE	= "tcp sequence"
	TCP_OPTION		= "tcp options"
	IP				= "ip options"
	SKUID			= "skuid"
	ETHER			= "ether"
	ALL				= "all"
LOG_FLAG_ARRAY = List[LOG_FLAG]
LOG_FLAGS = Union[LOG_FLAG, LOG_FLAG_ARRAY]

class QUEUE_FLAG(Enum):
	BYPASS	= "bypass"
	FANOUT	= "fanout"
QUEUE_FLAG_ARRAY = List[QUEUE_FLAG]
QUEUE_FLAGS = Union[QUEUE_FLAG, QUEUE_FLAG_ARRAY]

class BASE(Enum):
	LL	= "ll"
	NH	= "nh"
	TH	= "th"

class META_KEY(Enum):
	LENGTH		= "length"
	PROTOCOL	= "protocol"
	PRIORITY	= "priority"
	RANDOM		= "random"
	MARK		= "mark"
	IIF			= "iif"
	IIFNAME		= "iifname"
	IIFTYPE		= "iiftype"
	OIF			= "oif"
	OIFNAME		= "oifname"
	OIFTYPE		= "oiftype"
	SKUID		= "skuid"
	SKGID		= "skgid"
	NFTRACE		= "nftrace"
	RTCLASSID	= "rtclassid"
	IBRIPORT	= "ibriport"
	OBRIPORT	= "obriport"
	IBRIDGENAME	= "ibridgename"
	OBRIDGENAME	= "obridgename"
	PKTTYPE		= "pkttype"
	CPU			= "cpu"
	IIFGROUP	= "iifgroup"
	OIFGROUP	= "oifgroup"
	CGROUP		= "cgroup"
	NFPROTO		= "nfproto"
	L4PROTO		= "l4proto"
	SECPATH		= "secpath"

class RT_KEY(Enum):
	CLASSID	= "classid"
	NEXTHOP	= "nexthop"
	MTU		= "mtu"

class RT_FAMILY(Enum):
	IP	= "ip"
	IP6	= "ip6"

class CT_FAMILY(Enum):
	IP	= "ip"
	IP6	= "ip6"

class CT_DIRECTION(Enum):
	ORIGINAL	= "original"
	REPLY		= "reply"

class NG_MODE(Enum):
	INC		= "inc"
	RANDOM	= "random"

class FIB_RESULT(Enum):
	OIF		= "oif"
	OIFNAME	= "oifname"
	TYPE	= "type"

class FIB_FLAG(Enum):
	SADDR	= "saddr"
	DADDR	= "daddr"
	MARK	= "mark"
	IIF		= "iif"
	OIF		= "oif"

class BO_KEY(Enum):
	OR			= "|"
	XOR			= "^"
	AND			= "&"
	LEFT_SHIFT	= "<<"
	RIGHT_SHIFT	= ">>"

class SOCKET_KEY(Enum):
	TRANSPARENT = "transparent"

class OSF_KEY(Enum):
	NAME = "name"

class OSF_TTL(Enum):
	LOOSE	= "loose"
	SKIP	= "skip"