import re


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
        # Split on "---- #" delimiter lines (e.g. "---- #1 Title")
        sections = re.split(r'----\s*#', text_input)
        scheduled_texts = []

        for section in sections:
            # Strip the section number/title from the first line, keep the rest
            lines = section.strip().splitlines()
            if not lines:
                continue
            # The first line after the split contains the number and title (e.g. "1 Comic Page Layout")
            # Skip it and use the remaining content as the prompt
            content = '\n'.join(lines[1:]).strip() if len(lines) > 1 else lines[0].strip()
            if content:
                scheduled_texts.append(content)

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