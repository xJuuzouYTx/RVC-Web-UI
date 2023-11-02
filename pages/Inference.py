import streamlit as st
from jrvc.inference import Inference
import os

os.makedirs("audios", exist_ok=True)

def infer(
        audio_path,
        model_url,
        f0_method,
        index_rate,
        filter_radius1,
        vc_transform0,
        protect0,
        resample_sr1
):
    with st.spinner('Convirtiendo'):
        
        infer = Inference(
            f0_method=f0_method,
            source_audio_path=audio_path,
            feature_ratio=index_rate,
            transposition=vc_transform0,
            protection_amnt=protect0,
            resample=resample_sr1,
            harvest_median_filter=filter_radius1,
            output_file_name=os.path.join(
                "./audio-outputs", os.path.basename(audio_path)),
            auto_remove=True
        )
        output = infer.infer_by_model_url(model_url)
        print(output)
        
        st.markdown("### Result")
        st.audio(output)

def main():
    uploaded_file = st.file_uploader("Upload your acapella audio", )

    if uploaded_file:
        audio_path = os.path.join("audios", uploaded_file.name)
        with open(audio_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        model_url = st.text_input(
            'Url de modelo RVC', 'https://huggingface.co/AIVER-SE/BillieEilish/resolve/main/BillieEilish.zip')

        f0_method = st.selectbox(
            options=["harvest", "pm", "crepe", "crepe-tiny",
                     "mangio-crepe", "mangio-crepe-tiny", "rmvpe"],
            index=6,
            label="Algoritmo"
        )

        index_rate = st.slider(
            min_value=0.0, max_value=1.0, label="Search feature ratio:", value=0.75,)

        filter_radius1 = st.slider(
            min_value=0, max_value=7, label="Filtro (reducción de asperezas respiración)", value=3, step=1)

        vc_transform0 = st.slider(
            min_value=-12,
            max_value=12,
            label="Número de semitonos, subir una octava: 12, bajar una octava: -12",
            value=0,
            step=1
        )

        protect0 = st.slider(
            min_value=0.0, max_value=0.5, label="Protejer las consonantes sordas y los sonidos respiratorios. 0.5 para desactivarlo.", value=0.33,
            step=0.01,
        )
        resample_sr1 = st.slider(
            min_value=0,
            max_value=48000,
            label="Re-muestreo sobre el audio de salida hasta la frecuencia de muestreo final. 0 para no re-muestrear.",
            value=0,
            step=1,
        )

        st.button(
            "Convertir",
            on_click=infer,
            type="secondary",
            disabled=False,
            use_container_width=True,
            args=(
                audio_path,
                model_url,
                f0_method,
                index_rate,
                filter_radius1,
                vc_transform0,
                protect0,
                resample_sr1
            )
        )


main()
