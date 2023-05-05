import setuptools

setuptools.setup(
    name="PSFvisual",
    version="0.1",
    author="Audrey Cesene",
    author_email="audrey.cesene@yale.edu",
    description="A learning tool designed to teach point spread function to undergraduate students",
    packages=["PSFvisual", "PSFvisual/pages"],
    install_requires=["numpy","scipy","astropy","streamlit","PIL"],
    url='https://github.com/acesene/PSFvisual'
)
