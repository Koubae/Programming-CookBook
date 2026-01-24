import asyncio


async def co_a():
    print("A")

async def co_b(i):
    print("B " + str(i))

async def main():
    task_a = asyncio.create_task(co_a())

    repeats = 5

    # for _ in range(repeats):
    #     coroutine_b = co_b(_)
    #     # await coroutine_b
    #
    #     await asyncio.create_task(coroutine_b)

    tasks_co_wrapped = []
    for _ in range(repeats):
        coroutine_b = co_b(_)
        # await coroutine_b
        tasks_co_wrapped.append((_, asyncio.create_task(coroutine_b)))

        # await asyncio.create_task(coroutine_b)

    for i, task in reversed(tasks_co_wrapped):
        # print(i, end="")
        await task

    await task_a


if __name__ == '__main__':
    asyncio.run(main(), debug=True)
