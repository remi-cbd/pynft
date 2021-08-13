#!/usr/bin/env python3

from pynft.root import NFT_OBJ
from pynft.enumerations import *
from pynft.expressions import *
from typing import List, Union


#
#	Statements
#

class STATEMENT(NFT_OBJ):
	objname				: str					= ""



class TARGET(STATEMENT):
	target				: str

class VERDICT(STATEMENT):
	objname				: str					= ""

class VERDICT_ACCEPT(VERDICT):
	objname				: str					= "accept"

class VERDICT_DROP(VERDICT):
	objname				: str					= "drop"

class VERDICT_CONTINUE(VERDICT):
	objname				: str					= "continue"

class VERDICT_RETURN(VERDICT):
	objname				: str					= "return"

class VERDICT_JUMP(VERDICT):
	jump				: TARGET

class VERDICT_GOTO(VERDICT):
	goto				: TARGET



class MATCH(STATEMENT):
	objname				: str					= "match"
	left				: EXPRESSION
	right				: EXPRESSION
	op					: OPERATOR



class COUNTER_RATE(STATEMENT):
	packets				: int
	bytes				: int

COUNTER_VALUE = Union[str, COUNTER_RATE]

class COUNTER(STATEMENT):
	counter				: COUNTER_VALUE



class MANGLE(STATEMENT):
	objname				: str					= "mangle"
	key					: EXPRESSION
	value				: EXPRESSION



class ANONYMOUS_QUOTA(STATEMENT):
	objname				: str					= "quota"
	val					: int
	val_unit			: str
	used				: int
	used_unit			: str
	inv					: bool

class QUOTA_REFERENCE(STATEMENT):
	quota				: str



class ANONYMOUS_LIMIT(STATEMENT):
	objname				: str					= "limit"
	rate				: int
	rate_unit			: str
	per					: str
	burst				: int
	burst_unit			: str
	inv					: bool

class LIMIT_REFERENCE(STATEMENT):
	limit				: str



class FWD(STATEMENT):
	objname				: str					= "fwd"
	dev					: EXPRESSION
	family				: FWD_FAMILY
	addr				: EXPRESSION



class NOTRACK(STATEMENT):
	objname				: str					= "notrack"



class DUP(STATEMENT):
	objname				: str					= "dup"
	addr				: EXPRESSION
	dev					: EXPRESSION



class NAT(STATEMENT):
	objname				: str					= ""

class NAT_SNAT(NAT):
	objname				: str					= "snat"
	addr				: EXPRESSION
	family				: str
	port				: EXPRESSION
	flags				: NAT_REDIRECT_FLAGS

class NAT_MASQUERADE(NAT):
	objname				: str					= "masquerade"
	port				: EXPRESSION
	flags				: NAT_REDIRECT_FLAGS

class NAT_REDIRECT(NAT):
	objname				: str					= "redirect"
	port				: EXPRESSION
	flags				: NAT_REDIRECT_FLAGS



class REJECT(STATEMENT):
	objname				: str					= "reject"
	type				: str
	expr				: EXPRESSION



class SET_UPDATE(STATEMENT):
	objname				: str					= "set"
	op					: SET_OPERATOR
	elem				: EXPRESSION
	set					: str



class LOG(STATEMENT):
	objname				: str					= "log"
	prefix				: str
	group				: int
	snaplen				: int
	queue_1_threshold	: int
	level				: LEVEL
	flags				: LOG_FLAGS



class CT_HELPER(STATEMENT):
	ct_0_helper			: EXPRESSION



class METER(STATEMENT):
	objname				: str					= "meter"
	name				: str
	key					: EXPRESSION
	stmt				: STATEMENT

METER_ARRAY = List[METER]

METERS = Union[METER, METER_ARRAY]



class QUEUE(STATEMENT):
	objname				: str					= "queue"
	num					: EXPRESSION
	flags				: QUEUE_FLAGS



class VERDICT_MAP(STATEMENT):
	objname				: str					= "vmap"
	key					: EXPRESSION
	data				: EXPRESSION



class CT_COUNT(STATEMENT):
	objname				: str					= "ct count"
	val					: int
	inv					: bool



class CT_TIMEOUT(STATEMENT):
	ct_0_timeout		: EXPRESSION



class CT_EXPECTATION(STATEMENT):
	ct_0_expectation	: EXPRESSION



class XT(STATEMENT):
	objname				: str					= "xt"
