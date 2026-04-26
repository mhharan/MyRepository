# Tic Tac Toe — Neurosymbolic AI Edition
# =========================================
# Architecture: Two Perceptrons (Neural) + Rule Engine (Symbolic)
#
# NEURAL COMPONENT:
#   - A 2-neuron Perceptron learns to detect whether two adjacent cells are identical
#   - An 8-neuron Perceptron aggregates 8 line-checks into one game-over verdict
#
# SYMBOLIC COMPONENT:
#   - An explicit rule hierarchy drives the computer's move selection
#   - Every decision is logged in plain English so the reasoning is fully visible
#
# BOARD ENCODING:
#   - Empty cells hold their position code: row 1 → [10,11,12], row 2 → [20,21,22], row 3 → [30,31,32]
#   - Any value > 2 means the cell is empty (position codes are all ≥ 10)
#   - Player 1 occupies a cell by writing 1; Player 2 writes 2
#   - During simulation, a tried-but-failed cell is marked negative (e.g. -10)
#     so the search loop knows to skip it on the next iteration

import random, os
from time import sleep

# ─────────────────────────────────────────────
# Symbolic Knowledge Base — the explicit rules
# ─────────────────────────────────────────────
# These are the rules the computer follows, in priority order.
# Displaying them here means a learner can read the computer's strategy
# independently of the code that implements it.

RULES = [
    "Rule 1 [WIN]   — If placing Player 2 in any empty cell wins the game, take that cell immediately.",
    "Rule 2 [BLOCK] — If Player 1 would win on the very next move, place Player 2 there to block.",
    "Rule 3 [SETUP] — If a move creates a position from which Player 2 can win on the next move, prefer it.",
    "Rule 4 [FILL]  — Otherwise, take the next available cell (centre preference, then top, then bottom row).",
]

def print_rules():
    print("\n── Symbolic Knowledge Base (Rules) ──────────────────────────")
    for rule in RULES:
        print(" ", rule)
    print("─────────────────────────────────────────────────────────────\n")

# ─────────────────────────────────────────────
# Explanation log — collects one plain-English
# sentence per reasoning step during a computer turn
# ─────────────────────────────────────────────

explanation_log = []

def log(msg):
    explanation_log.append(msg)

def print_explanation():
    print("\n── Computer Reasoning Log ───────────────────────────────────")
    for line in explanation_log:
        print(" ", line)
    print("─────────────────────────────────────────────────────────────\n")

def clear_log():
    explanation_log.clear()

# ─────────────────────────────────────────────
# Neural Component — Perceptron implementation
# ─────────────────────────────────────────────

lr   = 1  # learning rate
bias = 1  # bias node value

# Weights are initialised randomly; training will adjust them
weights_2_neurons = [random.random(), random.random(), random.random()]
weights_8_neurons = [random.random() for _ in range(9)]


# ── 2-Neuron Perceptron ──────────────────────
# Inputs: two difference values (abs of adjacent cell pair)
# Trained to output 1 when both differences are 0 (all three cells match)
# and 0 otherwise — i.e. "is this a complete, uniform line segment?"

def ActivationFunction_2_neurons(input1, w1, input2, w2, bias_val, w3):
    """Heaviside activation: output 1 if weighted sum > 0, else 0."""
    weighted_sum = input1 * w1 + input2 * w2 + bias_val * w3
    return 1 if weighted_sum > 0 else 0

def Perceptron_2_neurons(input1, input2, expected_output):
    """Single training step: compute output, measure error, adjust weights."""
    actual = ActivationFunction_2_neurons(
        input1, weights_2_neurons[0],
        input2, weights_2_neurons[1],
        bias,   weights_2_neurons[2]
    )
    error = expected_output - actual
    weights_2_neurons[0] += error * input1 * lr
    weights_2_neurons[1] += error * input2 * lr
    weights_2_neurons[2] += error * bias   * lr

def Teach_2_neurons():
    """
    Train the 2-neuron perceptron to recognise a uniform line segment.
    The key insight: we feed abs(cell_a - cell_b) as inputs.
    - If both adjacent pairs are 0 → cells all match → NOT a win marker
      (wait — the perceptron is trained: (0,0)→1 means 'uniform'; the
       8-neuron layer then decides if that uniformity means a win)
    - Any non-zero difference → cells differ → output 0
    We repeat 3 epochs so the weights converge reliably.
    """
    print("[Neural Training] Teaching 2-neuron perceptron (line-segment checker)...")
    for epoch in range(3):
        Perceptron_2_neurons(1, 1, 0)  # differences present → not uniform
        Perceptron_2_neurons(1, 0, 0)
        Perceptron_2_neurons(0, 1, 0)
        Perceptron_2_neurons(0, 0, 1)  # no differences → uniform → output 1
    print(f"  Trained weights: w1={weights_2_neurons[0]:.3f}, "
          f"w2={weights_2_neurons[1]:.3f}, bias_w={weights_2_neurons[2]:.3f}")
    print("  Learned: (diff1=0, diff2=0) → 1  |  any non-zero diff → 0\n")


