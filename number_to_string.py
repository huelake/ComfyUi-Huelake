class NumberToString:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "number": ("NUMBER", {"default": 0.0}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "convert"
    CATEGORY = "utils"
    
    def convert(self, number):
        return (str(number),)

NODE_CLASS_MAPPINGS = {
    "NumberToString": NumberToString
}