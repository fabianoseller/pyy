#https://blog.finxter.com/fixed-modulenotfounderror-no-module-named-tiktoken/
# pip install tiktoken

#https://pypi.org/project/tiktoken/

import tiktoken

string = """Lo que subyace al racismo algorítmico
Entre las causas apuntadas para tales situaciones, están:

Datos de entrenamiento sesgados: los algoritmos de IA aprenden a partir de datos históricos. Si estos datos reflejan desigualdades raciales o no representan adecuadamente la diversidad de la población, el algoritmo puede aprender y reproducir estos sesgos. Un estudio de 2019 mostró que los sistemas de reconocimiento facial tenían tasas de error más altas para personas de piel oscura, especialmente mujeres negras, debido a la falta de representación en los conjuntos de datos de entrenamiento.
Diseño algorítmico: la inteligencia artificial no es magia. Quienes diseñan y desarrollan los algoritmos y sistemas de IA pueden, con o sin intencionalidad, incorporar sus propios prejuicios en la creación de algoritmos. Las decisiones sobre cuáles variables incluir, cómo ponderarlas y de qué manera interpretarlas pueden influir en los resultados finales.
Interpretación y uso de resultados: incluso si un algoritmo es técnicamente imparcial, la forma en que se utilizan sus resultados puede conducir a prácticas discriminatorias.
La investigación de Tarcízio Silva aborda el impacto del racismo algorítmico en la visión computacional, destacando cómo los sistemas de inteligencia artificial (IA) y aprendizaje automático pueden perpetuar y amplificar prejuicios raciales a través de sus mecanismos de reconocimiento y clasificación de imágenes. Silva examina la construcción y expresión del racismo en la infraestructura online y las interfaces digitales, argumentando que tanto los algoritmos (el “back end”) como las representaciones visuales y textuales (el “front end”) son materializan estereotipos invisibles que afectan a grupos racializados.

A través de un análisis fundamentado en la Teoría Racial Crítica y estudios sobre la blanquitud, Silva propone un marco para comprender y desmantelar la opresión algorítmica, subrayando la necesidad de abrir las “cajas negras” de la tecnología para revelar y confrontar los sesgos raciales inherentes en los sistemas de visión computacional. Su trabajo resalta la importancia de abordar tanto los aspectos técnicos como los culturales y sociales en la lucha contra el racismo algorítmico, instando a una mayor diversidad e inclusión en los campos de la ciencia y la tecnología. 

El racismo algorítmico es un desafío significativo en la era de la IA. Es crucial que las personas en roles de desarrollo, investigación e, incluso, las usuarias sean conscientes de estos sesgos y trabajen activamente para crear algoritmos más inclusivos y equitativos. Esto implica diversificar los conjuntos de datos, y también cuestionar y revisar constantemente los supuestos subyacentes en el desarrollo de tecnologías. El fiasco de Google Gemini, por citar un ejemplo reciente, nos enseña que no se trata de corregir el racismo con más racismo, sino de desarrollar colectivamente algoritmos igualitarios.

La lucha contra el racismo algorítmico y la creación de tecnologías más equitativas se basa en un principio clave: aprender y enseñar cómo funcionan realmente los sistemas tecnológicos por dentro. Comprender el funcionamiento interno de los algoritmos y los sistemas de IA es esencial para identificar y corregir los sesgos y prejuicios que estos pueden perpetuar. Esto requiere un enfoque educativo y formativo que no solo se centre en las habilidades técnicas —necesarias para desarrollar y programar software— sino también en la sensibilización respecto de los impactos sociales y culturales de la tecnología. En este sentido, la educación en tecnología debe incluir un currículo que aborde la ética en IA, la justicia social y los estudios sobre el racismo y la discriminación, proporcionando a los estudiantes las herramientas para construir sistemas más justos y representativos.

Desde Latinoamérica y entre los grupos minoritarios, la creación de capacidades en tecnología es especialmente crucial para desafiar y cambiar las narrativas dominantes en el campo de la IA. Al empoderar a estos grupos para que participen activamente en el desarrollo tecnológico, se abre la puerta a una diversidad de perspectivas y experiencias que pueden informar y enriquecer el proceso de diseño de algoritmos.

Fomentar la inclusión de voces marginadas en la ciencia y la tecnología contribuye a reducir los estereotipos raciales y sesgos en los sistemas de IA, y promueve la creación de soluciones innovadoras que atienden a las necesidades y desafíos de todas las personas. Por último, construir una comunidad tecnológica inclusiva y diversa, en nuestra región y más allá, es un paso fundamental hacia la eliminación de estereotipos raciales y la creación de algoritmos que sirvan equitativamente a toda la sociedad.

Solo así podremos asegurar que la IA sea un aporte al desarrollo."""

enc = tiktoken.encoding_for_model("gpt-4")
result = enc.encode(string)
print(len(result))