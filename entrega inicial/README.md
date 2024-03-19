# Trabajo Práctico Entrega Inicial

### ¿Cuál es el objetivo u objetivos que desean lograr con el Chatbot?
El objetivo principal que deseamos lograr con el Chatbot es crear un chat interactivo enfocado en el ámbito universitario para facilitarle la vida académica a los estudiantes, la idea es construir un Chatbot que se encargue de resolver funciones como, mostrar ofertas de comisión, brindar información básica sobre las materias, informa sobre aulas de cursada, dar fechas de inscripción a materias y exámenes, entre otra información útil referente a cursadas que puedan ahorrarle tiempo de búsqueda a los estudiantes. También, además de esto, la idea es que el Chatbot pueda mantener una conversación con los estudiantes interpretando lo que envían y respondiendo adecuadamente.
Para lograr esto, la idea es alimentar a la IA con información referente a estos temas, con el uso de los PDF disponibles en la universidad, tales como, el calendario académico, oferta de comisiones, entre otros, además de utilizar modelados de lenguaje para que pueda mantener una conversación.
A continuación se muestran unos mockups de una posible vista final del Chatbot construido.

![Mockup](../img/mockup.png)

### Herramientas a utilizar
Para llevar a cabo este proyecto, se emplearán diversas herramientas, en primer lugar, se utilizará el lenguaje de programación Python junto a diversas librerías. Entre estas librerías, se destacan aspose.pdf, que permite la manipulación de archivos PDF de forma eficiente. Entre sus funcionalidades se encuentra la extracción de texto, imágenes y tablas de documentos PDF, que utilizaremos para la conversión de archivos PDF a formato CSV y poder alimentar a la IA con la información recopilada de las diferentes fuentes de la universidad. La librería pandas, especializada en el análisis y manipulación de datos. Permite leer archivos CSV, limpiar y transformar los datos, y realizar análisis estadísticos. Otra librería importante es pythorch o tenserflow (junto con keras), para el aprendizaje automático que nos servirán a la hora de entrenar a esta IA. Son unas de las librerías más populares para IA y ofrecen una amplia gama de funcionalidades, incluyendo el entrenamiento de redes neuronales profundas, entre otras.

### Aplicación de la IA
La inteligencia artificial se puede encontrar en todos los aspectos de la vida moderna, ya sea en como la recomendación de series en plataformas de streaming, en asistentes virtuales para servicios, o en los mismos smartphones que la gente usa a diario. Esto se debe a que con el avance en el campo de la inteligencia artificial se ha logrado optimizar ciertas partes de la informática a través de modelos de aprendizaje. Esto implica que la tecnología moderna ha dejado de ser tan determinista y ha avanzado a ser más reaccionaria al impulso de los usuarios. Esto permite que los programas informáticos tengan respuestas personalizadas para los usuarios sin tener que estar fijamente programadas para hacer dicha tarea.
Varios ejemplos de estas aplicaciones serían:
- Atención al cliente automatizada (chatbots): Por ejemplo un negocio que utiliza tal chatbot para poder resolver la atención 
al cliente. Pudiendo así ayudar a descargar presión sobre la atención al cliente física.
- Plataformas de streaming: Es utilizada para recomendar series o películas con base en lo que el usuario haya visto en la plataforma para poder generar más engagement del usuario.
- Procesos selectivos: Se puede utilizar de manera tal que permita analizar muchos archivos de manera rápida y ágil pudiendo agilizar trabajos de gestión como leer cv para trabajos.
- Aplicaciones GPS: Se utiliza para poder generar rutas óptimas de manera rápida e inteligente pudiendo observar el tráfico en tiempo real y reaccionar al mismo.

### Onboarding
El Onboarding Digital se refiere al proceso de orientar y guiar a los clientes a través de su primera interacción con un producto o servicio de manera remota, utilizando tecnologías avanzadas como la inteligencia artificial (IA). Este proceso permite a las empresas incorporar a sus clientes al inicio de su relación con ellos en entornos digitales, a través de un proceso tecnológico seguro y simple que verifica la identidad del cliente. Es el proceso clave en el que se emplean tecnologías avanzadas para garantizar la autenticidad y seguridad de los usuarios en un registro de una plataforma. 
La tecnología IA juega un papel fundamental en el onboarding digital al permitir la mejora de la eficiencia operativa, la reducción de errores humanos y una mayor facilidad en la automatización de procesos.
Pasos para la implementación un proceso de onboarding digital
- Define los objetivos del proceso y los requisitos necesarios para lograrlos. Esto incluye:
    - La identificación de las etapas del proceso de ncorporación
    - La información que quieres recopilar de tus clientes durante el proceso
    - Los estándares de seguridad y cumplimiento que deben cumplirse
