import streamlit as st
import random

st.set_page_config(
    page_title="📚 English con Cuaderno",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ══════════════════════════════════════════════════════════════
# CSS – DUOLINGO STYLE
# ══════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap');
* { font-family: 'Nunito', sans-serif !important; }
body, .main, [data-testid="stAppViewContainer"] { background: #f0f4f8 !important; }
section[data-testid="stSidebar"] { background: #ffffff !important; border-right: 3px solid #e5e7eb !important; }
section[data-testid="stSidebar"] > div { padding-top: 0.5rem !important; }
.main .block-container { padding: 1.5rem 2rem 2rem !important; max-width: 940px !important; }
#MainMenu, footer, header { visibility: hidden !important; }

/* ── TOPBAR BADGES ── */
.badge { border-radius: 50px; padding: 0.3rem 0.9rem; font-size: 0.82rem; font-weight: 800; color: white; display: inline-block; margin: 0.15rem; }

/* ── CARDS ── */
.duo-card { background: white; border-radius: 20px; padding: 1.4rem 1.6rem; box-shadow: 0 4px 16px rgba(0,0,0,0.08); margin-bottom: 1rem; border: 2px solid #f0f0f0; }
.duo-card-colored { border-radius: 20px; padding: 1.4rem 1.6rem; box-shadow: 0 4px 16px rgba(0,0,0,0.12); margin-bottom: 1rem; color: white; }

/* ── STAT CARD ── */
.stat-card { background: white; border-radius: 18px; padding: 1rem 0.8rem; text-align: center; box-shadow: 0 3px 12px rgba(0,0,0,0.07); border: 2px solid #f0f0f0; }
.stat-val { font-size: 1.6rem; font-weight: 900; line-height: 1.1; }
.stat-label { font-size: 0.75rem; color: #aaa; font-weight: 700; margin-top: 0.1rem; }

/* ── LESSON ITEM ── */
.lesson-item { background: white; border-radius: 16px; padding: 1rem 1.2rem 1rem 0.8rem; margin-bottom: 0.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.06); display: flex; align-items: center; gap: 0.8rem; border: 2px solid #f0f0f0; transition: box-shadow 0.2s; }

/* ── VOCAB ROW ── */
.vocab-row { background: white; border-radius: 12px; padding: 0.6rem 1rem; border-left: 5px solid #58CC02; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 1px 5px rgba(0,0,0,0.06); margin-bottom: 0.4rem; }
.vocab-en { font-weight: 800; font-size: 0.9rem; color: #333; }
.vocab-es { color: #58CC02; font-weight: 700; font-size: 0.88rem; }

/* ── THEORY PAIR ── */
.theory-en { background: #e8f4fd; border-radius: 12px; padding: 0.65rem 1rem; font-weight: 700; font-size: 0.9rem; color: #1a6fa3; border-left: 4px solid #1CB0F6; }
.theory-es { background: #edfce8; border-radius: 12px; padding: 0.65rem 1rem; font-size: 0.9rem; color: #2d7a3a; border-left: 4px solid #58CC02; }
.grammar-box { background: #fff8e1; border-radius: 14px; padding: 0.9rem 1.1rem; margin-bottom: 1rem; font-size: 0.88rem; font-weight: 700; color: #7c6000; border-left: 5px solid #FFC800; }

/* ── OPTION BUTTONS ── */
.opt-correct { background: #d4edda !important; border: 3px solid #28a745 !important; color: #155724 !important; border-radius: 14px !important; padding: 0.8rem 1rem !important; font-weight: 700 !important; width: 100% !important; text-align: left !important; margin-bottom: 0.5rem !important; font-size: 0.95rem !important; }
.opt-wrong { background: #f8d7da !important; border: 3px solid #dc3545 !important; color: #721c24 !important; border-radius: 14px !important; padding: 0.8rem 1rem !important; font-weight: 700 !important; width: 100% !important; text-align: left !important; margin-bottom: 0.5rem !important; font-size: 0.95rem !important; }
.opt-neutral { background: white !important; border: 3px solid #e8e8e8 !important; color: #333 !important; border-radius: 14px !important; padding: 0.8rem 1rem !important; font-weight: 700 !important; width: 100% !important; text-align: left !important; margin-bottom: 0.5rem !important; font-size: 0.95rem !important; cursor: pointer !important; }

/* ── FEEDBACK ── */
.feedback-ok { background: #d4edda; border: 3px solid #28a745; color: #155724; border-radius: 16px; padding: 1rem 1.2rem; font-weight: 800; font-size: 1rem; margin: 0.6rem 0; }
.feedback-ko { background: #f8d7da; border: 3px solid #dc3545; color: #721c24; border-radius: 16px; padding: 1rem 1.2rem; font-weight: 800; font-size: 1rem; margin: 0.6rem 0; }

/* ── PROGRESS ── */
.prog-outer { background: #e9ecef; border-radius: 50px; height: 12px; margin: 8px 0; }
.prog-inner { height: 12px; border-radius: 50px; transition: width 0.4s ease; }

/* ── NOTEBOOK ── */
.nb-notes { background: #fafafa; border-radius: 10px; padding: 0.8rem 1rem; margin-top: 0.6rem; font-family: Georgia, serif; line-height: 2; font-size: 0.88rem; }

/* ── SPORT CARD ── */
.sport-card { border-radius: 20px; padding: 1.3rem 1rem; color: white; text-align: center; cursor: pointer; box-shadow: 0 6px 20px rgba(0,0,0,0.15); transition: transform 0.2s; }
.sport-card:hover { transform: translateY(-3px); }
.sport-card .sc-icon { font-size: 2.2rem; margin-bottom: 0.3rem; }
.sport-card h3 { font-size: 0.95rem; font-weight: 900; margin: 0.2rem 0 0.1rem; }
.sport-card p { font-size: 0.75rem; opacity: 0.88; margin: 0; }

/* ── BUTTONS ── */
div.stButton > button {
    border-radius: 14px !important; font-weight: 800 !important; font-size: 0.9rem !important;
    border: 3px solid transparent !important; transition: all 0.15s !important;
    padding: 0.55rem 1rem !important;
}
div.stButton > button[kind="primary"] { background: #58CC02 !important; color: white !important; border-color: #46a302 !important; box-shadow: 0 4px 0 #46a302 !important; }
div.stButton > button[kind="primary"]:hover { transform: translateY(-2px) !important; box-shadow: 0 6px 0 #46a302 !important; }
div.stButton > button[kind="secondary"] { background: white !important; color: #333 !important; border-color: #e8e8e8 !important; box-shadow: 0 3px 0 #e0e0e0 !important; }
div.stButton > button[kind="secondary"]:hover { border-color: #58CC02 !important; color: #58CC02 !important; }

/* ── SIDEBAR NAV ── */
.nav-title { font-size: 1.3rem; font-weight: 900; background: linear-gradient(135deg,#58CC02,#1CB0F6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; padding: 0.5rem 0; }

/* ── WORD CHIPS ── */
.chip-avail { display:inline-block; background:white; border:3px solid #1CB0F6; border-radius:10px; padding:0.4rem 0.9rem; font-weight:800; font-size:0.9rem; margin:0.25rem; cursor:pointer; box-shadow:0 3px 0 #a8d4f0; }
.chip-used { display:inline-block; background:#e9ecef; border:3px solid #dee2e6; border-radius:10px; padding:0.4rem 0.9rem; font-weight:800; font-size:0.9rem; margin:0.25rem; color:#ccc; }
.chip-sel { display:inline-block; background:#667eea; color:white; border:3px solid #5570d5; border-radius:10px; padding:0.4rem 0.9rem; font-weight:800; font-size:0.9rem; margin:0.25rem; cursor:pointer; box-shadow:0 3px 0 #4455bb; }

/* ── HOME HERO ── */
.hero-title { font-size: 2.4rem; font-weight: 900; background: linear-gradient(135deg,#58CC02,#1CB0F6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; line-height: 1.1; }
.hero-sub { color: #888; font-size: 1rem; margin-top: 0.2rem; }

/* ── HANGMAN ── */
.hangman-display { font-size: 2rem; font-weight: 900; letter-spacing: 0.4rem; text-align: center; padding: 1rem; color: #333; }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# DATA – VOCABULARIO COMPLETO
# ══════════════════════════════════════════════════════════════
VOCAB = {
    "⚽ Deportes (Sports)": [
        ("Basketball","Baloncesto"),("Football","Fútbol"),("Swimming","Natación"),
        ("Gymnastics","Gimnasia"),("Running","Correr"),("Karate","Kárate"),
        ("Table Tennis","Tenis de mesa"),("Skateboarding","Monopatín"),("Yoga","Yoga"),
        ("Volleyball","Voleibol"),("Baseball","Béisbol"),("Snowboarding","Snowboard"),
        ("Handball","Balonmano"),("Cycling","Ciclismo"),("Athletics","Atletismo"),
    ],
    "👕 Ropa (Clothes)": [
        ("Jeans","Vaqueros"),("T-shirt","Camiseta"),("Shorts","Pantalones cortos"),
        ("Shoes","Zapatos"),("Skirt","Falda"),("Dress","Vestido"),("Jumper","Jersey"),
        ("Socks","Calcetines"),("Hat","Sombrero"),("Cap","Gorra"),
        ("Trainers","Zapatillas de deporte"),("Helmet","Casco"),("Body","Body"),("Uniform","Uniforme"),
    ],
    "👷 Profesiones (Jobs)": [
        ("Doctor","Médico/a"),("Nurse","Enfermero/a"),("Firefighter","Bombero/a"),
        ("Teacher","Profesor/a"),("Cook / Chef","Cocinero/a"),("Builder","Constructor/a"),
        ("Mechanic","Mecánico/a"),("Farmer","Agricultor/a"),("Dancer","Bailarín/a"),
        ("Singer","Cantante"),("Judge","Juez/a"),("Designer","Diseñador/a"),
        ("Vet","Veterinario/a"),("Welder","Soldador/a"),("Police officer","Policía"),("Pilot","Piloto/a"),
    ],
    "🔤 Verbos de clase (Classroom verbs)": [
        ("Like","Gustar"),("Watch","Ver"),("Make","Hacer"),("Follow","Seguir"),
        ("Select","Seleccionar"),("Repeat","Repetir"),("Correct","Corregir"),
        ("Find","Encontrar / Buscar"),("Catch","Coger / Atrapar"),("Choose","Elegir"),
        ("Read","Leer"),("Say","Decir"),("Write","Escribir"),
    ],
    "🔤 Verbos generales (Verbs)": [
        ("Play","Jugar / Tocar"),("Study","Estudiar"),("Call","Llamar"),("Come","Venir"),
        ("Buy","Comprar"),("Lose","Perder"),("Teach","Enseñar"),("Wake","Despertar"),
        ("Swim","Nadar"),("Fly","Volar"),("Help","Ayudar"),("See","Ver"),
        ("Brush","Cepillar"),("Kiss","Besar"),("Take","Tomar / Coger"),("Give","Dar"),
        ("Go","Ir"),("Get up","Levantarse"),("Run","Correr"),("Dance","Bailar"),
        ("Build","Construir"),("Repair","Reparar"),("Design","Diseñar"),("Grow","Cultivar / Crecer"),
        ("Drive","Conducir"),("Eat","Comer"),("Drink","Beber"),("Sleep","Dormir"),
        ("Work","Trabajar"),("Live","Vivir"),("Think","Pensar"),("Know","Saber / Conocer"),
        ("Send","Enviar"),("Arrive","Llegar"),("Catch","Coger"),("Watch","Ver"),
    ],
    "📺 Programas de TV": [
        ("Cartoon","Dibujos animados"),("Documentary","Documental"),
        ("Reality show","Reality show"),("Music programme","Programa de música"),
        ("Cookery programme","Programa de cocina"),("Film","Película"),
        ("Match","Partido / Carrera"),("News","Noticias"),
        ("Talent show","Concurso de talentos"),("Quiz show","Concurso de preguntas"),
        ("She doesn't like cookery programmes","No le gustan los programas de cocina"),
        ("She likes music programmes","Le gustan los programas de música"),
        ("She likes documentaries about amazing animals","Le gustan los documentales de animales"),
        ("Does Kieran like talent shows?","¿A Kieran le gustan los talent shows?"),
        ("Does Mia like the news? True","¿A Mia le gustan las noticias? Verdadero"),
    ],
    "💪 CAN / CAN'T": [
        ("I can swim","Puedo nadar"),("I can't swim","No puedo nadar"),
        ("Can you play?","¿Puedes jugar?"),("He can dance","Él puede bailar"),
        ("She can't fly","Ella no puede volar"),("He can't swim!","¡Él no sabe nadar!"),
        ("Yes, I can","Sí, puedo"),("No, I can't","No, no puedo"),
    ],
    "⏰ Las horas (Time)": [
        ("O'clock","En punto"),("Quarter past","Y cuarto"),("Half past","Y media"),
        ("Quarter to","Menos cuarto"),("Morning","Mañana"),("Afternoon","Tarde"),
        ("Evening","Tarde / noche"),("Night","Noche"),
        ("What time is it?","¿Qué hora es?"),
        ("What time does he get up?","¿A qué hora se levanta?"),
        ("It's five o'clock","Son las cinco en punto"),
        ("It's half past six","Son las seis y media"),
        ("It's quarter past three","Son las tres y cuarto"),
        ("It's quarter to eight","Son las ocho menos cuarto"),
        ("It's twenty to eleven","Son las once menos veinte"),
        ("It's twenty past seven","Son las siete y veinte"),
        ("It's seven and a half","Son las siete y media (informal)"),
    ],
    "🏠 Lugares (Places)": [
        ("Hospital","Hospital"),("School","Colegio"),("Office","Oficina"),
        ("Kitchen","Cocina"),("Bank","Banco"),("Garden","Jardín"),
        ("Park","Parque"),("Beach","Playa"),("Sea","Mar"),("Farm","Granja"),
        ("Library","Biblioteca"),("Cinema","Cine"),("Town","Ciudad / pueblo"),
        ("Workshop","Taller"),("Restaurant","Restaurante"),("College","Facultad / instituto"),
    ],
    "💬 Frases útiles": [
        ("The competition is finished","La competición está terminada"),
        ("The judge likes the dessert","Al juez le gusta el postre"),
        ("Does he wear a uniform?","¿Lleva uniforme?"),
        ("Yes, he does","Sí, lleva"),("No, he doesn't","No, no lleva"),
        ("She works outdoors","Trabaja al aire libre"),
        ("He helps patients","Ayuda a los pacientes"),
        ("Well done!","¡Bien hecho!"),("You're amazing!","¡Eres increíble!"),
        ("Have some hot chocolate!","¡Toma chocolate caliente!"),
        ("You need to wear a helmet","Necesitas llevar casco"),
        ("There is a boy in the water","Hay un chico en el agua"),
        ("He can't swim!","¡No sabe nadar!"),
        ("I can't do it","No puedo hacerlo"),
        ("Today I don't eat","Hoy no como"),
        ("She doesn't like it","No le gusta"),
    ],
    "🎭 Acciones laborales (Job actions)": [
        ("Take care of animals","Cuidar animales"),("Grow plants","Cultivar plantas"),
        ("Repair cars","Reparar coches"),("Build houses","Construir casas"),
        ("Design things","Diseñar cosas"),("Help people","Ayudar a la gente"),
        ("Teach children","Enseñar a niños"),("Cook food","Cocinar comida"),
        ("Fight fires","Combatir incendios"),("Turn off","Apagar / dejar de"),
    ],
    "🌍 Presentarse (Introducing yourself)": [
        ("My name's...","Me llamo..."),("I'm from...","Soy de..."),
        ("I'm ... years old","Tengo ... años"),("I speak...","Hablo..."),
        ("I play...","Juego a... / Toco..."),("I do gymnastics","Hago gimnasia"),
        ("I go swimming","Voy a nadar"),("I live in...","Vivo en..."),
        ("My birthday is in...","Mi cumpleaños es en..."),
    ],
    "🔢 Números (Numbers)": [
        ("One","Uno"),("Two","Dos"),("Three","Tres"),("Four","Cuatro"),("Five","Cinco"),
        ("Six","Seis"),("Seven","Siete"),("Eight","Ocho"),("Nine","Nueve"),("Ten","Diez"),
        ("Eleven","Once"),("Twelve","Doce"),("Thirteen","Trece"),("Fourteen","Catorce"),
        ("Fifteen","Quince"),("Sixteen","Dieciséis"),("Seventeen","Diecisiete"),
        ("Eighteen","Dieciocho"),("Nineteen","Diecinueve"),("Twenty","Veinte"),
        ("Thirty","Treinta"),("Forty","Cuarenta"),("Fifty","Cincuenta"),
        ("Sixty","Sesenta"),("Seventy","Setenta"),("Eighty","Ochenta"),
        ("Ninety","Noventa"),("One hundred","Cien"),("One thousand","Mil"),("One million","Un millón"),
    ],
    "🏫 Palabras del colegio": [
        ("Library","Biblioteca"),("Everybody","Todo el mundo"),
        ("Choose","Elegir"),("Dictionary","Diccionario"),("Follow me","Sígueme"),
        ("Lot of","Muchos"),("Zebra crossing","Paso de cebra"),("Arrive","Llegar"),
        ("River","Río"),("Country","Campo / país"),("Postcard","Postal"),
        ("Town","Ciudad / pueblo"),("Classroom","Aula"),("Lesson","Lección / clase"),
    ],
    "🔤 Has got / Have got": [
        ("I have got a cat","Tengo un gato"),("I have not got a cat","No tengo un gato"),
        ("Pedro has not got a book","Pedro no tiene un libro"),
        ("Have you got maths?","¿Tienes matemáticas?"),
        ("Has Pedro got English?","¿Pedro tiene inglés?"),
        ("He hasn't got it","Él no lo tiene"),("She has got it","Ella lo tiene"),
        ("Has not got","No tiene (he/she/it)"),("Have not got","No tienen (I/you/we/they)"),
    ],
    "❓ Interrogativos (Question words)": [
        ("What?","¿Qué?"),("Where?","¿Dónde?"),("When?","¿Cuándo?"),
        ("Which?","¿Cuál?"),("Why?","¿Por qué?"),("How?","¿Cómo?"),
        ("How many?","¿Cuántos?"),("Who?","¿Quién?"),("How much?","¿Cuánto?"),
        ("What time?","¿A qué hora?"),
        ("Does Laura go to the swimming pool?","¿Va Laura a la piscina?"),
        ("Does Laura go on Mondays?","¿Va Laura los lunes?"),
        ("Does Laura go to the park?","¿Va Laura al parque?"),
        ("Where do Laura go?","¿Adónde va Laura?"),
    ],
    "🍳 Junior Chef / Cocina": [
        ("To wear","Llevar puesto"),("To make","Hacer"),("To help","Ayudar"),
        ("Burnt","Quemado"),("Dessert","Postre"),("Show","Espectáculo / mostrar"),
        ("Jake helps Drew","Jake ayuda a Drew"),
        ("You can use these together","Podéis usarlos juntos"),
        ("He makes another item","Hace otro elemento"),
        ("Thank you Jake!","¡Gracias Jake!"),("Oh no! It's a mess!","¡Madre mía!"),
        ("Everybody STOP!","¡Todo el mundo para!"),
        ("There is one hour left","Queda una hora"),
        ("We have a lot of time","Tenemos mucho tiempo"),
        ("You can sort them","Puedes clasificarlos"),("Don't worry!","¡No te preocupes!"),
    ],
    "🎵 Canción – Where do you work?": [
        ("Where do you work all day?","¿Dónde trabajas todo el día?"),
        ("Places of work","Lugares de trabajo"),
        ("My mum works as an English teacher","Mi mamá trabaja como profesora de inglés"),
        ("My dad works in a restaurant","Mi papá trabaja en un restaurante"),
        ("This is the college where she works","Este es el colegio donde trabaja"),
        ("It's near my school","Está cerca de mi colegio"),
        ("My brother is a police officer","Mi hermano es policía"),
        ("My uncle is a firefighter","Mi tío es bombero"),
        ("Garages, factories, shops","Garajes, fábricas, tiendas"),
        ("Did you catch a bus or train?","¿Cogiste un autobús o un tren?"),
        ("Did you work all day?","¿Trabajaste todo el día?"),
        ("Is it near or far away?","¿Está cerca o lejos?"),
        ("Do you work on Saturday?","¿Trabajas el sábado?"),
    ],
    "🏘️ There is / There are": [
        ("There is a cinema in the city","Hay un cine en la ciudad"),
        ("Is there a cinema in your city?","¿Hay un cine en tu ciudad?"),
        ("There are dictionaries in the library","Hay diccionarios en la biblioteca"),
        ("Are there dictionaries in the library?","¿Hay diccionarios en la biblioteca?"),
        ("No, there aren't","No, no hay"),("Yes, there are","Sí, hay"),
        ("No, there isn't","No, no hay"),("Yes, there is","Sí, hay"),
        ("No, there isn't a library in the town","No hay biblioteca en el pueblo"),
        ("There are dictionaries","Hay diccionarios"),
        ("Has Juan got maths on Friday?","¿Tiene Juan mates el viernes?"),
    ],
    "📅 Traducir frases (Translate)": [
        ("Elkan learns with children","Elkan aprende con niños"),
        ("Mary y Elba have a TV programme","Mary y Elba tienen un programa de TV"),
        ("Mr. Menardre rehearses","El Sr. Menardre ensaya"),
        ("Daniel y Jerry play together","Daniel y Jerry juegan juntos"),
        ("They read a book","Leen un libro"),
        ("My mum writes","Mi mamá escribe"),
        ("Daniel and Jerry play basketball on Saturday","Daniel y Jerry juegan al baloncesto el sábado"),
        ("Mieres drinks water","Mieres bebe agua"),
        ("Fred is my brother","Fred es mi hermano"),
        ("He hasn't got the maths book in the bag","No tiene el libro de mates en la mochila"),
        ("Are there dictionaries in the library? No, there aren't","¿Hay diccionarios en la biblioteca? No, no hay"),
    ],
    "🏙️ Ciudad (Town)": [
        ("City","Ciudad"),("Nearby","Cerca"),("Small","Pequeño/a"),
        ("Building","Edificio"),("Buy","Comprar"),("Village","Pueblo pequeño"),
        ("Country","Campo / país"),("Far","Lejos"),("Near","Cerca"),
        ("Shopping centre","Centro comercial"),("Swimming pool","Piscina"),
        ("Traffic","Tráfico"),("Park","Parque"),("Street","Calle"),("Road","Carretera"),
        ("Always cross the road carefully","Siempre cruza la carretera con cuidado"),
        ("There is a lot of traffic in the city","Hay mucho tráfico en la ciudad"),
        ("There is a zebra crossing","Hay un paso de cebra"),
        ("Is there a shopping centre in your village?","¿Hay un centro comercial en tu pueblo?"),
        ("There isn't a police station in my village","No hay comisaría en mi pueblo"),
        ("We go shopping on Mondays","Vamos de compras los lunes"),
    ],
    "🐊 Animales (Animals)": [
        ("Crocodile","Cocodrilo"),("Elephant","Elefante"),("Flamingo","Flamenco"),
        ("Kangaroo","Canguro"),("Monkey","Mono"),("Cheetah","Guepardo"),
        ("Lion","León"),("Shark","Tiburón"),("Bear","Oso"),
        ("Swim","Nadar"),("Run","Correr"),("Climb","Trepar / Escalar"),
        ("Hide","Esconderse"),("Eat","Comer"),("Fly","Volar"),
        ("The lion is drinking","El león está bebiendo"),
        ("Is the lion drinking?","¿Está bebiendo el león?"),
    ],
    "🏊 Present Continuous": [
        ("I am drawing","Estoy dibujando"),("We are swimming","Estamos nadando"),
        ("She is eating","Está comiendo"),("They are running","Están corriendo"),
        ("He is swimming","Él está nadando"),("It is swimming","Está nadando"),
        ("It isn't running","No está corriendo"),("Is it swimming?","¿Está nadando?"),
        ("Yes, it is","Sí, está"),("No, it isn't","No, no está"),
        ("Are they swimming?","¿Están nadando?"),
        ("The lion is drinking","El león está bebiendo"),
        ("There are four pens under the table","Hay cuatro bolígrafos debajo de la mesa"),
        ("Are there four pens under the table?","¿Hay cuatro bolígrafos debajo de la mesa?"),
        ("We haven't got English at 9","No tenemos inglés a las 9"),
    ],
    "📅 Días de la semana (Days)": [
        ("Sunday","Domingo"),("Monday","Lunes"),("Tuesday","Martes"),
        ("Wednesday","Miércoles"),("Thursday","Jueves"),("Friday","Viernes"),("Saturday","Sábado"),
        ("What time...?","¿A qué hora...?"),
        ("What time do you go to school?","¿A qué hora vas al colegio?"),
    ],
    "🕐 Rutina diaria (Daily Routine)": [
        ("Get up","Levantarse"),("Go home","Ir a casa"),("Go to bed","Ir a la cama"),
        ("Go to school","Ir al colegio"),("Have a shower","Ducharse"),
        ("Have breakfast","Desayunar"),("Have dinner","Cenar"),("Have lunch","Comer"),
        ("I get up at seven and I have a shower at half past seven.","Me levanto a las siete y me ducho a las siete y media."),
        ("What time does Izzy get up?","¿A qué hora se levanta Izzy?"),
        ("It is seven o'clock.","Son las siete en punto."),
        ("What time does Eric get up?","¿A qué hora se levanta Eric?"),
        ("It is half past seven.","Son las siete y media."),
    ],
    "🚗 Transporte (Transport)": [
        ("By car","En coche"),("By train","En tren"),("By bus","En autobús"),
        ("By bike","En bicicleta"),("By taxi","En taxi"),("Walk","Andando"),
        ("How do you go to...?","¿Cómo vas a...?"),
        ("I go to school by car.","Voy al colegio en coche."),
        ("I go to school by bike, ferry and bus.","Voy al colegio en bici, ferry y autobús."),
        ("On the ferry, I can see a castle.","En el ferry, puedo ver un castillo."),
        ("Long","Largo"),("Journey","Viaje"),("Lighthouse","Faro"),("Friends","Amigos"),
    ],
    "📚 Asignaturas (Subjects)": [
        ("Art","Plástica"),("English","Inglés"),("IT","Informática"),
        ("Maths","Matemáticas"),("Music","Música"),("PE","Educación Física"),
        ("Science","Ciencias"),("Spanish","Español"),
        ("What test has Izzy got today?","¿Qué examen tiene Izzy hoy?"),
        ("What day has Eric got football?","¿Qué día tiene fútbol Eric?"),
    ],
    "📖 La biblioteca (Library)": [
        ("Librarian","Bibliotecario/a"),("Help","Ayudar"),("Cookbook","Un libro de cocina"),
        ("Want","Querer"),("Make","Hacer"),("Joke book","Libro de chistes"),
        ("Noise","Ruido"),("Sit down","Siéntate"),("Quietly","En silencio"),
        ("Scary","Miedo"),("Hear","Escuchar"),
        ("Hello! I'm the new librarian.","¡Hola! Soy la nueva bibliotecaria."),
        ("Everybody go and choose a book!","¡Todo el mundo va y elige un libro!"),
        ("Yes, follow me!","¡Sí, sígueme!"),
        ("You need a cookbook. Follow me!","Tú necesitas un libro de cocina. ¡Sígueme!"),
        ("I want to make a cake!","¡Yo quiero hacer un pastel!"),
    ],
    "🏥 Edificios de la ciudad (Buildings)": [
        ("Hospital","Hospital"),("Shopping centre","Centro comercial"),
        ("Museum","Museo"),("Fire station","Parque de bomberos"),
        ("Cinema","Cine"),("Swimming pool","Piscina"),
        ("Train station","Estación de tren"),("Post office","Oficina de correos"),
        ("There is a pencil on the table.","Hay un lápiz en la mesa."),
        ("There are four rubbers on the table.","Hay cuatro gomas en la mesa."),
        ("There isn't a police station in my city.","No hay comisaría en mi ciudad."),
        ("There aren't two schools.","No hay dos colegios."),
        ("Is there a school in your town?","¿Hay un colegio en tu pueblo?"),
        ("Are there...?","¿Hay...?"),
    ],
    "🤸 Mary – Reading (Vocab)": [
        ("Wardrobe","Armario"),("Camping","Camping"),("Morning","Mañana"),
        ("Dressed","Bien vestida"),("Long","Largo"),("Of years","Muchos años"),
        ("Supermarket","Supermercado"),("Watermelons","Sandías"),
        ("She wouldn't like to go camping with her grandfather.","No le gustaría ir de camping con su abuelo."),
        ("Mary likes going athletics and playing table tennis.","Mary le gusta hacer atletismo y jugar al ping-pong."),
        ("She has a toast and coffee for breakfast.","Desayuna tostadas y café."),
    ],
}

# ══════════════════════════════════════════════════════════════
# DATA – LECCIONES COMPLETAS (25 lecciones)
# ══════════════════════════════════════════════════════════════
LESSONS = [
    {"id":0,"title":"Presentarse en inglés","icon":"👋","date":"Tuesday 21st October 2025","color":"#ff9a56",
     "grammar":"MY NAME'S = My name is | I'M = I am | 'I' is ALWAYS capital!",
     "theory":[
         {"en":"My name's Nettie and I'm from Canada.","es":"Me llamo Nettie y soy de Canadá."},
         {"en":"I'm nine years old and I speak English.","es":"Tengo nueve años y hablo inglés."},
         {"en":"I play football and do gymnastics.","es":"Juego al fútbol y hago gimnasia."},
         {"en":"I got PE on Tuesday and Friday.","es":"Tengo EF el martes y el viernes."},
         {"en":"My birthday is in February.","es":"Mi cumpleaños es en febrero."},
     ],
     "ex":[
         {"q":"Soy de España.","a":"I'm from Spain.","o":["I'm from Spain.","I am of Spain.","I come from of Spain.","I from Spain."]},
         {"q":"Hablo inglés y español.","a":"I speak English and Spanish.","o":["I speak English and Spanish.","I talking English and Spanish.","I speaks English and Spanish.","I am speak English and Spanish."]},
         {"q":"Juego al fútbol.","a":"I play football.","o":["I play football.","I plays football.","I am play football.","I playing football."]},
         {"q":"Me llamo Sara y tengo 10 años.","a":"My name's Sara and I'm ten years old.","o":["My name's Sara and I'm ten years old.","My names Sara and Im ten.","I name Sara and I am ten years.","My name Sara and I'm ten years old."]},
     ]},
    {"id":1,"title":"Mayúsculas (Capital Letters)","icon":"✏️","date":"Thursday 16th October 2025","color":"#a29bfe",
     "grammar":"Capital: I, names, countries, languages, months, days, start of sentence.",
     "theory":[
         {"en":"Names, countries, languages → CAPITAL letter","es":"Nombres, países, idiomas → mayúscula"},
         {"en":"At the start of a sentence → Capital.","es":"Inicio de oración → mayúscula."},
         {"en":"Days and months → Capital.","es":"Días y meses → mayúscula."},
         {"en":"I → ALWAYS capital! Never 'i'","es":"I (yo) → ¡siempre mayúscula!"},
     ],
     "ex":[
         {"q":"¿Cuál va en mayúscula? i am from spain","a":"I am from Spain.","o":["I am from Spain.","i am from Spain.","I am from spain.","i am from spain."]},
         {"q":"¿El mes en mayúscula?","a":"February","o":["February","february","FEBRUARY","februarY"]},
         {"q":"¿El idioma en mayúscula?","a":"English","o":["English","english","ENGLISH","englisH"]},
         {"q":"¿El día en mayúscula?","a":"Monday","o":["Monday","monday","MONDAY","mondaY"]},
     ]},
    {"id":2,"title":"CAN / CAN'T","icon":"💪","date":"Friday 25th October 2025","color":"#00b894",
     "grammar":"I can swim. / I can't swim. / Can you play? Yes, I can. / No, I can't.",
     "theory":[
         {"en":"I can swim.","es":"Puedo nadar."},
         {"en":"I can't swim.","es":"No puedo nadar."},
         {"en":"He can't swim!","es":"¡Él no sabe nadar!"},
         {"en":"Can you play? Yes, I can.","es":"¿Puedes jugar? Sí, puedo."},
         {"en":"She can't fly.","es":"Ella no puede volar."},
     ],
     "ex":[
         {"q":"Puedo nadar.","a":"I can swim.","o":["I can swim.","I can swims.","I cans swim.","I am can swim."]},
         {"q":"Ella no puede volar.","a":"She can't fly.","o":["She can't fly.","She can fly.","She cans't fly.","She can't flies."]},
         {"q":"¿Puedes jugar al fútbol?","a":"Can you play football?","o":["Can you play football?","Can you plays football?","You can play football?","Do you can play football?"]},
         {"q":"No, no puedo.","a":"No, I can't.","o":["No, I can't.","No, I can.","No, I cans't.","No, I not can."]},
     ]},
    {"id":3,"title":"Present Simple – 3ª persona","icon":"📝","date":"Friday 7th November 2025","color":"#6c5ce7",
     "grammar":"He/She/It: play→plays | write→writes | watch→watches | study→studies | fly→flies",
     "theory":[
         {"en":"He plays football every day.","es":"Él juega al fútbol cada día."},
         {"en":"She watches TV in the evening.","es":"Ella ve la tele por la noche."},
         {"en":"He studies English at school.","es":"Estudia inglés en el colegio."},
         {"en":"She flies to London on Monday.","es":"Vuela a Londres el lunes."},
         {"en":"He brushes his teeth twice a day.","es":"Se cepilla los dientes dos veces al día."},
     ],
     "ex":[
         {"q":"Ella ve la tele. (watch)","a":"She watches TV.","o":["She watches TV.","She watch TV.","She is watching TV.","She watchs TV."]},
         {"q":"Él estudia inglés. (study)","a":"He studies English.","o":["He studies English.","He study English.","He studys English.","He is study English."]},
         {"q":"Ella vuela a España. (fly)","a":"She flies to Spain.","o":["She flies to Spain.","She fly to Spain.","She flys to Spain.","She flying to Spain."]},
         {"q":"Él se cepilla. (brush)","a":"He brushes.","o":["He brushes.","He brush.","He brusches.","He brushs."]},
     ]},
    {"id":4,"title":"Sports Vocabulary","icon":"⚽","date":"Friday 25th October 2025","color":"#fdcb6e",
     "grammar":"PLAY → Basketball, Football | DO → Gymnastics, Karate | GO → Swimming, Running",
     "theory":[
         {"en":"I play basketball / football / volleyball.","es":"Juego al baloncesto / fútbol / voleibol."},
         {"en":"I do gymnastics / karate / yoga.","es":"Hago gimnasia / kárate / yoga."},
         {"en":"I go swimming / running / skateboarding.","es":"Voy a nadar / correr / hacer monopatín."},
         {"en":"My favourite sport is cycling.","es":"Mi deporte favorito es el ciclismo."},
         {"en":"You need to wear a helmet for cycling.","es":"Necesitas llevar casco para el ciclismo."},
     ],
     "ex":[
         {"q":"Hago gimnasia. (do/go/play?)","a":"I do gymnastics.","o":["I do gymnastics.","I go gymnastics.","I play gymnastics.","I does gymnastics."]},
         {"q":"Voy a nadar. (do/go/play?)","a":"I go swimming.","o":["I go swimming.","I do swimming.","I play swimming.","I goes swimming."]},
         {"q":"Juego al fútbol. (do/go/play?)","a":"I play football.","o":["I play football.","I go football.","I do football.","I plays football."]},
         {"q":"Hago kárate. (do/go/play?)","a":"I do karate.","o":["I do karate.","I go karate.","I play karate.","I does karate."]},
     ]},
    {"id":5,"title":"TV Programmes + Likes","icon":"📺","date":"Thursday 13th November 2025","color":"#0984e3",
     "grammar":"She likes... | She doesn't like... | Does she like...? Yes/No she does/doesn't",
     "theory":[
         {"en":"She likes cookery programmes.","es":"Le gustan los programas de cocina."},
         {"en":"She doesn't like cookery programmes.","es":"No le gustan los programas de cocina."},
         {"en":"Brianna doesn't like cookery programmes.","es":"A Brianna no le gustan los programas de cocina."},
         {"en":"She likes documentaries about amazing animals.","es":"Le gustan los documentales de animales."},
         {"en":"Does Kieran like talent shows?","es":"¿A Kieran le gustan los talent shows?"},
     ],
     "ex":[
         {"q":"A ella le gustan los documentales.","a":"She likes documentaries.","o":["She likes documentaries.","She like documentaries.","She is like documentaries.","She liking documentaries."]},
         {"q":"A ella no le gustan los programas de cocina.","a":"She doesn't like cookery programmes.","o":["She doesn't like cookery programmes.","She don't like cookery programmes.","She not likes cookery programmes.","She doesn't likes cookery programmes."]},
         {"q":"¿Le gustan los concursos? Sí.","a":"Yes, she does.","o":["Yes, she does.","Yes, she like.","Yes, she likes.","Yes, she do."]},
         {"q":"Programa de cocina en inglés:","a":"Cookery programme","o":["Cookery programme","Music programme","Documentary","Reality show"]},
     ]},
    {"id":6,"title":"Translate – Nov (frases)","icon":"🔤","date":"Thursday 13th November 2025","color":"#e17055",
     "grammar":"Present Simple: he/she + verb-s | they + verb (sin -s)",
     "theory":[
         {"en":"Elkan learns with children.","es":"Elkan aprende con niños."},
         {"en":"Mary and Elba have a TV programme.","es":"Mary y Elba tienen un programa de TV."},
         {"en":"They read a book.","es":"Leen un libro."},
         {"en":"Daniel and Jerry play basketball on Saturday.","es":"Daniel y Jerry juegan al baloncesto el sábado."},
         {"en":"Mieres drinks water.","es":"Mieres bebe agua."},
     ],
     "ex":[
         {"q":"Elkan aprende con niños.","a":"Elkan learns with children.","o":["Elkan learns with children.","Elkan learn with children.","Elkan learning with children.","Elkan is learns with children."]},
         {"q":"Leen un libro.","a":"They read a book.","o":["They read a book.","They reads a book.","They reading a book.","They is read a book."]},
         {"q":"Daniel y Jerry juegan al baloncesto el sábado.","a":"Daniel and Jerry play basketball on Saturday.","o":["Daniel and Jerry play basketball on Saturday.","Daniel and Jerry plays basketball on Saturday.","Daniel and Jerry playing basketball Saturday.","Daniel and Jerry is play basketball on Saturday."]},
         {"q":"Mieres bebe agua.","a":"Mieres drinks water.","o":["Mieres drinks water.","Mieres drink water.","Mieres drinking water.","Mieres is drinks water."]},
     ]},
    {"id":7,"title":"Interrogativos + Laura","icon":"❓","date":"Friday 25th November 2025","color":"#6c5ce7",
     "grammar":"Do + sujeto + verbo? | Does + he/she/it + verbo? | Question words: What/Where/When/How many",
     "theory":[
         {"en":"Where does Laura go?","es":"¿Adónde va Laura?"},
         {"en":"Does Laura go on Mondays?","es":"¿Va Laura los lunes?"},
         {"en":"Does Laura go to the park?","es":"¿Va Laura al parque?"},
         {"en":"What? Where? When? Which? Why? How? How many? Who?","es":"¿Qué? ¿Dónde? ¿Cuándo? ¿Cuál? ¿Por qué? ¿Cómo? ¿Cuántos? ¿Quién?"},
         {"en":"How many? → Incredible!","es":"¿Cuántos? → ¡Increíble!"},
     ],
     "ex":[
         {"q":"¿Adónde va Laura?","a":"Where does Laura go?","o":["Where does Laura go?","Where Laura goes?","Where go Laura?","Where is Laura go?"]},
         {"q":"¿Va Laura los lunes?","a":"Does Laura go on Mondays?","o":["Does Laura go on Mondays?","Laura goes on Mondays?","Do Laura go on Mondays?","Does Laura goes on Mondays?"]},
         {"q":"¿Cuántos? en inglés","a":"How many?","o":["How many?","How much?","How?","Which?"]},
         {"q":"¿Por qué? en inglés","a":"Why?","o":["Why?","Where?","When?","Which?"]},
     ]},
    {"id":8,"title":"What time is it?","icon":"⏰","date":"Tuesday 27th November 2025","color":"#f093fb",
     "grammar":"O'clock | Quarter past | Half past | Quarter to | Twenty past | Twenty to",
     "theory":[
         {"en":"It's half past six.","es":"Son las seis y media."},
         {"en":"It's quarter past three.","es":"Son las tres y cuarto."},
         {"en":"It's twenty to eleven.","es":"Son las once menos veinte."},
         {"en":"It's quarter to twelve.","es":"Son las doce menos cuarto."},
         {"en":"It's five o'clock.","es":"Son las cinco en punto."},
     ],
     "ex":[
         {"q":"Son las once menos veinte.","a":"It's twenty to eleven.","o":["It's twenty to eleven.","It's twenty past eleven.","It's eleven twenty.","It's twenty to ten."]},
         {"q":"Son las seis y media.","a":"It's half past six.","o":["It's half past six.","It's six half.","It's half six.","It's six thirty."]},
         {"q":"Son las doce menos cuarto.","a":"It's quarter to twelve.","o":["It's quarter to twelve.","It's quarter past twelve.","It's twelve quarter.","It's to quarter twelve."]},
         {"q":"Son las siete y diez.","a":"It's ten past seven.","o":["It's ten past seven.","It's ten to seven.","It's seven ten.","It's past ten seven."]},
     ]},
    {"id":9,"title":"Numbers 1–1,000,000","icon":"🔢","date":"Various 2025","color":"#fdcb6e",
     "grammar":"1-15: one, two... | 16+: sixteen, seventeen... | 20,30,40...: twenty, thirty, forty...",
     "theory":[
         {"en":"One, Two, Three, Four, Five","es":"Uno, Dos, Tres, Cuatro, Cinco"},
         {"en":"Six, Seven, Eight, Nine, Ten","es":"Seis, Siete, Ocho, Nueve, Diez"},
         {"en":"Eleven, Twelve, Thirteen, Fourteen, Fifteen","es":"Once, Doce, Trece, Catorce, Quince"},
         {"en":"Sixteen, Seventeen, Eighteen, Nineteen, Twenty","es":"Dieciséis, Diecisiete, Dieciocho, Diecinueve, Veinte"},
         {"en":"Thirty, Forty, Fifty, Sixty, Seventy, Eighty, Ninety, One hundred","es":"Treinta, Cuarenta, Cincuenta, Sesenta, Setenta, Ochenta, Noventa, Cien"},
     ],
     "ex":[
         {"q":"¿Cómo se dice 13?","a":"Thirteen","o":["Thirteen","Thirty","Three","Fourteen"]},
         {"q":"¿Cómo se dice 40?","a":"Forty","o":["Forty","Four","Fourteen","Four hundred"]},
         {"q":"¿Cómo se dice 15?","a":"Fifteen","o":["Fifteen","Fifty","Five","Fourteen"]},
         {"q":"¿Cómo se dice 1000?","a":"One thousand","o":["One thousand","One hundred","One million","Ten hundred"]},
     ]},
    {"id":10,"title":"Junior Chef Competition","icon":"👨‍🍳","date":"Thursday 19th February 2026","color":"#43e97b",
     "grammar":"IS = está/es (he/she/it) | LIKES = le gusta (he/she/it)",
     "theory":[
         {"en":"The competition is finished.","es":"La competición está terminada."},
         {"en":"The judge likes Tobi's dessert.","es":"Al juez le gusta el postre de Tobi."},
         {"en":"Jake helps Drew.","es":"Jake ayuda a Drew."},
         {"en":"You can use these together.","es":"Podéis usarlos juntos para hacer otro elemento."},
         {"en":"Everybody STOP!","es":"¡Todo el mundo para!"},
     ],
     "ex":[
         {"q":"La competición está terminada.","a":"The competition is finished.","o":["The competition is finished.","The competition has finish.","Competition is finish.","The competition finished is."]},
         {"q":"Jake ayuda a Drew.","a":"Jake helps Drew.","o":["Jake helps Drew.","Jake help Drew.","Jake is help Drew.","Jake helping Drew."]},
         {"q":"¡Todo el mundo para!","a":"Everybody STOP!","o":["Everybody STOP!","Everybody STOPS!","Everybody STOPPED!","STOP everybody!"]},
         {"q":"¿Cuánto tiempo queda?","a":"There is one hour left.","o":["There is one hour left.","There are one hour left.","Is one hour left.","One hour is left."]},
     ]},
    {"id":11,"title":"Present Simple Jobs (+/-/?)","icon":"💼","date":"Thursday 20th February 2026","color":"#667eea",
     "grammar":"(+) He works | (-) He doesn't work | (?) Does he work? Yes/No he does/doesn't",
     "theory":[
         {"en":"He wears a uniform.","es":"Lleva uniforme."},
         {"en":"She works outdoors.","es":"Trabaja al aire libre."},
         {"en":"He doesn't wear a uniform.","es":"No lleva uniforme."},
         {"en":"Does he wear a uniform? Yes, he does.","es":"¿Lleva uniforme? Sí."},
         {"en":"Does he work in a bank? No, he doesn't.","es":"¿Trabaja en un banco? No."},
     ],
     "ex":[
         {"q":"¿Lleva uniforme?","a":"Does he wear a uniform?","o":["Does he wear a uniform?","He wears uniform?","Is he wear a uniform?","Do he wear a uniform?"]},
         {"q":"Ella trabaja en un hospital.","a":"She works in a hospital.","o":["She works in a hospital.","She work in a hospital.","She is working in hospital.","She working in hospital."]},
         {"q":"Él no lleva uniforme.","a":"He doesn't wear a uniform.","o":["He doesn't wear a uniform.","He don't wear a uniform.","He not wears a uniform.","He doesn't wears a uniform."]},
         {"q":"¿Trabaja en un banco? No.","a":"Does he work in a bank? No, he doesn't.","o":["Does he work in a bank? No, he doesn't.","Do he work in bank? No.","Does he works in bank? No, he don't.","He work in a bank? No, he doesn't."]},
     ]},
    {"id":12,"title":"Telling the Time","icon":"⏰","date":"Thursday 26th February 2026","color":"#fd79a8",
     "grammar":"O'clock=en punto | Quarter past=y cuarto | Half past=y media | Quarter to=menos cuarto",
     "theory":[
         {"en":"It's five o'clock.","es":"Son las cinco en punto."},
         {"en":"It's quarter past three.","es":"Son las tres y cuarto."},
         {"en":"It's half past six.","es":"Son las seis y media."},
         {"en":"It's quarter to eight.","es":"Son las ocho menos cuarto."},
         {"en":"What time does Tom get up? He gets up at...","es":"¿A qué hora se levanta Tom?"},
     ],
     "ex":[
         {"q":"Son las tres y cuarto.","a":"It's quarter past three.","o":["It's quarter past three.","It's three quarter.","It's three and quarter.","It's past quarter three."]},
         {"q":"Son las cinco en punto.","a":"It's five o'clock.","o":["It's five o'clock.","It's five clock.","It's five in point.","It's the five."]},
         {"q":"Son las seis y media.","a":"It's half past six.","o":["It's half past six.","It's half six past.","It's six half.","It's past half six."]},
         {"q":"Son las ocho menos cuarto.","a":"It's quarter to eight.","o":["It's quarter to eight.","It's quarter past eight.","It's eight quarter.","It's to quarter eight."]},
     ]},
    {"id":13,"title":"Job Descriptions","icon":"👔","date":"Thursday 27th February 2026","color":"#4facfe",
     "grammar":"He/She IS a + job | WORKS in + place | WEARS a + clothing | HELPS + people",
     "theory":[
         {"en":"He is a nurse and works in a hospital.","es":"Es enfermero y trabaja en un hospital."},
         {"en":"She is a firefighter and helps people.","es":"Es bombera y ayuda a la gente."},
         {"en":"He wears a blue uniform.","es":"Lleva uniforme azul."},
         {"en":"She doesn't get dressed in a uniform.","es":"Ella no se pone uniforme."},
         {"en":"He works in a workshop. He repairs cars.","es":"Trabaja en un taller. Repara coches."},
     ],
     "ex":[
         {"q":"Ella es médica.","a":"She is a doctor.","o":["She is a doctor.","She is doctor.","She a doctor is.","She are a doctor."]},
         {"q":"Él trabaja en una cocina.","a":"He works in a kitchen.","o":["He works in a kitchen.","He work in kitchen.","He is working a kitchen.","He working in a kitchen."]},
         {"q":"¿Lleva uniforme? Sí.","a":"Does she wear a uniform? Yes, she does.","o":["Does she wear a uniform? Yes, she does.","Does she wears uniform? Yes.","Is she wearing uniform? Yes.","She wear uniform? Yes, she does."]},
         {"q":"Él repara coches.","a":"He repairs cars.","o":["He repairs cars.","He repair cars.","He repairing cars.","He is repairs cars."]},
     ]},
    {"id":14,"title":"Has got / Have got","icon":"🎒","date":"Various 2025-2026","color":"#00cec9",
     "grammar":"I/You/We/They HAVE GOT | He/She/It HAS GOT | Negative: hasn't / haven't got",
     "theory":[
         {"en":"I have not got a cat.","es":"No tengo un gato."},
         {"en":"Pedro has not got a book.","es":"Pedro no tiene un libro."},
         {"en":"Have you got maths?","es":"¿Tienes matemáticas?"},
         {"en":"Has Pedro got English?","es":"¿Pedro tiene inglés?"},
         {"en":"Fred is my brother. He hasn't got the maths book.","es":"Fred es mi hermano. No tiene el libro de mates."},
     ],
     "ex":[
         {"q":"No tengo un gato.","a":"I have not got a cat.","o":["I have not got a cat.","I has not got a cat.","I haven't get a cat.","I not have got a cat."]},
         {"q":"Pedro no tiene un libro.","a":"Pedro has not got a book.","o":["Pedro has not got a book.","Pedro have not got a book.","Pedro hasn't get a book.","Pedro not has got a book."]},
         {"q":"¿Tienes matemáticas?","a":"Have you got maths?","o":["Have you got maths?","Has you got maths?","Do you have got maths?","You have got maths?"]},
         {"q":"¿Tiene Pedro inglés?","a":"Has Pedro got English?","o":["Has Pedro got English?","Have Pedro got English?","Does Pedro has got English?","Pedro has got English?"]},
     ]},
    {"id":15,"title":"There is / There are","icon":"🏘️","date":"Thursday 13th February 2026","color":"#e84393",
     "grammar":"There IS + singular | There ARE + plural | Is there...? / Are there...? Yes/No",
     "theory":[
         {"en":"There is a cinema in the city.","es":"Hay un cine en la ciudad."},
         {"en":"Is there a cinema in your city?","es":"¿Hay un cine en tu ciudad?"},
         {"en":"There are dictionaries in the library.","es":"Hay diccionarios en la biblioteca."},
         {"en":"Are there dictionaries in the library? No, there aren't.","es":"¿Hay diccionarios en la biblioteca? No, no hay."},
         {"en":"No, there isn't a library in the town.","es":"No hay biblioteca en el pueblo."},
     ],
     "ex":[
         {"q":"Hay un cine en la ciudad.","a":"There is a cinema in the city.","o":["There is a cinema in the city.","There are a cinema in the city.","Is there a cinema in the city.","There is cinema in city."]},
         {"q":"¿Hay diccionarios en la biblioteca?","a":"Are there dictionaries in the library?","o":["Are there dictionaries in the library?","Is there dictionaries in the library?","There are dictionaries in the library?","Do there dictionaries in library?"]},
         {"q":"No, no hay.","a":"No, there aren't.","o":["No, there aren't.","No, there isn't.","No, there aren't got.","No, there not are."]},
         {"q":"No hay biblioteca en el pueblo.","a":"There isn't a library in the town.","o":["There isn't a library in the town.","There aren't a library in the town.","No there is a library in the town.","There isn't library in town."]},
     ]},
    {"id":16,"title":"Translate – Fred & dictionaries","icon":"📖","date":"Tuesday 19th February 2026","color":"#6c5ce7",
     "grammar":"Translate from Spanish to English using has got / there is / there are",
     "theory":[
         {"en":"Fred is my brother.","es":"Fred es mi hermano."},
         {"en":"He hasn't got the maths book in the bag.","es":"No tiene el libro de mates en la mochila."},
         {"en":"Are there dictionaries in the library? No, there aren't.","es":"¿Hay diccionarios en la biblioteca? No, no hay."},
         {"en":"Has Juan got maths on Friday?","es":"¿Tiene Juan mates el viernes?"},
         {"en":"Is there a cinema in the city? Yes, there is.","es":"¿Hay un cine en la ciudad? Sí, hay."},
     ],
     "ex":[
         {"q":"Fred es mi hermano.","a":"Fred is my brother.","o":["Fred is my brother.","Fred is my sister.","Fred are my brother.","Fred my brother is."]},
         {"q":"No tiene el libro de mates.","a":"He hasn't got the maths book.","o":["He hasn't got the maths book.","He haven't got the maths book.","He not has the maths book.","He hasn't get the maths book."]},
         {"q":"¿Hay cine en la ciudad? Sí.","a":"Yes, there is.","o":["Yes, there is.","Yes, there are.","Yes, there has.","Yes, it is."]},
         {"q":"¿Tiene Juan mates el viernes?","a":"Has Juan got maths on Friday?","o":["Has Juan got maths on Friday?","Have Juan got maths on Friday?","Does Juan has got maths on Friday?","Juan has got maths on Friday?"]},
     ]},
    {"id":17,"title":"Joe and Amy – Daily routine","icon":"🕐","date":"Tuesday 5th November 2025","color":"#fd79a8",
     "grammar":"I get up at... | I have breakfast at... | My favourite sport is...",
     "theory":[
         {"en":"I get up at ten o'clock. (Amy)","es":"Me levanto a las diez en punto."},
         {"en":"I have breakfast at half past nine. (Joe)","es":"Desayuno a las nueve y media."},
         {"en":"My favourite sport is karate. (Joe)","es":"Mi deporte favorito es el kárate."},
         {"en":"I have lunch at half past one.","es":"Como a la una y media."},
         {"en":"In the afternoon, I read books.","es":"Por la tarde, leo libros."},
     ],
     "ex":[
         {"q":"Me levanto a las diez en punto.","a":"I get up at ten o'clock.","o":["I get up at ten o'clock.","I get up at ten past.","I get up ten o'clock.","I gets up at ten o'clock."]},
         {"q":"Desayuno a las nueve y media.","a":"I have breakfast at half past nine.","o":["I have breakfast at half past nine.","I have breakfast at nine o'clock.","I have breakfast at quarter past nine.","I have breakfast at quarter to nine."]},
         {"q":"Mi deporte favorito es el kárate.","a":"My favourite sport is karate.","o":["My favourite sport is karate.","My favourite sport are karate.","My sport favourite is karate.","My favourite is karate sport."]},
         {"q":"Juego a juegos de ordenador.","a":"I play computer games.","o":["I play computer games.","I plays computer games.","I playing computer games.","I am play computer games."]},
     ]},
    {"id":18,"title":"Where do you work? (Song)","icon":"🎵","date":"Various Feb 2026","color":"#00b894",
     "grammar":"My mum/dad works as a... | This is where he/she works | Places of work",
     "theory":[
         {"en":"Where do you work all day?","es":"¿Dónde trabajas todo el día?"},
         {"en":"My mum works as an English teacher.","es":"Mi mamá trabaja como profesora de inglés."},
         {"en":"This is the college where she works.","es":"Este es el instituto donde trabaja."},
         {"en":"My brother is a police officer.","es":"Mi hermano es policía."},
         {"en":"Garages, factories, shops, places of work.","es":"Garajes, fábricas, tiendas, lugares de trabajo."},
     ],
     "ex":[
         {"q":"¿Dónde trabajas todo el día?","a":"Where do you work all day?","o":["Where do you work all day?","Where does you work all day?","Where you work all day?","Where do you works all day?"]},
         {"q":"Mi mamá trabaja como maestra.","a":"My mum works as a teacher.","o":["My mum works as a teacher.","My mum work as a teacher.","My mum is working as teacher.","My mum working as a teacher."]},
         {"q":"Este es el colegio donde trabaja.","a":"This is the school where she works.","o":["This is the school where she works.","This is the school where she work.","This is where school she works.","This school is where she works."]},
         {"q":"¿Está cerca o lejos?","a":"Is it near or far away?","o":["Is it near or far away?","Is it close or far?","It is near or far?","Near or far it is?"]},
     ]},
    {"id":19,"title":"Jobs Vocabulary","icon":"👷","date":"Thursday 20th February 2026","color":"#e17055",
     "grammar":"Builder→Albañil | Farmer→Granjero | Firefighter→Bombero | Nurse→Enfermero | Vet→Veterinario",
     "theory":[
         {"en":"Builder → Albañil/a","es":"Construye casas"},
         {"en":"Farmer → Granjero/a","es":"Grow plants / Take care of animals"},
         {"en":"Firefighter → Bombero/a","es":"Fight fires"},
         {"en":"Nurse → Enfermero/a","es":"Helps patients in hospital"},
         {"en":"Vet → Veterinario/a | Pilot → Piloto/a","es":"Takes care of animals | Flies planes"},
     ],
     "ex":[
         {"q":"Builder en español:","a":"Albañil/a","o":["Albañil/a","Granjero/a","Bombero/a","Piloto/a"]},
         {"q":"¿Qué hace un granjero?","a":"He grows plants and takes care of animals.","o":["He grows plants and takes care of animals.","He builds houses.","He repairs cars.","He fights fires."]},
         {"q":"Vet en español:","a":"Veterinario/a","o":["Veterinario/a","Bombero/a","Enfermero/a","Albañil/a"]},
         {"q":"¿Qué hace un bombero?","a":"He fights fires.","o":["He fights fires.","He builds houses.","He repairs cars.","He designs things."]},
     ]},
    {"id":20,"title":"La ciudad (Town)","icon":"🏙️","date":"Thursday 6th February 2026","color":"#4facfe",
     "grammar":"There IS a + singular | There ARE + plural | Is there / Are there...? near / far",
     "theory":[
         {"en":"There is a lot of traffic in the city.","es":"Hay mucho tráfico en la ciudad."},
         {"en":"There is a swimming pool near here.","es":"Hay una piscina cerca de aquí."},
         {"en":"There is a zebra crossing.","es":"Hay un paso de cebra."},
         {"en":"Is there a shopping centre in your village?","es":"¿Hay un centro comercial en tu pueblo?"},
         {"en":"Always cross the road carefully.","es":"Siempre cruza la carretera con cuidado."},
     ],
     "ex":[
         {"q":"Hay mucho tráfico en la ciudad.","a":"There is a lot of traffic in the city.","o":["There is a lot of traffic in the city.","There are a lot of traffic in the city.","Is there a lot of traffic.","There is lot of traffic city."]},
         {"q":"¿Hay un centro comercial en tu pueblo?","a":"Is there a shopping centre in your village?","o":["Is there a shopping centre in your village?","Are there a shopping centre?","There is a shopping centre?","Is there shopping centre your village?"]},
         {"q":"Siempre cruza la carretera con cuidado.","a":"Always cross the road carefully.","o":["Always cross the road carefully.","Always cross the road careful.","Always crossing the road.","Cross always the road."]},
         {"q":"Ciudad pequeña en inglés:","a":"Village","o":["Village","City","Town","Country"]},
     ]},
    {"id":21,"title":"Present Continuous","icon":"🏊","date":"Tuesday 18th March 2026","color":"#fd79a8",
     "grammar":"Sujeto + TO BE + verbo-ING | I am drawing | She is eating | They are running",
     "theory":[
         {"en":"I am drawing.","es":"Estoy dibujando."},
         {"en":"We are swimming.","es":"Estamos nadando."},
         {"en":"She is eating.","es":"Ella está comiendo."},
         {"en":"It isn't running.","es":"No está corriendo."},
         {"en":"Is it swimming? Yes, it is. / No, it isn't.","es":"¿Está nadando? Sí. / No."},
     ],
     "ex":[
         {"q":"Estoy dibujando.","a":"I am drawing.","o":["I am drawing.","I is drawing.","I drawing.","I am draw."]},
         {"q":"Estamos nadando.","a":"We are swimming.","o":["We are swimming.","We is swimming.","We swimming.","We am swimming."]},
         {"q":"¿Está nadando? No.","a":"No, it isn't.","o":["No, it isn't.","No, it aren't.","No, it doesn't.","No, it isn't swimming."]},
         {"q":"El león está bebiendo.","a":"The lion is drinking.","o":["The lion is drinking.","The lion are drinking.","The lion drinking.","The lion drinks."]},
     ]},
    {"id":22,"title":"Animals + Actions","icon":"🐊","date":"Thursday 6th March 2026","color":"#43e97b",
     "grammar":"Crocodile, elephant, flamingo, kangaroo, monkey, cheetah + swim, run, climb, hide",
     "theory":[
         {"en":"Crocodile → Cocodrilo","es":"Can swim and hide"},
         {"en":"Elephant → Elefante","es":"Can run and eat"},
         {"en":"Flamingo → Flamenco","es":"Can fly and run"},
         {"en":"Kangaroo → Canguro","es":"Can jump and run"},
         {"en":"Monkey → Mono | Cheetah → Guepardo","es":"Can climb, run, eat"},
     ],
     "ex":[
         {"q":"Cocodrilo en inglés:","a":"Crocodile","o":["Crocodile","Elephant","Flamingo","Kangaroo"]},
         {"q":"Canguro en inglés:","a":"Kangaroo","o":["Kangaroo","Crocodile","Flamingo","Monkey"]},
         {"q":"Trepar en inglés:","a":"Climb","o":["Climb","Swim","Run","Hide"]},
         {"q":"Esconderse en inglés:","a":"Hide","o":["Hide","Climb","Fly","Eat"]},
     ]},
    {"id":23,"title":"True / False – Reading","icon":"📖","date":"Thursday 6th March 2026","color":"#ff9a56",
     "grammar":"Read carefully and say True (T) or False (F). Always check the text!",
     "theory":[
         {"en":"There is a swimming pool in the town.","es":"Hay una piscina en el pueblo."},
         {"en":"Scarlett's favourite sport is skateboarding.","es":"El deporte favorito de Scarlett es el monopatín."},
         {"en":"Central Park is Scarlett's favourite place.","es":"Central Park es el lugar favorito de Scarlett."},
         {"en":"I go skating with my family.","es":"Voy a patinar con mi familia."},
         {"en":"You can't make the statue of liberty.","es":"No puedes hacer la estatua de la libertad."},
     ],
     "ex":[
         {"q":"There is a swimming pool near the town. (True/False?)","a":"True","o":["True","False"]},
         {"q":"Scarlett likes puzzles. (True/False?)","a":"True","o":["True","False"]},
         {"q":"Central Park is Scarlett's favourite place. (True/False?)","a":"True","o":["True","False"]},
         {"q":"I go skating with my family. (True/False?)","a":"True","o":["True","False"]},
     ]},
    {"id":24,"title":"Unit 1 – A Busy Day","icon":"📅","date":"Thursday 16th October 2025","color":"#fdcb6e",
     "grammar":"Days of the week + What time...? + Daily routines",
     "theory":[
         {"en":"Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday","es":"Domingo, Lunes, Martes, Miércoles, Jueves, Viernes, Sábado"},
         {"en":"Get up → Levantarse | Go home → Ir a casa","es":"Go to bed → Ir a la cama | Go to school → Ir al colegio"},
         {"en":"Have a shower → Ducharse | Have breakfast → Desayunar","es":"Have dinner → Cenar | Have lunch → Comer"},
         {"en":"What time does Izzy get up? It's seven o'clock.","es":"¿A qué hora se levanta Izzy? Son las siete."},
     ],
     "ex":[
         {"q":"¿Cómo se dice 'jueves'?","a":"Thursday","o":["Thursday","Tuesday","Friday","Wednesday"]},
         {"q":"¿Cómo se dice 'ducharse'?","a":"Have a shower","o":["Have a shower","Have breakfast","Go home","Get up"]},
         {"q":"What time does Eric get up? (7:30)","a":"It's half past seven.","o":["It's half past seven.","It's seven o'clock.","It's quarter past seven.","It's half past six."]},
         {"q":"¿Cómo se dice 'ir al colegio'?","a":"Go to school","o":["Go to school","Go to bed","Get up","Go home"]},
     ]},
]

# ══════════════════════════════════════════════════════════════
# DATA – CUADERNO COMPLETO
# ══════════════════════════════════════════════════════════════
NOTEBOOK = [
    {"date":"16th Oct 2025","title":"Capital Letters","icon":"✏️","color":"#a29bfe","notes":["Names, countries, languages → CAPITAL","Start of sentence → CAPITAL","I → always CAPITAL! Never write 'i'","Days and months → CAPITAL","When you write the day and month → capital"]},
    {"date":"16th Oct 2025","title":"Have some hot chocolate!","icon":"🍫","color":"#e17055","notes":["Have some hot chocolate!","You're amazing! Well done! Thank you!","There's some chocolate","When you write names and countries → capital"]},
    {"date":"21st Oct 2025","title":"Presenting Yourself","icon":"👋","color":"#ff9a56","notes":["My name's Nettie. I'm from Canada.","I'm nine years old and I speak English.","I play football and do gymnastics.","I got PE on Tuesday and Friday.","My birthday is in February. I'm from Ghana."]},
    {"date":"25th Oct 2025","title":"CAN / CAN'T + Sports","icon":"💪","color":"#00b894","notes":["There is a boy in the water. He can't swim!","I CAN swim! / I CAN'T swim.","You can do volleyball at the beach.","You need to wear a helmet for this sport.","PLAY football / DO karate / GO swimming","There are nine players in her team."]},
    {"date":"25th Oct 2025","title":"Sports Vocabulary Tree","icon":"⚽","color":"#fdcb6e","notes":["PLAY → Basketball, Football, Table Tennis","DO → Gymnastics, Karate","GO → Swimming, Running, Skateboarding","Volleyball, Baseball, Snowboarding, Handball","Cycling, Athletics, Yoga"]},
    {"date":"5th Nov 2025","title":"Joe and Amy – Daily Routine","icon":"🕐","color":"#fd79a8","notes":["I get up at ten o'clock. (Amy)","I have breakfast at half past nine. (Joe)","My favourite sport is karate. (Joe)","I have lunch at half past one. (Joe and Amy)","In the afternoon, I read books.","I play computer games. (Amy)","I go by bus at eight o'clock / half past eight"]},
    {"date":"7th Nov 2025","title":"Present Simple – 3rd Person","icon":"📝","color":"#6c5ce7","notes":["write the third person of: I/You → He/She","play→plays | write→writes | watch→watches","study→studies | fly→flies | brush→brushes","See→Sees | Call→Calls | Come→Comes","Buy→Buys | Choose→Chooses | Take→Takes"]},
    {"date":"13th Nov 2025","title":"Translate – Family & TV","icon":"🔤","color":"#e17055","notes":["Elkan learns with children.","Mary y Elba have a TV programme.","Mr. Menardre rehearses.","Daniel y Jerry play together.","They read a book. / My mum writes.","Daniel and Jerry play basketball on Saturday.","Mieres drinks water."]},
    {"date":"13th Nov 2025","title":"TV Programmes – Likes/Dislikes","icon":"📺","color":"#0984e3","notes":["She doesn't like cookery programmes.","She likes documentaries about amazing animals.","Brianna doesn't like cookery programmes.","She likes superheroes (Black Panther).","The menu and music programme she likes.","She sometimes watches TV in the evening with her dad."]},
    {"date":"16th Oct 2025","title":"Vocabulary – Clothes","icon":"👕","color":"#a29bfe","notes":["Jeans→Vaqueros | T-shirt→Camiseta | Shorts→Pantalones cortos","Shoes→Zapatos | Body→Body | Skirt→Falda","Dress→Vestido | Jumper→Jersey","Socks→Calcetines | Hat→Sombrero | Cap→Gorra","Trainers→Zapatillas de deporte | Helmet→Casco"]},
    {"date":"25th Nov 2025","title":"Interrogativos + Laura","icon":"❓","color":"#6c5ce7","notes":["What? Where? When? Which? Why? How? How many? Who?","Do + Suj + verb | Does + he/she/it + verb","Where does Laura go?","Does Laura go on Mondays? Does Laura go to the park?","How many? → Incredible!","Where + verb + compl"]},
    {"date":"27th Nov 2025","title":"What time is it?","icon":"⏰","color":"#f093fb","notes":["It's half past... (y media) ✓","It's quarter past... (y cuarto) ✓","It's ten past... (y diez)","It's twenty to eleven (once menos veinte)","It's quarter to twelve (doce menos cuarto)","It's five to ten (diez menos cinco) ✓"]},
    {"date":"13th Feb 2026","title":"There is / There are – Translate","icon":"🏘️","color":"#e84393","notes":["No hay libros en el hospital / There aren't books in the hospital","Has Juan got maths on Friday?","Is there a cinema in your city? Yes, there is.","There are dictionaries in the library.","Vocabulary: cinema→cine, country→campo/país, send→enviar, postcard→postal"]},
    {"date":"19th Feb 2026","title":"Has got / Translate","icon":"🎒","color":"#00cec9","notes":["Fred is my brother. He hasn't got the maths book in the bag.","Are there dictionaries in the library? No, there aren't.","lot of→muchos | zebra crossing→paso de cebra | arrive→llegar | river→río","Has not got = no tiene (he/she) | Have not got = no tiene (I/you/we/they)"]},
    {"date":"19th Feb 2026","title":"Junior Chef – Vocabulary","icon":"👨‍🍳","color":"#43e97b","notes":["To wear→llevar puesto | To warn→advertir | To make→hacer","To help→ayudar | Burnt→quemado | Dessert→postre","Everybody→todo el mundo | Show→espectáculo","Jake helps Drew. You can use these together.","There is one hour left. / Don't worry! / Everybody STOP!"]},
    {"date":"20th Feb 2026","title":"Present Simple Jobs (+/-/?)","icon":"💼","color":"#667eea","notes":["(+) He works in a hospital","(-) He doesn't wear a uniform","(?) Does he wear a uniform? Yes/No","She works outdoors / He helps patients","Does he work in a bank? No, he doesn't."]},
    {"date":"Various Feb 2026","title":"Song: Where do you work?","icon":"🎵","color":"#00b894","notes":["Where do you work all day? / Places of work","My mum works as an English teacher","My dad works in a restaurant. Let's go inside!","My brother is a police officer. My uncle is a firefighter.","Garages, factories, shops, places of work.","Is it near or far away? Do you work on Saturday?"]},
    {"date":"26th Feb 2026","title":"Telling the Time","icon":"⏰","color":"#f093fb","notes":["O'clock = en punto (5 o'clock = las 5)","Quarter past = y cuarto (quarter past 3 = 3:15)","Half past = y media (half past 6 = 6:30)","Quarter to = menos cuarto (quarter to 8 = 7:45)","What time does Tom get up? → He gets up at..."]},
    {"date":"27th Feb 2026","title":"Job Descriptions + Clothes","icon":"👔","color":"#4facfe","notes":["He is a nurse. He works in a hospital in London.","She is a firefighter. She helps people outdoors.","Jeans, T-shirt, Shorts, Dress, Helmet, Trainers...","He wears a blue uniform. She doesn't fly.","He works in a workshop. He repairs cars."]},
    {"date":"27th Feb 2026","title":"VOCABULARY – Jobs","icon":"👷","color":"#e17055","notes":["Builder→Albañil/a | Farmer→Granjero/a | Firefighter→Bombero/a","Nurse→Enfermero/a | Vet→Veterinario/a","Learner→Aprendiz | Pilot→Piloto/a | Singer→Cantante","Teach→Enseñar | Fly→Volar | Doctor→Médico/a","Grow plants→cultivar plantas | Turn off→apagar juego"]},
    {"date":"6th Feb 2026","title":"La ciudad – There is/are","icon":"🏙️","color":"#4facfe","notes":["Luke wants to find a postcard for his family","There is a swimming pool near here","There is a lot of traffic in the city","There is a zebra crossing","Remember! Always cross the road safely","Is there a shopping centre in your village?","There isn't a police station in my village"]},
    {"date":"6th Feb 2026","title":"Town Vocabulary","icon":"🏘️","color":"#0984e3","notes":["city→ciudad | nearby→cerca | small→pequeño","traffic→tráfico | village→pueblo pequeño","swimming pool→piscina | street→calle | road→carretera","We go shopping on Mondays"]},
    {"date":"6th Mar 2026","title":"Vocabulary – Animals","icon":"🐊","color":"#43e97b","notes":["Crocodile→Cocodrilo | Elephant→Elefante","Flamingo→Flamenco | Kangaroo→Canguro","Monkey→Mono | Cheetah→Guepardo","Swim→Nadar | Run→Correr | Climb→Trepar","Hide→Esconderse | Eat→Comer | Fly→Volar"]},
    {"date":"6th Mar 2026","title":"True/False – Scarlett","icon":"📖","color":"#ff9a56","notes":["Thursday 6th March – True or False","1: You can mark it wrong. F","2: There is a swimming pool in the town. V","3: Scarlett likes puzzles. V","Central Park is Scarlett favourite place. V","I go skating with my friends and family."]},
    {"date":"18th Mar 2026","title":"Present Continuous","icon":"🏊","color":"#fd79a8","notes":["Tuesday 18th March – PRESENT CONTINUOUS","To be + verb-ing = acción en progreso ahora","I am drawing / We are swimming / She is eating","Is it swimming? Yes, it is. / No, it isn't.","It isn't running. / It's swimming.","Affirmative: I am / you-we-they ARE / he-she-it IS + verb-ing","Negative: I'm not / he isn't / they aren't + verb-ing","The lion is drinking. Are there four pens under the table?"]},
]

FILL_QUESTIONS = [
    {"sentence":"He ___ football every day.","blank":"plays","opts":["play","plays","playing","is play"],"hint":"3ª persona del singular"},
    {"sentence":"She ___ like cookery programmes.","blank":"doesn't","opts":["don't","doesn't","isn't","not"],"hint":"Negativo she/he/it"},
    {"sentence":"___ he wear a uniform?","blank":"Does","opts":["Do","Does","Is","Has"],"hint":"Pregunta 3ª persona"},
    {"sentence":"I ___ swim but I can't fly.","blank":"can","opts":["can","could","am","do"],"hint":"Habilidad presente"},
    {"sentence":"It's quarter ___ three.","blank":"past","opts":["past","to","of","at"],"hint":"Y cuarto"},
    {"sentence":"There ___ a hospital in my town.","blank":"is","opts":["is","are","have","has"],"hint":"Singular"},
    {"sentence":"I ___ gymnastics on Mondays.","blank":"do","opts":["do","go","play","make"],"hint":"DO + gymnastics"},
    {"sentence":"She ___ in a hospital. She's a nurse.","blank":"works","opts":["work","works","is work","working"],"hint":"3ª persona"},
    {"sentence":"He ___ got a blue uniform.","blank":"has","opts":["has","have","got","is"],"hint":"Has got = tiene"},
    {"sentence":"___ there a cinema in your town?","blank":"Is","opts":["Is","Are","Has","Does"],"hint":"There is → pregunta"},
    {"sentence":"They ___ basketball on Saturdays.","blank":"play","opts":["plays","play","playing","do play"],"hint":"They/I/you/we → sin -s"},
    {"sentence":"What time does Tom ___ up?","blank":"get","opts":["gets","get","got","getting"],"hint":"Does + verbo base"},
    {"sentence":"I go to school ___ bus.","blank":"by","opts":["by","in","on","with"],"hint":"Medio de transporte"},
    {"sentence":"She ___ documentaries about animals.","blank":"likes","opts":["like","likes","is like","liking"],"hint":"Like + 3ª persona"},
    {"sentence":"It's twenty ___ eleven.","blank":"to","opts":["to","past","of","before"],"hint":"Menos → TO"},
    {"sentence":"I ___ drawing. (right now)","blank":"am","opts":["am","is","are","be"],"hint":"Present Continuous I"},
    {"sentence":"She ___ eating lunch now.","blank":"is","opts":["is","am","are","be"],"hint":"Present Continuous she"},
    {"sentence":"___ you got PE today?","blank":"Have","opts":["Have","Has","Do","Are"],"hint":"Have got – pregunta"},
]

# ══════════════════════════════════════════════════════════════
# SESSION STATE
# ══════════════════════════════════════════════════════════════
DEFAULTS = {
    "page":"home","sub":"menu","score":0,"streak":0,
    "lesson_id":None,"lesson_tab":"theory","ex_idx":0,
    "ex_answered":False,"ex_correct":False,"hearts":3,"shuffled_opts":[],
    "game_mode":None,"game_qs":[],"game_idx":0,"game_score":0,
    "game_answered":False,"game_correct":False,"game_opts":[],
    "mem_cards":[],"mem_flipped":[],"mem_matched":[],"mem_moves":0,
    "hg_word":"","hg_hint":"","hg_guessed":[],"hg_wrong":0,
    "ag_words":[],"ag_idx":0,"ag_score":0,"ag_answered":False,
    "sb_phrases":[],"sb_idx":0,"sb_score":0,"sb_selected":[],"sb_answered":False,
    "fq_qs":[],"fq_idx":0,"fq_score":0,"fq_answered":False,
}
for k,v in DEFAULTS.items():
    if k not in st.session_state: st.session_state[k] = v

def go(page, sub="menu"):
    st.session_state.page = page
    st.session_state.sub = sub

def rnd(lst): l=list(lst); random.shuffle(l); return l

# ══════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════
total_words = sum(len(v) for v in VOCAB.values())

with st.sidebar:
    st.markdown("""
    <div style="text-align:center;padding:1.2rem 0 0.8rem">
      <div style="font-size:3rem">📚</div>
      <div class="nav-title">English con Cuaderno</div>
      <div style="font-size:0.78rem;color:#aaa;margin-top:0.2rem">¡Aprende con tus apuntes! 🌟</div>
    </div>""", unsafe_allow_html=True)

    st.markdown(f"""
    <div style="display:flex;justify-content:center;gap:0.3rem;flex-wrap:wrap;margin:0 0 1rem">
      <span class="badge" style="background:#FFC800">⭐ {st.session_state.score}</span>
      <span class="badge" style="background:#FF9600">🔥 {st.session_state.streak}</span>
      <span class="badge" style="background:#1CB0F6">📝 {total_words}</span>
    </div>""", unsafe_allow_html=True)

    pages = [
        ("🏠 Inicio","home","#58CC02"),
        ("📖 Lecciones","lessons","#667eea"),
        ("📝 Vocabulario","vocab","#1CB0F6"),
        ("🎮 Juegos","games","#f093fb"),
        ("📒 Cuaderno","notebook","#fdcb6e"),
    ]
    for label, key, color in pages:
        active = st.session_state.page == key
        st.markdown(f"""
        <div style="margin-bottom:0.3rem">""", unsafe_allow_html=True)
        if st.button(label, key=f"nav_{key}", use_container_width=True,
                     type="primary" if active else "secondary"):
            go(key); st.rerun()

# ══════════════════════════════════════════════════════════════
# HELPERS
# ══════════════════════════════════════════════════════════════
def prog(pct, color="#58CC02"):
    st.markdown(f"""<div class="prog-outer"><div class="prog-inner" style="background:{color};width:{min(pct,100):.0f}%"></div></div>""", unsafe_allow_html=True)

def badge_html(text, color):
    return f'<span class="badge" style="background:{color}">{text}</span>'

def fb(ok, msg):
    cls = "feedback-ok" if ok else "feedback-ko"
    st.markdown(f'<div class="{cls}">{msg}</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# HOME
# ══════════════════════════════════════════════════════════════
def page_home():
    st.markdown(f"""
    <div style="text-align:center;padding:1.5rem 0 1rem">
      <div style="font-size:3.5rem">📚</div>
      <div class="hero-title">English con Cuaderno</div>
      <div class="hero-sub">¡Aprende inglés con tus apuntes de clase! 🌟</div>
    </div>""", unsafe_allow_html=True)

    c1,c2,c3,c4 = st.columns(4)
    for col,icon,val,lbl,clr in [
        (c1,"⭐",st.session_state.score,"Puntos","#FFC800"),
        (c2,"🔥",st.session_state.streak,"Racha","#FF9600"),
        (c3,"📝",total_words,"Palabras","#1CB0F6"),
        (c4,"📖",len(LESSONS),"Lecciones","#58CC02"),
    ]:
        with col:
            st.markdown(f"""<div class="stat-card">
              <div style="font-size:1.8rem">{icon}</div>
              <div class="stat-val" style="color:{clr}">{val}</div>
              <div class="stat-label">{lbl}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)

    # Accesos rápidos
    cards_row1 = [
        ("📖","Lecciones","Teoría + ejercicios","linear-gradient(135deg,#667eea,#764ba2)","lessons"),
        ("🎮","Juegos","Mini-juegos","linear-gradient(135deg,#f093fb,#f5576c)","games"),
        ("📝","Vocabulario","Todas las palabras","linear-gradient(135deg,#4facfe,#00f2fe)","vocab"),
        ("📒","Cuaderno","Resumen de clase","linear-gradient(135deg,#43e97b,#38f9d7)","notebook"),
        ("🔤","ES → EN","Juego vocabulario","linear-gradient(135deg,#e17055,#d63031)","games_esn"),
        ("🔢","Números","Aprende números","linear-gradient(135deg,#fdcb6e,#e17055)","lessons_num"),
    ]
    cols = st.columns(3)
    for i,(icon,title,desc,bg,dest) in enumerate(cards_row1):
        with cols[i%3]:
            st.markdown(f"""
            <div class="sport-card" style="background:{bg};margin-bottom:0.6rem">
              <div class="sc-icon">{icon}</div>
              <h3>{title}</h3>
              <p>{desc}</p>
            </div>""", unsafe_allow_html=True)
            if st.button(f"Ir →", key=f"hc_{i}", use_container_width=True):
                if dest == "games_esn": start_game("es_en"); go("games","quiz"); st.rerun()
                elif dest == "lessons_num":
                    l = next(x for x in LESSONS if "Number" in x["title"])
                    open_lesson(l["id"]); st.rerun()
                else: go(dest); st.rerun()

    st.markdown("---")
    st.markdown("### 📅 Últimas lecciones")
    for l in list(reversed(LESSONS))[:6]:
        ca,cb = st.columns([5,1])
        with ca:
            st.markdown(f"""
            <div class="lesson-item" style="border-left:5px solid {l['color']}">
              <span style="font-size:1.8rem">{l['icon']}</span>
              <div>
                <div style="font-weight:800;font-size:0.95rem">{l['title']}</div>
                <div style="color:#aaa;font-size:0.78rem">📅 {l['date']} · ✏️ {len(l['ex'])} ejercicios</div>
                <div style="font-size:0.82rem;color:#555;margin-top:0.1rem">
                  🇬🇧 {l['theory'][0]['en'][:50]}… → 🇪🇸 <em>{l['theory'][0]['es'][:40]}…</em>
                </div>
              </div>
            </div>""", unsafe_allow_html=True)
        with cb:
            if st.button("▶", key=f"hl_{l['id']}", use_container_width=True, type="primary"):
                open_lesson(l["id"]); go("lessons","detail"); st.rerun()

# ══════════════════════════════════════════════════════════════
# VOCABULARY
# ══════════════════════════════════════════════════════════════
def page_vocab():
    st.markdown(f"## 📝 Vocabulario del Cuaderno {badge_html(total_words, '#1CB0F6')}", unsafe_allow_html=True)
    c1,c2 = st.columns([3,1])
    with c1: search = st.text_input("", placeholder="🔍 Buscar palabra...", key="vs", label_visibility="collapsed")
    with c2:
        topics = ["Todos"] + list(VOCAB.keys())
        topic = st.selectbox("", topics, key="vt", label_visibility="collapsed")

    total_shown = 0
    for t,words in VOCAB.items():
        if topic != "Todos" and t != topic: continue
        filtered = [(en,es) for en,es in words if not search or search.lower() in en.lower() or search.lower() in es.lower()]
        if not filtered: continue
        total_shown += len(filtered)
        st.markdown(f"""<div class="duo-card">
          <div style="font-weight:900;font-size:1rem;color:#1CB0F6;margin-bottom:0.7rem">
            {t} {badge_html(len(filtered),'#1CB0F6')}
          </div>""", unsafe_allow_html=True)
        html = ""
        for en,es in filtered:
            html += f"""<div class="vocab-row">
              <span class="vocab-en">🇬🇧 {en}</span>
              <span class="vocab-es">🇪🇸 {es}</span>
            </div>"""
        st.markdown(html + "</div>", unsafe_allow_html=True)

    if not total_shown:
        st.info("Sin resultados para tu búsqueda.")

# ══════════════════════════════════════════════════════════════
# LESSONS
# ══════════════════════════════════════════════════════════════
def open_lesson(lid):
    l = next(x for x in LESSONS if x["id"]==lid)
    st.session_state.lesson_id = lid
    st.session_state.lesson_tab = "theory"
    st.session_state.ex_idx = 0
    st.session_state.ex_answered = False
    st.session_state.hearts = 3
    st.session_state.shuffled_opts = rnd(l["ex"][0]["o"]) if l["ex"] else []
    st.session_state.sub = "detail"

def page_lessons():
    if st.session_state.sub == "detail" and st.session_state.lesson_id is not None:
        render_lesson_detail(); return

    st.markdown(f"## 📖 Lecciones del Cuaderno {badge_html(len(LESSONS),'#58CC02')}", unsafe_allow_html=True)

    # Search/filter
    search = st.text_input("", placeholder="🔍 Buscar lección...", key="ls_search", label_visibility="collapsed")

    for l in LESSONS:
        if search and search.lower() not in l["title"].lower() and search.lower() not in l["date"].lower():
            continue
        ca,cb = st.columns([5,1])
        with ca:
            st.markdown(f"""
            <div class="lesson-item" style="border-left:6px solid {l['color']}">
              <div style="font-size:2.2rem;min-width:2.5rem;text-align:center">{l['icon']}</div>
              <div style="flex:1">
                <div style="font-weight:900;font-size:1rem">{l['title']}</div>
                <div style="color:#aaa;font-size:0.78rem">📅 {l['date']} · ✏️ {len(l['ex'])} ejercicios</div>
                <div style="font-size:0.8rem;color:#888;margin-top:0.1rem;font-style:italic">{l['grammar'][:60]}…</div>
              </div>
              <span style="background:{l['color']};color:white;border-radius:50px;padding:0.2rem 0.8rem;font-weight:800;font-size:0.8rem">▶</span>
            </div>""", unsafe_allow_html=True)
        with cb:
            if st.button("Iniciar", key=f"ls_{l['id']}", use_container_width=True, type="primary"):
                open_lesson(l["id"]); st.rerun()

def render_lesson_detail():
    l = next((x for x in LESSONS if x["id"]==st.session_state.lesson_id), None)
    if not l: go("lessons","menu"); st.rerun(); return

    if st.button("← Todas las lecciones", type="secondary"):
        go("lessons","menu"); st.rerun()

    st.markdown(f"""
    <div class="duo-card" style="border-top:6px solid {l['color']};margin-bottom:0.8rem">
      <div style="display:flex;align-items:center;gap:0.8rem">
        <span style="font-size:2.5rem">{l['icon']}</span>
        <div>
          <div style="font-size:1.3rem;font-weight:900">{l['title']}</div>
          <div style="color:#aaa;font-size:0.82rem">📅 {l['date']}</div>
        </div>
      </div>
    </div>""", unsafe_allow_html=True)

    t1,t2 = st.columns(2)
    with t1:
        if st.button("📚 Teoría", use_container_width=True,
                     type="primary" if st.session_state.lesson_tab=="theory" else "secondary"):
            st.session_state.lesson_tab = "theory"; st.rerun()
    with t2:
        if st.button("✏️ Ejercicios", use_container_width=True,
                     type="primary" if st.session_state.lesson_tab=="exercises" else "secondary"):
            st.session_state.lesson_tab = "exercises"
            st.session_state.ex_idx = 0; st.session_state.ex_answered = False
            st.session_state.hearts = 3
            st.session_state.shuffled_opts = rnd(l["ex"][0]["o"]) if l["ex"] else []
            st.rerun()

    if st.session_state.lesson_tab == "theory":
        st.markdown(f'<div class="grammar-box">📐 {l["grammar"]}</div>', unsafe_allow_html=True)
        for t in l["theory"]:
            ca,cb = st.columns(2)
            with ca: st.markdown(f'<div class="theory-en">🇬🇧 {t["en"]}</div><div style="height:0.3rem"></div>', unsafe_allow_html=True)
            with cb: st.markdown(f'<div class="theory-es">🇪🇸 {t["es"]}</div><div style="height:0.3rem"></div>', unsafe_allow_html=True)
    else:
        ex_list = l["ex"]; idx = st.session_state.ex_idx
        if idx >= len(ex_list):
            st.markdown("""<div class="duo-card" style="text-align:center;padding:2rem">
              <div style="font-size:4rem">🎉</div>
              <h2 style="color:#58CC02">¡Lección completada!</h2>
              <p style="color:#888">Excelente trabajo</p>
            </div>""", unsafe_allow_html=True)
            if st.button("🔄 Repetir", use_container_width=True, type="primary"):
                st.session_state.ex_idx=0; st.session_state.ex_answered=False
                st.session_state.hearts=3; st.session_state.shuffled_opts=rnd(ex_list[0]["o"]); st.rerun()
            return

        ex = ex_list[idx]
        prog((idx/len(ex_list))*100, l["color"])
        ca,cb,cc = st.columns(3)
        ca.markdown(badge_html(f"✏️ {idx+1}/{len(ex_list)}",l["color"]), unsafe_allow_html=True)
        cb.markdown(badge_html(f"❤️ {st.session_state.hearts}","#dc3545"), unsafe_allow_html=True)
        cc.markdown(badge_html(f"⭐ {st.session_state.score}","#FFC800"), unsafe_allow_html=True)

        st.markdown(f"""
        <div class="duo-card" style="text-align:center;margin:0.8rem 0;border-top:4px solid {l['color']}">
          <div style="color:#aaa;font-size:0.85rem;font-weight:700">Traduce al inglés:</div>
          <div style="font-size:1.2rem;font-weight:900;margin-top:0.4rem">🇪🇸 {ex['q']}</div>
        </div>""", unsafe_allow_html=True)

        if not st.session_state.shuffled_opts:
            st.session_state.shuffled_opts = rnd(ex["o"])

        answered = st.session_state.ex_answered
        for opt in st.session_state.shuffled_opts:
            if answered:
                if opt == ex["a"]: st.markdown(f'<div class="opt-correct">✅ {opt}</div>', unsafe_allow_html=True)
                else: st.markdown(f'<div class="opt-wrong">❌ {opt}</div>', unsafe_allow_html=True)
            else:
                if st.button(opt, key=f"eo_{idx}_{opt}", use_container_width=True):
                    st.session_state.ex_answered = True
                    if opt == ex["a"]:
                        st.session_state.ex_correct = True
                        st.session_state.score += 10; st.session_state.streak += 1
                    else:
                        st.session_state.ex_correct = False
                        st.session_state.hearts = max(0, st.session_state.hearts-1)
                        st.session_state.streak = 0
                    st.rerun()

        if answered:
            if st.session_state.ex_correct: fb(True, f"✅ ¡Correcto! +10 pts 🎉")
            else: fb(False, f"❌ La respuesta era: **{ex['a']}**")
            if st.button("Siguiente →", use_container_width=True, type="primary"):
                st.session_state.ex_idx += 1; st.session_state.ex_answered = False
                if st.session_state.ex_idx < len(ex_list):
                    st.session_state.shuffled_opts = rnd(ex_list[st.session_state.ex_idx]["o"])
                st.rerun()

# ══════════════════════════════════════════════════════════════
# NOTEBOOK
# ══════════════════════════════════════════════════════════════
def page_notebook():
    st.markdown(f"## 📒 Cuaderno de Clase {badge_html(len(NOTEBOOK),'#fdcb6e')}", unsafe_allow_html=True)
    for e in NOTEBOOK:
        st.markdown(f"""
        <div class="duo-card" style="border-left:6px solid {e['color']}">
          <div style="display:flex;align-items:center;gap:0.6rem;margin-bottom:0.3rem">
            <span style="font-size:1.6rem">{e['icon']}</span>
            <div>
              <div style="font-weight:900;font-size:0.95rem">{e['title']}</div>
              <div style="color:#aaa;font-size:0.76rem">📅 {e['date']}</div>
            </div>
          </div>
          <div class="nb-notes">{'<br>'.join('• '+n for n in e['notes'])}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("""<div class="duo-card" style="background:linear-gradient(135deg,#e8f4fd,#d0ecff);border:2px dashed #1CB0F6">
      <h4 style="margin:0;color:#1CB0F6">💡 ¿Nuevas páginas del cuaderno?</h4>
      <p style="margin:0.4rem 0 0;color:#555;font-size:0.9rem">Manda fotos y se añade todo automáticamente. ¡La app es modular! 🚀</p>
    </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# GAMES MENU
# ══════════════════════════════════════════════════════════════
def page_games():
    sub = st.session_state.sub
    if sub == "quiz":     game_quiz(); return
    if sub == "memory":   game_memory(); return
    if sub == "hangman":  game_hangman(); return
    if sub == "anagram":  game_anagram(); return
    if sub == "sentence": game_sentence(); return
    if sub == "fill":     game_fill(); return

    st.markdown("## 🎮 Juegos de Práctica")

    st.markdown(f"""<div style="font-weight:900;color:#888;font-size:0.8rem;letter-spacing:0.08em;margin:0.5rem 0 0.3rem">🔤 VOCABULARIO</div>""", unsafe_allow_html=True)
    g1 = st.columns(3)
    game_cards_v = [
        ("🔤","ES → EN","Español a inglés","linear-gradient(135deg,#f093fb,#f5576c)","es_en"),
        ("🔗","EN → ES","Inglés a español","linear-gradient(135deg,#4facfe,#00f2fe)","en_es"),
        ("🧠","Memory","Empareja cartas","linear-gradient(135deg,#43e97b,#38f9d7)","memory"),
        ("🪄","Ahorcado","Adivina la palabra","linear-gradient(135deg,#00cec9,#00b894)","hangman"),
        ("🔀","Anagrama","Ordena las letras","linear-gradient(135deg,#fdcb6e,#e17055)","anagram"),
    ]
    for i,(icon,title,desc,bg,mode) in enumerate(game_cards_v):
        with g1[i%3]:
            st.markdown(f"""<div class="sport-card" style="background:{bg}">
              <div class="sc-icon">{icon}</div><h3>{title}</h3><p>{desc}</p>
            </div>""", unsafe_allow_html=True)
            if st.button(f"Jugar", key=f"gv_{mode}", use_container_width=True):
                if mode in ("es_en","en_es"): start_game(mode)
                elif mode=="memory": init_memory()
                elif mode=="hangman": init_hangman()
                elif mode=="anagram": init_anagram()
                st.rerun()

    st.markdown(f"""<div style="font-weight:900;color:#888;font-size:0.8rem;letter-spacing:0.08em;margin:1rem 0 0.3rem">📝 FRASES Y GRAMÁTICA</div>""", unsafe_allow_html=True)
    g2 = st.columns(3)
    game_cards_g = [
        ("🧩","Construye frases","Ordena palabras","linear-gradient(135deg,#667eea,#764ba2)","sentence"),
        ("✍️","Rellena el hueco","Completa la frase","linear-gradient(135deg,#00b894,#00cec9)","fill"),
    ]
    for i,(icon,title,desc,bg,mode) in enumerate(game_cards_g):
        with g2[i]:
            st.markdown(f"""<div class="sport-card" style="background:{bg}">
              <div class="sc-icon">{icon}</div><h3>{title}</h3><p>{desc}</p>
            </div>""", unsafe_allow_html=True)
            if st.button(f"Jugar", key=f"gg_{mode}", use_container_width=True):
                if mode=="sentence": init_sentence()
                elif mode=="fill": init_fill()
                st.rerun()

    st.markdown(f"""
    <div class="duo-card" style="text-align:center;margin-top:1rem">
      <div style="font-size:2rem">⭐</div>
      <div style="font-size:1.3rem;font-weight:900">Puntuación total: {st.session_state.score}</div>
      <div style="color:#888;font-size:0.9rem">🔥 Racha actual: {st.session_state.streak}</div>
    </div>""", unsafe_allow_html=True)

# ── QUIZ ──────────────────────────────────────────────────────
def start_game(mode):
    all_w = [(en,es) for wds in VOCAB.values() for en,es in wds]
    sl = rnd(all_w)[:12]
    all_es=[w[1] for w in all_w]; all_en=[w[0] for w in all_w]
    qs=[]
    for en,es in sl:
        if mode=="es_en":
            wg=rnd([x for x in all_en if x!=en])[:3]
            qs.append({"question":f"🇪🇸 {es}","answer":en,"opts":rnd([en]+wg),"en":en})
        else:
            wg=rnd([x for x in all_es if x!=es])[:3]
            qs.append({"question":f"🇬🇧 {en}","answer":es,"opts":rnd([es]+wg),"en":en})
    st.session_state.game_mode=mode; st.session_state.game_qs=qs
    st.session_state.game_idx=0; st.session_state.game_score=0
    st.session_state.game_answered=False; st.session_state.game_opts=list(qs[0]["opts"])
    st.session_state.sub="quiz"

def game_quiz():
    if st.button("← Salir", type="secondary"): go("games"); st.rerun()
    qs=st.session_state.game_qs; idx=st.session_state.game_idx
    mode=st.session_state.game_mode
    icon="🔤 ES→EN" if mode=="es_en" else "🔗 EN→ES"
    color="#f093fb" if mode=="es_en" else "#4facfe"

    if idx>=len(qs):
        pct=round((st.session_state.game_score/len(qs))*100)
        em="🏆" if pct>=80 else "👍" if pct>=60 else "💪"
        msg="¡Excelente!" if pct>=80 else "¡Bien hecho!" if pct>=60 else "¡Sigue practicando!"
        st.markdown(f"""<div class="duo-card" style="text-align:center;padding:2.5rem;border-top:6px solid {color}">
          <div style="font-size:4rem">{em}</div><h2>{msg}</h2>
          <p style="font-size:1.4rem;font-weight:900">{st.session_state.game_score}/{len(qs)} ({pct}%)</p>
        </div>""", unsafe_allow_html=True)
        c1,c2=st.columns(2)
        with c1:
            if st.button("🔄 Jugar de nuevo", use_container_width=True, type="primary"): start_game(mode); st.rerun()
        with c2:
            if st.button("🏠 Volver", use_container_width=True): go("games"); st.rerun()
        return

    q=qs[idx]; pct=(idx/len(qs))*100
    prog(pct, color)
    ca,cb=st.columns(2)
    ca.markdown(badge_html(f"{icon} {idx+1}/{len(qs)}",color), unsafe_allow_html=True)
    cb.markdown(badge_html(f"✅ {st.session_state.game_score}","#58CC02"), unsafe_allow_html=True)

    st.markdown(f"""<div class="duo-card" style="text-align:center;margin:0.8rem 0;border-top:4px solid {color}">
      <div style="color:#aaa;font-size:0.82rem;font-weight:700">Traduce:</div>
      <div style="font-size:1.4rem;font-weight:900;margin-top:0.4rem">{q['question']}</div>
    </div>""", unsafe_allow_html=True)

    answered=st.session_state.game_answered
    for opt in st.session_state.game_opts:
        if answered:
            if opt==q["answer"]: st.markdown(f'<div class="opt-correct">✅ {opt}</div>', unsafe_allow_html=True)
            else: st.markdown(f'<div class="opt-wrong">❌ {opt}</div>', unsafe_allow_html=True)
        else:
            if st.button(opt, key=f"qo_{idx}_{opt}", use_container_width=True):
                st.session_state.game_answered=True
                st.session_state.game_correct=(opt==q["answer"])
                if st.session_state.game_correct: st.session_state.game_score+=1; st.session_state.score+=5; st.session_state.streak+=1
                else: st.session_state.streak=0
                st.rerun()

    if answered:
        if st.session_state.game_correct: fb(True,"✅ ¡Correcto! +5 pts")
        else: fb(False,f"❌ Era: **{q['answer']}**")
        if st.button("Siguiente →", use_container_width=True, type="primary"):
            st.session_state.game_idx+=1; st.session_state.game_answered=False
            if st.session_state.game_idx<len(qs): st.session_state.game_opts=list(qs[st.session_state.game_idx]["opts"])
            st.rerun()

# ── MEMORY ────────────────────────────────────────────────────
def init_memory():
    all_w=[(en,es) for wds in VOCAB.values() for en,es in wds]
    pairs=rnd(all_w)[:8]
    cards=[]
    for i,(en,es) in enumerate(pairs):
        cards.append({"id":i*2,"text":en,"pair":i,"type":"en"})
        cards.append({"id":i*2+1,"text":es,"pair":i,"type":"es"})
    st.session_state.mem_cards=rnd(cards)
    st.session_state.mem_flipped=[]; st.session_state.mem_matched=[]; st.session_state.mem_moves=0
    st.session_state.sub="memory"

def game_memory():
    if st.button("← Salir",type="secondary"): go("games"); st.rerun()
    st.markdown("## 🧠 Memory – Empareja cartas")
    cards=st.session_state.mem_cards; matched=st.session_state.mem_matched; flipped=st.session_state.mem_flipped

    if len(matched)==len(cards) and len(cards)>0:
        st.balloons()
        st.markdown(f"""<div class="duo-card" style="text-align:center;padding:2rem;border-top:6px solid #43e97b">
          <div style="font-size:3.5rem">🏆</div><h2 style="color:#43e97b">¡Todas las parejas!</h2>
          <p>Movimientos: <strong>{st.session_state.mem_moves}</strong></p>
        </div>""", unsafe_allow_html=True)
        if st.button("🔄 Nueva partida",use_container_width=True,type="primary"): init_memory(); st.rerun()
        return

    ca,cb=st.columns(2)
    ca.markdown(f"🔁 Movimientos: **{st.session_state.mem_moves}**")
    cb.markdown(f"✅ Parejas: **{len(matched)//2}/{len(cards)//2}**")

    cols=st.columns(4)
    for i,card in enumerate(cards):
        with cols[i%4]:
            is_matched=card["id"] in matched; is_flipped=card["id"] in flipped
            if is_matched:
                st.markdown(f"""<div style="background:#d4edda;border:3px solid #28a745;border-radius:14px;
                  padding:0.7rem;text-align:center;font-weight:800;min-height:65px;
                  display:flex;align-items:center;justify-content:center;font-size:0.82rem;margin-bottom:0.4rem;word-break:break-word">
                  ✅ {card['text']}</div>""", unsafe_allow_html=True)
            elif is_flipped:
                bg="#e8f4fd" if card["type"]=="en" else "#edfce8"
                border="#1CB0F6" if card["type"]=="en" else "#58CC02"
                st.markdown(f"""<div style="background:{bg};border:3px solid {border};border-radius:14px;
                  padding:0.7rem;text-align:center;font-weight:800;min-height:65px;
                  display:flex;align-items:center;justify-content:center;font-size:0.82rem;margin-bottom:0.4rem;word-break:break-word">
                  {card['text']}</div>""", unsafe_allow_html=True)
            else:
                if st.button("❓", key=f"m_{card['id']}", use_container_width=True):
                    if len(flipped)<2 and card["id"] not in flipped:
                        flipped.append(card["id"]); st.session_state.mem_flipped=flipped
                        if len(flipped)==2:
                            st.session_state.mem_moves+=1
                            c1n=next(c for c in cards if c["id"]==flipped[0])
                            c2n=next(c for c in cards if c["id"]==flipped[1])
                            if c1n["pair"]==c2n["pair"] and c1n["type"]!=c2n["type"]:
                                matched.extend(flipped); st.session_state.mem_matched=matched
                                st.session_state.score+=10; st.session_state.streak+=1
                            st.session_state.mem_flipped=[]
                        st.rerun()

# ── HANGMAN ───────────────────────────────────────────────────
def init_hangman():
    all_w=[(en,es) for wds in VOCAB.values() for en,es in wds if 4<=len(en)<=10 and " " not in en]
    pick=random.choice(all_w)
    st.session_state.hg_word=pick[0].lower(); st.session_state.hg_hint=pick[1]
    st.session_state.hg_guessed=[]; st.session_state.hg_wrong=0
    st.session_state.sub="hangman"

def game_hangman():
    if not st.session_state.hg_word: init_hangman()
    if st.button("← Salir",type="secondary"): go("games"); st.rerun()
    st.markdown("## 🪄 Ahorcado")

    word=st.session_state.hg_word; guessed=st.session_state.hg_guessed
    wrong=st.session_state.hg_wrong; MAX=6
    display=" ".join(c if c in guessed else "＿" for c in word)
    won=all(c in guessed for c in word); lost=wrong>=MAX

    stages=["  ╔══════\n  ║      |\n  ║\n  ║\n  ║\n  ╚══════",
             "  ╔══════\n  ║      |\n  ║      😐\n  ║\n  ║\n  ╚══════",
             "  ╔══════\n  ║      |\n  ║      😵\n  ║      |\n  ║\n  ╚══════",
             "  ╔══════\n  ║      |\n  ║      😵\n  ║     /|\n  ║\n  ╚══════",
             "  ╔══════\n  ║      |\n  ║      😵\n  ║     /|\\\n  ║\n  ╚══════",
             "  ╔══════\n  ║      |\n  ║      😵\n  ║     /|\\\n  ║     /\n  ╚══════",
             "  ╔══════\n  ║      |\n  ║      😵\n  ║     /|\\\n  ║     / \\\n  ╚══════"]
    st.code(stages[min(wrong,6)],language=None)
    st.markdown(f'<div class="hangman-display">{display}</div>', unsafe_allow_html=True)
    st.markdown(f"""<div style="background:#fff8e1;border-radius:12px;padding:0.7rem;text-align:center;
      color:#856404;font-weight:700;border-left:4px solid #FFC800;margin:0.5rem 0">
      💡 Pista: {st.session_state.hg_hint} &nbsp;|&nbsp; Intentos restantes: <strong>{MAX-wrong}</strong>
    </div>""", unsafe_allow_html=True)

    if won:
        st.session_state.score+=20; st.session_state.streak+=1
        fb(True,f"✅ ¡Correcto! La palabra era **{word.upper()}** +20 pts 🎉")
        if st.button("🔄 Nueva palabra",use_container_width=True,type="primary"): init_hangman(); st.rerun()
    elif lost:
        st.session_state.streak=0
        fb(False,f"😢 Era: **{word.upper()}**")
        if st.button("🔄 Intentar de nuevo",use_container_width=True,type="primary"): init_hangman(); st.rerun()
    else:
        alpha=list("abcdefghijklmnopqrstuvwxyz")
        cols=st.columns(9)
        for i,lt in enumerate(alpha):
            used=lt in guessed; is_wrong=used and lt not in word
            with cols[i%9]:
                if used:
                    bg="#f8d7da" if is_wrong else "#d4edda"
                    bd="#dc3545" if is_wrong else "#28a745"
                    st.markdown(f"""<div style="background:{bg};border:2px solid {bd};border-radius:8px;
                      width:36px;height:36px;display:flex;align-items:center;justify-content:center;
                      font-weight:800;font-size:0.88rem;margin:2px">{lt}</div>""", unsafe_allow_html=True)
                else:
                    if st.button(lt, key=f"hg_{lt}"):
                        guessed.append(lt); st.session_state.hg_guessed=guessed
                        if lt not in word: st.session_state.hg_wrong+=1; st.session_state.streak=0
                        st.rerun()

# ── ANAGRAM ───────────────────────────────────────────────────
def init_anagram():
    all_w=[(en,es) for wds in VOCAB.values() for en,es in wds if 4<=len(en)<=12 and " " not in en]
    st.session_state.ag_words=rnd(all_w)[:10]; st.session_state.ag_idx=0
    st.session_state.ag_score=0; st.session_state.ag_answered=False
    st.session_state.sub="anagram"

def game_anagram():
    if not st.session_state.ag_words: init_anagram()
    if st.button("← Salir",type="secondary"): go("games"); st.rerun()
    st.markdown("## 🔀 Anagrama")
    words=st.session_state.ag_words; idx=st.session_state.ag_idx

    if idx>=len(words):
        pct=round((st.session_state.ag_score/len(words))*100)
        em="🎉" if pct>=80 else "👍" if pct>=60 else "🔀"
        st.markdown(f"""<div class="duo-card" style="text-align:center;padding:2rem;border-top:6px solid #fdcb6e">
          <div style="font-size:3.5rem">{em}</div>
          <h2>{"¡Anagramas resueltos!" if pct>=80 else "¡Bien!" if pct>=60 else "¡Practica más!"}</h2>
          <p style="font-size:1.3rem;font-weight:900">{st.session_state.ag_score}/{len(words)} ({pct}%)</p>
        </div>""", unsafe_allow_html=True)
        if st.button("🔄 Jugar de nuevo",use_container_width=True,type="primary"): init_anagram(); st.rerun()
        return

    en,es=words[idx]
    scrambled="".join(rnd(list(en)))
    prog((idx/len(words))*100,"#fdcb6e")
    ca,cb=st.columns(2)
    ca.markdown(badge_html(f"🔀 {idx+1}/{len(words)}","#fdcb6e"), unsafe_allow_html=True)
    cb.markdown(badge_html(f"✅ {st.session_state.ag_score}","#58CC02"), unsafe_allow_html=True)

    st.markdown(f"""<div class="duo-card" style="text-align:center;border-top:4px solid #fdcb6e">
      <div style="color:#aaa;font-size:0.82rem;font-weight:700">Letras mezcladas → ¿qué palabra es?</div>
      <div style="font-size:2.2rem;font-weight:900;letter-spacing:0.3rem;color:#fdcb6e;margin:0.5rem 0">{scrambled.upper()}</div>
      <div style="font-weight:700;color:#555">🇪🇸 Significa: <em>{es}</em></div>
    </div>""", unsafe_allow_html=True)

    if not st.session_state.ag_answered:
        ans=st.text_input("",placeholder="Escribe la palabra en inglés...",key=f"ag_{idx}",label_visibility="collapsed")
        if st.button("✅ Comprobar",use_container_width=True,type="primary"):
            st.session_state.ag_answered=True; st.session_state["ag_last"]=ans
            if ans.strip().lower()==en.lower(): st.session_state.ag_score+=1; st.session_state.score+=10; st.session_state.streak+=1
            else: st.session_state.streak=0
            st.rerun()
    else:
        ans=st.session_state.get("ag_last","")
        correct=ans.strip().lower()==en.lower()
        if correct: fb(True,f"✅ ¡Correcto! La palabra era **{en}** +10 pts")
        else: fb(False,f"❌ Era: **{en}**")
        if st.button("Siguiente →",use_container_width=True,type="primary"):
            st.session_state.ag_idx+=1; st.session_state.ag_answered=False; st.rerun()

# ── SENTENCE BUILDER ──────────────────────────────────────────
def init_sentence():
    phrases=[]
    for l in LESSONS:
        for t in l["theory"]:
            ws=t["en"].replace(".","").replace("?","").replace("!","").replace(",","").split()
            if 3<=len(ws)<=8 and len(t["en"])<60: phrases.append({"en":t["en"],"es":t["es"],"words":ws})
    st.session_state.sb_phrases=rnd(phrases)[:12]; st.session_state.sb_idx=0
    st.session_state.sb_score=0; st.session_state.sb_selected=[]; st.session_state.sb_answered=False
    st.session_state.sub="sentence"

def game_sentence():
    if not st.session_state.sb_phrases: init_sentence()
    if st.button("← Salir",type="secondary"): go("games"); st.rerun()
    st.markdown("## 🧩 Construye frases")
    phrases=st.session_state.sb_phrases; idx=st.session_state.sb_idx

    if idx>=len(phrases):
        pct=round((st.session_state.sb_score/len(phrases))*100)
        em="🏆" if pct>=80 else "👍" if pct>=60 else "💪"
        st.markdown(f"""<div class="duo-card" style="text-align:center;padding:2rem;border-top:6px solid #667eea">
          <div style="font-size:3.5rem">{em}</div>
          <h2>{"¡Frases perfectas!" if pct>=80 else "¡Muy bien!" if pct>=60 else "¡Sigue practicando!"}</h2>
          <p style="font-size:1.3rem;font-weight:900">{st.session_state.sb_score}/{len(phrases)} ({pct}%)</p>
        </div>""", unsafe_allow_html=True)
        if st.button("🔄 Jugar de nuevo",use_container_width=True,type="primary"): init_sentence(); st.rerun()
        return

    phrase=phrases[idx]
    key=f"sb_w_{idx}"
    if key not in st.session_state: st.session_state[key]=rnd(phrase["words"])
    scr=st.session_state[key]; sel=st.session_state.sb_selected

    prog((idx/len(phrases))*100,"#667eea")
    ca,cb=st.columns(2)
    ca.markdown(badge_html(f"🧩 {idx+1}/{len(phrases)}","#667eea"), unsafe_allow_html=True)
    cb.markdown(badge_html(f"✅ {st.session_state.sb_score}","#58CC02"), unsafe_allow_html=True)

    st.markdown(f"""<div class="duo-card" style="text-align:center;border-top:4px solid #667eea">
      <div style="color:#aaa;font-size:0.82rem;font-weight:700">Traduce al inglés:</div>
      <div style="font-size:1.2rem;font-weight:900;margin-top:0.4rem">🇪🇸 {phrase['es']}</div>
    </div>""", unsafe_allow_html=True)

    # Answer zone
    if sel:
        built=" ".join(scr[i] for i in sel)
        chips="".join(f'<span class="chip-sel">{scr[i]}</span>' for i in sel)
    else:
        built=""; chips="<span style='color:#ccc;font-size:0.88rem'>Toca las palabras en orden correcto...</span>"
    st.markdown(f"""<div style="background:#f8f9fb;border-radius:14px;padding:0.8rem;min-height:52px;
      border:3px solid #e0e0e0;margin:0.5rem 0;display:flex;flex-wrap:wrap;align-items:center">{chips}</div>""",
      unsafe_allow_html=True)

    if not st.session_state.sb_answered:
        # Word bank
        bank="".join(
            f'<span class="chip-avail">{w}</span>' if i not in sel else f'<span class="chip-used">{w}</span>'
            for i,w in enumerate(scr))
        st.markdown(f'<div style="margin:0.5rem 0;display:flex;flex-wrap:wrap">{bank}</div>', unsafe_allow_html=True)

        # invisible buttons for each word
        cols_w=st.columns(min(len(scr),6))
        for i,w in enumerate(scr):
            used=i in sel
            with cols_w[i%6]:
                if not used:
                    if st.button(w, key=f"sb_{idx}_{i}", use_container_width=True):
                        sel.append(i); st.session_state.sb_selected=sel; st.rerun()

        ca2,cb2=st.columns(2)
        with ca2:
            if st.button("🗑️ Borrar todo",use_container_width=True):
                st.session_state.sb_selected=[]; st.rerun()
        with cb2:
            if st.button("✅ Comprobar",use_container_width=True,type="primary"):
                if sel:
                    correct=" ".join(scr[i] for i in sel).lower()==" ".join(phrase["words"]).lower()
                    if correct: st.session_state.sb_score+=1; st.session_state.score+=10; st.session_state.streak+=1
                    else: st.session_state.streak=0
                    st.session_state.sb_answered=True; st.rerun()
    else:
        correct=built.lower()==" ".join(phrase["words"]).lower()
        if correct: fb(True,"✅ ¡Correcto! +10 pts")
        else: fb(False,f"❌ Era: **{phrase['en']}**")
        if st.button("Siguiente →",use_container_width=True,type="primary"):
            st.session_state.sb_idx+=1; st.session_state.sb_answered=False; st.session_state.sb_selected=[]; st.rerun()

# ── FILL THE BLANK ────────────────────────────────────────────
def init_fill():
    st.session_state.fq_qs=rnd(FILL_QUESTIONS); st.session_state.fq_idx=0
    st.session_state.fq_score=0; st.session_state.fq_answered=False
    st.session_state.sub="fill"

def game_fill():
    if not st.session_state.fq_qs: init_fill()
    if st.button("← Salir",type="secondary"): go("games"); st.rerun()
    st.markdown("## ✍️ Rellena el hueco")
    qs=st.session_state.fq_qs; idx=st.session_state.fq_idx

    if idx>=len(qs):
        pct=round((st.session_state.fq_score/len(qs))*100)
        em="🏆" if pct>=80 else "👍" if pct>=60 else "💪"
        st.markdown(f"""<div class="duo-card" style="text-align:center;padding:2rem;border-top:6px solid #00b894">
          <div style="font-size:3.5rem">{em}</div>
          <h2>{"¡Perfecto!" if pct>=80 else "¡Bien!" if pct>=60 else "¡Sigue practicando!"}</h2>
          <p style="font-size:1.3rem;font-weight:900">{st.session_state.fq_score}/{len(qs)} ({pct}%)</p>
        </div>""", unsafe_allow_html=True)
        if st.button("🔄 Jugar de nuevo",use_container_width=True,type="primary"): init_fill(); st.rerun()
        return

    q=qs[idx]
    prog((idx/len(qs))*100,"#00b894")
    ca,cb=st.columns(2)
    ca.markdown(badge_html(f"✍️ {idx+1}/{len(qs)}","#00b894"), unsafe_allow_html=True)
    cb.markdown(badge_html(f"✅ {st.session_state.fq_score}","#58CC02"), unsafe_allow_html=True)

    st.markdown(f"""<div class="duo-card" style="text-align:center;border-top:4px solid #00b894">
      <div style="font-size:1.3rem;font-weight:900">{q['sentence']}</div>
      <div style="color:#888;font-size:0.82rem;margin-top:0.5rem">💡 Pista: {q['hint']}</div>
    </div>""", unsafe_allow_html=True)

    key=f"fq_opts_{idx}"
    if key not in st.session_state: st.session_state[key]=rnd(q["opts"])
    opts=st.session_state[key]; answered=st.session_state.fq_answered

    for opt in opts:
        if answered:
            if opt==q["blank"]: st.markdown(f'<div class="opt-correct">✅ {opt}</div>', unsafe_allow_html=True)
            else: st.markdown(f'<div class="opt-wrong">❌ {opt}</div>', unsafe_allow_html=True)
        else:
            if st.button(opt, key=f"fq_{idx}_{opt}", use_container_width=True):
                st.session_state.fq_answered=True
                if opt==q["blank"]: st.session_state.fq_score+=1; st.session_state.score+=10; st.session_state.streak+=1
                else: st.session_state.streak=0
                st.rerun()

    if answered:
        filled=q['sentence'].replace("___",f"**{q['blank']}**")
        fb(True if st.session_state.get(f"fq_correct_{idx}",False) else True,
           f"Respuesta: {filled}")
        if st.button("Siguiente →",use_container_width=True,type="primary"):
            st.session_state.fq_idx+=1; st.session_state.fq_answered=False; st.rerun()

# ══════════════════════════════════════════════════════════════
# ROUTER
# ══════════════════════════════════════════════════════════════
p = st.session_state.page
if   p == "home":     page_home()
elif p == "vocab":    page_vocab()
elif p == "lessons":  page_lessons()
elif p == "games":    page_games()
elif p == "notebook": page_notebook()
