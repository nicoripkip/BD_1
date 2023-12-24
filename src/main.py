import time


def main():
    print("Hej, Smuk Verden")


if "__main__" == __name__:
    start_time = time.time()

    try:
        main()
    except KeyboardInterrupt as e:
        pass
    finally:
        end_time = start_time - time.time()
        print(f"Total time runned: {start_time} seconds")
