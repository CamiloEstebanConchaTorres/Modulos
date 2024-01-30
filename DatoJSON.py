import json
# data = '{"nombre":"MIGUEL","APELLIDO": "Castro"}'
# convertir = json.loads(data)                              // PARA CONVERTIR UN JSON A UN DICCIONARIO
# print(convertir)





# diccionario = {
#     "nombre": "MIGUEL",
#     "APELLIDO": "Castro"
# }
# jsonData = json.dumps(diccionario, indent=4)    // PARA CONVERTIR UN  DICCIONARIO A JSON
# print(jsonData)


convertir = ""
with open("data.json", "r") as f:
    convertir = json.loads(f.read())
    f.close()

with open("data.json", "w") as f:
    convertir["Altura"] = 1.63
    data = json.dumps(convertir, indent=4)
    f.write(data)
    f.close()