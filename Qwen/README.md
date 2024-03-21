* `finetune.ipynb`: 程序主入口，调用sh脚本文件
* `finetune/.+\.sh$`: lora、qlora等微调脚本
* `finetune/finetune.py`: py微调脚本，解析超参数配置、执行模型加速等

> You should first download models in your checkpoints folder

原始代码仓库：https://github.com/QwenLM/Qwen