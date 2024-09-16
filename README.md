Este programa necesita **Pillow** para funcionar correctamente. Para instalarlo, ejecuta el siguiente comando:

```bash
pip install Pillow
```

Para compilar correctamente el programa para Windows teniendo pyinstaller, se debe ingresar:

```bash
pyinstaller --onefile -w --add-data "src/uiMain/imagenes;imagenes" .\src\uiMain\gui.py
```