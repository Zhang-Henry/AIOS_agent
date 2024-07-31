export GEMINI_API_KEY=AIzaSyA2sA2f3BA1X9HUHb6KrBZbJqGZYF4Tx4U
python main.py --llm_name gemini-1.5-pro --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:7"
