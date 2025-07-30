## 1. Introduction

We provide a test script to evaluate the performance of the **d2c** model on code generation benchmarks. We select the widely-used benchmarks: **[HumanEval-Python](https://huggingface.co/datasets/openai_humaneval), [HumanEval-Multilingual](https://huggingface.co/datasets/nuprl/MultiPL-E)**.



## 2. Setup

```
pip install accelerate
pip install attrdict
pip install transformers
pip install pytorch
```


## 3. Evaluation

We've created a sample script, **eval.sh**, that demonstrates how to test the **D2C-1.3b-Base** model on the HumanEval dataset leveraging **8** GPUs. If your use case involves a different model or dataset, simply adjust the script to fit your needs.

Additionally, for various programming languages, the execution path may differ. Please ensure you update the appropriate paths in the **humaneval/execution.py** file accordingly.

```bash
MODEL_NAME_OR_PATH="/path/to/model"
DATASET_ROOT="data/"
LANGUAGE="python"
python -m accelerate.commands.launch --config_file test_config.yaml eval_pal.py --logdir ${MODEL_NAME_OR_PATH} --language ${LANGUAGE} --dataroot ${DATASET_ROOT} 
```

To evaluate the instruction-based model, please follow the script below:
```bash
LANG="python"
OUPUT_DIR="output"
MODEL="d2c-33b-instruct"

CUDA_VISIBLE_DEVICES=0,1 python eval_instruct.py \
    --model "$MODEL" \
    --output_path "$OUPUT_DIR/${LANG}.$MODEL.jsonl" \
    --language $LANG \
    --temp_dir $OUPUT_DIR
```

