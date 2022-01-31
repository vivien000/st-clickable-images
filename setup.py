import setuptools

setuptools.setup(
    name="st-clickable-images",
    version="0.0.3",
    author="",
    author_email="",
    description="A Streamlit component to display clickable images",
    long_description="A Streamlit component to display images and retrieve the indices of the images that were clicked on",
    long_description_content_type="text/plain",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
