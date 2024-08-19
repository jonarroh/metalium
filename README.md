# Proyect metalium

## entorno virtual
```
python3 -m venv venv
source venv/bin/activate
```

## Instalación de dependencias
```
pip install -r requirements.txt
```

## obligatorio

para que funcione selenium es necesario tener instalado el driver de chrome
```bash
# actualizar el sistema
sudo apt update
sudo apt upgrade
# descargar el driver
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# instalar el driver
apt-get install -y ./google-chrome-stable_current_amd64.deb
# verificar la instalación
google-chrome --version
```
