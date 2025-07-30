## 1. Introduction
We construct the LeetCode Contest benchmark to to further validate the model's capability in real-world programming problems.
[LeetCode](https://leetcode.com/) presents competition-level problems, offering significant challenges that test the model's problem understanding and code generation skills. We collected the latest problems from LeetCode Contests to prevent the appearance of both the problems or their solutions in our pre-training data. A total of `180` problems were collected from July 2023 to January 2024. For each problem, we collected `100` test cases. The data format is the same as human-eval. For more details, please refer to [leetcode_contest_data](./data/20240121-Jul.jsonl).

## 2. Evaluation
Please follow the following two steps to evaluate the model's performance on our LeetCode Contest benchmark:

1. Run `vllm_inference.py` to get generation results.
```bash
cd Evaluation/LeetCode

# Set the model or path here
MODEL="/path/to/model"

python vllm_inference.py --model_name_or_path $MODEL --saved_path output/20240121-Jul.d2c-7b-instruct.jsonl
```

If you want to evaluate the model with COT, please add `--cot` to the command:
```bash
python vllm_inference.py --model_name_or_path $MODEL --saved_path output/20240121-Jul.d2c-7b-instruct.jsonl --cot
```

2. Run `evaluate_leetcode.py` to get evaluation results.
```bash
python evaluate_leetcode.py --generation_path output/20240121-Jul.d2c-7b-instruct.jsonl --result_path output/20240121-Jul.d2c-7b-instruct.result.jsonl
```

