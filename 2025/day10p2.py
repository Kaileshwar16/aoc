from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpInteger, PULP_CBC_CMD

def parse_line(line):
    parts = line.strip().split()
    buttons = []
    joltages = []
    
    for part in parts:
        if part.startswith('(') and part.endswith(')'):
            indices = list(map(int, part[1:-1].split(',')))
            buttons.append(indices)
        elif part.startswith('{') and part.endswith('}'):
            joltages = list(map(int, part[1:-1].split(',')))
    
    return buttons, joltages

def solve_machine(buttons, targets):
    n_counters = len(targets)
    n_buttons = len(buttons)
    
    prob = LpProblem("MinimizeButtonPresses", LpMinimize)
    
    presses = [LpVariable(f"press_{i}", lowBound=0, cat=LpInteger) for i in range(n_buttons)]
    
    prob += lpSum(presses)
    
    for counter_idx in range(n_counters):
        prob += lpSum([presses[btn_idx] for btn_idx in range(n_buttons) 
                       if counter_idx in buttons[btn_idx]]) == targets[counter_idx]
    
    prob.solve(PULP_CBC_CMD(msg=0))
    
    if prob.status == 1:
        return int(sum([presses[i].varValue for i in range(n_buttons)]))
    
    return 0

with open('input10.txt', 'r') as f:
    lines = f.readlines()

total = 0
for line in lines:
    if line.strip():
        buttons, joltages = parse_line(line)
        result = solve_machine(buttons, joltages)
        total += result

print(total)
