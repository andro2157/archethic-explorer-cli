# Archethic Explorer CLI

A simple cli tool to explore the [Archethic](https://www.archethic.net/) blockchain.

#### Installation :
* Clone the repo : `git clone https://github.com/andro2157/archethic-explorer-cli`
* Install the `requests` library : `pip install requests`
* Start `main.py` : `python main.py`

#### Commands :

<details>
<summary>Balance</summary>

`balance <address> (exact)`
gets the balance of an addresss (UCO & tokens). With the 'exact' option, it won't seek for the last address

Example :
```
> balance 0000CAD48F1A24096BE11BB49AD3A82F6B9E73AF69FDBF8E8929F2F645AE267AC90C
1803.64674858 UCO
1.0 BUZZ (0000F9535C5C80385DEDC96F71FB62C7289D36AA1F934B858CACC8FF0507CBA4F9B8)

> balance 0000BE4EA178A11D62950C248707579E32EFB6F927F7B72472C818E88AEA4D004805
381658493.7855685 UCO

> balance 0000BE4EA178A11D62950C248707579E32EFB6F927F7B72472C818E88AEA4D004805 exact
381666010.9175275 UCO
```
</details>

<details>
<summary>Transaction chain</summary>

`chain <address> (pagingaddress)`
query the network to find a transaction chain

Example :
```
> chain 0000BE4EA178A11D62950C248707579E32EFB6F927F7B72472C818E88AEA4D004805
0000BE4EA178A11D62950C248707579E32EFB6F927F7B72472C818E88AEA4D004805 2022-12-10 13:22:53 transfer

> chain 0000BE4EA178A11D62950C248707579E32EFB6F927F7B72472C818E88AEA4D004805 0000BE4EA178A11D62950C248707579E32EFB6F927F7B72472C818E88AEA4D004805
0000E98002964BC49E604524B1270EA8B4085796DA0EEB7A6FD3D4732758635F8231 2022-12-21 17:08:22 transfer
0000E1E62826D3CAAEFC18B9DAC063FA1F03182EE32305D19BD1DFC06760989CA766 2022-12-21 19:50:02 transfer
000045D4BFAA5909180F952381BA9035C6EE0F9A4537BE4265C624F32BEED0EB9B7B 2022-12-22 11:17:11 transfer
```
</details>

<details>
<summary>Endpoint</summary>

`endpoint <nearest,mainnet,testnet,list,custom> (custom url)`
get current enpoint, select a new endpoint, or list nearest endpoints

Example :
```
> endpoint
Endpoint : https://mainnet.archethic.net

> endpoint nearest
Endpoint : http://46.101.13.189:40000

> endpoint mainnet
Endpoint : https://mainnet.archethic.net

> endpoint testnet
Endpoint : https://testnet.archethic.net

> endpoint list
http://64.227.8.83:40000
http://64.227.136.218:40000
http://139.59.149.234:40000

> endpoint custom http://127.0.0.1:40000
Endpoint : http://127.0.0.1:40000
```
</details>

<details>
<summary>Help</summary>

`help`

Example :
```
> help

        - balance <address> (exact) : gets the balance of an addresss. With the 'exact' option, it won't seek for the last address
        - chain <address> (pagingaddress) : query the network to find a transaction chain
        - endpoint <nearest,mainnet,testnet,list,custom> (custom url)
        - help
        - last <address> : gets the last transaction from an address
        - nodes : list all the nodes registered in the network
        - oracle (timestamp) : gets oracle price
        - query (query) : custom graphql query. Multiline input if no query is provided
        - token <address> (dump) : gets the info of a token. Can dump the NFT content
        - transaction <address> (raw) : gets the info of a transaction
        - transactions (page) : query the network to find all the transactions locally stored
        - type <type> (page) : query the network to list the transaction on the type

```
</details>

<details>
<summary>Last address</summary>

`last <address>`
gets the last transaction from an address

Example :
```
> last 0000BE4EA178A11D62950C248707579E32EFB6F927F7B72472C818E88AEA4D004805
000045D4BFAA5909180F952381BA9035C6EE0F9A4537BE4265C624F32BEED0EB9B7B
```
</details>

<details>
<summary>Nodes</summary>

`nodes`
list all the nodes registered in the network

Example :
```
> nodes
188.166.234.20:30002
        authorizationDate 2022-12-10 01:00:00
        authorized True
        available True
        averageAvailability 0.948
        enrollmentDate 2022-12-08 20:44:30
        firstPublicKey 00017EB361D06C3CB2A0102F664422542E9AB6E88C9867A4EAE082C86274B83AD041
        lastPublicKey 00017EB361D06C3CB2A0102F664422542E9AB6E88C9867A4EAE082C86274B83AD041
        originPublicKey 010104119BDD4DB10EF796F97BB66C4E8AD3923C8BA3EF94230BBC5DEF7D1B8E7DC9E70A42D70C3554BC7ECE06BC130937F1C6B21DC680825D3DCA011A20D33F941FE3
        geoPatch 402
        networkPatch 402
        rewardAddress 00006089F9810A02F22B0CB12DDD2468CAF538AEBE7BB8C168B23FC52769EEC94CFD
95.174.165.23:30002
        authorizationDate None
        authorized False
        available False
        averageAvailability 0.0
        enrollmentDate 2022-12-14 07:48:07
        firstPublicKey 0001501902231B0496CCBC6A18EB8AE4203F5AC5ECF174E4A6F8E3513BE5D992B7AB
        lastPublicKey 0001501902231B0496CCBC6A18EB8AE4203F5AC5ECF174E4A6F8E3513BE5D992B7AB
        originPublicKey 010204BBB51109353DAE37E606F09AD2EB339DA605D2E578D9080E366D84965B3765E123FF7DEDABB67837175AF3A4AFA90AF4ED781B8FFA76B24922FD1D1DC1A8B485
        geoPatch F1F
        networkPatch F1F
        rewardAddress 00008B353DB05ABB6C4CB6E02F791437DD28A301F118C41DB738DC7AA2BE6581F842
[...]
```
</details>

<details>
<summary>Oracle</summary>

`oracle (timestamp)`
gets oracle price

Example :
```
> oracle
Timestamp : 1672171080
Price :
$0.089652
0.084267€

> oracle 1672170010
Timestamp : 1672169980
Price :
$0.089771
0.08434€
```
</details>

<details>
<summary>Query</summary>

`query (query)`
custom graphql query. Multiline input if no query is provided

Example :
```
> query query { networkTransactions(type: "oracle") { address } }
{
    "data": {
        "networkTransactions": [
            {
                "address": "0000D24E4C073FB08AB86E6041AAE23B0D7A76FB1373632FE6E9C4A300168ACACC79"
            },
[...]
            {
                "address": "0000AA46D9D12D57D986166642474BA01F546C000B81052B03A2C0189C5CB528EA9A"
            }
        ]
    }
}

> query
Enter the query :
~ query {
~       transaction(address: "0000BE4EA178A11D62950C248707579E32EFB6F927F7B72472C818E88AEA4D004805") {
~               type,
~               balance { uco },
~               validationStamp {
~                       signature, timestamp
~               }
~       }
~ }
{
    "data": {
        "transaction": {
            "balance": {
                "uco": 38166601091752751
            },
            "type": "transfer",
            "validationStamp": {
                "signature": "F988E4E1F23186383D90A3659868A66421FABA0AF551A66B02DB872BA2C4E9B6AF0397FE92B54ABECCEABAF8D3F1782C7DC28965458AB70BF6CD3C1A97B61507",
                "timestamp": 1670674973
            }
        }
    }
}
```
</details>

<details>
<summary>Token</summary>

`token <address> (dump)`
gets the info of a token. Can dump the NFT content

Example :
```
> token 0000F9535C5C80385DEDC96F71FB62C7289D36AA1F934B858CACC8FF0507CBA4F9B8
BUZZ ($BUZZ) id : EF9AD01E68539D43E28413DD572C66924D0656E2653B5D0470AC4810476F4CC7
Supply : 100000000 (Decimals : 8)
Type : non-fungible
Genesis : 0000FAE37FC2D817C6865945AEE9A41AF95E058C1C8C64C58D15F038372961E7ADF1
Proprties :
        content : {'raw': '/9j/4QI7RXhpZgAATU0AKgAAAAgACAEAAAQAAAABA...
        description : Vers l'infini est au delà ☄️
        name : BUZZ
        type_mime : image/jpeg

> token 0000F9535C5C80385DEDC96F71FB62C7289D36AA1F934B858CACC8FF0507CBA4F9B8 dump
Type : image/jpeg
Filename ? > (Default : BUZZ_0000F9535C5C80385DEDC96F71FB62C7289D36AA1F934B858CACC8FF0507CBA4F9B8.jpeg)
Saved to BUZZ_0000F9535C5C80385DEDC96F71FB62C7289D36AA1F934B858CACC8FF0507CBA4F9B8.jpeg
```
</details>

<details>
<summary>Transaction</summary>

`transaction <address> (raw)`
gets the info of a transaction

Example :
```
> transaction 00006B4686539C65BF91CF6CAB24B9B6AA3CAF5AEE7DBFDBCFA5C5DDD701A1B4654D
Type : transfer
Timestamp : 2022-12-08 20:42:02
Chain Length : 1
Version : 1
Fee : 0.0 UCO

Inputs :

Movements :
        381966011.0 UCO to 0000E0EF0C5A8242D7F743E452E3089B7ACAC43763A3F18C8F5DD38D22299B61CE0E
        236067977.0 UCO to 000047C827E93C4F1106906D3F43546EB09176F03DFF15275759D47BF33D9B0D168A
        145898033.0 UCO to 000012023D76D65F4A20E563682522576963E36789897312CB6623FDF7914B60ECEF
        90169943.0 UCO to 00004769C94199BCA872FFAFA7CE912F6DE4DD8B2B1F4A41985CD25F3C4A190C72BB
        55728090.0 UCO to 0000DBE5D04070411325BA8254BC0CE005DF30EBFDFEEFADBC6659FA3D5FA3263DFD
        34441857.0 UCO to 0000BB90E7EC3051BF7BE8D2BF766DA8BED88AFA696D282ACF5FF8479CE787397E16
        21286236.0 UCO to 000050CEEE9CEEB411FA027F1FB9247FE04297FF00358D87DE4B7B8F2A7051DF47F7

Unspent outputs :
        0.0 UCO from 00006B4686539C65BF91CF6CAB24B9B6AA3CAF5AEE7DBFDBCFA5C5DDD701A1B4654D
        
> transaction 00006B4686539C65BF91CF6CAB24B9B6AA3CAF5AEE7DBFDBCFA5C5DDD701A1B4654D raw
{
    "chainLength": 1,
    "data": {
        "content": "",
        "ledger": {
            "token": {
                "transfers": []
            },
            "uco": {
                "transfers": [
                    {
                        "amount": 38196601100000000,
                        "to": "0000E0EF0C5A8242D7F743E452E3089B7ACAC43763A3F18C8F5DD38D22299B61CE0E"
                    },
                    {
                        "amount": 23606797700000000,
                        "to": "000047C827E93C4F1106906D3F43546EB09176F03DFF15275759D47BF33D9B0D168A"
                    },
                    {
                        "amount": 14589803300000000,
                        "to": "000012023D76D65F4A20E563682522576963E36789897312CB6623FDF7914B60ECEF"
                    },
                    {
                        "amount": 9016994300000000,
                        "to": "00004769C94199BCA872FFAFA7CE912F6DE4DD8B2B1F4A41985CD25F3C4A190C72BB"
                    },
                    {
                        "amount": 5572809000000000,
                        "to": "0000DBE5D04070411325BA8254BC0CE005DF30EBFDFEEFADBC6659FA3D5FA3263DFD"
                    },
                    {
                        "amount": 3444185700000000,
                        "to": "0000BB90E7EC3051BF7BE8D2BF766DA8BED88AFA696D282ACF5FF8479CE787397E16"
                    },
                    {
                        "amount": 2128623600000000,
                        "to": "000050CEEE9CEEB411FA027F1FB9247FE04297FF00358D87DE4B7B8F2A7051DF47F7"
                    }
                ]
            }
        },
        "recipients": []
    },
    "inputs": [],
    "type": "transfer",
    "validationStamp": {
        "ledgerOperations": {
            "fee": 0,
            "transactionMovements": [
                {
                    "amount": 38196601100000000,
                    "to": "0000E0EF0C5A8242D7F743E452E3089B7ACAC43763A3F18C8F5DD38D22299B61CE0E",
                    "tokenAddress": null,
                    "tokenId": null,
                    "type": "UCO"
                },
                {
                    "amount": 23606797700000000,
                    "to": "000047C827E93C4F1106906D3F43546EB09176F03DFF15275759D47BF33D9B0D168A",
                    "tokenAddress": null,
                    "tokenId": null,
                    "type": "UCO"
                },
                {
                    "amount": 14589803300000000,
                    "to": "000012023D76D65F4A20E563682522576963E36789897312CB6623FDF7914B60ECEF",
                    "tokenAddress": null,
                    "tokenId": null,
                    "type": "UCO"
                },
                {
                    "amount": 9016994300000000,
                    "to": "00004769C94199BCA872FFAFA7CE912F6DE4DD8B2B1F4A41985CD25F3C4A190C72BB",
                    "tokenAddress": null,
                    "tokenId": null,
                    "type": "UCO"
                },
                {
                    "amount": 5572809000000000,
                    "to": "0000DBE5D04070411325BA8254BC0CE005DF30EBFDFEEFADBC6659FA3D5FA3263DFD",
                    "tokenAddress": null,
                    "tokenId": null,
                    "type": "UCO"
                },
                {
                    "amount": 3444185700000000,
                    "to": "0000BB90E7EC3051BF7BE8D2BF766DA8BED88AFA696D282ACF5FF8479CE787397E16",
                    "tokenAddress": null,
                    "tokenId": null,
                    "type": "UCO"
                },
                {
                    "amount": 2128623600000000,
                    "to": "000050CEEE9CEEB411FA027F1FB9247FE04297FF00358D87DE4B7B8F2A7051DF47F7",
                    "tokenAddress": null,
                    "tokenId": null,
                    "type": "UCO"
                }
            ],
            "unspentOutputs": [
                {
                    "amount": 0,
                    "from": "00006B4686539C65BF91CF6CAB24B9B6AA3CAF5AEE7DBFDBCFA5C5DDD701A1B4654D",
                    "tokenAddress": null,
                    "tokenId": null,
                    "type": "UCO"
                }
            ]
        },
        "timestamp": 1670528522
    },
    "version": 1
}
```
</details>

<details>
<summary>Transactions</summary>

`transactions (page)`
query the network to find all the transactions locally stored

Example :
```
> transactions 1
0000AD77DF8EF48437E40241AD04CEE942BA5C7A87A1F81957E22BB67B83E67FE47F 2022-12-15 04:23:31 keychain_access
00000DFAED30D92A383404A4709F2198764095019E85D7B82FF1C7E563796FCE1C9E 2022-12-13 16:15:38 keychain_access
000073B4B27C618A4E18D2F2C7A5925D72EEDADCDB199BB2A8D3498FF5C66CC5391F 2022-12-17 09:08:22 transfer
0000EAD9808CFE44D3F47A5C2075FE04BC435138304846B183FE29B497310681C411 2022-12-13 01:24:21 keychain
000071F6DB2BF03FD957EA0C388A4F9D7797C9C2B2279844F18634AD6D21263A66B5 2022-12-20 01:23:36 keychain_access
00003AF3CBB9986FF4D0F6F8BF12731A4FE9754BBA4C0DAC1A36A3A9DCD07EE34F77 2022-12-15 12:01:56 keychain_access
0000FCA5383BDD8DE90DCB748C6E3AB1047D25B2C9ACFFE3D2513C160C38304873C0 2022-12-25 21:21:13 keychain_access
0000A7E08ED276D1FA9F740C49C54651028601E9C294ED9A38A4774F77E7056444B4 2022-12-13 21:53:27 keychain_access
0000EEB5FA8AD4AEE88FEA751AEC4763F7A7F69A598E2DDC0E7407F6EAF1660DB0CF 2022-12-10 15:04:16 keychain
0000069047F8090A0CB98EE76EF630A71E76FFB651BDA7476CADF087E95DADD63166 2022-12-14 04:44:28 keychain_access
```
</details>

<details>
<summary>Transaction Type</summary>

`type <type> (page)`
query the network to list the transaction on the type

Example :
```
> type transfer 10
000014A56E42C6A26B4597E6138A1D0D08B6B487614DA3D2071FDB8BD84DCFA6580C 2022-12-10 15:25:41 transfer
0000089605C79EF257ABCF1B46C82062CC68C6DAD2D019018C0ABDCA40DE8D0B4C72 2022-12-10 15:25:47 transfer
00009A488D94443DC7D5CE3741D6A97B2DFD9517C71E40D644684764F20D0375DA47 2022-12-10 15:25:50 transfer
0000D66229C02B54C15DDDF7AC83CA133EF0960734227BDBD2384B22E7A739B71DB4 2022-12-10 15:26:02 transfer
0000431DE2FBDB5C230FFC40CB95AAED3B1AF73D96AE8C11F6655E652E4655D679D2 2022-12-10 15:26:39 transfer
0000C4FDF72E76BBF08EEC744664AA028A4B55445F9563E323C86DF2D75957F12B16 2022-12-10 15:26:52 transfer
00001DC83235DAF80182BAA6944BFC835D4A733532F9E174F08995EFB4CB9427A65C 2022-12-10 15:26:58 transfer
0000CEE339FAF4F53D9849D90B0D8956851C9FDBBAFBFC0C60019ABFEA012CEE1D5E 2022-12-10 15:27:20 transfer
0000AAB66F25A6AC0176AE9A00EA6A1C37D37B5E56C012399B07A552BF06CB9323B0 2022-12-10 15:27:31 transfer
000004D58053103D822615ADD91D15EC9BBCA2AACA733F5E01522136CDA9EA3DB9D9 2022-12-10 15:27:36 transfer

> type token 5
0000C1DCC713E7CD9743DFE98A7701B19A109D4BAA514B9D3A29842098039DCAED51 2022-12-10 16:27:18 token
00009E3007202913A4ED475E9541D22C565CF44857F9E355241E069D5FA635CC19B5 2022-12-10 16:28:28 token
0000CEE3A5E217C5EE897E9E155CD7E9BBACC7A4F62BBE89D8E470743C044535E46C 2022-12-10 16:29:59 token
00001667B390D975DFC71B6B1EC79F1FF630FDC3831901B81A51051A1FEEE5150601 2022-12-10 16:31:09 token
0000F35D8F76A44CB3B929698B0E5CD3DD84AA4085B61E0D421E41CFCFC4DC8AC043 2022-12-10 16:31:13 token
0000F6C53A868713A9EF173C09692EB1ABE487720FAEA6A84FD4556881EAD73D7C3C 2022-12-10 16:32:33 token
0000F23B70C6526FC98DA9309747E715077D04CB4CF712FC86829A8282FBA536536A 2022-12-10 16:33:53 token
00002388FA91EA05FEBFF7572BF78B0E1347F9692767629FE631E2DD9ADE54CB2491 2022-12-10 16:35:26 token
00000B024B8DAC377090DB07914DBC8C67CB31577332B7A364ADC30C8F318012FA87 2022-12-10 16:42:41 token
0000231CEBD195200F042F4B7ADEC766D3390DFB914A116E9E7C6B8449195274E9D0 2022-12-10 16:42:44 token
```
</details>
