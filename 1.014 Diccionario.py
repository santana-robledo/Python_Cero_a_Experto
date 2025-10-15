mi_diccionario={}
mi_diccionario=dict()

mi_diccionario={
    "nombre":"Armando",
    "edad":35,
    "ciudad":"New York"
}
mi_diccionario["profesion"]="Developer Python"
mi_diccionario["nombre"]="Jose Luis"
del mi_diccionario["profesion"]
print(mi_diccionario)

for k,v in mi_diccionario.items():
    print(f"La clave {k} y el valor {v}")

d={"a":"1"}
d.update({"b":2,"c":3})
item=d.popitem()
print(item)
print(d)

print(mi_diccionario.get("nombre"))
print(mi_diccionario.items())
print(mi_diccionario.keys())