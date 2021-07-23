#!/usr/bin/env python3

from pynft.objects.rulesets import *



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


class CMD_ADD(CMD_OBJ):
	add : ADD_OBJ

class CMD_REPLACE(CMD_OBJ):
	replace : RULE

class CMD_CREATE(CMD_OBJ):
	create : ADD_OBJ

class CMD_INSERT(CMD_OBJ):
	insert : RULE

class CMD_DELETE(CMD_OBJ):
	delete : ADD_OBJ

class CMD_LIST(CMD_OBJ):
	list : LIST_OBJ

class CMD_RESET(CMD_OBJ):
	reset : RESET_OBJ

class CMD_FLUSH(CMD_OBJ):
	flush : FLUSH_OBJ

class CMD_RENAME(CMD_OBJ):
	rename : CHAIN
