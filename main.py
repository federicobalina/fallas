from pyknow import *

class Tuberculosis(KnowledgeEngine):

    # R1 - Danios en el sistema respiratorio
    
    @Rule(Fact(sistema_respiratorio=P(lambda x: x < 3)))
    def danio_respiratorio_bajo(self):
        self.declare(Fact(danios_respiratorios=1))

    @Rule(Fact(sistema_respiratorio=3))
    def danio_respiratorio_medio(self):
        self.declare(Fact(danios_respiratorios=2))

    @Rule(Fact(sistema_respiratorio=P(lambda x: x > 3)))
    def danio_respiratorio_alto(self):
        self.declare(Fact(danios_respiratorios=3))

    # R2 - Propension al contagio 

    @Rule(Fact(contacto_social=P(lambda x: x <= 3)), 
          Fact(exposicion=P(lambda x: x <= 2)))
    def propension_contagio_baja(self):
        self.declare(Fact(propension_contagio=1))

    @Rule(OR(
            AND(Fact(contacto_social=P(lambda x: x > 3)), Fact(exposicion=P(lambda x: x > 2))),
            Fact(exposicion=5))
        )
    def propension_contagio_alta(self):
        self.declare(Fact(propension_contagio=3))

    @Rule(OR(
            AND(Fact(exposicion=P(lambda x: x > 2 and x < 5)),
              Fact(contacto_social=P(lambda x: x <= 3 ))),
            AND(Fact(contacto_social=P(lambda x: x > 3)),
              Fact(exposicion=P(lambda x: x <= 2 )))
        )) 
    def propension_contagio_media(self):
        self.declare(Fact(propension_contagio=2))


    # R3 - Sindrome de impregnación

    @Rule(Fact(astenia=P(lambda x: x < 3)),
          Fact(hiporexia=P(lambda x: x < 3)),
          Fact(adinamia=P(lambda x: x < 3))
        )
    def sindrome_impregnacion_bajo(self):
        self.declare(Fact(sindrome_impregnacion=1))

    @Rule(Fact(sudores_nocturnos=True),
          Fact(astenia=P(lambda x: x > 3)),
          Fact(hiporexia=P(lambda x: x > 3)),
          Fact(adinamia=P(lambda x: x > 3))
        )
    def sindrome_impregnacion_alto(self):
        self.declare(Fact(sindrome_impregnacion=3))

    @Rule(NOT(AND(
                Fact(sudores_nocturnos=True),
                Fact(astenia=P(lambda x: x > 3)),
                Fact(hiporexia=P(lambda x: x > 3)),
                Fact(adinamia=P(lambda x: x > 3)))),
          NOT(AND(
                Fact(astenia=P(lambda x: x < 3)),
                Fact(hiporexia=P(lambda x: x < 3)),
                Fact(adinamia=P(lambda x: x < 3))))
        )
    def sindrome_impregnacion_medio(self):
        self.declare(Fact(sindrome_impregnacion=2))

    # R4 - Propension por clase social

    @Rule(Fact(alimentacion=P(lambda x: x < 3)),
          Fact(contacto_social=P(lambda x: x < 3)),
          Fact(salubridad=P(lambda x: x < 3)))
    def propension_clase_social_baja(self):
        self.declare(Fact(propension_clase_social=1))

    @Rule(Fact(alimentacion=P(lambda x: x > 3)),
          Fact(contacto_social=P(lambda x: x > 3)),
          Fact(salubridad=P(lambda x: x > 3)))
    def propension_clase_social_alta(self):
        self.declare(Fact(propension_clase_social=3))
    
    @Rule(NOT(AND(
            Fact(alimentacion=P(lambda x: x < 3)),
            Fact(contacto_social=P(lambda x: x < 3)),
            Fact(salubridad=P(lambda x: x < 3)))),
          NOT(AND(
            Fact(alimentacion=P(lambda x: x > 3)),
            Fact(contacto_social=P(lambda x: x > 3)),
            Fact(salubridad=P(lambda x: x > 3))))
        )    
    def propension_clase_social_media(self):
        self.declare(Fact(propension_clase_social=2))

    # R5 - Danios en el sistema inmunológico

    @Rule(
          Fact(inmunodeficiencia=False),
          Fact(hiv=False),
          Fact(inmunosupresion=1), 
          Fact(bcg=True))
    def danio_sistema_inmunologico_bajo(self):
        self.declare(Fact(danio_sistema_inmunologico=1))
    
    @Rule(
          Fact(inmunodeficiencia=False),
          Fact(hiv=False),
          OR(Fact(inmunosupresion=2), Fact(bcg=False))
        )
    def danio_sistema_inmunologico_medio(self):
        self.declare(Fact(danio_sistema_inmunologico=2))

    @Rule(OR(Fact(inmunosupresion=P(lambda x: x > 2)),
             Fact(inmunodeficiencia=True),
             Fact(hiv=True))
        )
    def danio_sistema_inmunologico_alto(self):
        self.declare(Fact(danio_sistema_inmunologico=3))

    # R6 - Presencia de bacilos

    @Rule(Fact(bacilos_esputo=False),
          Fact(bacilos_secrecion=False))
    def presencia_bacilos_baja(self):
        self.declare(Fact(presencia_bacilos=1))

    @Rule(OR(
            AND(Fact(bacilos_esputo=True), Fact(bacilos_secrecion=False)),
            AND(Fact(bacilos_secrecion=True), Fact(bacilos_esputo=False))
        ))
    def presencia_bacilos_media(self):
        self.declare(Fact(presencia_bacilos=2))

    @Rule(Fact(bacilos_esputo=True), 
          Fact(bacilos_secrecion=True))
    def presencia_bacilos_alta(self):
        self.declare(Fact(presencia_bacilos=3))

    # R7 - Recomendacion de visita al médico

    @Rule(Fact(presencia_bacilos=3))
    def presencia_bacilos_alta_visita_médico(self):
        print("VISITA MÉDICA")

    @Rule(Fact(presencia_bacilos=2),
          OR(
              Fact(danios_respiratorios=3),
              Fact(propension_contagio=3),
              Fact(sindrome_impregnacion=3),
              Fact(propension_clase_social=3),
              Fact(danio_sistema_inmunologico=3)              
          ))
    def presencia_bacilos_media_y_un_indicio_alto_visita_médico(self):
        print("VISITA MÉDICA")

    @Rule(OR(
            AND(Fact(danios_respiratorios=3), Fact(propension_contagio=3)),
            AND(Fact(danios_respiratorios=3), Fact(sindrome_impregnacion=3)),
            AND(Fact(danios_respiratorios=3), Fact(propension_clase_social=3)),
            AND(Fact(danios_respiratorios=3), Fact(danio_sistema_inmunologico=3)),
            AND(Fact(propension_contagio=3), Fact(sindrome_impregnacion=3)),
            AND(Fact(propension_contagio=3), Fact(propension_clase_social=3)),
            AND(Fact(propension_contagio=3), Fact(danio_sistema_inmunologico=3)),
            AND(Fact(sindrome_impregnacion=3), Fact(propension_clase_social=3)),
            AND(Fact(sindrome_impregnacion=3), Fact(danio_sistema_inmunologico=3)),
            AND(Fact(propension_clase_social=3), Fact(danio_sistema_inmunologico=3))
    ))
    def dos_indicios_altos(self):
        print("VISITA MÉDICA")

    @Rule(OR(
            AND(Fact(danios_respiratorios=2),
                Fact(propension_contagio=2),
                Fact(sindrome_impregnacion=2),
                Fact(propension_clase_social=2),
                Fact(danio_sistema_inmunologico=2)
            ),
            AND(Fact(danios_respiratorios=2),
                Fact(propension_contagio=2),
                Fact(sindrome_impregnacion=2),
                Fact(propension_clase_social=2),
                Fact(presencia_bacilos=2)
            ),
            AND(Fact(danios_respiratorios=2),
                Fact(propension_contagio=2),
                Fact(sindrome_impregnacion=2),
                Fact(danio_sistema_inmunologico=2),
                Fact(presencia_bacilos=2)
            ),
            AND(Fact(danios_respiratorios=2),
                Fact(propension_contagio=2),
                Fact(propension_clase_social=2),
                Fact(danio_sistema_inmunologico=2),
                Fact(presencia_bacilos=2)
            ),
            AND(Fact(danios_respiratorios=2),
                Fact(sindrome_impregnacion=2),
                Fact(propension_clase_social=2),
                Fact(danio_sistema_inmunologico=2),
                Fact(presencia_bacilos=2)
            ),
            AND(Fact(propension_contagio=2),
                Fact(sindrome_impregnacion=2),
                Fact(propension_clase_social=2),
                Fact(danio_sistema_inmunologico=2),
                Fact(presencia_bacilos=2)
            ),
    ))
    def cinco_indicios_medios(self):
        print("VISITA MÉDICA")

    @Rule(OR(
            AND(Fact(danios_respiratorios=3),
                OR(
                    AND(Fact(propension_contagio=2), Fact(sindrome_impregnacion=2), Fact(propension_clase_social=2)),
                    AND(Fact(propension_contagio=2), Fact(sindrome_impregnacion=2), Fact(danio_sistema_inmunologico=2)),
                    AND(Fact(propension_contagio=2), Fact(propension_clase_social=2), Fact(danio_sistema_inmunologico=2)),
                    AND(Fact(sindrome_impregnacion=2), Fact(propension_clase_social=2), Fact(danio_sistema_inmunologico=2))
                )),

            AND(Fact(propension_contagio=3),
                OR(
                    AND(Fact(danios_respiratorios=2), Fact(sindrome_impregnacion=2), Fact(propension_clase_social=2)),
                    AND(Fact(danios_respiratorios=2), Fact(sindrome_impregnacion=2), Fact(danio_sistema_inmunologico=2)),
                    AND(Fact(danios_respiratorios=2), Fact(propension_clase_social=2), Fact(danio_sistema_inmunologico=2)),
                    AND(Fact(sindrome_impregnacion=2), Fact(propension_clase_social=2), Fact(danio_sistema_inmunologico=2))
                )),

            AND(Fact(sindrome_impregnacion=3),
                OR(
                    AND(Fact(propension_contagio=2), Fact(danios_respiratorios=2), Fact(propension_clase_social=2)),
                    AND(Fact(propension_contagio=2), Fact(danios_respiratorios=2), Fact(danio_sistema_inmunologico=2)),
                    AND(Fact(propension_contagio=2), Fact(propension_clase_social=2), Fact(danio_sistema_inmunologico=2)),
                    AND(Fact(danios_respiratorios=2), Fact(propension_clase_social=2), Fact(danio_sistema_inmunologico=2))
                )),
            
            AND(Fact(propension_clase_social=3),
                OR(
                    AND(Fact(propension_contagio=2), Fact(sindrome_impregnacion=2), Fact(danios_respiratorios=2)),
                    AND(Fact(propension_contagio=2), Fact(sindrome_impregnacion=2), Fact(danio_sistema_inmunologico=2)),
                    AND(Fact(propension_contagio=2), Fact(danios_respiratorios=2), Fact(danio_sistema_inmunologico=2)),
                    AND(Fact(sindrome_impregnacion=2), Fact(danios_respiratorios=2), Fact(danio_sistema_inmunologico=2))
                )),
            
            AND(Fact(danio_sistema_inmunologico=3),
                OR(
                    AND(Fact(propension_contagio=2), Fact(sindrome_impregnacion=2), Fact(propension_clase_social=2)),
                    AND(Fact(propension_contagio=2), Fact(sindrome_impregnacion=2), Fact(danios_respiratorios=2)),
                    AND(Fact(propension_contagio=2), Fact(propension_clase_social=2), Fact(danios_respiratorios=2)),
                    AND(Fact(sindrome_impregnacion=2), Fact(propension_clase_social=2), Fact(danios_respiratorios=2))
                )),
    ))                
    def un_indicio_alto_tres_medios(self):
        print("VISITA MÉDICA")

engine = Tuberculosis()
engine.reset()  # Prepare the engine for the execution.

engine.declare(Fact(sistema_respiratorio=3))

engine.declare(Fact(contacto_social=2))
engine.declare(Fact(exposicion=3))

engine.declare(Fact(sudores_nocturnos=True))
engine.declare(Fact(astenia=3))
engine.declare(Fact(hiporexia=3))
engine.declare(Fact(adinamia=3))

engine.declare(Fact(alimentacion=3))
engine.declare(Fact(salubridad=3))

engine.declare(Fact(inmunosupresion=2))
engine.declare(Fact(inmunodeficiencia=False))
engine.declare(Fact(hiv=False))
engine.declare(Fact(bcg=False))

engine.declare(Fact(bacilos_esputo=False))
engine.declare(Fact(bacilos_secrecion=False))

engine.run()  # Run it!
