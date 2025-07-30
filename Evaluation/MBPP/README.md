## 1. Introduction

We provide a test script to evaluate the performance of the **d2c** model on code generation benchmarks, [**MBPP**](https://huggingface.co/datasets/mbpp), with 3-shot setting.



## 2. Setup

```
pip install accelerate
pip install attrdict
pip install transformers
pip install pytorch
```



## 3. Evaluation

We've created a sample script, **eval.sh**, that demonstrates how to test the **d2c-1.3b-base** model on the MBPP dataset leveraging **8** GPUs.

```bash
MODEL_NAME_OR_PATH="/path/to/model"
DATASET_ROOT="data/"
LANGUAGE="python"
python -m accelerate.commands.launch --config_file test_config.yaml eval_pal.py --logdir ${MODEL_NAME_OR_PATH} --dataroot ${DATASET_ROOT} 
```

