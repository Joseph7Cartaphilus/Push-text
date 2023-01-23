import win10toast


def message():
    toast = win10toast.ToastNotifier()
    toast.show_toast(title='Title', msg='Message', duration=10)


def main():
    message()


if __name__ == '__main__':
    main()
