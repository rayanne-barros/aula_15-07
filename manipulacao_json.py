import json

json_conta = '{"id": 1, "nome": "Rayanne", "saldo": 2000}'
conta = json.loads(json_conta)

print(conta["id"])
print(conta["nome"])
print(conta["saldo"])
