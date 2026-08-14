# Flet Testing

Proyecto base para aprender desarrollo de aplicaciones con **Python + Flet**, utilizando **uv** para gestionar Python, entornos virtuales y dependencias.

El objetivo es mantener un entorno sencillo y reproducible que permita desarrollar aplicaciones visuales para escritorio, web y, más adelante, dispositivos móviles.

## Stack

* **Python 3.14**
* **Flet 0.86.5**
* **uv** — gestión de Python, entornos y dependencias
* **pytest 9.1.1** — testing
* **Ruff 0.16.3** — linting y formateo
* **Git** — control de versiones

## Estructura del proyecto

```text
flet-testing/
├── src/
│   ├── assets/
│   │   ├── images/
│   │   └── sounds/
│   └── main.py
│
├── tests/
│   └── test_main.py
│
├── .python-version
├── pyproject.toml
├── uv.lock
└── README.md
```

El punto de entrada de la aplicación es:

```text
src/main.py
```

---

# Instalación desde cero

## 1. Instalar uv

Es necesario tener `uv` instalado en el sistema.

Puedes comprobarlo con:

```powershell
uv --version
```

`uv` se encargará de gestionar tanto la versión de Python como el entorno virtual y las dependencias del proyecto.

---

## 2. Crear el proyecto

Crear una carpeta para el proyecto:

```powershell
mkdir flet-testing
cd flet-testing
```

Inicializar Git:

```powershell
git init
git branch -M main
```

Inicializar el proyecto con `uv`:

```powershell
uv init --no-package --python 3.14.7 .
```

Usamos `--no-package` porque nuestra aplicación Flet no necesita ser instalada como un paquete Python.

Esto evita generar estructuras adicionales como:

```text
src/flet_testing/__init__.py
```

o configuraciones de packaging como:

```toml
[build-system]
```

Para este proyecto queremos una estructura más sencilla, con un punto de entrada explícito:

```text
src/main.py
```

---

## 3. Fijar la versión de Python

Si fuera necesario, podemos instalar Python mediante `uv`:

```powershell
uv python install 3.14.7
```

Y fijar esa versión para el proyecto:

```powershell
uv python pin 3.14.7
```

Esto genera:

```text
.python-version
```

con:

```text
3.14.7
```

Podemos verificar la versión utilizada por el proyecto con:

```powershell
uv run python --version
```

---

# Dependencias

## 4. Instalar Flet

Añadimos Flet junto con sus herramientas de desarrollo:

```powershell
uv add "flet[all]==0.86.5"
```

Utilizamos:

```text
flet[all]
```

en lugar de únicamente:

```text
flet
```

porque necesitamos también herramientas como el CLI de Flet para ejecutar, diagnosticar y posteriormente compilar la aplicación.

Por ejemplo:

```powershell
uv run flet --version
```

o:

```powershell
uv run flet doctor
```

---

## 5. Instalar dependencias de desarrollo

Añadimos las herramientas que no forman parte de la aplicación final:

```powershell
uv add --dev "flet[test]==0.86.5"
uv add --dev "pytest==9.1.1"
uv add --dev "ruff==0.16.3"
```

Estas dependencias tienen diferentes responsabilidades:

### `flet[test]`

Añade las herramientas necesarias para realizar tests de integración sobre aplicaciones Flet.

### `pytest`

Framework utilizado para ejecutar nuestros tests.

### `ruff`

Se utiliza para:

* detectar problemas en el código;
* aplicar reglas de estilo;
* ordenar y limpiar código;
* formatear automáticamente Python.

---

# Configuración

Nuestro `pyproject.toml` contiene aproximadamente:

```toml
[project]
name = "flet-testing"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.14"

dependencies = [
    "flet[all]==0.86.5",
]

[dependency-groups]
dev = [
    "flet[test]==0.86.5",
    "pytest==9.1.1",
    "ruff==0.16.3",
]

[tool.pytest.ini_options]
asyncio_mode = "auto"
testpaths = ["tests"]
```

## Configuración de pytest

```toml
[tool.pytest.ini_options]
```

permite configurar pytest directamente desde `pyproject.toml`, evitando necesitar un archivo `pytest.ini` separado.

### `testpaths`

```toml
testpaths = ["tests"]
```

indica que pytest debe buscar los tests dentro de:

```text
tests/
```

### `asyncio_mode`

```toml
asyncio_mode = "auto"
```

