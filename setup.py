from setuptools import setup, find_packages


with open("requirements.txt") as file:
    requirements = file.read().splitlines()

if __name__ == "__main__":
    setup(name="synth",
          version="1.0",
          description="A synth package.",
          package_dir={"": "src"},
          packages=find_packages(where="src"),
          python_requires=">=3.10",
          install_requires=requirements)
