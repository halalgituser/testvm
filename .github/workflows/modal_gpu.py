import modal
import os

# Create a Linux environment with a GPU and Sunshine (streaming)
image = (
    modal.Image.debian_slim()
    .apt_install("curl", "libgl1-mesa-glx", "libpulse0", "xserver-xorg-video-dummy")
    .pip_install("modal")
)

app = modal.App("gaming-vm")

@app.function(gpu="T4", image=image, timeout=3600)
def start_gpu_session():
    import subprocess
    print("🚀 NVIDIA Tesla T4 GPU is now ACTIVE!")
    print("Your $5 is running. Current cost: ~$0.60/hour")
    
    # This keeps the GPU alive for 1 hour so you can connect via AnyDesk/Moonlight
    # You can add your Sunshine or AnyDesk Linux commands here
    subprocess.run(["sleep", "3600"]) 

if __name__ == "__main__":
    with modal.enable_output():
        start_gpu_session.remote()
