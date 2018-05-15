## Python EOS Api Client
This is an unofficial API wrapper by [@furion](https://steemit.com/@furion)

## Installation
```
pip install -U git+https://github.com/guaiguaihw/py-eos-api
```

## Usage
```python
>>> from eosapi import Client
>>> c = Client(nodes=['http://localhost:8888'])

>>> c.get_info()

    {'head_block_id': '0000652e92c1f73e14503383ee18c28901dd301ff5be0b94c77d846d799d5050',
     'head_block_num': 25902,
     'head_block_producer': 'initi',
     'head_block_time': '2017-09-16T04:25:18',
     'last_irreversible_block_num': 25884,
     'participation_rate': '1.00000000000000000',
     'recent_slots': '1111111111111111111111111111111111111111111111111111111111111111'}

>>> c.get_actions('user')

    {
    "actions": [{
      "global_action_seq": 3475,
      "account_action_seq": 0,
      "block_num": 3466,
      "block_time": "2018-05-15T03:17:55.000",
      "action_trace": {
        "receipt": {
          "receiver": "user",
          "act_digest": "14e6fdb4f96b67e96801aa72702b06fdc0d05be857a1010f65e1f9bf2ceae305",
          "global_sequence": 3475,
          "recv_sequence": 1,
          "auth_sequence": [[
              "eosio",
              3472

            ]
          ]
        },
        "act": {
          "account": "eosio.token",
          "name": "transfer",
          "authorization": [{
              "actor": "eosio",
              "permission": "active"
            }
          ],
          "data": {
            "from": "eosio",
            "to": "user",
            "quantity": "20000.0000 EOS",
            "memo": "memo"
          },
          "hex_data": "0000000000ea305500000000007015d600c2eb0b0000000004454f5300000000046d656d6f"
        },
        "elapsed": 4,
        "cpu_usage": 0,
        "console": "",
        "total_cpu_usage": 0,
        "trx_id": "d8ccad0fc0af1594d837612f31a95862a13931bfa14306cfc406a752cbd4dcb7",
        "inline_traces": []
      }
    }
    ],
    "last_irreversible_block": 5558
    }
```

You can also use a lower level `HttpClient` directly:
```python
from eosapi import HttpClient

h = HttpClient(["http://localhost:8888"])

print(h.exec('chain', 'get_block', '{"block_num_or_id": 5}'))
print(h.exec('chain', 'get_block', {"block_num_or_id": 5}))
print(h.exec('chain', 'get_info'))
```

You can also stream raw blocks (polling indefinitely):
```python
from eosapi import Client
c = Client()

for block in c.stream_blocks(start_block=100, mode='head'):
    print(block)
```

### TODO
 - add support for type hints _(Union[NativeType, PythonType])_
 - split api into submodules to avoid potential collisions
 - apigen: load from json spec files once they are finalized

### License
MIT
