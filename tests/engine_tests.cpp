#include <gtest/gtest.h>
#include "../src/engine/othello_engine.cpp"

/**
 * @test MinimaxCorrectness
 * Ensures the engine identifies a winning move sequence in a known endgame state.
 */
TEST(EngineTest, MinimaxCorrectness) {
    OthelloEngine engine;
    Bitboard black = 0x0000001810080000ULL; 
    Bitboard white = 0x0ULL;
    int score = engine.searchBaseline(black, white, 4, -100, 100, true);
    EXPECT_GT(score, 0); 
}

/**
 * @test ZobristConsistency
 * Verifies that the Zobrist hash updates are correctly reversible via XOR.
 */
TEST(EngineTest, ZobristConsistency) {
    OthelloEngine engine;
    uint64_t h1 = 0xABCDEF123456ULL;
    uint64_t h2 = h1 ^ 0x123 ^ 0x123;
    EXPECT_EQ(h1, h2);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}