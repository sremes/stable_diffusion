import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, TranslationPipeline
from PIL.Image import Image


class StableDiffusionDemo:
    translation_model_name: str = "Helsinki-NLP/opus-mt-fi-en"
    diffusion_model_name: str = "CompVis/stable-diffusion-v1-4"
    __name__: str = "stable_diffusion"
    
    def __init__(self):
        # create translation pipeline from Finnish to English
        tokenizer = AutoTokenizer.from_pretrained(self.translation_model_name)
        translation_model = AutoModelForSeq2SeqLM.from_pretrained(self.translation_model_name).eval()
        self.translator = TranslationPipeline(translation_model, tokenizer)
        # load the stable diffusion model
        self.diffuser = StableDiffusionPipeline.from_pretrained(
            self.diffusion_model_name, 
            torch_dtype=torch.float16, 
            revision="fp16", 
            use_auth_token=True,
        ).to("cuda")
    
    @torch.no_grad()
    def __call__(self, prompt: str) -> Image:
        with autocast("cuda"):
            prompt = self.translator(prompt)[0]["translation_text"]
            image = self.diffuser(prompt).images[0]
        return image


if __name__ == "__main__":
    import gradio as gr
    demo = gr.Interface(fn=StableDiffusionDemo(), inputs="text", outputs="image")
    demo.launch(server_name="0.0.0.0")