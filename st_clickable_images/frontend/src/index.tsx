import { Streamlit, RenderData } from "streamlit-component-lib"

function onRender(event: Event): void {
  const data = (event as CustomEvent<RenderData>).detail

  // Remove existing content
  let child = document.body.lastElementChild;
  if (child) {
    document.body.removeChild(child)
  }

  // Add and style the image container
  let div = document.body.appendChild(document.createElement("div"))
  for (let key in data.args["div_style"]) {
    div.style[key as any] = data.args["div_style"][key]
  }

  // Add and style all images
  // for (let i = 0; i < data.args["paths"].length; i++) {
  //   let img = div.appendChild(document.createElement("img"))
  //   for (let key in data.args["img_style"]) {
  //     img.style[key as any] = data.args["img_style"][key]
  //   }
  //   img.src = data.args["paths"][i]
  //   if (data.args["titles"].length > i) {
  //     img.title = data.args["titles"][i]
  //   }
  //   img.onclick = function (): void {
  //     Streamlit.setComponentValue(i)
  //   }
  //   // eslint-disable-next-line
  //   img.onload = function (): void {
  //     imagesLoaded++
  //     if (imagesLoaded === data.args["paths"].length) {
  //       Streamlit.setFrameHeight()
  //     }
  //   }
  // }
  let img = div.appendChild(document.createElement("img"))
  for (let key in data.args["img_style"]) {
    img.style[key as any] = data.args["img_style"][key]
  }
  img.src = data.args["paths"]
  img.title = data.args["title"]
  img.onclick = function (): void {
    Streamlit.setComponentValue(true)
  }
  img.onload = function (): void {
    Streamlit.setFrameHeight()
  }
}

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
Streamlit.setComponentReady()