from persona import Persona

juan = Persona("juan","castellanos",15)
juan.mostrarpersona()

luisa= Persona("luisa","castro",18)
luisa.mostrarpersona()

luisa.apellidos = "perez"
luisa.mostrarpersona()

juan=luisa

juan.mostrarpersona()       