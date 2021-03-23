import chess
from chess import Move
import sys
import numpy
board = chess.Board()

def alphabeta(node, depth, a, B, maximizingPlayer, pv):
    if board.is_checkmate():
        return ((1 if maximizingPlayer else -1) * sys.maxsize, pv)
    if board.is_stalemate():
        return (0, pv)
    if depth == 0:
        return (numpy.random.normal(0,1), pv)
    if maximizingPlayer:
        value = sys.maxsize * -1
        for child in list(board.legal_moves):
            board.push(child)
            recur = alphabeta(board, depth - 1, a, B, False, pv)
            if recur[0] > value:
                pv = board.move_stack[0]
            value = max(value, recur[0])
            board.pop()
            a = max(a, value)
            if a >= B:
                break 
        return (value, pv)
    else:
        value = sys.maxsize
        for child in list(board.legal_moves):
            board.push(child)
            recur = alphabeta(board, depth - 1, a, B, True, pv)
            if recur[0] < value:
                pv = board.move_stack
            value = min(value, recur[0])
            board.pop()
            B = min(B, value)
            if B <= a:
                break
        return (value, pv)
print(alphabeta(board, 2, 0, 0, True, []))