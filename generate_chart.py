# # import matplotlib.pyplot as plt
# # import numpy as np

# # # Data from Table 2 (Depth 8 Mean Nodes) scaled to Millions for readability
# # labels = ['Standard AB\n(Control)', 'AB + TT', 'AB + TT +\nMove Ordering']
# # means = [8.92, 5.61, 0.485] # In millions
# # stds = [0.41, 0.28, 0.0215] # Standard Deviations in millions

# # x = np.arange(len(labels))
# # width = 0.5

# # # Create the plot
# # fig, ax = plt.subplots(figsize=(8, 6))
# # rects = ax.bar(x, means, width, yerr=stds, capsize=8, 
# #                color=['#e63946', '#f4a261', '#2a9d8f'], 
# #                edgecolor='black', alpha=0.9)

# # # Formatting and Labels
# # ax.set_ylabel('Mean Nodes Expanded (Millions)', fontsize=12, fontweight='bold')
# # ax.set_title('Figure 3: Ablation Study - Node Expansion at Depth 8', fontsize=14, fontweight='bold', pad=15)
# # ax.set_xticks(x)
# # ax.set_xticklabels(labels, fontsize=11)
# # ax.grid(axis='y', linestyle='--', alpha=0.7)

# # # Add exact data labels on top of the bars
# # for rect in rects:
# #     height = rect.get_height()
# #     ax.annotate(f'{height:.2f}M',
# #                 xy=(rect.get_x() + rect.get_width() / 2, height),
# #                 xytext=(0, 10),  # 10 points vertical offset to clear error bars
# #                 textcoords="offset points",
# #                 ha='center', va='bottom', fontsize=11, fontweight='bold')

# # # Save the high-resolution image
# # plt.tight_layout()
# # plt.savefig('figure2_ablation_study.png', dpi=300, bbox_inches='tight')
# # print("✅ Success! 'figure2_ablation_study.png' has been saved to your directory.")


# # # import matplotlib.pyplot as plt
# # # import numpy as np

# # # # Data from Table 1: Baseline Proficiency vs. Controls
# # # labels = ['Pure Random\nControl', 'Naive Greedy\nControl']
# # # win_rates = [99.7, 96.4]
# # # mean_margins = [41.2, 34.5]
# # # std_devs = [4.1, 6.3]

# # # # Create a figure with two side-by-side subplots
# # # fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# # # # --- Subplot 1: Win Rates ---
# # # bars1 = ax1.bar(labels, win_rates, width=0.5, color=['#457b9d', '#1d3557'], edgecolor='black', alpha=0.9)
# # # ax1.set_ylabel('Baseline Win Rate (%)', fontsize=12, fontweight='bold')
# # # ax1.set_title('A: Baseline Dominance (Win Rates)', fontsize=14, fontweight='bold', pad=15)
# # # ax1.set_ylim(0, 115) # Extra space for labels
# # # ax1.grid(axis='y', linestyle='--', alpha=0.7)

# # # # Add percentage labels on top of bars
# # # for bar in bars1:
# # #     height = bar.get_height()
# # #     ax1.annotate(f'{height}%',
# # #                  xy=(bar.get_x() + bar.get_width() / 2, height),
# # #                  xytext=(0, 5),  
# # #                  textcoords="offset points",
# # #                  ha='center', va='bottom', fontsize=12, fontweight='bold')

# # # # --- Subplot 2: Mean Disc Margins with Error Bars ---
# # # bars2 = ax2.bar(labels, mean_margins, width=0.5, yerr=std_devs, capsize=8, 
# # #                 color=['#2a9d8f', '#e9c46a'], edgecolor='black', alpha=0.9)
# # # ax2.set_ylabel('Mean Disc Margin (Final Piece Difference)', fontsize=12, fontweight='bold')
# # # ax2.set_title('B: Average Winning Margin & Variance', fontsize=14, fontweight='bold', pad=15)
# # # ax2.set_ylim(0, 60) # Extra space for labels and error bars
# # # ax2.grid(axis='y', linestyle='--', alpha=0.7)

# # # # Add exact margin labels on top of bars
# # # for bar in bars2:
# # #     height = bar.get_height()
# # #     ax2.annotate(f'+{height}',
# # #                  xy=(bar.get_x() + bar.get_width() / 2, height),
# # #                  xytext=(0, 15), # Offset higher to clear the error bars 
# # #                  textcoords="offset points",
# # #                  ha='center', va='bottom', fontsize=12, fontweight='bold')

# # # # Save the high-resolution image
# # # plt.tight_layout()
# # # plt.savefig('figure1_baseline_performance.png', dpi=300, bbox_inches='tight')
# # # print("✅ Success! 'figure1_baseline_performance.png' has been saved.")

# import matplotlib.pyplot as plt
# import numpy as np

# # Data extracted from Table 3: Transposition Table Size Sensitivity
# labels = ['2^16\n(~1 MB)', '2^18\n(~4 MB)', '2^20\n(~16 MB)', '2^22 (Optimum)\n(~64 MB)', '2^24\n(~256 MB)']
# hit_rates = [14.2, 28.5, 51.1, 68.4, 70.2]

