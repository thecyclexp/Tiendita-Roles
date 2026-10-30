import time

datos = {
  "usuarios" : {
    "jonathan": {
      "rol" : "dueño",
      "gender": "male",
      "password": 55235
    },
    "yuki": {
      "rol": "gerente",
      "gender": "female",
      "password": 27467
    },
    "mindy": {
      "rol": "empleado",
      "gender": "female",
      "password": 97051
    }
  },
  "rolPermission": {
    "owner":{
      "verEmpleados": True,
      "verIngresos/Costos": True,
      "verProvedores": True,
      "cancelarMovimientos":True,
      "verHistoral_Movimientos":True,
      "contratar/despedir":True,
      "pedirAyuda":False
    },
    "manager": {
      "verEmpleados":True,
      "verIngresos/Costos":True,
      "verProvedores":True,
      "cancelarMovimientos":True,
      "verHistoral_Movimientos":True,
      "contratar/despedir":True,
      "pedirAyuda": False
    },
    "empleado": {
      "verEmpleados":False,
      "verIngresos/Costos":False,
      "verProvedores":False,
      "cancelarMovimientos":False,
      "verHistoral_Movimientos":True,
      "contratar/despedir":False,
      "cobrar": True,
      "pedirAyuda": True
    }
  },
  "provedores" : {
    "pepsico" : {
      "refrescos": ["7UP","mirinda","manzanita","pepsi"],
      "bebidas": ["gatorade","mountain","lipton"],
      "frituras": ["sabritas","doritos","cheetos","ruffles","tostitos","fritos","rancheritos","churrumais","paquetaxos","crujitos","sabritones","mafer","karate"]
    },
    "cocaCola": {
      "refrescos": ["cocaCola","fanta","sprite","fresca","sidral"],
      "bebidas": ["ciel","powerade","monster","fuzeTea","topoChico","santaClara","vitaminWater","flashLyte"],
      "jugos": ["delValle","adeS"]
    },
    "leche": {
      "marcas": ["selloRojo","lala","alpura"]
    },
    "tortillas": {
      "maiz": ["timo","maseca","tortiricas","mision"],
      "harina": ["mission","tiaRosa","exquisitas","tortiricas"]
    },
    "licores":{
      "cervezas": ["corona","victoria","indio","bohemia","tecate"],
      "cocteles": ["bacardi","topoChico","newMix"]
    },
    "azucar": {
      "precio-kilo": 28
    },
    "arroz":{
      "precio-kilo": 30
    },
    "nuez": {
      "precio-100g": 10
    },
    "cacahuate": {
      "precio-salado-100g": 25,
      "precio-cascara-100g": 34,
      "precio-japones-100g": 28
    }
  }
}

print("------------------------------------------------------------------------------------------------------------------------")
time.sleep(2)
print("                                             ====Doña Chole====                                                         ")

time.sleep(1)
print("------------------------------------------------------------------------------------------------------------------------")
print("Iniciando el sistema")
for i in range(3,0,-1):
  time.sleep(1)
  print(f"faltan {i} segundos")

print("------------------------------------------------------------------------------------------------------------------------")
nombre = input("Ingresa tu nombre: ").strip().lower()

if nombre in datos["usuarios"]:
  print("verificando usuario")
  time.sleep(1)
  rol1 = datos["usuarios"][nombre]["rol"]
  print("Usuario encontrado")
  print("------------------------------------------------------------------------------------------------------------------------")
else:
  print("este usuario no existe")
  print("------------------------------------------------------------------------------------------------------------------------")

if rol1 in datos["usuarios"][nombre]["rol"]:
  time.sleep(1)
  print("Rol encontrado")
  print("------------------------------------------------------------------------------------------------------------------------")
else:
  print("rol no compatible")
  print("------------------------------------------------------------------------------------------------------------------------")


password=int(input("Ingrese su contraseña: "))

if password == datos["usuarios"][nombre]["password"]:
  print("verificando")
  time.sleep(1)
  print("Hecho")
  passuser=datos["usuarios"][nombre]["password"]
  print("------------------------------------------------------------------------------------------------------------------------")
else:
  print("acceso denegado")
  print("------------------------------------------------------------------------------------------------------------------------")

if rol1 == "dueño" and password == datos["usuarios"][nombre]["password"]:
  while True:
    print("Binevenido",nombre)
    print("1.-Ver ingresos\n2.- Ver salarios\n3.- Ver empleados\n4.- Ver Provedores\n5.- Cancelar Movimientos\n6.- Contratar/Despedir")
    op = int(input("Eliga una opcion: "))
elif rol1 == "gerente" and password == datos["usuarios"][nombre]["password"]:
  print("MENU GERENTE")
elif rol1 == "empleado" and password == datos["usuarios"][nombre]["password"]:
  print("MENU EMPLEADO")
