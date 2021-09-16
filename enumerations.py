#!/usr/bin/env python3

from enum import Enum
from typing import List, Union



#
#	PyNFT Enumerations
#

class NFT_ENUM(Enum):
	def __str__(self):
		return str(self.value)

class ADDR_FAMILY(NFT_ENUM):
	IP		= "ip"
	IP6		= "ip6"
	INET	= "inet"
	ARP		= "arp"
	BRIDGE	= "bridge"
	NETDEV	= "netdev"

class CHAIN_TYPE(NFT_ENUM):
	FILTER	= "filter"
	ROUTE	= "route"
	NAT		= "nat"

class CHAIN_HOOK(NFT_ENUM):
	PREROUTING	= "prerouting"
	INPUT		= "input"
	FORWARD		= "forward"
	OUTPUT		= "output"
	POSTROUTING	= "postrouting"
	INGRESS		= "ingress"

class CHAIN_PRIORITY(NFT_ENUM):
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

class CHAIN_POLICY(NFT_ENUM):
	ACCEPT		= "accept"
	DROP		= "drop"
	QUEUE		= "queue"
	CONTINUE	= "continue"
	RETURN		= "return"

class SET_TYPE(NFT_ENUM):
	IPV4_ADDR		= "ipv4_addr"
	IPV6_ADDR		= "ipv6_addr"
	ETHER_ADDR		= "ether_addr"
	INET_PROTO		= "inet_proto"
	INET_SERVICE	= "inet_service"
	MARK			= "mark"
	IFNAME			= "ifname"
SET_TYPE_ARRAY = List[SET_TYPE]
SET_TYPES = Union[SET_TYPE, SET_TYPE_ARRAY]

class SET_POLICY(NFT_ENUM):
	PERFORMANCE	= "performance"
	MEMORY		= "memory"

class SET_FLAG(NFT_ENUM):
	CONSTANT	= "constant"
	INTERVAL	= "interval"
	TIMEOUT		= "timeout"
SET_FLAG_ARRAY = List[SET_FLAG]

class CT_HELPER_PROTO(NFT_ENUM):
	TCP	= "tcp"
	UDP	= "udp"

class TIME_UNIT(NFT_ENUM):
	SECOND	= "second"
	MINUTE	= "minute"
	HOUR	= "hour"
	DAY		= "day"
	WEEK	= "week"

class LIMIT_UNIT(NFT_ENUM):
	PACKETS	= "packets"
	BYTES	= "bytes"

class CT_TIMEOUT_PROTO(NFT_ENUM):
	TCP		= "tcp"
	UDP		= "udp"
	DCCP	= "dccp"
	SCTP	= "sctp"
	GRE		= "gre"
	ICMPV6	= "icmpv6"
	ICMP	= "icmp"
	GENERIC	= "generic"

class CT_EXPECTATION_PROTO(NFT_ENUM):
	TCP		= "tcp"
	UDP		= "udp"
	DCCP	= "dccp"
	SCTP	= "sctp"
	GRE		= "gre"
	ICMPV6	= "icmpv6"
	ICMP	= "icmp"
	GENERIC	= "generic"

class OPERATOR(NFT_ENUM):
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


class FWD_FAMILY(NFT_ENUM):
	IP	= "ip"
	IP6	= "ip6"

class NAT_REDIRECT_FLAG(NFT_ENUM):
	RANDOM		= "random"
	FULLY		= "fully-random"
	PERSISTENT	= "persistent"
NAT_REDIRECT_FLAG_ARRAY = List[NAT_REDIRECT_FLAG]
NAT_REDIRECT_FLAGS = Union[NAT_REDIRECT_FLAG, NAT_REDIRECT_FLAG_ARRAY]

class SET_OPERATOR(NFT_ENUM):
	ADD		= "add"
	UPDATE	= "update"

class LEVEL(NFT_ENUM):
	EMERG	= "emerg"
	ALERT	= "alert"
	CRIT	= "crit"
	ERR		= "err"
	WARN	= "warn"
	NOTICE	= "notice"
	INFO	=  "info"
	DEBUG	= "debug"
	AUDIT	= "audit"

class LOG_FLAG(NFT_ENUM):
	TCP_SEQUENCE	= "tcp sequence"
	TCP_OPTION		= "tcp options"
	IP				= "ip options"
	SKUID			= "skuid"
	ETHER			= "ether"
	ALL				= "all"
LOG_FLAG_ARRAY = List[LOG_FLAG]
LOG_FLAGS = Union[LOG_FLAG, LOG_FLAG_ARRAY]

class QUEUE_FLAG(NFT_ENUM):
	BYPASS	= "bypass"
	FANOUT	= "fanout"
QUEUE_FLAG_ARRAY = List[QUEUE_FLAG]
QUEUE_FLAGS = Union[QUEUE_FLAG, QUEUE_FLAG_ARRAY]

class BASE(NFT_ENUM):
	LL	= "ll"
	NH	= "nh"
	TH	= "th"

class META_KEY(NFT_ENUM):
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

class RT_KEY(NFT_ENUM):
	CLASSID	= "classid"
	NEXTHOP	= "nexthop"
	MTU		= "mtu"

class RT_FAMILY(NFT_ENUM):
	IP	= "ip"
	IP6	= "ip6"

class CT_FAMILY(NFT_ENUM):
	IP	= "ip"
	IP6	= "ip6"

class CT_DIRECTION(NFT_ENUM):
	ORIGINAL	= "original"
	REPLY		= "reply"

class NG_MODE(NFT_ENUM):
	INC		= "inc"
	RANDOM	= "random"

class FIB_RESULT(NFT_ENUM):
	OIF		= "oif"
	OIFNAME	= "oifname"
	TYPE	= "type"

class FIB_FLAG(NFT_ENUM):
	SADDR	= "saddr"
	DADDR	= "daddr"
	MARK	= "mark"
	IIF		= "iif"
	OIF		= "oif"
FIB_FLAG_ARRAY = List[FIB_FLAG]
FIB_FLAGS = Union[FIB_FLAG, FIB_FLAG_ARRAY]

class BO_KEY(NFT_ENUM):
	OR			= "|"
	XOR			= "^"
	AND			= "&"
	LEFT_SHIFT	= "<<"
	RIGHT_SHIFT	= ">>"

class SOCKET_KEY(NFT_ENUM):
	TRANSPARENT = "transparent"

class OSF_KEY(NFT_ENUM):
	NAME = "name"

class OSF_TTL(NFT_ENUM):
	LOOSE	= "loose"
	SKIP	= "skip"