from pyknow import *

class Tuberculosis(KnowledgeEngine):

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

engine.declare(Fact(danios_respiratorios=2))
engine.declare(Fact(propension_contagio=2))
engine.declare(Fact(sindrome_impregnacion=3))
engine.declare(Fact(propension_clase_social=1))
engine.declare(Fact(danio_sistema_inmunologico=1))
engine.declare(Fact(presencia_bacilos=1))

engine.run()  # Run it!