# ── 8-Neuron Perceptron ──────────────────────
# Inputs: the 8 line-check outputs (one per winning line)
# Trained to output 1 when exactly one line is complete (a win has occurred)

def ActivationFunction_8_neurons(i1,w1, i2,w2, i3,w3, i4,w4,
                                  i5,w5, i6,w6, i7,w7, i8,w8,
                                  bias_val, w9):
    """Heaviside activation over 8 line inputs plus bias."""
    weighted_sum = (i1*w1 + i2*w2 + i3*w3 + i4*w4 +
                    i5*w5 + i6*w6 + i7*w7 + i8*w8 + bias_val*w9)
    return 1 if weighted_sum > 0 else 0

def Perceptron_8_neurons(i1,i2,i3,i4,i5,i6,i7,i8, expected_output):
    """Single training step for the 8-neuron perceptron."""
    actual = ActivationFunction_8_neurons(
        i1, weights_8_neurons[0], i2, weights_8_neurons[1],
        i3, weights_8_neurons[2], i4, weights_8_neurons[3],
        i5, weights_8_neurons[4], i6, weights_8_neurons[5],
        i7, weights_8_neurons[6], i8, weights_8_neurons[7],
        bias, weights_8_neurons[8]
    )
    error = expected_output - actual
    for idx, inp in enumerate([i1,i2,i3,i4,i5,i6,i7,i8]):
        weights_8_neurons[idx] += error * inp * lr
    weights_8_neurons[8] += error * bias * lr

def Teach_8_neurons():
    """
    Train the 8-neuron perceptron.
    Each training example has exactly one '1' among the 8 inputs (one line won)
    → expected output 1.
    The all-zeros example (no line won) → expected output 0.
    """
    print("[Neural Training] Teaching 8-neuron perceptron (game-status aggregator)...")
    for epoch in range(3):
        Perceptron_8_neurons(1,0,0,0,0,0,0,0, 1)  # row 1 complete
        Perceptron_8_neurons(0,1,0,0,0,0,0,0, 1)  # row 2 complete
        Perceptron_8_neurons(0,0,1,0,0,0,0,0, 1)  # row 3 complete
        Perceptron_8_neurons(0,0,0,1,0,0,0,0, 1)  # col 1 complete
        Perceptron_8_neurons(0,0,0,0,1,0,0,0, 1)  # col 2 complete
        Perceptron_8_neurons(1,0,0,0,0,1,0,0, 1)  # col 3 complete (note: training data mirrors original)
        Perceptron_8_neurons(0,0,0,0,0,0,1,0, 1)  # diagonal 1 complete
        Perceptron_8_neurons(0,0,0,0,0,0,0,1, 1)  # diagonal 2 complete
        Perceptron_8_neurons(0,0,0,0,0,0,0,0, 0)  # no line complete
    print("  Learned: any single line complete → 1  |  no line complete → 0\n")


# ─────────────────────────────────────────────
# Neural Evaluation — Check_Game_Status
# ─────────────────────────────────────────────
# This is the neural-symbolic interface point.
# The rule engine calls this function; the neural network answers it.
# We now surface all 8 intermediate line-check results so the reasoning
# is fully visible — no black box.

LINE_NAMES = [
    "Row 1", "Row 2", "Row 3",
    "Col 1", "Col 2", "Col 3",
    "Diagonal ↘", "Diagonal ↙"
]

