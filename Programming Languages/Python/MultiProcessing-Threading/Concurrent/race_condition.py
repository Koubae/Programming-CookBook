import concurrent.futures

class Storage:
    def __init__(self):
        self.data = 0

    def update(self, name):
        print(f'Thread -> {name} updating..current value {self.data}..')
        local_copy = self.data
        local_copy += 1
        time.sleep(1)
        self.data = local_copy
        print(f'Thread -> {name} updated | New value --> {self.data}')

def main():
    storage = Storage()
    number_of_updates = 10
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(1, number_of_updates+1):
            executor.submit(storage.update, index)
    final_value = storage.data
    print(f"Final Value --> {final_value} | Expected Value ---> {number_of_updates}")


if __name__ == '__main__':
    main()