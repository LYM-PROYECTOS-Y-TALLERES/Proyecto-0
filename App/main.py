entrada_predeterminada = """
|nom x y one k W|
 proc putChips: n andBalloons: m [
 |c b|
 c := n .
 b := m .
 move: 3 .
 turn: #left .
 face: #north .
 pick: k ofType: #balloons .
 move: one toThe: #front .
 move: 1233 inDir: #west .
 jump: nom toThe: #front .
 nop .
 put: c ofType: #chips . put: c ofType: #balloons .]
 proc goNorth [
 while: not: canMove: W inDir: #north do: [ move: 1 inDir: #north . nop . nop . nop .
]
]
 proc goWest [
    if: canPick: 5 ofType: #balloons then: [ move: x inDir: #west . ] else: [nop .]]
  proc gonorth [
     if: canPut: 5 ofType: #balloons then: [ move: x inDir: #west . ] else: [nop .]]
   proc goeast [
      if: canJump: 100000 inDir: #north then: [ move: x inDir: #west . ] else: [nop .]]
    proc gosouth [
       if: canMove: nom toThe: #front then: [ move: x inDir: #west . ] else: [nop .]]
     proc golock [
        if: canJump: k toThe: #front then: [ if: canJump: k toThe: #front then: [ move: x inDir: #west . ] else: [nop .] ] else: [nop .]]
     [
 goto: 3 with: 3 .
 putChips: 2 andBalloons: 1 .
 ]
"""

import parser as p

def ejecutar_lexer_parser(entrada_predeterminada: str):
    opcion = input("¿Quieres usar un archivo (A) o la entrada predeterminada (P)? [A/P]: ").strip().upper()
    
    if opcion == 'A':
        archivo_nombre = input("Ingrese el nombre del archivo: ").strip()
        try:
            with open(archivo_nombre, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
        except FileNotFoundError:
            print("❌ Error: El archivo no se encontró. Asegúrese de ingresar un nombre válido.")
            return
    else:
        contenido = entrada_predeterminada  
    
    resultado = p.lexer_parser(contenido)
    
    if resultado:
        print(resultado)
        print("✅ La cadena ingresada fue aceptada correctamente.")
    else:
        print(resultado)
        print("❌ La cadena ingresada fue rechazada.")

ejecutar_lexer_parser(entrada_predeterminada)

    