# # Calculating error margins from the 95% CI [lower, upper]
# # e.g., 14.2 - 12.8 = 1.4 margin
# ci_margins = [1.4, 1.4, 1.6, 1.2, 1.1] 

# x = np.arange(len(labels))

# # Create the plot
# fig, ax = plt.subplots(figsize=(9, 6))

# # Plot line with error bars
# ax.errorbar(x, hit_rates, yerr=ci_margins, fmt='-o', color='#d62828', 
#             ecolor='#003049', elinewidth=2, capsize=6, capthick=2, 
#             markersize=8, markerfacecolor='#fcbf49', markeredgecolor='#003049', 
#             linewidth=3, label='Mean Cache Hit Rate')

# # Formatting and Labels
# ax.set_ylabel('Mean Cache Hit Rate (%)', fontsize=12, fontweight='bold')
# ax.set_xlabel('Transposition Table Size (Entries & Approx. Memory)', fontsize=12, fontweight='bold', labelpad=10)
# ax.set_title('Figure 4: Transposition Table Memory Sensitivity (Depth 9)', fontsize=14, fontweight='bold', pad=15)
# ax.set_xticks(x)
# ax.set_xticklabels(labels, fontsize=11)
# ax.set_ylim(0, 85) # Provide headroom for labels
# ax.grid(axis='both', linestyle='--', alpha=0.6)

# # Add exact percentage labels slightly offset from the markers
# for i, rate in enumerate(hit_rates):
#     ax.annotate(f'{rate}%',
#                 xy=(x[i], rate),
#                 xytext=(0, 15),  # 15 points vertical offset
#                 textcoords="offset points",
#                 ha='center', va='bottom', fontsize=11, fontweight='bold', color='#003049')

# # Save the high-resolution image
# plt.tight_layout()
# plt.savefig('figure3_memory_sensitivity.png', dpi=300, bbox_inches='tight')
# print("✅ Success! 'figure3_memory_sensitivity.png' has been saved.")

import matplotlib.pyplot as plt
import numpy as np

# Data extracted from Table 4: Final Tournament Benchmark
scenarios = ['Early Game\n(Turn 1)', 'Complex\nMid-Game']

# Execution Times (seconds)
classical_times = [0.0002, 0.0012]
hybrid_times = [0.0000, 0.0000] 

# Heuristic Scores
classical_scores = [0, 3]
hybrid_scores = [0, 0]

x = np.arange(len(scenarios))
width = 0.35

# Create a figure with two side-by-side subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# --- Subplot 1: Execution Time ---
rects1 = ax1.bar(x - width/2, classical_times, width, label='Classical (Depth 6)', color='#2b2d42', edgecolor='black', alpha=0.9)
rects2 = ax1.bar(x + width/2, hybrid_times, width, label='Hybrid Neural (Depth 4)', color='#ef233c', edgecolor='black', alpha=0.9)

ax1.set_ylabel('Mean Execution Time (seconds)', fontsize=12, fontweight='bold')
ax1.set_title('A: Search Execution Latency', fontsize=14, fontweight='bold', pad=15)
ax1.set_xticks(x)
ax1.set_xticklabels(scenarios, fontsize=12)
ax1.legend(loc='upper left')
ax1.set_ylim(0, 0.0015) # Add headroom for labels
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate exact times on bars
def autolabel_time(rects, ax):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.4f}s',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 5),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=11, fontweight='bold')
autolabel_time(rects1, ax1)
autolabel_time(rects2, ax1)

# --- Subplot 2: Heuristic Score ---
rects3 = ax2.bar(x - width/2, classical_scores, width, label='Classical (Depth 6)', color='#2b2d42', edgecolor='black', alpha=0.9)
rects4 = ax2.bar(x + width/2, hybrid_scores, width, label='Hybrid Neural (Depth 4)', color='#ef233c', edgecolor='black', alpha=0.9)

ax2.set_ylabel('Heuristic Utility Score', fontsize=12, fontweight='bold')
ax2.set_title('B: Positional Accuracy (False Positives)', fontsize=14, fontweight='bold', pad=15)
ax2.set_xticks(x)
ax2.set_xticklabels(scenarios, fontsize=12)
ax2.set_ylim(0, 4) # Add headroom for labels
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate exact scores on bars
def autolabel_score(rects, ax):
    for rect in rects:
        height = rect.get_height()
        text = f'+{int(height)}' if height > 0 else '0'
        ax.annotate(text,
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 5),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=12, fontweight='bold')
autolabel_score(rects3, ax2)
autolabel_score(rects4, ax2)

# Save the high-resolution image
plt.tight_layout()
plt.savefig('figure4_latency_vs_accuracy.png', dpi=300, bbox_inches='tight')
print("✅ Success! 'figure4_latency_vs_accuracy.png' has been saved.")