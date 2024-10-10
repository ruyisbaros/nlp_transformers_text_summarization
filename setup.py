import setuptools

# Get the long description from the README file

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="text_summarizer",
    version="0.0.1",
    author="Ahmet Erdonmez",
    author_email="ahmet.erdonmez77@gmail.com",
    description="Text summarization and text generation with Pytorch and Transformers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ruyisbaros/nlp_transformers_text_summarization",
    package_dir={"": "src"},
    packages=setuptools.find_packages("src", exclude=["test"]),
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
