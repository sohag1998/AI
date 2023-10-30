# This program is for implement for tower of Hanoi

def move(disk, start, end):
    print(f"Move disk {disk} from {start} to {end}")


def toh(n, start, aux, end):
    if n == 1:
        move(n, start, end)
        return
    else:
        toh(n-1, start, end, aux)
        move(n, start, end)
        toh(n-1, aux, start, end)


disks = int(input("Enter your disk number: "))
toh(disks, "A", "B", "C")
