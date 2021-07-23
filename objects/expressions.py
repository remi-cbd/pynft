#!/usr/bin/env python3

from typing import List, Union
from pynft.objects.root import NFT_OBJ

class EXPRESSION(NFT_OBJ):
	objname : str = "expression"

EXPRESSION_ARRAY = List[EXPRESSION]
EXPRESSIONS = Union[EXPRESSION, EXPRESSION_ARRAY]