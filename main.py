from dustbin_controller import run_dustbin

if __name__ == "__main__":
    try:
        print("Starting AI IoT Smart Dustbin...")
        run_dustbin()
    except KeyboardInterrupt:
        print("Stopped manually")