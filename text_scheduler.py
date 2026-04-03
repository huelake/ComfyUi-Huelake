import torch

class TextSchedulerNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text_input": ("STRING", {"multiline": True}),
                "index": ("INT", {"default": 0, "min": 0, "max": 9999}),
            },
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "schedule_text"
    CATEGORY = "scheduling"

    def schedule_text(self, text_input, index):
        # Split the input text by lines and filter out lines containing '----'
        lines = text_input.split('\n')
        scheduled_texts = []
        
        for line in lines:
            line = line.strip()
            # Skip empty lines and lines containing '----'
            if line and '----' not in line:
                scheduled_texts.append(line)
        
        # Return the text at the specified index, cycling if index is out of range
        if len(scheduled_texts) > 0:
            selected_index = index % len(scheduled_texts)
            return (scheduled_texts[selected_index],)
        else:
            return ("",)

# We need to add the node class to the NODE_CLASS_MAPPINGS dictionary
NODE_CLASS_MAPPINGS = {
    "TextSchedulerNode": TextSchedulerNode
}

# We can also add some information about the node
NODE_DISPLAY_NAME_MAPPINGS = {
    "TextSchedulerNode": "Text Scheduler"
}