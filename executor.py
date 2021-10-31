#!/usr/bin/env python3

import	nftables
import	json
import	jsonschema
from	pynft.commands import CMD_OBJ, NFT_OBJ
from	pynft.exceptions import PyNFTException



#
#	The Executor class wraps CMD_OBJ execution
#	for better user experience
#

class Executor():

	def __init__(self):
		self.nft = nftables.Nftables()
		self.nft.set_json_output(True)

	def execute(self, cmd:CMD_OBJ, cmdName:str="cmdName"):
		baked = ""
		try:
			baked = cmd.bake()
			if (baked == None or isinstance(baked, int)):
				return None
		except PyNFTException as err:
			return self.__format_response(cmdName, (err.rc, err.obj, err.msg))

		cmdStr = "{ \"nftables\" : [ " + baked + " ] }"
		cmdJSON = json.loads(cmdStr)

		try:
			self.nft.json_validate(cmdJSON)
		except jsonschema.exceptions.ValidationError as err:
			print("WARNING: " + cmdName + " => command has invalid syntax")
			print(cmdStr + "\n" + err)
			return None
		
		return self.__format_response(cmdName, self.nft.json_cmd(cmdJSON))

	def __format_response(self, cmdName, retTuple):
		return {
			"cmd" : cmdName,
			"rc" : retTuple[0],
			"output" : retTuple[1],
			"error" : retTuple[2]
		}

	def print_obj(self, cmd:NFT_OBJ):
		res = cmd.bake()
		print(f"printing NFT_OBJ\n---------------------\n{res}\n---------------------\n")

	def print_cmd_output(self, output, indentOutput = 2):
		if (output == None):
			print("Print Command Output => Failed")
			print("output is None")
		else:
			print("Print Command Output => " + output["cmd"])
			print("return code :\t\t{}".format(output["rc"]))
			print("output :\t\t{}".format(json.dumps(output["output"], indent=indentOutput)))
			if (output["rc"] != 0):
				print("error :\t\t\t{}".format(output["error"]))
		print()