# importar librerias
import streamlit as st
import pickle
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from plotly.subplots import make_subplots


@st.cache(allow_output_mutation=True)
def data_up():
    return pd.read_csv('ObesityDataNew.csv')


# Extrar los archivos pickle
with open('My_model.pkl', 'rb') as li:
    model = pickle.load(li)

st.set_page_config(page_title='Niveles de obesidad en personas', layout='wide')
df = data_up()


def grafP(c2):
    menores = [
        len(df[(df.Tipo_obesidad == "Peso_normal") & (df.Edad < 18)]),
        len(df[(df.Tipo_obesidad == "Sobrepeso_Nivel_I") & (df.Edad < 18)]),
        len(df[(df.Tipo_obesidad == "Sobrepeso_Nivel_II") & (df.Edad < 18)]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_I") & (df.Edad < 18)]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_II") & (df.Edad < 18)]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_III") & (df.Edad < 18)]),
        len(df[(df.Tipo_obesidad == "Peso_insuficiente") & (df.Edad < 18)]),
    ]

    mayores = [
        len(df[(df.Tipo_obesidad == "Peso_normal") & (df.Edad >= 18)]),
        len(df[(df.Tipo_obesidad == "Sobrepeso_Nivel_I") & (df.Edad >= 18)]),
        len(df[(df.Tipo_obesidad == "Sobrepeso_Nivel_II") & (df.Edad >= 18)]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_I") & (df.Edad >= 18)]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_II") & (df.Edad >= 18)]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_III") & (df.Edad >= 18)]),
        len(df[(df.Tipo_obesidad == "Peso_insuficiente") & (df.Edad >= 18)]),
    ]

    labels = list(df.Tipo_obesidad.unique())

    night_colors = ['#53BF9D', '#F94C66', '#BD4291',
                    '#FFC54D', '#005F99', '#FFF5B7', '#3AB4F2']

    fig = make_subplots(rows=1, cols=2, specs=[
                        [{'type': 'domain'}, {'type': 'domain'}]])
    fig.add_trace(go.Pie(labels=labels, values=mayores,
                  name="Mayor Edad", marker_colors=night_colors), 1, 1)
    fig.add_trace(go.Pie(labels=labels, values=menores,
                  name="Menor Edad", marker_colors=night_colors), 1, 2)

    fig.update_traces(hole=.4, hoverinfo="label+percent+name")

    fig.update_layout(

        annotations=[dict(text='', x=0.18, y=0.5, font_size=20, showarrow=False),
                     dict(text='', x=0.82, y=0.5, font_size=20, showarrow=False)])
    c2.write(fig)


