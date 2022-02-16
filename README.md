# st-clickable-image

`st-clickable-images` is a [Streamlit](https://streamlit.io) component to display one or several images and detect when they are clicked on.

![Screenshot](screenshot.gif)

A more advanced example can be seen live [here](https://huggingface.co/spaces/vivien/clip).

## Installation

```bash
pip install st-clickable-images
```

## Quickstart

```python
import streamlit as st
from st_clickable_images import clickable_images

clicked = clickable_images(
    [
        "https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=700",
        "https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=700",
        "https://images.unsplash.com/photo-1582550945154-66ea8fff25e1?w=700",
        "https://images.unsplash.com/photo-1591797442444-039f23ddcc14?w=700",
        "https://images.unsplash.com/photo-1518727818782-ed5341dbd476?w=700",
    ],
    titles=[f"Image #{str(i)}" for i in range(5)],
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "5px", "height": "200px"},
)

st.markdown(f"Image #{clicked} clicked" if clicked > -1 else "No image clicked")
```

This works as well with local images if you use `base64` encodings:

```python
import base64
import streamlit as st
from st_clickable_images import clickable_images

images = []
for file in ["image1.jpeg", "image2.jpeg"]:
    with open(file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
        images.append(f"data:image/jpeg;base64,{encoded}")

clicked = clickable_images(
    images,
    titles=[f"Image #{str(i)}" for i in range(len(images))],
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "5px", "height": "200px"},
)

st.markdown(f"Image #{clicked} clicked" if clicked > -1 else "No image clicked")
```

## Usage

**clickable_images(paths,
    titles=[],
    div_style={},
    img_style={},
    key=None
)**

Displays one or several images and returns the index of the last image clicked on (or -1 before any click)

### Parameters

- `paths` (list): the list of URLS of the images
- `titles` (list): the (optional) titles of the images
- `div_style` (dict): a dictionary with the CSS property/value pairs for the div container
- `img_style` (dict): a dictionary with the CSS property/value pairs for the images
- `key` (str or None): an optional key that uniquely identifies this component. If this is None, and the component's arguments are changed, the component will be re-mounted in the Streamlit frontend and lose its current state