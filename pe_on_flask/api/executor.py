# https://zenn.dev/aerialstairs/articles/fac4b29e61e6d2
import subprocess


def execute(request):
    code = request.json["code"]
    inputs = request.json["inputs"]
    return execute_code(code, inputs)


def execute_code(code, inputs):
    # Write code to a temporary file
    with open("temp.py", "w") as file:
        file.write(code)

    # Add code to call the main function with provided inputs
    with open("temp.py", "a") as file:
        file.write(f"\nif __name__ == '__main__':\n    main([{inputs}])")

    # Execute the code file
    try:
        result = subprocess.check_output(
            ["python", "temp.py"], stderr=subprocess.STDOUT, universal_newlines=True
        )
        return result, None
    except subprocess.CalledProcessError as e:
        return None, e.output
