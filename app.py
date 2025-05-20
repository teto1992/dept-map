import streamlit as st
import pydeck as pdk
import pandas as pd

hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
        .block-container {
        padding-top: 1rem !important;
     }
    </style>
    '''

st.set_page_config(
    page_title="Connessioni Informatica UniPi",
    page_icon="🧭",
    layout="wide"
)

st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

# Dati dei visitatori
visitors = [
    {'name': 'Prof. Smith', 'lat': 51.5074, 'lon': -0.1278, 'affiliation': 'UCL'},
    {'name': 'Dr. Rossi', 'lat': 43.7167, 'lon': 10.4, 'affiliation': 'UniPi'},
]

df = pd.DataFrame(visitors)

# Pinpoint per le icone
icon_data = {
    "url": "https://png.pngtree.com/png-vector/20220630/ourmid/pngtree-location-pin-point-marker-placeholder-png-image_5326979.png",
    "width":65,
    "height": 65,
    "anchorY": 65,
}

# Aggiunta delle informazioni sull'icona al DataFrame
df["icon_data"] = None
for i in df.index:
    df.at[i, "icon_data"] = icon_data

# Definizione del layer con icone personalizzate
icon_layer = pdk.Layer(
    type="IconLayer",
    data=df,
    get_icon="icon_data",
    get_size=2,
    size_scale=8,
    get_position="[lon, lat]",
    pickable=True,
)

# Vista iniziale
view_state = pdk.ViewState(
    latitude=0,
    longitude=0,
    zoom=0.5,    # tutto il mondo
    pitch=0,
)

# Creazione della mappa
r = pdk.Deck(
    layers=[icon_layer],
    initial_view_state=view_state,
    tooltip={"text": "{name} ({affiliation})"},
    map_style='https://basemaps.cartocdn.com/gl/positron-gl-style/style.json'  # stile chiaro, free
)

st.html("<style>[data-testid='stHeaderActionElements'] {display: none;}</style>")


cherubino_url = "https://www.unipi.it/wp-content/uploads/Raggruppa-3020.svg"

st.markdown(
    f"""
    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
        <a href="https://www.unipi.it/"><img src="{cherubino_url}" alt="Cherubino UniPi" width="200"></a>
        <h5 style="color:#003C71; margin:0;">Dipartimento di Informatica</h5><br>
    </div>
    """,
    unsafe_allow_html=True
)


st.write("Questa è una mappa delle connessioni del Dipartimento di Informatica dell'Università di Pisa")

st.pydeck_chart(r)
