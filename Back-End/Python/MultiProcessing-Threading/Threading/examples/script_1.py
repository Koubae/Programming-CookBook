import threading


def main():
    thread_func = lambda arg_1, arg_2, key_arg_1=None, key_arg_2=None: print(f'{arg_1}  | {arg_2}  | {key_arg_1}  | {key_arg_2} ')
    thread_one = threading.Thread(target=thread_func, args=(1, 2), kwargs={"key_arg_1": "Value1", "key_arg_2": "Value2"})
    thread_one.start()
    thread_one.join()


if __name__ == '__main__':
    main()