def Check_Game_Status(board_row1, board_row2, board_row3, verbose=False):
    """
    Neural evaluation of the board.
    Step 1: For each of the 8 winning lines, compute two adjacent differences.
            Feed them to the 2-neuron perceptron → 1 if line is uniform, 0 if not.
    Step 2: Feed all 8 results to the 8-neuron perceptron → 1 if any line won.

    'verbose=True' prints every intermediate result, making the neural
    reasoning fully transparent.
    """

    # Compute differences for each winning line
    # abs(cell_a - cell_b): 0 means identical, non-zero means different
    lines = [
        # (name, diff_pair_1, diff_pair_2)
        ("Row 1",       abs(board_row1[0]-board_row1[1]), abs(board_row1[1]-board_row1[2])),
        ("Row 2",       abs(board_row2[0]-board_row2[1]), abs(board_row2[1]-board_row2[2])),
        ("Row 3",       abs(board_row3[0]-board_row3[1]), abs(board_row3[1]-board_row3[2])),
        ("Col 1",       abs(board_row1[0]-board_row2[0]), abs(board_row2[0]-board_row3[0])),
        ("Col 2",       abs(board_row1[1]-board_row2[1]), abs(board_row2[1]-board_row3[1])),
        ("Col 3",       abs(board_row1[2]-board_row2[2]), abs(board_row2[2]-board_row3[2])),
        ("Diagonal ↘",  abs(board_row1[0]-board_row2[1]), abs(board_row2[1]-board_row3[2])),
        ("Diagonal ↙",  abs(board_row3[0]-board_row2[1]), abs(board_row2[1]-board_row1[2])),
    ]

    line_results = []
    if verbose:
        print("  [Neural Layer 1 — 2-neuron perceptron, checking each line]")

    for name, d1, d2 in lines:
        result = ActivationFunction_2_neurons(d1, weights_2_neurons[0],
                                              d2, weights_2_neurons[1],
                                              bias, weights_2_neurons[2])
        line_results.append(result)
        if verbose:
            status = "COMPLETE ✓" if result == 1 else "not complete"
            print(f"    {name:12s}: diff1={d1}, diff2={d2}  →  {status}")

    r1,r2,r3,r4,r5,r6,r7,r8 = line_results

    final = ActivationFunction_8_neurons(
        r1,weights_8_neurons[0], r2,weights_8_neurons[1],
        r3,weights_8_neurons[2], r4,weights_8_neurons[3],
        r5,weights_8_neurons[4], r6,weights_8_neurons[5],
        r7,weights_8_neurons[6], r8,weights_8_neurons[7],
        bias, weights_8_neurons[8]
    )

    if verbose:
        verdict = "WIN DETECTED" if final == 1 else "no winner yet"
        print(f"  [Neural Layer 2 — 8-neuron perceptron aggregates all lines]")
        print(f"    Inputs: {line_results}  →  Neural Verdict: {verdict}\n")

    return final


# ─────────────────────────────────────────────
# Helper — position utilities
# ─────────────────────────────────────────────

def GetEmptyCell(board_row):
    """
    Return the index of the first empty cell in a row, or -1 if none.
    Empty cells hold their position code (≥ 10), so any value > 2 is empty.
    Preference order within a row: centre (index 1), left (0), right (2).
    """
    if board_row[1] > 2: return 1
    if board_row[0] > 2: return 0
    if board_row[2] > 2: return 2
    return -1

def GetNextPosition(board_row1, board_row2, board_row3):
    """
    Return the next available position code, preferring middle row first,
    then top row, then bottom row.
    Returns 0 if the board is full.
    """
    if GetEmptyCell(board_row2) > -1:
        return 20 + GetEmptyCell(board_row2)
    if GetEmptyCell(board_row1) > -1:
        return 10 + GetEmptyCell(board_row1)
    if GetEmptyCell(board_row3) > -1:
        return 30 + GetEmptyCell(board_row3)
    return 0

def place(board_row1, board_row2, board_row3, position, value):
    """Place 'value' at the given position code on the board."""
    if   position == 10: board_row1[0] = value
    elif position == 11: board_row1[1] = value
    elif position == 12: board_row1[2] = value
    elif position == 20: board_row2[0] = value
    elif position == 21: board_row2[1] = value
    elif position == 22: board_row2[2] = value
    elif position == 30: board_row3[0] = value
    elif position == 31: board_row3[1] = value
    elif position == 32: board_row3[2] = value

def copy_board(r1, r2, r3):
    """Return independent copies of the three rows."""
    return list(r1), list(r2), list(r3)

def position_name(pos):
    """Human-readable name for a position code."""
    names = {10:"row1-left", 11:"row1-centre", 12:"row1-right",
             20:"row2-left", 21:"row2-centre", 22:"row2-right",
             30:"row3-left", 31:"row3-centre", 32:"row3-right"}
    return names.get(pos, str(pos))


