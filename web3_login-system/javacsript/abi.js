let abi = [
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_uesrName",
				"type": "string"
			}
		],
		"name": "checkAccont",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_accountId",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "_userName",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_passWord",
				"type": "uint256"
			}
		],
		"name": "getAccount",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_accountId",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "_userName",
				"type": "string"
			}
		],
		"name": "getPassword",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_accountId",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "_userName",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_passWord",
				"type": "uint256"
			}
		],
		"name": "setAccount",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]