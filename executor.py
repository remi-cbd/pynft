#!/usr/bin/env python3

import nftables
import json
import jsonschema
from pynft.objects.commands import *



#
#	The NFT_Executor class serves the firewall manager
#	It offers nft initialization and CMD_OBJ execution
#

class NFT_Executor():

	def __init__(self):
		self.nft = nftables.Nftables()
		self.nft.set_json_output(True)

	def execute(self, cmd:CMD_OBJ, cmdName:str):
		cmdStr = cmd.bake()
		try:
			self.nft.json_validate(json.loads(cmdStr))
		except jsonschema.exceptions.ValidationError as err:
			print("WARNING: " + cmdName + " => command has invalid syntax")
			print(cmdStr)
			print(err)
			return None
		return self.__format_response(self.nft.json_cmd(cmdStr), cmdName)

	def __format_response(self, retTuple, cmdName):
		return {
			"cmd" : cmdName,
			"rc" : retTuple[0],
			"output" : retTuple[1],
			"error" : retTuple[2]
		}

	def print_cmd(self, cmd:NFT_OBJ):
		res = cmd.bake()
		print(f"printing command\n---------------------\n{res}\n---------------------\n")

	def print_cmd_output(self, output, indentOutput = 2):
		print("Print Command Output => " + output["cmd"])
		print("return value :\t\t{}".format(output["rc"]))
		print("output :\t\t{}".format(json.dumps(output["output"], indent=indentOutput)))
		if (output["rc"] != 0):
			print("error :\t\t\t{}".format(output["error"]))
		print()