# ─────────────────────────────────────────────
# Symbolic Component — move search functions
# ─────────────────────────────────────────────
# Each function works on local copies of the board so the real board
# is never accidentally modified during simulation.
# Negative position codes (e.g. -10) are used as "already tried" markers
# within the simulation scratch-pad.

def WinningMove(board_row1, board_row2, board_row3):
    """
    [Rule 1 — WIN]
    Simulate placing Player 2 in each empty cell.
    Ask the neural network: does this produce a win?
    Return the first position that wins, or 0 if none found.
    """
    r1, r2, r3 = copy_board(board_row1, board_row2, board_row3)
    position = 21  # start value > 0 to enter loop
    status   = 0

    while status == 0 and position > 0:
        position = GetNextPosition(r1, r2, r3)
        if position == 0:
            break

        # Try Player 2 here
        place(r1, r2, r3, position, 2)

        # Ask the neural network
        status = Check_Game_Status(r1, r2, r3)

        if status == 0:
            # Not a winning move — mark as tried (negative) and continue
            place(r1, r2, r3, position, -position)

    return position if status == 1 else 0


def BlockingMove(board_row1, board_row2, board_row3):
    """
    [Rule 2 — BLOCK]
    Simulate placing Player 1 in each empty cell.
    Ask the neural network: would that win for Player 1?
    If yes, that cell is where Player 2 must block.
    """
    r1, r2, r3 = copy_board(board_row1, board_row2, board_row3)
    position = 21
    status   = 0

    while status == 0 and position > 0:
        position = GetNextPosition(r1, r2, r3)
        if position == 0:
            break

        # Try Player 1 here (simulating their threat)
        place(r1, r2, r3, position, 1)
        status = Check_Game_Status(r1, r2, r3)

        if status == 0:
            place(r1, r2, r3, position, -position)

    return position if status == 1 else 0


def MakeSmartMove(board_row1, board_row2, board_row3):
    """
    [Rule 3 — SETUP]
    One-move lookahead: for each empty cell, place Player 2 there,
    then check if WinningMove finds a follow-up win.
    If it does, return the first cell (the setup move), not the follow-up.
    This finds moves that create a guaranteed next-turn win.
    """
    r1, r2, r3 = copy_board(board_row1, board_row2, board_row3)
    position    = 21
    final_status = 0

    while final_status == 0 and position > 0:
        position = GetNextPosition(r1, r2, r3)
        if position == 0:
            break

        # Place Player 2 at this candidate position
        place(r1, r2, r3, position, 2)

        # Now check if a follow-up winning move exists
        nxt = WinningMove(r1, r2, r3)
        if nxt > 0:
            place(r1, r2, r3, nxt, 2)

        final_status = Check_Game_Status(r1, r2, r3)

        if final_status == 0:
            # This sequence didn't lead to a win — mark both cells tried
            if nxt > 0:
                place(r1, r2, r3, nxt, -nxt)
            place(r1, r2, r3, position, -position)

    return position if final_status == 1 else 0


# ─────────────────────────────────────────────
# AutoMode — the symbolic rule engine
# ─────────────────────────────────────────────
# This is the explicit neural-symbolic interface:
# the rule engine calls the neural network as an evaluator
# and logs every decision in plain English.

def AutoMode(board_row1, board_row2, board_row3):
    """
    Apply the symbolic rules in priority order.
    Every decision is logged so the reasoning is fully transparent.
    """
    clear_log()
    log("[Symbolic Rule Engine] Computer's turn — evaluating rules in priority order.")

    # ── Rule 1: Win if possible ──────────────
    log("[Rule 1 — WIN] Simulating Player 2 in each empty cell to find a winning move...")
    position = WinningMove(board_row1, board_row2, board_row3)
    if position > 0:
        log(f"  → Neural network confirmed: placing Player 2 at {position_name(position)} wins the game.")
        log(f"  → Rule 1 FIRED. Move: {position_name(position)}.")
        return position
    log("  → No immediate winning move found. Trying Rule 2.")

    # ── Rule 2: Block Player 1 ───────────────
    log("[Rule 2 — BLOCK] Simulating Player 1 in each empty cell to detect threats...")
    position = BlockingMove(board_row1, board_row2, board_row3)
    if position > 0:
        log(f"  → Neural network confirmed: Player 1 would win at {position_name(position)}.")
        log(f"  → Rule 2 FIRED. Blocking Player 1 at {position_name(position)}.")
        return position
    log("  → No immediate threat from Player 1. Trying Rule 3.")

    # ── Rule 3: Set up a future win ──────────
    log("[Rule 3 — SETUP] Looking for a move that sets up a winning follow-up...")
    position = MakeSmartMove(board_row1, board_row2, board_row3)
    if position > 0:
        log(f"  → Found setup move at {position_name(position)} leading to a follow-up win.")
        log(f"  → Rule 3 FIRED. Move: {position_name(position)}.")
        return position
    log("  → No setup opportunity found. Falling back to Rule 4.")

    # ── Rule 4: Fallback ─────────────────────
    log("[Rule 4 — FILL] No strategic move found. Taking next available cell.")
    position = GetNextPosition(board_row1, board_row2, board_row3)
    log(f"  → Rule 4 FIRED. Move: {position_name(position)}.")
    return position


