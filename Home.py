import streamlit as st
from streamlit.components.v1 import html

app_title = "RVC Web UI by Juuxn"


def main():
    st.set_page_config(page_title=app_title, page_icon="favicon.ico",
                       layout="centered", initial_sidebar_state="auto", menu_items=None)

    button = """<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="woojae" data-color="#FFDD00" data-emoji="☕"  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>"""

    st.title(app_title)
    st.divider()
    st.header('RVC inference with GPU')

    st.markdown(
        """
        # Welcome, Everyone!
        
        This is the first version of the inference web user interface for Colab.
        Visit the **Inference** tab on the left panel, where you can upload your audio file and provide the model's .zip URL.
        You can find models for both RVC and Kits.ai on the following link: [RVC Community Models Sheet](https://docs.google.com/spreadsheets/d/1owfUtQuLW9ReiIwg6U9UkkDmPOTkuNHf0OKQtWu1iaI)
        
        # ¡Bienvenidos a Todos!
        Esta es la primera versión de la interfaz de usuario web para inferencias en Colab.
        Visita la pestaña **Inferencia** en el panel izquierdo, donde puedes cargar tu archivo de audio y proporcionar la URL del modelo en formato .zip.
        Puedes encontrar modelos tanto para RVC como para Kits.ai en el siguiente enlace: [Hoja de Modelos de la Comunidad RVC](https://docs.google.com/spreadsheets/d/1owfUtQuLW9ReiIwg6U9UkkDmPOTkuNHf0OKQtWu1iaI)
    """
    )

    html(button, height=70, width=240)

    st.markdown(
        """
        <style>
            iframe[width="240"] {
                position: fixed;
                bottom: 30px;
                right: 10px;
            }
        </>
        """,
        unsafe_allow_html=True,
    )


if __name__ == '__main__':
    main()
