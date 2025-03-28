def main():
    return "\n".join(map(lambda x: f"{x // b} {x % b} {x / b}", map(int, input().split())))