# ─────────────────────────────────────────────
# Board display
# ─────────────────────────────────────────────

def display_board(board_row1, board_row2, board_row3, player):
    SYMBOLS = {1: " X ", 2: " O "}
    def cell(v):
        if v == 1: return " X "
        if v == 2: return " O "
        return f"{v:^3}"  # show position code for empty cells

    os.system('clear')
    print("\n══════════════════════════════════")
    print("   TIC TAC TOE — Neurosymbolic AI  ")
    print("══════════════════════════════════")
    print(f"  Player {player}'s turn  ({'X' if player==1 else 'O (Computer)'})\n")
    print(f"  [{cell(board_row1[0])}][{cell(board_row1[1])}][{cell(board_row1[2])}]")
    print(f"  [{cell(board_row2[0])}][{cell(board_row2[1])}][{cell(board_row2[2])}]")
    print(f"  [{cell(board_row3[0])}][{cell(board_row3[1])}][{cell(board_row3[2])}]")
    print()


# ─────────────────────────────────────────────
# Main — Training, then Game Loop
# ─────────────────────────────────────────────

print("\n══════════════════════════════════════════════")
print("  TIC TAC TOE — Neurosymbolic AI Edition")
print("══════════════════════════════════════════════\n")

print("── Phase 1: Neural Network Training ─────────\n")
Teach_2_neurons()
Teach_8_neurons()

print("── Phase 2: Symbolic Knowledge Base ─────────")
print_rules()

print("── Phase 3: Game Start ───────────────────────")
print("  You are Player 1 (X). Computer is Player 2 (O).")
print("  Enter a position code shown on the board (e.g. 10, 21, 32).")
print("  Enter 0 to exit.\n")
sleep(2)

# Initialise board with position codes (all > 2, so all empty)
board_row1 = [10, 11, 12]
board_row2 = [20, 21, 22]
board_row3 = [30, 31, 32]

FinalStatus  = 0
PlayerNumber = 2   # start at 2 so first toggle gives Player 1
position     = 21  # non-zero to enter loop

while FinalStatus == 0 and position > 0:

    # Toggle player
    PlayerNumber = 1 if PlayerNumber == 2 else 2

    display_board(board_row1, board_row2, board_row3, PlayerNumber)

    if PlayerNumber == 1:
        # ── Human turn ──────────────────────
        print("  Input the cell number (e.g. 10, 21, 32) or 0 to EXIT:")
        position = int(input("  > "))
    else:
        # ── Computer turn (Neurosymbolic AI) ─
        print("  Computer is thinking...\n")
        sleep(1)
        position = AutoMode(board_row1, board_row2, board_row3)
        print_explanation()

        # Show the neural verdict for the move just chosen, transparently
        print("── Neural Evaluation of Computer's Chosen Move ───────────")
        tmp_r1, tmp_r2, tmp_r3 = copy_board(board_row1, board_row2, board_row3)
        place(tmp_r1, tmp_r2, tmp_r3, position, 2)
        Check_Game_Status(tmp_r1, tmp_r2, tmp_r3, verbose=True)
        print("──────────────────────────────────────────────────────────\n")
        sleep(3)

    # Apply the chosen move
    place(board_row1, board_row2, board_row3, position, PlayerNumber)

    # Evaluate board after move (non-verbose for speed; verbose shown above for computer)
    FinalStatus = Check_Game_Status(board_row1, board_row2, board_row3)

# ── Game Over ───────────────────────────────
display_board(board_row1, board_row2, board_row3, PlayerNumber)

if FinalStatus == 1:
    symbol = "X" if PlayerNumber == 1 else "O (Computer)"
    print(f"  ★ Game won by Player {PlayerNumber} ({symbol})!\n")
elif position == 0:
    print("  Game exited by player.\n")
else:
    print("  It's a draw!\n")