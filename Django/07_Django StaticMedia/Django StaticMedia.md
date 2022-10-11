* Managing static files
* Image Upload
* lmage Resizing
* QuerySet API Advanced(DB 내용)



가. Managing static files

1. 개요

   가) 개발자가 서버에 미리 준비한 

   나) 혹은 사용자가 업로드한 정적파일을 클라이언트에게 제공하는 방법

2. Static files(정적 파일)

   가) 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일

   * 사용자의 요청에 따라 내용이 바뀌는 것이 아니라 요청한 것을 그대로 보여주는 파일

   나) 파일 자체가 고정, 서비스 중에도 추가되거나 변경되지 않고 고정

   * 예를 들어, 웹 사이트는 일반적으로 이미지, 자바스크립트 또는 CSS와 같은 미리 준비된 추가 파일(움직이지 않는)을 제공해야 함

   다) 장고에서는 이러한 파일들을 'static file'이라 함

   * 관리하는 앱은 staticfiles 내장앱을 통해 정적 파일과 관련된 기능을 제공(settings.py에 기본 작성되어 있음)

3. Media file

   가) Static files 중 하나

   나) “사용자가 업로드한” 정적 파일

4. 웹 서버와 정적 파일

   가) 웹 서버의 기본동작은

   * 특정 위치(URL)에 있는 자원을 요청(HTTP request)받아서
   * 응답(HTTP response)을 처리하고 제공(serving)하는 것

   나) 이는 '자원과 자원에 접근 가능한 주소가 있다.'라는 의미

   * 예를 들어, 사진 파일은 자원이고 해당 사진 파일을 얻기 위한 경로인 웹 주소(URL)가 존재

   다) 즉, 웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원을 제공

5. Static files 구성하기

   가) 장고에서 정적파일을 구성하고 사용하기 위한 몇가지 단계

   * INSTALLED_APPS에 django.contrib.staticfiles가 포함되어 있는지 확인하기(자동 구성)

   * settings.py에서 STATIC_URL을 정의하기(자동 구성)

   * 앱의 static 폴더에 정적 파일을 위치하기 

     * 예) my_app/static/sample_img.jpg

   * 템플릿에서 static 템플릿 태그를 사용하여 지정된 경로에 있는 정적 파일의 URL 만들기

     ```html
     {% load static %}
     <!-- load tag : 특정 라이브러리, 패키지에 등록된 모든 템플릿 태그와 필터를 로드 -->
     
     <img src="{% static 'sample_img.jpg' %}" alt="sample image">
     <!-- static tag : STATIC_ROOT에 저장된 정적 파일에 연결 -->
     ```

   나) Static files 관련 Core Settings

   * STATIC_ROOT
     * Default : None
     * 장고 프로젝트에서 사용하는 모든 정적 파일을 한곳에 모아 넣는 경로
     * collectstatic이 배포를 위해 정적파일을 수집하는 디렉토리의 절대 경로
     * 개발 과정에서 settings.py의 DEBUG 값이 True로 설정되어 있으면 해당 값은 작용되지 않음
       * 실제 사용할 때는 DEBUG 값을 False로 바꿈, 그래야 디버깅 화면(노란색, 흰색)이 안뜸(너무 많은 정보가 포함되어 있기에)
     * 실 서비스 환경(배포 환경)에서 장고의 모든 정적 파일을 다른 웹 서버가 직접 제공하기 위해 사용
     * 배포 환경에서는 장고를 직접 실행하는 것이 아니라, 다른 서버에 의해 실행되기 때문에 실행하는 다른 서버는 장고에 내장되어 있는 정적 파일들을 인식하지 못함, 다른 컴퓨터에서 장고 서버(Local Server)를 실행시키는 것이기 때문에 경로들을 절대 경로로 설정해줘야 함 (내장되어 있는 정적 파일들을 밖으로 꺼내는 이유)
       * cf) 소프트웨어 배포 : 프로그램 및 애플리케이션을 서버와 같은 기기에 설치하여 서비스를 제공하는 것
         * Local Server를 어딘가에 업로드
         * 어딘가는 “AWS”, Google Cloud, MS Azure같은 클라우드 컴퓨팅 서비스에 업로드(설치)해줘서 클라우드 서버가 구동을 해주는 거지
   * STATICFILES_DIRS
     * Default : []
     * app/static/ 디렉토리 경로를 사용하는 것(기본 경로) 외에 추가적인 정적 파일 경로 목록 정의하는 리스트
     * 추가 파일 디렉토리에 대한 전체 경로를 포함하는 문자열 목록으로 작성되어야 함(템플릿도 추가경로 작성했듯이..)
   * STATIC_URL
     * 기본값 : None이지만 ‘/static/’로 덮어씌여짐 
     * STATIC_ROOT(내장된 정적파일의 실제 절대경로)에 있는 정적 파일을 참조할 때 사용할 URL (URL을 만드는 주소값이 STATIC_URL)
     * 개발단계에서는 실제 정적파일들이 저장되어 있는 app/static/경로(기본 경로) 및 STATICFILES_DIRS에 정의된 추가 경로들을 탐색
     * 실제 파일이나 디렉토리가 아니며, URL로만 존재
     * 비어 있지 않은 값으로 설정한다면 반드시 slash(/)로 끝나야 함

