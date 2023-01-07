import os
import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "clickable_images",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("st_clickable_images", path=build_dir)


def clickable_images(paths, title: str = "", div_style={}, img_style={}, key=None):
    """Create a new instance of "my_component".

    Parameters
    ----------
    paths: list
        The list of URLS of the images

    title: list
        The (optional) titles of the images

    div_style: dict
        A dict with the CSS property/value pairs for the div container

    img_style: dict
        A dict with the CSS property/value pairs for the images

    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    int
        The index of the last image clicked on (or -1 before any click)

    """
    component_value = _component_func(
        paths=paths,
        titles=title,
        div_style=div_style,
        img_style=img_style,
        key=key,
        default=False,
    )

    return component_value
