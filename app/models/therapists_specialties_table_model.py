from app.configs.database import db

therapists_specialties_table = db.Table('therapists_specialties',
                                        db.Column(
                                            'id_therapist_specialties', db.Integer, primary_key=True),
                                        db.Column('id_therapist', db.Integer,
                                                  db.ForeignKey('therapists.id_therapist')),
                                        db.Column('id_specialty', db.Integer,
                                                  db.ForeignKey('specialties.id_specialty'))
                                        )