- Selección de una plataforma de verificación de Identidad y personalizar el proceso de verificación, como el escaneo de documentos adicionales o la verificación biométrica, para garantizar la autenticidad de los usuarios. Optar por un proceso de verificación más ágil puede ser preferible para no obstaculizar la experiencia del usuario. También se puede abordar preocupaciones específicas de privacidad y seguridad, permitiendo a los usuarios elegir entre diferentes métodos de verificación o ajustar el nivel de información que desean compartir.
- Garantiza la seguridad y el cumplimiento, la seguridad y el cumplimiento son aspectos críticos del proceso de onboarding digital. Utilizando medidas de seguridad robustas para proteger la información personal de tus usuarios y cumplir con las regulaciones de privacidad y protección de datos vigentes.
- Prueba y optimización continuamente, es importante realizar pruebas exhaustivas para identificar posibles problemas o áreas de mejora. Es fundamental optimizar continuamente el proceso en función de los comentarios de los usuarios y las tendencias del mercado de verificación de identidad.
- Adaptarse a los cambios, es crucial adaptar el proceso de onboarding digital a las necesidades y preferencias cambiantes de los usuarios. 
### Proceso de Onboarding Digital
- Análisis de un documento de identidad: Este paso implica verificar la autenticidad de los documentos proporcionados por el usuario durante el proceso de registro. Puede incluir la validación de DNI, pasaportes, licencias de conducir u otros documentos oficiales.
- Biometría: La biometría se utiliza para confirmar la identidad de una persona mediante características físicas o comportamientos únicos, como huellas dactilares, reconocimiento facial, iris o voz. Es una herramienta poderosa para garantizar la seguridad durante el onboarding.
- Listas AML (Anti Money Laundering): Durante el proceso de onboarding, es crucial verificar si el nuevo colaborador está en listas de personas sancionadas o relacionadas con actividades ilegales, como el lavado de activos. Las listas AML ayudan a prevenir el lavado de dinero y el financiamiento del terrorismo.

### Normativas existentes
Cuando hablamos de normativas nos referimos a las leyes y decretos establecidos en Argentina para la regular y fomentar la autenticación digital.

En Argentina no hay una ley específica que aborde el reconocimiento facial y la huella digital pero sí entran dentro  del marco de datos personales y una de las principales leyes que aborda este tema es la ley de protección de datos personales (Ley 25.326), la cual establece un marco legal para la protección de la privacidad de los individuos en relación con el tratamiento de sus datos, esta ley se aplica a todas las actividades que involucran el manejo de los mismos, ya sea en el sector público o privado. Algunos de los puntos más importantes de esta ley son:

- Principio de Consentimiento: El tratamiento de datos personales requiere el consentimiento expreso, previo e informado del titular de los datos, a menos que exista una excepción prevista por la ley.
- Principio de Finalidad: Los datos personales deben ser recopilados para fines determinados, explícitos y legítimos, y no pueden ser tratados de manera incompatible con dichos propósitos.
- Principio de Seguridad de los Datos: Se deben implementar medidas técnicas y organizativas adecuadas para garantizar la seguridad de los datos personales y protegerlos contra el acceso no autorizado, la pérdida, la alteración o la divulgación indebida.

Por el lado de las inteligencias artificiales el gobierno de la nación emitió una serie de aspectos éticos para el uso y desarrollo de las mismas. Algunos de los aspectos son:
- Equidad y no discriminación. Los actores de la Inteligencia artificial deben promover la diversidad y la inclusión,proteger la equidad y luchar contra todo tipo de discriminación.
- Seguridad y protección. Los daños no deseados (riesgos de seguridad) y las vulnerabilidades a los ataques (riesgos de protección) deben ser evitados y deben tenerse en cuenta, prevenirse y eliminarse.
- Supervisión y decisión humanas. La decisión de ceder el control a los sistemas de IA en contextos limitados sigue siendo de los seres humanos, porque un sistema de IA no puede reemplazar la responsabilidad final de los seres humanos y su obligación de rendir cuentas.

### Tipos de chatbots

- __Dumb chatbots__: Estos chatbots utilizan una línea de conversación ya predefinida la cual es manejada comúnmente por opciones en el chat. Este chatbot no requiere de una IA para que funcione de manera óptima, ya que la misma no requiere de entender el lenguaje humano. Un ejemplo de esto sería un chatbot de un banco el cual al comunicarse por WhatsApp te ofrezca un menú de opciones para elegir con números y así poder obtener una respuesta o servicio del sistema.
- __Smart chatbots__: Estos chatbots utilizan la inteligencia artificial para poder tratar de entender lo que comunique el usuario, pudiendo así generar conversaciones más naturales y ágiles. Esto también se apoya en su constante evolución al consumir la información obtenida de las mismas charlas en las que participa, pudiendo así mejorar y adaptarse a las situaciones que se le aplique. Un ejemplo de esto sería un chatbot que se utilice para ayudar a obtener información y responder preguntas del usuario tal cual las escriba, pudiendo así generar una conversación fluida y orgánica con el usuario.
- __Word spotting chatbot__: Estos chatbots vendrían a ser un intermedio entre los dos chatbots ya mencionados, ya que pueden leer la información obtenida de la comunicación con el usuario y tratar de observar palabras claves dentro del mensaje para así poder dar una respuesta ya programada, esto le permite ser más versátil que un dumb chatbot, ya que puede interpretar la información del mensaje sin tener que recurrir a un set de opciones predefinidas. Un ejemplo de esto sería un chatbot de una hotelería la cual un usuario pueda hablar con la misma y obtener información a través de la observación de lo que pida el usuario, ya que el usuario puede formular una pregunta sobre el precio de la estadía y el chatbot al leerlo ya puede ver la palabra precios y va a devolver una lista de precios.
