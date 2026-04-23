from persona import Persona

juan = Persona("juan","castellanos",15)
juan.mostrarpersona()

sara= Persona("sara","blonde",18)
sara.mostrarpersona()

sara.apellidos = "perez"
sara.mostrarpersona()

juan=sara

juan.mostrarpersona()       