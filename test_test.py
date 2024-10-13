import subprocess

def test_hello_world():
    result = subprocess.run(['python3', 'main.py'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8').strip() == "Hello, World!"
