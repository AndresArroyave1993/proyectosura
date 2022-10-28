from django import forms
class FormularioMedico (forms.Form):

    ESPECIALIDADES=(
        (1,'Cardiologia'),
        (2,'Medicina Interna'),
        (3,'Medicina general'),
        (4,'Ortopedia'),
        (5,'Pediatria')
    )
    JORNADAS=(
        (1,'6:00am a 2:00pm'),
        (2,'2:00pm a 10:00pm'),
        (3,'10:00pm a 6:00am')
    )
    SEDES=(
        (1,'Almacentro'),
        (2,'Punto clave'),
        (3,'Los Molinos')

    )

    nombre=forms.CharField()
    apellidos=forms.CharField()
    cedula=forms.CharField()
    tarjetaProfesional=forms.CharField()
    especialidad=forms.ChoiceField()
    jornada=forms.CharField()
    contacto=forms.CharField()
    sede=forms.ChoiceField()
