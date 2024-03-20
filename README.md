# 微调垂直领域代码生成大模型-Example
此项目为代码生成项目，为避免数据泄露，仅包含37条训练数据集和11条验证数据集以做演示
`finetune.ipynb`: 程序主入口，调用sh脚本文件
`finetune/.+\.sh$`: lora、qlora等微调脚本
`finetune/finetune.py`: py微调脚本，解析超参数配置、执行模型加速等

原始代码仓库：https://github.com/QwenLM/Qwen