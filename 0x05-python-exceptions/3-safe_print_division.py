#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        a = a / b
    except ZeroDivisionError:
        a = None
    finally:
        print("Inside result:", "{}".format(a))
    return a

4
#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

