import asyncio


async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print(f'Полученно {message} from {addr}')

    print(f'Отправленно: {message}')
    writer.write(data)
    await writer.drain()

    print('Клиент отключился')
    writer.close()

try:
    port = int(input('Введите порт: '))
    if not 1024 <= port <= 65535:
        raise ValueError
except ValueError:
    port = 9090

loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, '127.0.0.1', port)
server = loop.run_until_complete(coro)


print(f'Прослушивание порта {port}')
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass


server.close()
loop.run_until_complete(server.wait_closed())
loop.close()