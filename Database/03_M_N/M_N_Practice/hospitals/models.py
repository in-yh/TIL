from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


# 현재 N, 외래키 가지고 있음
class Patient(models.Model):
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    # 다대다필드로 가져옴 (데이터베이스 초기화 후 마이그레이션)
    doctors = models.ManyToManyField(Doctor, related_name='patients', through='Reservation') # symmetrical : 대칭, ManyToManyField가 동일한 모델을 가리키는 정의에서만 사용, True면 한쪽에서 추가하면 다른쪽에서도 추가됨, False면 팔로우의 개념(User-User)
    # 알아서 중개 테이블을 가져옴 (patient_doctors)
    # Doctor에 작성해도 상관없음(비종속적인 관계) 참조랑 역참조 관계만 달라질뿐
    # Patient에서 Doctor를 참조할 때는 참조, 그 반대는 역참조
    # 의사와 환자가 예약을 만들어내게끔 함 (Reservation과는 다름)
    # patient1.doctors.add(doctor1) : patient가 예약 잡기, add는 이미 존재하는 관계에 사용하면 관계가 복제되지 않음
    # patient1.doctors.all() : 조회(참조)
    # doctor1.patient_set.all() : doctor에서 patient 조회할 때는 역참조
    # doctor1.patient_set.add(patient2) : doctor가 예약 잡기
    # doctor1.patient_set.remove(patient1) : doctor의 예약 취소
    # patient2.doctors.remove(doctor1) : patient의 예약 취소
    # patient_set을 patients로 바꾸면 좀 일관성 있어보이지? related_name 바꾸자! (마이그레이션) / 단일일 때는 objects만 썼었는데..
    
    # 예약일, 증상(extra data) 등을 추가할 때
    # 중개테이블을 만들어 수동으로 지정(through 사용)
    # Reservation 다시 살려!
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'


class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)
    # doctor1 = Doctor.objects.create(name='alice')
    # patient1 = Patient.objects.create(name='carol')
    # reservation1 = Reservation(doctor=doctor1, patient=patient1, symptom='headache')  
    # reservation1.save()
    # patient2.doctors.add(doctor1, through_defaults={'symptom': 'flu'})

    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
    # 만든 후 마이그레이션(이전 설계도(번호붙은)와 데이터베이스는 삭제하고 진행하자)


# migrations 진행
# doctor1 = Doctor.objects.create(name='alice')
# patient1 = Patient.objects.create(name='carol', doctor=doctor1) # 외래키에는 객체를 넣는다
# N:1의 한계(1번 환자가 두 의사 모두에게 방문하려고 함)
# patient3 = Patient.objects.create(name='carol', doctor=doctor2) # 동일한 환자지만 객체를 하나 더 만들어! 가능은 하지만 데이터베이스 상 어색함
# 그리고 동시 예약할 수 없을까? 1,2는 INTEGER 타입이 아니기 때문에 불가능!
# 예약 테이블을 따로 만들자!

# 중개 모델
# 예약 모델은 의사와 환자에 각각 N:1 관계를 가짐
# 모델 만든 후
# doctor1 = Doctor.objects.create(name='alice')
# patient1 = Patient.objects.create(name='carol')
# Reservation.objects.create(doctor=doctor1, patient=patient1)
 
# 의사 혹은 환자가 예약된 목록 확인할 때(역참조)
# doctor1.reservation_set.all()
# patient1.reservation_set.all()

# M:N (Article-User) : 좋아요 기능