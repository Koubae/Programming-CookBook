
class AsyncTask:
    def __await__(self):
        print(f"[TASK] {self.__class__.__name__} working...")
        received = yield 10
        print(f"[TASK] {self.__class__.__name__} received: {received}")
        return received * 2


async def main():
    print("[COROUTINE] Coroutine start")

    task = AsyncTask()
    print("[COROUTINE] Task will start now")

    value_from_task = await task
    print(f"[COROUTINE] Task returned: {value_from_task}")
    return 3


print("[SYNC] Sync script started")
coroutine = main()

intermediate_result = coroutine.send(None)
print(f"[SYNC] Coroutine sent result: {intermediate_result}")

value_to_send = 5
print(f"[SYNC] Will send now {value_to_send} to waiting Coroutine + task")
return_val = -1
try:
    coroutine.send(value_to_send)
except StopIteration as e:
    return_val = e.value

print(f"Coroutine sent result: {return_val}")
