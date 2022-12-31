def tower_of_hanoi(n , source, dest, aux):
    if n == 1:
        print(f"Move disk 1 from {source} to {dest}")
        return
    tower_of_hanoi(n - 1, source, aux, dest)
    print(f"Move disk {n} from {source} to {dest}")
    tower_of_hanoi(n - 1, aux, dest, source)