6. Static files 사용하기

   가) 기본 경로에 있는 static file 가져오기, app/static/~

   * articles/static/articles 경로에 이미지 파일 배치하기(templates 같이)

   나) 추가 경로에 있는 static file 가져오기, STATICFILES_DIRS

   * static/ 경로에 이미지 파일 배치하기

나. Image Upload

1. Django ImageField를 사용해 사용자가 업로드한 정적 파일(미디어 파일) 관리하기

2. ImageField()

   가) 이미지 업로드에 사용하는 모델 필드

   나) FileField를 상속받는 서브 클래스이기 때문에 FileField의 모든 속성 및 메서드를 사용 가능

   다) 더해서 사용자에 의해 업로드 된 객체가 유효한 이미지인지 검사

   라) ImageField 인스턴스는 최대 길이가 100자인 문자열로 DB에 생성(이미지가 들어가는게 아니라)되며, max_length 인자를 사용하여 최대 길이를 변경할 수 있음

3. FileField()

   가) FileField(upload_to=’’, max_length=100)

   나) 파일 업로드에 사용하는 모델 필드

   다) 선택인자 2개

   * upload_to : 어디에 업로드를 할 것인가, 어디부터 경로를 설정할 건지는 아직 모름

4. FileField / ImageField를 사용하기 위한 단계

   가) settings.py에 MEDIA_ROOT, MEDIA_URL 설정

   나) `upload_to` 속성을 정의하여 업로드 된 파일에 사용할 MEDIA_ROOT의 하위경로를 지정(선택사항) / 여기서 어디부터 경로 설정할지 정함

   다) MEDIA_ROOT

   * Default : ''
   * 사용자가 업로드 한 미디어 파일들을 보관할 디렉토리의 절대 경로
   * 장고는 성능을 위해 업로드 파일은 데이터베이스에 저장하지 않음
     * 데이터베이스에 저장되는 것은 `파일 경로`
   * MEDIA_ROOT는 STATIC_ROOT와 반드시 다른 경로로 지정해야 함

   라) MEDIA_URL

   * Default : ''
   * MEDIA_ROOT에서 제공되는 미디어 파일을 처리하는 URL 
   * 업로드 된 파일의 주소(URL)를 만들어 주는 역할
     * 웹 서버 사용자가 사용하는 public URL
   * 비어 있지 않은 값으로 설정한다면 반드시 slash로 끝나야 함
   * MEDIA_URL은 STATIC_URL과 반드시 다른 경로로 지정해야 함

다. lmage Resizing

1. django-imagekit 모듈 설치 및 등록

   ```bash
   pip install django-imagekit
   pip freeze > requirements.txt
   ```

   ```python
   INSTALLED_APPS = [
       ...
       'imagekit',
   ]
   ```

   가) cf) django-imagekit

   * 이미지 처리를 위한 장고 앱
     * 썸네일, 해상도, 사이즈, 색깔 등을 조정할 수 있음

2. 썸네일 만들기

   가) 원본 이미지 저장 X

   나) 원본 이미지 저장 O

