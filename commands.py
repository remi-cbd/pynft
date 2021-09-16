#!/usr/bin/env python3

from typing import Union

from pynft.root import NFT_OBJ
from pynft.statements import METER, METERS
from pynft.objects import CHAIN, CHAINS, COUNTER, COUNTERS, CT_EXPECTATION, CT_HELPER, CT_HELPERS, CT_TIMEOUT, ELEMENT, FLOWTABLE, FLOWTABLES, LIMIT, LIMITS, MAP, MAPS, QUOTA, QUOTAS, RULE, RULESET, SET, SETS, TABLE, TABLES



#
#	Command Unions
#

ADD_OBJ = Union[TABLE,
				CHAIN,
				RULE,
				SET,
				MAP,
				ELEMENT,
				FLOWTABLE,
				COUNTER,
				QUOTA,
				CT_HELPER,
				LIMIT,
				CT_TIMEOUT,
				CT_EXPECTATION ]

LIST_OBJ = Union[RULESET,
				TABLES,
				CHAINS,
				SETS,
				MAPS,
				COUNTERS,
				QUOTAS,
				CT_HELPERS,
				LIMITS,
				METERS,
				FLOWTABLES,
				CT_TIMEOUT,
				CT_EXPECTATION ]

RESET_OBJ = Union[COUNTERS, QUOTAS]

FLUSH_OBJ = Union[RULESET, TABLE, CHAIN, SET, MAP, METER]



#
#	Command Objects
#

class CMD_OBJ(NFT_OBJ):
	objname : str = ""


class ADD(CMD_OBJ):
	add : ADD_OBJ

class REPLACE(CMD_OBJ):
	replace : RULE

class CREATE(CMD_OBJ):
	create : ADD_OBJ

class INSERT(CMD_OBJ):
	insert : RULE

class DELETE(CMD_OBJ):
	delete : ADD_OBJ

class LIST(CMD_OBJ):
	list : LIST_OBJ

class RESET(CMD_OBJ):
	reset : RESET_OBJ

class FLUSH(CMD_OBJ):
	flush : FLUSH_OBJ

class RENAME(CMD_OBJ):
	rename : CHAIN