def grafS(co2):

    Transporte_Publico = [
        len(df[(df.Tipo_obesidad == "Peso_normal") & (
            df.Medio_transporte == "Transporte_Publico")]),
        len(df[(df.Tipo_obesidad == "Sobrepeso_Nivel_I") & (
            df.Medio_transporte == "Transporte_Publico")]),
        len(df[(df.Tipo_obesidad == "Sobrepeso_Nivel_II") &
            (df.Medio_transporte == "Transporte_Publico")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_I") & (
            df.Medio_transporte == "Transporte_Publico")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_II") & (
            df.Medio_transporte == "Transporte_Publico")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_III") & (
            df.Medio_transporte == "Transporte_Publico")]),
        len(df[(df.Tipo_obesidad == "Peso_insuficiente") & (
            df.Medio_transporte == "Transporte_Publico")]),
    ]

    Caminar = [
        len(df[(df.Tipo_obesidad == "Peso_normal")
            & (df.Medio_transporte == "Caminar")]),
        len(df[(df.Tipo_obesidad == "Sobrepeso_Nivel_I")
            & (df.Medio_transporte == "Caminar")]),
        len(df[(df.Tipo_obesidad == "Sobrepeso_Nivel_II")
            & (df.Medio_transporte == "Caminar")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_I")
            & (df.Medio_transporte == "Caminar")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_II")
            & (df.Medio_transporte == "Caminar")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_III")
            & (df.Medio_transporte == "Caminar")]),
        len(df[(df.Tipo_obesidad == "Peso_insuficiente")
            & (df.Medio_transporte == "Caminar")]),
    ]

    Automovil = [
        len(df[(df.Tipo_obesidad == "Peso_normal") &
            (df.Medio_transporte == "Automovil")]),
        len(df[(df.Tipo_obesidad == "Sobrepeso_Nivel_I")
            & (df.Medio_transporte == "Automovil")]),
        len(df[(df.Tipo_obesidad == "Sobrepeso_Nivel_II")
            & (df.Medio_transporte == "Automovil")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_I")
            & (df.Medio_transporte == "Automovil")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_II")
            & (df.Medio_transporte == "Automovil")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_III")
            & (df.Medio_transporte == "Automovil")]),
        len(df[(df.Tipo_obesidad == "Peso_insuficiente")
            & (df.Medio_transporte == "Automovil")]),
    ]

    Moto = [
        len(df[(df.Tipo_obesidad == "Peso_normal")
            & (df.Medio_transporte == "Moto")]),
        len(df[(df.Tipo_obesidad == "Sobrepeso_Nivel_I")
            & (df.Medio_transporte == "Moto")]),
        len(df[(df.Tipo_obesidad == "Sobrepeso_Nivel_II")
            & (df.Medio_transporte == "Moto")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_I")
            & (df.Medio_transporte == "Moto")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_II")
            & (df.Medio_transporte == "Moto")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_III")
            & (df.Medio_transporte == "Moto")]),
        len(df[(df.Tipo_obesidad == "Peso_insuficiente")
            & (df.Medio_transporte == "Moto")]),
    ]

    Bicicleta = [
        len(df[(df.Tipo_obesidad == "Peso_normal") &
            (df.Medio_transporte == "Bicicleta")]),
        len(df[(df.Tipo_obesidad == "Sobrepeso_Nivel_I")
            & (df.Medio_transporte == "Bicicleta")]),
        len(df[(df.Tipo_obesidad == "Sobrepeso_Nivel_II")
            & (df.Medio_transporte == "Bicicleta")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_I")
            & (df.Medio_transporte == "Bicicleta")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_II")
            & (df.Medio_transporte == "Bicicleta")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_III")
            & (df.Medio_transporte == "Bicicleta")]),
        len(df[(df.Tipo_obesidad == "Peso_insuficiente")
            & (df.Medio_transporte == "MoBicicletato")]),
    ]

    x = list(df.Tipo_obesidad.unique())
    fig2 = go.Figure(go.Bar(x=x, y=Transporte_Publico,
                     marker_color='#53BF9D', name='Transporte Publico'))
    fig2.add_trace(
        go.Bar(x=x, y=Caminar, name='Caminar',  marker_color='#F94C66'))
    fig2.add_trace(
        go.Bar(x=x, y=Automovil, name='Automovil',  marker_color='#BD4291'))
    fig2.add_trace(go.Bar(x=x, y=Moto, name='Moto',  marker_color='#FFC54D'))
    fig2.add_trace(
        go.Bar(x=x, y=Bicicleta, name='Bicicleta',  marker_color='#005F99'))

    fig2.update_layout(barmode='stack', xaxis={
                       'categoryorder': 'category ascending'})
    co2.write(fig2)


def grafF(col2):
    fig3 = px.bar(df.groupby(["Tipo_obesidad"]).mean().reset_index().sort_values(by="Consumo_agua", ascending=False),
                  x="Consumo_agua", y="Tipo_obesidad", barmode='stack', color_discrete_sequence=['#53BF9D'],
                  orientation='h')

    col2.write(fig3)


def grafFi(col3):
    fig4 = px.line(df.groupby(["Tipo_obesidad"]).mean().reset_index(),
                   x="Tipo_obesidad", y="F_actvidad_fisica", markers=True)
    col3.write(fig4)


