import streamlit as st
import multiprocessing
import os
import subprocess
import threading

# Initialize global queues for communication between the Streamlit interface and the gpt-engineer process.
q_to_engineer = multiprocessing.Queue()
q_from_engineer = multiprocessing.Queue()
queue_lock = threading.Lock()

def enqueue_output(out, queue):
    for line in iter(out.readline, b''):
        with queue_lock:
            queue.put(line)
    out.close()

def run_gpt_engineer(instructions, options):
    # Start the gpt-engineer process and redirect its stdout to a pipe
    process = subprocess.Popen(['python', 'gpt_engineer/main.py', instructions, options], stdout=subprocess.PIPE, text=True)
    # Start a thread to read the process's output and put it into the queue
    t = threading.Thread(target=enqueue_output, args=(process.stdout, q_from_engineer))
    t.daemon = True
    t.start()
    return process

def main():
    # Create a Streamlit interface with input fields for instructions and a button to start the gpt-engineer process.
    st.title('GPT Engineer Interface')
    st.write('Enter your instructions for the GPT Engineer:')
    instructions = st.text_input('')
    options = st.text_input('Enter options:')
    progress_bar = st.progress(0)
    status_update_component = st.empty()
    # Interactive input capability
    user_input = st.text_input("Enter input for GPT Engineer:")
    if st.button('Submit'):
        with queue_lock:
            q_to_engineer.put(user_input)  # Send the user input to the gpt-engineer process
    try:
        if st.button('Start'):
            p = run_gpt_engineer(instructions, options)
            with open('config.txt', 'a') as f:
                f.write(f'{p.pid},{options}\\n')
            q_to_engineer.put((instructions, options))
            for i in range(100):
                # Update the progress bar with each iteration.
                progress_bar.progress(i + 1)
                if not q_from_engineer.empty():
                    status_update = q_from_engineer.get()
                    status_update_component.markdown(f'**Status Update:** {status_update}')
        # Real-time output viewing with efficient scrolling
        output_container = st.empty()
        while True:
            with queue_lock:
                if not q_from_engineer.empty():
                    output_line = q_from_engineer.get_nowait()
                    output_container.code(output_line, height=300)  # Display the output in a code block with a fixed height
        if p.is_alive():
            st.write('GPT Engineer is running...')
        else:
            st.write('GPT Engineer has finished.')
    except Exception as e:
        st.error('An error occurred: ' + str(e))

# Run the Streamlit interface in a separate process.
if __name__ == "__main__":
    if os.path.exists('config.txt'):
        with open('config.txt', 'r') as f:
            for line in f:
                pid, options = line.strip().split(',')
                p = multiprocessing.Process(pid=int(pid))
                q_to_engineer.put(options)
    p = multiprocessing.Process(target=main)
    p.start()