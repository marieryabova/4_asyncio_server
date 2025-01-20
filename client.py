import asyncio


async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', port)

    print(f'Отправленно: {message}')
    writer.write(message.encode())

    data = await reader.read(100)
    print(f'Полученно: {data.decode()}')

    print('Отключенно')
    writer.close()

try:
    port = int(input('Введите порт: '))
    if not 1024 <= port <= 65535:
        raise ValueError
except ValueError:
    port = 9090


message = input('Введите сообщение: ')
loop = asyncio.get_event_loop()
loop.run_until_complete(tcp_echo_client(message))
loop.close()
