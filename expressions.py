#!/usr/bin/env python3

from typing import List, Union

from pynft.root import NFT_OBJ
from pynft.fixed_size_array import fixedSizeArray
from pynft.enumerations import BASE, CT_DIRECTION, CT_FAMILY, FIB_FLAGS, FIB_RESULT, META_KEY, NG_MODE, OSF_KEY, OSF_TTL, RT_FAMILY, RT_KEY, SOCKET_KEY
from pynft.statements import VERDICT



#
#	Expressions
#

class EXPRESSION_OBJ(NFT_OBJ):
	objname : str = ""

EXPRESSION = Union[str, int, bool, EXPRESSION_OBJ]
EXPRESSION_ARRAY = List[EXPRESSION]
EXPRESSIONS = Union[EXPRESSION, EXPRESSION_ARRAY]



#	TOOL +
#	TOOL
class two_expression_array(fixedSizeArray):
	def __init__(self, first_ex:EXPRESSION_OBJ, second_ex:EXPRESSION_OBJ):
		super.__init__(2)
		self.insert(0, first_ex)
		self.insert(1, second_ex)
#	TOOL
#	TOOL -



LIST = List[EXPRESSION_OBJ]

class CONCAT(EXPRESSION_OBJ):
	concat		: LIST

class SET(EXPRESSION_OBJ):
	set			: EXPRESSIONS

class MAP(EXPRESSION_OBJ):
	objname		: str					= "map"
	key			: EXPRESSION
	data		: EXPRESSION

class PREFIX(EXPRESSION_OBJ):
	objname		: str					= "prefix"
	addr		: EXPRESSION
	len			: int

class RANGE(EXPRESSION_OBJ):
	range		: two_expression_array

class RAW_PAYLOAD(NFT_OBJ):
	base		: BASE
	offset		: int
	len			: int

class REFERENCE_PAYLOAD(NFT_OBJ):
	protocol	: str
	field		: str

class PAYLOAD(EXPRESSION_OBJ):
	payload		: Union[RAW_PAYLOAD, REFERENCE_PAYLOAD]

class EXTHDR(EXPRESSION_OBJ):
	objname		: str					= "exthdr"
	name		: str
	field		: str
	offset		: int

class TCP_OPTION(EXPRESSION_OBJ):
	objname		: str					= "tcp option"
	name		: str
	field		: str

class META(EXPRESSION_OBJ):
	objname		: str					= "meta"
	key			: META_KEY

class RT(EXPRESSION_OBJ):
	key			: RT_KEY
	family		: RT_FAMILY

class CT(EXPRESSION_OBJ):
	key			: str
	family		: CT_FAMILY
	dir			: Union[None, CT_DIRECTION]

class NUMGEN(EXPRESSION_OBJ):
	objname		: str					= "numgen"
	mode		: NG_MODE
	mod			: int
	offset		: int

class HASH(EXPRESSION_OBJ):
	objname		: str					= ""

class JHASH(HASH):
	objname		: str					= "jhash"
	mod			: int
	offset		: int
	expr		: EXPRESSION
	seed		: int

class SYMHASH(HASH):
	objname		: str					= "symhash"
	mod			: int
	offset		: int

class FIB(EXPRESSION_OBJ):
	objname		: str					= "fib"
	result		: FIB_RESULT
	flags		: FIB_FLAGS

# class BINARY_OPERATION(NFT_OBJ):
# 	objname		: str					= ""

class ELEM(EXPRESSION_OBJ):
	objname		: str					= "elem"
	val			: EXPRESSION
	timeout		: int
	expires		: int
	comment		: str

class SOCKET(EXPRESSION_OBJ):
	objname		: str					= "socket"
	key			: SOCKET_KEY

class OSF(EXPRESSION_OBJ):
	objname		: str					= "osf"
	key			: OSF_KEY
	ttl			: OSF_TTL


EXPRESSION = Union[str, int, bool, LIST, CONCAT, SET, MAP, PREFIX, RANGE, PAYLOAD, EXTHDR, TCP_OPTION, META, RT, CT, NUMGEN, HASH, FIB, VERDICT, ELEM, SOCKET, OSF]