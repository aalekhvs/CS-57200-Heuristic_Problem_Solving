#include <iostream>
#include <vector>
#include <cstdint>
#include <unordered_map>
#include <algorithm>
#include <cstdlib>
#include <functional> // REQUIRED: For Python callback mapping

typedef uint64_t Bitboard;

struct TTEntry {
    int score;
    int depth;
    uint8_t type; 
    int bestMove;
};

class OthelloEngine {
private:
    uint64_t zobristKeys[2][64]; 
    uint64_t sideToMoveKey;
    std::unordered_map<uint64_t, TTEntry> transpositionTable;
    int killerMoves[64][2] = {{0}}; 

public:
    OthelloEngine() {
        initializeZobrist();
    }

    Bitboard generateMoves(Bitboard own, Bitboard opp) {
        Bitboard empty = ~(own | opp);
        Bitboard mask = opp & 0x7E7E7E7E7E7E7E7EULL;
        Bitboard moves = 0;

        auto shift = [](Bitboard b, int dir) -> Bitboard {
            if (dir == 1) return (b << 1) & 0xFEFEFEFEFEFEFEFEULL;
            if (dir == -1) return (b >> 1) & 0x7F7F7F7F7F7F7F7FULL;
            if (dir == 8) return b << 8;
            if (dir == -8) return b >> 8;
            if (dir == 7) return (b << 7) & 0xFEFEFEFEFEFEFEFEULL;
            if (dir == 9) return (b << 9) & 0x7F7F7F7F7F7F7F7FULL;
            if (dir == -7) return (b >> 7) & 0x7F7F7F7F7F7F7F7FULL;
            if (dir == -9) return (b >> 9) & 0xFEFEFEFEFEFEFEFEULL;
            return 0;
        };

        int directions[] = {1, -1, 8, -8, 7, 9, -7, -9}; 
        for (int d : directions) {
            Bitboard candidates = shift(own, d) & opp;
            for (int i = 0; i < 5; ++i) candidates |= shift(candidates, d) & opp;
            moves |= shift(candidates, d) & empty;
        }
        return moves;
    }

    int searchBaseline(Bitboard b, Bitboard w, int depth, int alpha, int beta, bool isBlack) {
        if (depth == 0 || isTerminal(b, w)) return staticEval(b, w);

        Bitboard moves = generateMoves(isBlack ? b : w, isBlack ? w : b);
        if (moves == 0) return searchBaseline(b, w, depth - 1, alpha, beta, !isBlack);

        int best = isBlack ? -100000 : 100000;
        for (int m : getIndices(moves)) {
            Bitboard nb = b, nw = w;
            applyMove(nb, nw, m, isBlack);
            int score = searchBaseline(nb, nw, depth - 1, alpha, beta, !isBlack);
            if (isBlack) {
                best = std::max(best, score);
                alpha = std::max(alpha, best);
            } else {
                best = std::min(best, score);
                beta = std::min(beta, best);
            }
            if (beta <= alpha) break;
        }
        return best;
    }

    // FINAL UPDATE: Accepts nnEval python callback
    int searchEnhanced(Bitboard b, Bitboard w, int depth, int alpha, int beta, bool isBlack, int ply, uint64_t hash, std::function<int(Bitboard, Bitboard)> nnEval = nullptr) {
        if (transpositionTable.count(hash) && transpositionTable[hash].depth >= depth) {
            return transpositionTable[hash].score;
        }

        if (depth == 0 || isTerminal(b, w)) {
            // SELECTIVE EVALUATION: Query PyTorch if callback exists, else use fast static
            if (nnEval != nullptr) {
                return nnEval(b, w);
            }
            return staticEval(b, w);
        }

        Bitboard movesBB = generateMoves(isBlack ? b : w, isBlack ? w : b);
        // Handle Pass Turn
        if (movesBB == 0) {
            uint64_t nextHash = hash ^ sideToMoveKey;
            return -searchEnhanced(b, w, depth - 1, -beta, -alpha, !isBlack, ply + 1, nextHash, nnEval);
        }

        std::vector<int> moves = getOrderedMoves(b, w, isBlack, ply);
        int bestMove = -1;
        int bestScore = -100000;

        for (int m : moves) {
            Bitboard nb = b, nw = w;
            applyMove(nb, nw, m, isBlack);
            
            uint64_t nextHash = hash ^ zobristKeys[isBlack ? 0 : 1][m] ^ sideToMoveKey; 
            int score = -searchEnhanced(nb, nw, depth - 1, -beta, -alpha, !isBlack, ply + 1, nextHash, nnEval);
            
            if (score > bestScore) {
                bestScore = score;
                bestMove = m;
            }
            alpha = std::max(alpha, bestScore);
            if (alpha >= beta) {
                killerMoves[ply][1] = killerMoves[ply][0]; 
                killerMoves[ply][0] = m;
                break;
            }
        }
        transpositionTable[hash] = {bestScore, depth, 0, bestMove};
        return bestScore;
    }

private:
    void initializeZobrist() {
        for(int i = 0; i < 64; ++i) {
            zobristKeys[0][i] = ((uint64_t)rand() << 32) | rand();
            zobristKeys[1][i] = ((uint64_t)rand() << 32) | rand();
        }
        sideToMoveKey = ((uint64_t)rand() << 32) | rand();
    }

    int staticEval(Bitboard b, Bitboard w) {
        return __builtin_popcountll(b) - __builtin_popcountll(w);
    }

    bool isTerminal(Bitboard b, Bitboard w) {
        return generateMoves(b, w) == 0 && generateMoves(w, b) == 0;
    }

    std::vector<int> getIndices(Bitboard b) {
        std::vector<int> indices;
        while(b) {
            indices.push_back(__builtin_ctzll(b));
            b &= (b - 1);
        }
        return indices;
    }

    std::vector<int> getOrderedMoves(Bitboard b, Bitboard w, bool isBlack, int ply) {
        return getIndices(generateMoves(isBlack ? b : w, isBlack ? w : b));
    }

    void applyMove(Bitboard& b, Bitboard& w, int pos, bool isBlack) {
        Bitboard m = 1ULL << pos;
        if (isBlack) b |= m; else w |= m;
    }
};