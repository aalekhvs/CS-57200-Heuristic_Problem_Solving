#include <gtest/gtest.h>
#include "../src/engine/othello_engine.cpp"

TEST(EngineTest, MinimaxCorrectness) {
    OthelloEngine engine;
    Bitboard b = 0x0000001810080000ULL; 
    Bitboard w = 0x0ULL;
    // Known win condition check
    int score = engine.minimax_baseline(b, w, 4, -100, 100, true);
    EXPECT_GT(score, 0); 
}

TEST(EngineTest, ZobristInversion) {
    OthelloEngine engine;
    uint64_t h1 = 0x12345678;
    uint64_t h2 = engine.update_hash(h1, 10, true);
    uint64_t h3 = engine.update_hash(h2, 10, true);
    EXPECT_EQ(h1, h3); // XOR property verification [10]
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}