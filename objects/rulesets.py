#!/usr/bin/env python3

# from pynft.objects.root import NFT_OBJ
# from pynft.objects.enumerations import *
# from pynft.objects.expressions import *
from pynft.objects.statements import *
from typing import List, Union



#
#	Ruleset Objects
#

class RULESET_OBJ(NFT_OBJ):
	objname			: str							= ""


class RULESET(RULESET_OBJ):
	objname			: str							= "ruleset"

class TABLE(RULESET_OBJ):
	objname			: str							= "table"
	family			: ADDR_FAMILY					= ADDR_FAMILY.IP
	name			: str
	handle			: Union[int, None]				= None

TABLE_ARRAY = List[TABLE]
TABLES = Union[TABLE, TABLE_ARRAY]


class CHAIN(RULESET_OBJ):
	objname			: str							= "chain"
	family			: ADDR_FAMILY
	table			: str
	name			: str
	newname			: Union[str, None]				= None
	handle			: Union[int, None]				= None
	type			: Union[CHAIN_TYPE, None]		= None
	hook			: Union[CHAIN_HOOK, None]		= None
	prio			: Union[CHAIN_PRIORITY, None]	= None
	dev				: Union[str, None]				= None
	policy			: Union[CHAIN_POLICY, None]		= None

CHAIN_ARRAY = List[CHAIN]
CHAINS = Union[CHAIN, CHAIN_ARRAY]


class RULE(RULESET_OBJ):
	objname			: str							= "rule"
	family			: ADDR_FAMILY
	table			: str
	chain			: str
	expr			: Union[str, None]				= None
	handle			: Union[int, None]				= None
	index			: Union[int, None]				= None
	comment			: Union[str, None]				= None

class ELEMENT(RULESET_OBJ):
	objname 		: str							= "element"
	family			: ADDR_FAMILY
	table			: str
	name			: str
	elem			: EXPRESSIONS

ELEMENT_ARRAY = List[ELEMENT]
ELEMENTS = Union[ELEMENT, ELEMENT_ARRAY]
SET_ELEMENTS = Union[EXPRESSIONS, ELEMENTS]


class SET(RULESET_OBJ):
	objname			: str							= "set"
	family			: ADDR_FAMILY
	table			: str
	name			: str
	handle			: Union[int, None]				= None
	type			: Union[SET_TYPES, None]		= None
	policy			: Union[SET_POLICY, None]		= None
	flags			: Union[SET_FLAG_ARRAY, None]	= None
	elem			: Union[SET_ELEMENTS, None]		= None
	timeout			: Union[int, None]				= None
	gc_1_interval	: Union[int, None]				= None
	size			: Union[int, None]				= None

SET_ARRAY = List[SET]
SETS = Union[SET, SET_ARRAY]


class MAP(RULESET_OBJ):
	objname			: str							= "map"
	family			: ADDR_FAMILY
	table			: str
	name			: str
	handle			: Union[int, None]				= None
	type			: Union[SET_TYPE, None]			= None
	map				: Union[str, None]				= None
	policy			: Union[SET_POLICY, None]		= None
	flags			: Union[SET_FLAG_ARRAY, None]	= None
	elem			: Union[SET_ELEMENTS, None]		= None
	timeout			: Union[int, None]				= None		# => in the doc:	NUMBER in this format: "v1dv2hv3mv4s" (ex: 3h45s)
	gc_1_interval	: Union[int, None]				= None
	size			: Union[int, None]				= None

MAP_ARRAY = List[MAP]
MAPS = Union[MAP, MAP_ARRAY]


class FLOWTABLE(RULESET_OBJ):
	objname			: str							= "flowtable"
	family			: ADDR_FAMILY
	table			: str
	name			: str
	handle			: Union[int, None]				= None
	hook			: str
	prio			: Union[int, None]				= None
	dev				: str

FLOWTABLE_ARRAY = List[FLOWTABLE]
FLOWTABLES = Union[FLOWTABLE, FLOWTABLE_ARRAY]


class COUNTER(RULESET_OBJ):
	objname			: str							= "counter"
	family			: ADDR_FAMILY
	table			: str
	name			: str
	handle			: Union[int, None]				= None
	packets			: int
	bytes			: int

COUNTER_ARRAY = List[COUNTER]
COUNTERS = Union[COUNTER, COUNTER_ARRAY]


class QUOTA(RULESET_OBJ):
	objname			: str							= "quota"
	family			: ADDR_FAMILY
	table			: str
	name			: str
	handle			: Union[int, None]				= None
	bytes			: int
	used			: int
	inv				: bool

QUOTA_ARRAY = List[QUOTA]
QUOTAS = Union[QUOTA, QUOTA_ARRAY]


class CT_HELPER(RULESET_OBJ):
	objname			: str							= "ct helper"
	family			: ADDR_FAMILY
	table			: str
	name			: str
	handle			: Union[int, None]				= None
	type			: str
	protocol		: CT_HELPER_PROTO
	l3proto			: str

CT_HELPER_ARRAY = List[CT_HELPER]
CT_HELPERS = Union[CT_HELPER, CT_HELPER_ARRAY]


class LIMIT(RULESET_OBJ):
	objname			: str							= "limit"
	family			: ADDR_FAMILY
	table			: str
	name			: str
	handle			: Union[int, None]				= None
	rate			: int
	per				: TIME_UNIT						= TIME_UNIT.SECOND
	burst			: int							= 0
	unit			: LIMIT_UNIT					= "packets"
	inv				: bool							= False

LIMIT_ARRAY = List[LIMIT]
LIMITS = Union[LIMIT, LIMIT_ARRAY]


class CT_TIMEOUT(RULESET_OBJ):
	objname			: str							= "ct timeout"
	family			: ADDR_FAMILY
	table			: str
	name			: str
	handle			: Union[int, None]				= None
	protocol		: CT_TIMEOUT_PROTO
	state			: str
	value			: int
	l3proto			: str

class CT_EXPECTATION(RULESET_OBJ):
	objname			: str							= "ct expectation"
	family			: ADDR_FAMILY
	table			: str
	name			: str
	handle			: Union[int, None]				= None
	l3proto			: str
	protocol		: CT_EXPECTATION_PROTO
	dport			: int
	timeout			: int
	size			: int