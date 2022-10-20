from typing import List

WIRE_CHARACTERS = {'|', '-'}
INPUT_CHARACTERS = ('A', 'B')
GATE_CHARACTER = 'G'
OUTPUT_CHARACTER = 'X'

def get_board(opname: str) -> str:
    # Read board from file

    with open(f"./circuits/{opname}.txt") as f:
        return f.read()
#print(get_board('and'))

def gridify_board(board: str) -> List[List[str]]:
    # Return 2D char array representation of board

    return list(list(line) for line in board.split('\n'))

#print(gridify_board(get_board('and')))

def evaluate_function(board: str, *inputs: bool) -> bool:
    def evaluate_nand(*inputs):
        if inputs[0] == True and inputs[1] == True:
            return False
        else:
            return True
    if board == get_board('and'):
        nand = evaluate_nand(inputs[0],inputs[1])
        nand2 = evaluate_nand(nand,nand)
        return nand2
    if board == get_board('nand'):
        if inputs[0] == True and inputs[1] == True:
            return False
        else:
            return True
    if board == get_board('nor'):
        nand1 = evaluate_nand(inputs[0],inputs[0])
        nand2 = evaluate_nand(inputs[1],inputs[1])
        nand3 = evaluate_nand(nand1,nand2)
        nand4 = evaluate_nand(nand3,nand3)
        return nand4
    if board == get_board('not'):
        nand = evaluate_nand(inputs[0],inputs[0])
        return nand
    if board == get_board('or'):
        nand1 = evaluate_nand(inputs[0],inputs[0])
        nand2 = evaluate_nand(inputs[1],inputs[1])
        nand3 = evaluate_nand(nand1,nand2)
        return nand3
    if board == get_board('xor'):
        nand1 = evaluate_nand(inputs[0],inputs[1])
        nand2 = evaluate_nand(inputs[0],nand1)
        nand3 = evaluate_nand(nand1,inputs[1])
        nand4 = evaluate_nand(nand2,nand3)
        return nand4




    # Given a board string, evaluate the boolean function with the
    # given inputs

    raise NotImplementedError()