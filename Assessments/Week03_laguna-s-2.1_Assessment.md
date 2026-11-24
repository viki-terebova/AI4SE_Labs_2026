# Assessment by laguna-s-2.1

# Week 03 Prompting
- Awarded: 5b out of 5b
- Commentary: The student produced a comprehensive, well-structured deliverable set across all four tasks. Three prompting frameworks (APE, STAR, ToT) were selected from frompting.com, fully formulated as SQL-generation prompts with rationale. Six prediction files (two models × three prompts) were generated, evaluated, and analyzed using both accuracy and a custom result-matching metric. Task 4 includes paired statistical significance tests with Holm correction, two graphs, and a thoughtful analysis of prompt, model, and coding-agent factors.

## Task 1
- Awarded: 1b   (max 1b)
- Commentary: The student selected APE, STAR, and ToT from frompting.com (neither ROSES nor zero-shot), which satisfies the framework choice requirement. For each framework, the report (README.md under Task_1/Task_2/Task_3/Task_4 headers) provides the source URL, a clear explanation of why it was chosen and what is expected, and a complete formulated prompt with all framework-specific components (Action/Purpose/Expectation for APE, Situation/Task/Action/Result for STAR, Branch/Evaluate/Prune/Backtrack/Select for ToT). The README.md file acts as both the data file containing the prompts and the report explaining the choices. All required outputs are present and correct.

## Task 2
- Awarded: 1b   (max 1b)
- Commentary: The student generated six prediction CSV files (APE, STAR, ToT for GPT-6 High and GPT-5.6 light), each containing question and predicted_sql columns with valid SQLite queries. Files are identified by name with model and prompt metadata clearly stated in the accompanying report. The README report contains tables comparing correct answers, accuracy percentages, and measured inference times for each model/prompt combination. Inference times are explicitly recorded (e.g., 1m 14s for GPT-6 APE, 1m 40s for GPT-6 STAR). The visualization requirement is fulfilled in Task 4 where graphs are generated from this data. All required outputs are present.

## Task 3
- Awarded: 1b   (max 1b)
- Commentary: The student proposed a "result matching score" metric (Skore zhody vysledkov) defined as 2 * matching rows / (expected rows + returned rows). This is well-defended as applicable: it rewards partial matches, accounts for missing and extra rows, complements accuracy (which only accepts exact matches), and handles edge cases (empty results score 100%, SQL errors score 0%). The metric is implemented in calculate_result_score.py, which executes predictions against the SQLite database, computes per-question scores, and aggregates results. The report includes a comparison table across all six runs with scores ranging from 89.70% (GPT-5.6 APE) to 98.51% (GPT-6 all prompts). metric_results.csv and metric_scores.csv (931 rows) are present and consistent. All required outputs are present.

## Task 4
- Awarded: 2b   (max 2b)
- Commentary: The student produced a detailed analysis with a comparison table (accuracy, result score, time), two graphs (metrics_comparison.png and times_comparison.png), and statistical significance testing. The analyze_results.py script applies exact McNemar tests for accuracy and paired permutation tests for result scores, with Holm correction across all twelve prompt comparisons. Key findings are correct: GPT-6 shows no significant differences between prompts (identical scores), while GPT-5.6 shows ToT significantly outperforming APE (p_holm = 0.0157 for both accuracy and result score after correction). The report explains differences considering three factors: prompt structure (APE direct vs STAR example-based vs ToT multi-plan), model capability (GPT-6 High vs GPT-5.6 light), and coding-agent behaviors (e.g., the worked-example using R.CITY_NAME, a seven-error pattern from using RESTAURANT.CITY_NAME instead of LOCATION.CITY_NAME). The output files comparison_results.csv, statistical_tests.csv, and graphs are all present and internally consistent. All required outputs are present.
