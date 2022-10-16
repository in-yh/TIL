* Many to many relationship
* M:N(Article-User) Like
* M:N(User-User) Follow



가. Many to many relationship

1. 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우

2. 양쪽 모두에서 N:1 관계를 가짐

   ex) 환자와 의사의 예약 시스템

   cf) 데이터 모델링

   * 주어진 개념으로부터 논리적인 데이터 모델을 구성하는 작업
   * 물리적인 데이터베이스 모델로 만들어 고객의 요구에 따라 특정 정보 시스템의 데이터 베이스에 반영하는 작업

3. 용어정리

   가) target model : 관계 필드를 가지지 않은 모델 1 Article

   나) source model : 관계 필드를 가진 모델 N Comment

   

