# ABD Clip Sync ![icon](icon.png)

Sincroniza a área de transferência do Android com o Linux

<details>
    <summary>Demonstração</summary>
    [![thumbnail](https://img.youtube.com/vi/AT1T1vVTaRY/0.jpg)](https://www.youtube.com/watch?v=AT1T1vVTaRY)
</details>

## Dependências

### `Linux`

    sudo apt install adb python3 python3-pip

### `Python3`

    pip3 install -r requirements.txt

## Execução

Antes conecte seu android com o seu computador em seguida instale o app em [releases](https://github.com/brunodavi/adb-clip-sync/releases)

    git clone https://github.com/brunodavi/adb-clip-sync.git
    cd ./adb-clip-sync

    # Inicia monitoramento da clipboard
    ./main.py

## Execução por tcpip

Para alternar entre conectado/desconectado execute `toggle_adb_connect.py`

    $ ./toggle_adb_connect.py
    connected to 192.168.43.1:5555
    $ ./toggle_adb_connect.py
    disconnected 192.168.43.1:5555

## Sobre o App

Aplicação desenvolvida no Tasker
[Importar Projeto](https://taskernet.com/shares/?user=AS35m8nXHtAHUb3g429CktIgI9aKlA1%2FEglWKHxy0IyPwx0q7aeQMBH2ekF4AG%2F7FRqn58T5R5q3qrGmIPwa&id=Project%3AADB+Clip+Sync)
