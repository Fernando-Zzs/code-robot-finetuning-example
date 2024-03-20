import json

prompt_prefix = "You are a code assistant of the SSDP platform which is an internal tool used to create 3D scenes. In the SSDP platform, write a function to "
prompt_suffix = " Directly give the code here:"

def convert_jsonl_to_conversations(jsonl_file):
    conversations = []
    with open(jsonl_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            data = json.loads(line)
            conversation = {
                "id": f"{i}",
                "conversations": [
                    {
                        "from": "user",
                        "value": prompt_prefix + data["instr"] + prompt_suffix
                    },
                    {
                        "from": "assistant",
                        "value": data["msg"]
                    }
                ]
            }
            conversations.append(conversation)
    return conversations

jsonl_file = "train_dataset_raw.jsonl"
output_file = "Qwen/dataset/human_qwen_train_output.json"
conversations = convert_jsonl_to_conversations(jsonl_file)

with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(conversations, file, indent=2, ensure_ascii=False)