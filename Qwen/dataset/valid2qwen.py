import json

def convert_jsonl_to_json(jsonl_file, json_file):
    with open(jsonl_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    conversations = []
    for idx, line in enumerate(lines):
        data = json.loads(line)
        messages = data['messages']
        system_message = messages[0]['content']
        user_message = messages[1]['content']
        assistant_message = messages[2]['content']
        
        conversation = [
            {"from": "user", "value": system_message + ' ' + user_message},
            {"from": "assistant", "value": assistant_message}
        ]
        conversations.append({"id": str(idx), "conversations": conversation})
    
    converted_data = conversations
    
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(converted_data, f, indent=2)

jsonl_file = "valid_dataset_raw.jsonl"
output_file = "Qwen/dataset/human_qwen_valid_output.json"
convert_jsonl_to_json(jsonl_file, output_file)