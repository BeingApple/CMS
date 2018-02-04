# CMS
스포카 프로그래밍 테스트용 CMS

http://13.125.115.234/customer_list/

### 의존성
- 기본 작업환경
  - Python 3.6.4
  - PostgreSQL 9.6.5
- Requirements
  - attrs==17.4.0
  - click==6.7
  - colorama==0.3.9
  - Flask==0.12.2
  - Flask-SQLAlchemy==2.3.2
  - gunicorn==19.7.1
  - itsdangerous==0.24
  - Jinja2==2.10
  - MarkupSafe==1.0
  - pluggy==0.6.0
  - psycopg2==2.7.3.2
  - py==1.5.2
  - pytest==3.4.0
  - six==1.11.0
  - SQLAlchemy==1.2.2
  - SQLAlchemy-Utils==0.32.21
  - uWSGI==2.0.15
  - Werkzeug==0.14.1
  
### 서버
실제 작동중인 서버는 AWS EC2에서 uWSGI + nginx 로 구동하였습니다.
DB는 RDS의 PostgreSQL 9.6.5 입니다

### 파일 설명
- cms
  - 프로젝트 디렉토리
- cms/entities
  - DB 모델
- cms/service
  - 서비스
- cms/create_app.py
  - 공통적으로 사용되는 Flask app 반환을 위한 파일
- cms/database.py
  - DB 모델에서 공통 사용할 SQLAlchemy 앱을 생성하고 실제 데이터베이스에 연결하는 역할
- cms/app.py
  - URL 라우팅 및 실제 웹 연결에 대한 정의 부분
- config
  - 설정 파일
- tests
  - pytest 파일
- wsgi.py
  - uWSGI 에서 실행을 위해 사용하는 파일

### pytest
최상위 디렉토리에서 pytest를 실행해주시면 됩니다. 현재 /customer_list/ 페이지와 /customer_list/30/ 페이지를 테스트 하게 되어있습니다.


### 작업 된 사항
- 페이징을 포함한 고객 정보(user) 리스트
- 매장 필터, 기간 필터 추가 시 고객의 매장 재방문율, 기간 내 방문자, 기간 내 처음 방문한 신규 방문자 출력(정합성 어긋나 있는 상태)
- 페이지 줄 수에 대한 사용자 입력 변경 기능(10개, 20개, 50개, 100개, 200개)