def main():

    menu = ["Datos", "Exploración", "Predicción", "About",]
    choice = st.sidebar.selectbox("Menú de opciones", menu)

    if choice == 'Datos':
        c1, c2, c3 = st.columns([1, 3, 1])
        c2.title(
            'Datos - Niveles de obesidad en personas de México, Perú y Colombia.')
        c2.write("""El presente Dataset muestra información de personas encuestadas en Colombia, Perú y México en un rango de 
        edades que va desde los 14 a los 61 años entre hombres y mujeres. El Dataset cuenta con 17 columnas y 2111 registros, donde en 
        la ultima columna se concluye el tipo de peso que tiene una persona la cual se clasifica en 7 categoría: peso insuficiente, peso 
        norma, sobre peso nivel I, sobrepeso nivel II, obesidad tipo I, obesidad tipo II y obesidad tipo III""")
        c2.title('')
        col1, col2, col3 = st.columns([1, 5, 1])
        col2.subheader('Datos registrados en el Dataframe')
        col2.write(df)
        code = """
        #Historial_familiar -> Si los familiares sufren de sobre peso.
        #C_rico_calorias -> Consumo frecuente de alimentos ricos en calorías
        #F_Consumo_verdura -> Frecuencia de consumo de verduras
        #N_comidas -> Número de comidas principales o número de comida al día
        #Meriendas -> Consumo de alimentos entre comidas.
        #Fumador -> Si fuma (respuesta verdadera o falso, ósea un valor booleano)
        #Consumo_agua-> Consumo de agua al día
        #Consumo_calorias -> Seguimiento de consumo de calorías (tu consumo de calorías, con 
        respuesta de si o no ósea un valor booleano
        #F_actividad_fisica -> Frecuencia de actividad física
        #T_usos_dispositivos -> Tiempo de uso de dispositivos electrónicos
        #C_alcohol -> Si consume alcohol (no, algunas veces, frecuentemente o siempre)
        #Medio_transporte -> Transporte utilizado (automóvil, motocicleta, bicicleta, transporte
        publicó, caminando)
        #Tipo_obesidad -> Este valor se crea en base a los demás y consta de lo siguiente 
        (peso_insuficiente, peso_normal, sobrepeso_nivel1, sobrepeso_nivel2, obesidad_tipo1, 
        obesidad_tipo2, obesidad_tipo3)"""
        col2.text(code)
        c2.title('')

        col2.subheader('Estadisticas')
        d_d2 = df.describe()
        col2.write(d_d2)

    elif choice == 'Exploración':
        c1, c2, c3 = st.columns([1, 3, 1])
        c2.title(
            'Exploración - Niveles de obesidad en personas de México, Perú y Colombia.')
        c2.title('')
        c2.subheader('Relación entre el Peso y la Edad')
        grafP(c2)
        c2.write("""Se podría afirmar según la gráfica, que el tipo de peso que mayormente padecen las personas independientemente de 
        cuál sea su edad, es el de obesidad. La moda para la población mayor de edad es obesidad tipo III, siendo la que tiene los 
        mayores índices de riesgos para la salud, en el caso de la población menor de edad, la obesidad tipo I y II son más comunes, 
        donde la primera es más frecuente que la segunda.""")

        co1, co2, co3 = st.columns([1, 3, 1])

        c2.subheader('')
        co2.subheader('Medio de Transporte Utilizado Segun su Peso')
        grafS(co2)

        col1, col2, col3, col4 = st.columns([1, 8, 8, 1])
        col1.title('')
        col1.title('')
        col2.subheader(
            '¿Cuál es el promedio de litros de agua consumida por categorías de obesidad?')
        grafF(col2)
        col2.write("""
            En la gráfica se observa que el consumo de agua por litro no afecta el hecho de pertenecer a una mayor o menor categoría de obesidad. 
            El consumo de agua siempre se mantiene en promedio de uno y dos que es lo normal que debe consumir una persona, es decir, que el consumo 
            de agua no afecta al aumento o disminución de masa""")

        col3.subheader('Relación Obesidad - Actividad Física')
        grafFi(col3)
        col3.write("""
            De la gráfica anterior se puede inferir que existe una relación directa entre el tipo de obesidad y la realización de actividad 
            física, debido a que entre más actividad física realicen las personas mejor va a estar su condición de peso o viceversa a menor 
            actividad física va a ser propenso a sufrir de algún tipo de obesidad.
        """)

    elif choice == 'Predicción':
        cl1, cl2, cl3 = st.columns([1, 4, 1])
        cl2.title(
            "Predicción - Niveles de obesidad en personas de México, Perú y Colombia.")
        cl2.title('')
        cl2.title('')
        cl2.subheader(
            "Ingrese los datos para realizar la predicción sobre el tipo de peso:")
        cl2.title('')
        c1, c2, c3, c4, c5, c6 = st.columns([1, 2, 2, 2, 2, 1])
        Edad = c3.slider(
            "Frecuencia en el consumo de verduras", min_value=14, max_value=61, value=22)
        F_consumo_verduras = c2.slider(
            "Frecuencia en el consumo de verduras", min_value=1, max_value=3)
        N_comidas = c2.slider(
            "Número de comidas al día", min_value=1, max_value=4)
        Consumo_agua = c3.slider(
            "Consumo de agua al día", min_value=1.0, max_value=3.0)

        F_actvidad_fisica = c2.slider(
            "Frecuencia de actividad fisica al día", min_value=0.0, max_value=3.0)

        c3.title('')

        data = {'Edad': Edad,
                'F_Consumo_verduras': F_consumo_verduras,
                'N_comidas': N_comidas,
                'F_actvidad_fisica': F_actvidad_fisica,
                'Consumo_agua': Consumo_agua,
                }
        features = pd.DataFrame(data, index=[0])

        st.write(features)

        if st.button('Predecir'):
            st.success(model.predict(features)[0])

    elif choice == 'About':
        cl1, cl2, cl3 = st.columns([1, 4, 1])
        cl2.title("Acerca del Dashboard ...")
        cl2.write("""
           El presente Dashboard se realiza como trabajo final para el diplomado denominado: PYTHON PARA EL ANÁLISIS DE DATOS 2022-II Ofrecido por la Universidad de Córdoba, donde se pone en practica todo el conocimiento adquirido durante el curso.
         El proyecto fue realizado por FERNANDO JOSE RUIZ NARANJO estudiante del programa de Ingeniería de Sistema.
""")


if __name__ == '__main__':
    main()
