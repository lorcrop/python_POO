from persona import Persona

juan = Persona("juan","castellanos",15)
juan.mostrarpersona()

vanessa= Persona("vanessa","rodriguez",18)
vanessa.mostrarpersona()

vanessa.apellidos = "perez"
vanessa.mostrarpersona()

juan=vanessa

juan.mostrarpersona()       
