# Stable Diffusion

## Simple demo with Finnish prompts

This demo accepts Finnish prompts. The prompts are machine translated by [`opus-mt-fi-en`](https://huggingface.co/Helsinki-NLP/opus-mt-fi-en) to English. 

The translated prompt is fed into the [Stable Diffusion](https://huggingface.co/CompVis/stable-diffusion-v1-4) model, which is loaded in fp16 precision in order to be able to run on low-memory GPU. The model runs fine on e.g. a NVIDIA GTX 1060 6GB card; generating one image takes about one minute.

## Running from WSL2

NVIDIA drivers only need to be installed on Windows. CUDA environment can be installed according to [instructions from NVIDIA](https://docs.nvidia.com/cuda/wsl-user-guide/index.html).

Add port forwarding and firewall rule for Windows from elevated Powershell prompt. The default gradio port is `7860`. 
The IP address of the WSL2 Linux VM in this example is `172.30.136.24`.
```powershell
netsh interface portproxy add v4tov4 listenport=7860 listenaddress=0.0.0.0 connectport=7860 connectaddress=172.30.136.24
netsh advfirewall firewall add rule name= "Open Port 7860" dir=in action=allow protocol=TCP localport=7860
```