permite ejecutar de forma automática tests asíncronos.

Esto será especialmente útil cuando empecemos a realizar tests de integración de Flet.

---

# Crear la estructura

Crear las carpetas:

```powershell
mkdir src
mkdir src\assets
mkdir src\assets\images
mkdir src\assets\sounds
mkdir tests
```

Crear el archivo principal:

```powershell
New-Item src\main.py
```

Y opcionalmente el primer archivo de tests:

```powershell
New-Item tests\test_main.py
```

---

# Primera aplicación

Un `src/main.py` mínimo puede ser:

```python
import flet as ft


def main(page: ft.Page) -> None:
    page.title = "Flet Testing"

    page.add(
        ft.Text(
            "Hola Flet! 👋",
            size=32,
        )
    )


ft.run(main)
```

---

# Ejecutar la aplicación

```powershell
uv run flet run src/main.py
```

Flet abrirá la aplicación en modo desarrollo.

Los cambios realizados sobre el código pueden visualizarse rápidamente durante el desarrollo gracias al sistema de recarga de Flet.

---

# Sincronizar el entorno

Para asegurarnos de que el entorno virtual coincide exactamente con las dependencias declaradas en el proyecto:

```powershell
uv sync
```

`uv` utilizará:

```text
pyproject.toml
      ↓
   uv.lock
      ↓
    .venv
```

Si existen paquetes en `.venv` que ya no forman parte del proyecto, `uv sync` puede eliminarlos.

Por tanto, ver mensajes como:

```text
Uninstalled 23 packages
```

no implica necesariamente un error.

Significa que `uv` está limpiando el entorno para que coincida con las dependencias declaradas.

---

# Ejecutar los tests

```powershell
uv run pytest
```

pytest buscará automáticamente los tests dentro de:

```text
tests/
```

---

# Comprobar el código con Ruff

Comprobar posibles problemas:

```powershell
uv run ruff check .
```

Comprobar el formato:

```powershell
uv run ruff format --check .
```

Aplicar automáticamente el formato:

```powershell
uv run ruff format .
```

Corregir automáticamente los problemas que Ruff pueda solucionar:

```powershell
uv run ruff check . --fix
```

Conceptualmente:

```text
Ruff
  │
  ├── ¿Está correctamente escrito?
  └── ¿Hay problemas detectables?

pytest
  │
  └── ¿Se comporta como esperamos?

Code Review
  │
  └── ¿El cambio realmente hace lo que debería?
```

---

# Comprobar Flet

Podemos comprobar que el CLI está instalado correctamente:

```powershell
uv run flet --version
```

Y obtener información completa del entorno con:

```powershell
uv run flet doctor
```

---

# Clonar el proyecto en otro ordenador

Una de las ventajas de utilizar `uv` es que, una vez creado el proyecto, otra persona no necesita instalar manualmente todas las dependencias.

Clonar el repositorio:

```powershell
git clone <repository-url>
cd flet-testing
```

Después:

```powershell
uv sync
```

`uv` utilizará `.python-version`, `pyproject.toml` y `uv.lock` para reconstruir el entorno.

Finalmente:

```powershell
uv run flet run src/main.py
```

---

# Archivos que deben incluirse en Git

Deben versionarse:

```text
.python-version
pyproject.toml
uv.lock
README.md
src/
tests/
```

Especialmente importante es:

```text
uv.lock
```

porque contiene las versiones exactas resueltas de las dependencias y permite que todos los desarrolladores trabajen con el mismo entorno.

El entorno virtual:

```text
.venv/
```

**no debe subirse a Git**.

Cada desarrollador puede recrearlo simplemente ejecutando:

```powershell
uv sync
```

---

# Flujo habitual de desarrollo

Una vez configurado el proyecto, los comandos que utilizaremos habitualmente serán:

```powershell
# Ejecutar aplicación
uv run flet run src/main.py

# Ejecutar tests
uv run pytest

# Revisar código
uv run ruff check .

# Formatear código
uv run ruff format .

# Sincronizar dependencias
uv sync
```

El objetivo es mantener un flujo sencillo:

```text
Código
  ↓
Ruff
  ↓
Tests
  ↓
Pull Request
  ↓
Code Review
  ↓
Merge
```

De esta forma, además de aprender Python y Flet, el proyecto servirá para aprender un flujo moderno de desarrollo asistido por IA en el que **el código generado debe ser entendido, probado y revisado antes de integrarse**.
