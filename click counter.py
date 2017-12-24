class Counter:
    def __init__(self):
        self.count = 0

    def reset(self):
        self.count = 0
        return self.count

    def push(self):
        self.count += 1
        return self.count


clicker = Counter()
action = input('Please enter your action: reset? push? exit? \n')
while True:
    if action == 'reset':
        print(clicker.reset())
        action = input('Please enter your action: reset? push? exit? \n')
    elif action == 'push':
        print(clicker.push())
        action = input('Please enter your action: reset? push? exit? \n')
    elif action == 'exit':
        break
    else:
        print('Please enter valid response.')
        action = input('Please enter your action: reset? push? exit? \n')
