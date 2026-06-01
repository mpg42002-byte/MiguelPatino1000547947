# Calculadora Simple — Actividad Guía 5

## Descripción
Proyecto de calculadora en Python con flujo CI/CD configurado
mediante GitHub Actions para la asignatura Aplicaciones y Servicios Web.

## Datos del Estudiante
- **Nombre:** Miguel Angel Patino Garcia
- **Documento:** 1000547947
- **Materia:** Aplicaciones y servicios web — Código 580202009
- **Institución:** ITM — Institución Universitaria

## Funciones disponibles
| Función | Descripción | Ejemplo |
|---|---|---|
| `sumar(a, b)` | Suma dos números | `sumar(3, 4)` → 7 |
| `restar(a, b)` | Resta dos números | `restar(10, 3)` → 7 |
| `multiplicar(a, b)` | Multiplica dos números | `multiplicar(2, 5)` → 10 |
| `dividir(a, b)` | Divide dos números | `dividir(10, 2)` → 5 |

## Cómo ejecutar
```bash
python calculadora.py
```

## Cómo ejecutar las pruebas
```bash
python -m pytest test_calculadora.py -v
```

## Flujo CI/CD
Cada commit activa automáticamente GitHub Actions, que:
1. Configura Python 3.13
2. Instala dependencias
3. Ejecuta el programa principal
4. Ejecuta todas las pruebas automáticas