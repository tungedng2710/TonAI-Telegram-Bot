import requests
import json

def ollama_stream_inference(
    prompt: str,
    model: str = "deepseek-r1:14b",
    url: str = "http://localhost:7860/api/generate"
):
    """
    Send a streaming request to Ollama using the given prompt and model,
    and print out the response text in real time.
    """
    # Configure the payload according to Ollama's API.
    # You can add parameters like 'temperature' or 'top_p' if your server supports them.
    payload = {
        "model": model,
        "prompt": prompt
    }

    # We’ll store the entire response in this list as we stream chunks
    all_chunks = []

    # Use 'stream=True' for streaming responses
    with requests.post(url, json=payload, stream=True) as resp:
        # Raise an error if the request is not 200 OK
        resp.raise_for_status()

        # Iterate over each line that Ollama sends back
        for line in resp.iter_lines(decode_unicode=True):
            if not line:
                # If there's a blank line (keep-alive), just skip
                continue

            try:
                # Each line is a separate JSON object
                data = json.loads(line)
            except json.JSONDecodeError:
                # If you get partial or malformed data, handle/log it
                continue

            # Extract the chunk of text
            text_chunk = data.get("response", "")
            # Print directly to terminal (no extra newline, flush so it appears in real time)
            print(text_chunk, end="", flush=True)

            # Append chunk to our list so we can reconstruct later if we want
            all_chunks.append(text_chunk)

            # If "done" is True, the server indicates it's done streaming
            if data.get("done", False):
                break

    # Combine all chunks if you want the comprehensive string
    full_response = "".join(all_chunks)
    # print("\n\n---\nComplete response:\n", full_response)
    return full_response