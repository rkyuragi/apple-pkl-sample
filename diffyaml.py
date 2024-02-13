import yaml

def load(path):
    with open(path, 'r') as yml:
        config = yaml.safe_load(yml)

    return config

def diff(file1, file2):
    data1 = load(file1)
    data2 = load(file2)

    if data1 == data2:
        print("YAML files are identical.")
    else:
        print("YAML files are different.")

        # Displaying the differences
        print("Differences:")
        for key in data1.keys() | data2.keys():
            if data1.get(key) != data2.get(key):
                print(f"Key: {key}")
                print(f"{file1}: {data1.get(key)}")
                print(f"{file2}: {data2.get(key)}")
                print()

if __name__ == "__main__":

    file_a = "./sample/serverlessframework/serverless.yaml"
    file_b = "./sample/serverlessframework/serverless-output.yaml"

    diff(file_a, file_b)
